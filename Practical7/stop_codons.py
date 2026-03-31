import re
# Define stop codons
STOP_CODONS = {'TAA', 'TAG', 'TGA'}
# Input file path (your local path)
INPUT_FILE = r"E:/fyx2025/zje/IBI/Week_7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
# Output file path
OUTPUT_FILE = r"stop_genes.fa"

#Function to read FASTA file
def read_fasta(file_path):
     fasta_dict = {}
     current_gene = None
     current_seq = []

     with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue # Skip empty lines
            # Identify header line (starts with >)
            if line.startswith('>'):
                # Save previous gene's sequence
                if current_gene is not None:
                    fasta_dict[current_gene] = ''.join(current_seq)
                # Extract gene name (from > to first space)
                gene_name = line.split()[0][1:]
                current_gene = gene_name
                current_seq = []
            else:
                # Sequence line, append to current sequence
                current_seq.append(line.upper())
        # Save the last gene's sequence
        if current_gene is not None:
            fasta_dict[current_gene] = ''.join(current_seq)
     return fasta_dict

# Function to detect in-frame stop codons
def find_in_frame_stop_codons(sequence):
    stop_found = set()
    seq_len = len(sequence)
    # Iterate all in-frame codons starting from index 0, step 3
    for i in range(0, seq_len - 2, 3):
        codon = sequence[i:i+3]
        if codon in STOP_CODONS:
            stop_found.add(codon)
    
    return stop_found

# Main program
if __name__ == "__main__":
    gene_seqs = read_fasta(INPUT_FILE)
    print("Read ",len(gene_seqs)," sequences")

    # Filter genes with in-frame stop codons
    stop_genes = {}
    for gene_name, seq in gene_seqs.items():
        stop_codons = find_in_frame_stop_codons(seq)
        if stop_codons:
            stop_genes[gene_name] = (seq, stop_codons)
    print("Identify ",len(stop_genes)," genes containing in-frame stop codons")

    # Write output FASTA file
    with open(OUTPUT_FILE, 'w') as f_out:
        for gene_name, (seq, stop_codons) in stop_genes.items():
             # Construct header line: >gene_name;TAA,TGA (sorted for consistent format)
             sorted_stops = sorted(stop_codons)
             header = f">{gene_name};{','.join(sorted_stops)}"
             f_out.write(header + '\n')

             for i in range(0, len(seq), 60):
                f_out.write(seq[i:i+60] + '\n')
    
    print("Process done")
