# Practical 8 - Task 1: Protein Mass Predictor
# IBI1 2025/26

def calculate_protein_mass(sequence):
    """
    Calculate monoisotopic mass of a protein in atomic mass units (amu).
    Input: amino acid sequence (string)
    Return: total mass (float)
    Error: raise ValueError for invalid amino acids
    """
    aa_mass = {
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

    total_mass = 0.0
    for aa in sequence:
        if aa not in aa_mass:
            raise ValueError(f"Error: Unknown amino acid '{aa}'")
        total_mass += aa_mass[aa]
    return total_mass


# Example usage (required)
if __name__ == "__main__":
    print("===== Protein Mass Calculation Example =====")
    test_seq = "GAS"
    mass = calculate_protein_mass(test_seq)
    print(f"Sequence: {test_seq}")
    print(f"Total mass: {mass:.2f} amu")