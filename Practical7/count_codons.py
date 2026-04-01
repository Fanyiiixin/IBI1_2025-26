import matplotlib.pyplot as plt
from Bio import SeqIO
from collections import Counter

def generate_codon_report():
    # 1. Input Handling
    valid_stops = ["TAA", "TAG", "TGA"]
    stop_codon = input("Enter a stop codon (TAA, TAG, or TGA): ").strip().upper()

    if stop_codon not in valid_stops:
        print("Invalid stop codon.")
        return

    fasta_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    all_codons = []

    try:
        for record in SeqIO.parse(fasta_file, "fasta"):
            sequence = str(record.seq).upper()
            
            # Find all in-frame stop codons
            stops = [i for i in range(0, len(sequence) - 2, 3) if sequence[i:i+3] == stop_codon]

            if stops:
                longest_orf_stop_index = max(stops)
                
                # Get all codons upstream of that specific stop codon
                orf_sequence = sequence[:longest_orf_stop_index]
                
                codons = [orf_sequence[i:i+3] for i in range(0, len(orf_sequence), 3)]
                all_codons.extend(codons)

    except FileNotFoundError:
        print(f"File {fasta_file} not found.")
        return

    if not all_codons:
        print("No data found.")
        return

    # Count frequencies
    counts = Counter(all_codons)
    
    # Group small slices into "Other"
    total = sum(counts.values())
    threshold = 0.01  # 1%
    
    final_counts = {}
    other_count = 0
    
    for codon, count in counts.items():
        if count / total >= threshold:
            final_counts[codon] = count
        else:
            other_count += count
    
    if other_count > 0:
        final_counts['Other (<1%)'] = other_count

    # Sorting for a prettier chart
    labels, values = zip(*sorted(final_counts.items(), key=lambda x: x[1], reverse=True))

    plt.figure(figsize=(14, 10))
    plt.pie(values, labels=labels, autopct='%1.1f%%', pctdistance=0.85, startangle=140)
    

    plt.title(f"In-frame Codon Distribution\n(Longest ORF ending in {stop_codon})", fontsize=15)
    plt.tight_layout()
    
    plt.show()
    


if __name__ == "__main__":
    generate_codon_report()