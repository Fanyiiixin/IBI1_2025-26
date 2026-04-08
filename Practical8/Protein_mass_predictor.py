# Define the monoisotopic residue mass dictionary for standard amino acids
amino_acid_masses = {
    'G': 57.02,
    'A': 71.04,
    'S': 87.03,
    'P': 97.05,
    'V': 99.07,
    'T': 101.05,
    'C': 103.01,
    'I': 113.08,
    'L': 113.08,
    'N': 114.04,
    'D': 115.03,
    'Q': 128.06,
    'K': 128.09,
    'E': 129.04,
    'M': 131.04,
    'H': 137.06,
    'F': 147.07,
    'R': 156.10,
    'Y': 163.06,
    'W': 186.08
}

def calculate_protein_mass(sequence):
    """
    Calculates the total mass of a protein from its amino acid sequence.
    
    Args:
        sequence (str): A string of one-letter amino acid symbols.
        
    Returns:
        float: Total mass of the protein in atomic mass units (amu), summed from residue masses.
        
        Error: If any character in the input sequence is not a valid amino acid symbol.
    """
    total_mass = 0.0
    # Iterate over each amino acid character in the input sequence
    for amino_acid in sequence:
        # Validate the amino acid symbol and accumulate mass
        if amino_acid in amino_acid_masses:
            total_mass += amino_acid_masses[amino_acid]
        else:
            # Report error for unrecognized amino acids
            print(f"Error: Amino acid symbol '{amino_acid}' is not defined in the mass table.")
            return None
    return total_mass

# ------------------- Example Function Call  -------------------
# Example 1: Valid sequence test
sample_sequence_1 = "ACDEFG"
calculated_mass_1 = calculate_protein_mass(sample_sequence_1)
if calculated_mass_1 is not None:
    print(f"Calculated total protein mass of {sample_sequence_1}: {calculated_mass_1} amu\n")




# Example 2: Invalid sequence test
sample_sequence_2 = "ACDXFG"
calculated_mass_2 = calculate_protein_mass(sample_sequence_2)
if calculated_mass_2 is not None:
    print(f"Calculated total protein mass: {calculated_mass_2} amu")




