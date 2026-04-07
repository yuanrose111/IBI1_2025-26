seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
start_codon= 'AUG'
stop_codon = ['UAA', 'UAG', 'UGA']

longest_orf = ''
seq_length = len(seq)

for i in range (seq_length -2):
    if seq [i:i+3] == start_codon:
       for j in range (i,seq_length -2, 3) :
           current_codon = seq[j:j+3]
           if current_codon in stop_codon:
               current_orf =seq[i:j+3]
               if len (current_orf) > len (longest_orf):
                   longest_orf = current_orf
               break
print ('Longest ORF:',longest_orf)
print ('Length of ORF (nucleotides):' , len(longest_orf))
