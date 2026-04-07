import matplotlib.pyplot as plt

def get_orfs_with_stop(seq, target_stop):
    stops = {'TAA', 'TAG', 'TGA'}
    orfs = []
    for i in range(0, len(seq)-2, 3):
        if seq[i:i+3] == 'ATG':
            codons = []
            for j in range(i, len(seq)-2, 3):
                c = seq[j:j+3]
                codons.append(c)
                if c == target_stop:
                    orfs.append(codons[:-1])
                    break
                elif c in stops:
                    break
    return orfs


target = input("Enter stop codon (TAA/TAG/TGA): ").strip().upper()

with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as f:
    data = f.read()

seqs = []
current = ''
for line in data.splitlines():
    if line.startswith('>'):
        if current:
            seqs.append(current)
            current = ''
    else:
        current += line.strip()
if current:
    seqs.append(current)

count = {}
for s in seqs:
    orfs = get_orfs_with_stop(s, target)
    for o in orfs:
        for c in o:
            count[c] = count.get(c, 0) + 1

print("Codon counts upstream of", target)
for c, n in sorted(count.items()):
    print(c, n)

plt.figure(figsize=(8,8))
plt.pie(count.values(), labels=count.keys(), autopct='%1.1f%%')
plt.title(f'Codon usage before {target}')
plt.savefig('codon_pie.png')
plt.close()