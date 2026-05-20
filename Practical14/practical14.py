import xml.dom.minidom
from xml.sax import ContentHandler, parse
from datetime import datetime

def dom_parse(xml_file):
    start = datetime.now()

    max_counts = {
        'molecular_function': (None, 0),
        'biological_process': (None, 0),
        'cellular_component': (None, 0)
    }

    dom = xml.dom.minidom.parse(xml_file)
    terms = dom.getElementsByTagName('term')

    for term in terms:
        go_id = term.getElementsByTagName('id')[0].firstChild.data
        ns = term.getElementsByTagName('namespace')[0].firstChild.data
        is_a_count = len(term.getElementsByTagName('is_a'))

        if ns in max_counts:
            current_id, current_num = max_counts[ns]
            if is_a_count > current_num:
                max_counts[ns] = (go_id, is_a_count)

    end = datetime.now()
    return max_counts, (end - start).total_seconds()


class GOHandler(ContentHandler):
    def __init__(self):
        self.current_content = ''
        self.current_go_id = ''
        self.current_ns = ''
        self.is_a_count = 0

        self.max_counts = {
            'molecular_function': (None, 0),
            'biological_process': (None, 0),
            'cellular_component': (None, 0)
        }

    def startElement(self, name, attrs):
        self.current_content = ''
        if name == 'term':
            self.current_go_id = ''
            self.current_ns = ''
            self.is_a_count = 0

    def characters(self, content):
        self.current_content += content

    def endElement(self, name):
        if name == 'id':
            self.current_go_id = self.current_content.strip()
        elif name == 'namespace':
            self.current_ns = self.current_content.strip()
        elif name == 'is_a':
            self.is_a_count += 1
        elif name == 'term':
            if self.current_ns in self.max_counts:
                cur_id, cur_num = self.max_counts[self.current_ns]
                if self.is_a_count > cur_num:
                    self.max_counts[self.current_ns] = (self.current_go_id, self.is_a_count)

def sax_parse(xml_file):
    start = datetime.now()
    handler = GOHandler()
    parse(xml_file, handler)
    end = datetime.now()
    return handler.max_counts, (end - start).total_seconds()


def main():
    xml_file = 'go_obo.xml'

    print('=== DOM Parser Result ===')
    dom_res, dom_t = dom_parse(xml_file)
    for cat, (go, num) in dom_res.items():
        print(f'{cat:25} | MAX is_a: {num} | GO ID: {go}')
    print(f'DOM time: {dom_t:.4f}s\n')

    print('=== SAX Parser Result ===')
    sax_res, sax_t = sax_parse(xml_file)
    for cat, (go, num) in sax_res.items():
        print(f'{cat:25} | MAX is_a: {num} | GO ID: {go}')
    print(f'SAX time: {sax_t:.4f}s\n')

    faster = 'SAX' if sax_t < dom_t else 'DOM'
    print(f'Faster API: {faster}')

if __name__ == '__main__':
    main()

