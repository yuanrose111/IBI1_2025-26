
input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "stop_genes.fa"


stops = ['TAA', 'TAG', 'TGA']


def has_in_frame_stop(seq):
    seq = seq.upper()

    for frame in range(3):
        
        for i in range(frame, len(seq) - 2, 3):
            codon = seq[i:i+3]
            if codon in stops:
                return True
    return False


total_genes = 0
kept_genes = 0


with open(input_file, 'r') as f, open(output_file, 'w') as out:
    current_header = ''
    current_seq = ''
    
    for line in f:
        line = line.strip()
        
        if not line:
            continue
        if line.startswith('>'):  
            if current_header and current_seq:
                total_genes += 1
                if has_in_frame_stop(current_seq):
                    kept_genes += 1
                    out.write(current_header + '\n')
                    out.write(current_seq + '\n')
            current_header = line
            current_seq = ''
        else:
            current_seq += line.upper()
    
    if current_header and current_seq:
        total_genes += 1
        if has_in_frame_stop(current_seq):
            kept_genes += 1
            out.write(current_header + '\n')
            out.write(current_seq + '\n')


print(f"total：{total_genes}")
print(f"✅：{kept_genes}")
print(f"final：{output_file}")
