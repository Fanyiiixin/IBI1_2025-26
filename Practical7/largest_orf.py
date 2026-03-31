seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
# define codons
START_CODON = 'AUG'
STOP_CODONS = {'UAA', 'UAG', 'UGA'}

def find_largest_orf(sequence):
    n = len(sequence)
    max_length = 0
    longest_orf_sequence = ''

    # Iterate through every possible position for a start codon
    for i in range(n):
        if sequence[i:i+3] == START_CODON:
            current_orf = [START_CODON]
            # Read codons in triplets until a stop codon or end of sequence
            for j in range(i + 3, n, 3):
                codon = sequence[j:j+3]
                # Stop if less than 3 nucleotides remain
                if len(codon) < 3:
                    break
                current_orf.append(codon)
                # Stop when a stop codon is found
                if codon in STOP_CODONS:
                    break
                # Build full ORF sequence
                orf_seq = ''.join(current_orf)
                orf_length = len(orf_seq)
                # Update the longest ORF
                if orf_length > max_length:
                    max_length = orf_length
                    longest_orf = orf_seq
    return longest_orf, max_length
# Run the function
longest_orf_seq, longest_orf_len = find_largest_orf(seq)
# Print the results
print("The longest ORF sequence: ",longest_orf_seq)
print("The length of that ORF: ",longest_orf_len)


            

                
                
