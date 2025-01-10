from Bio.Seq import Seq

def read_text_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return None

file_path = "C:\\Users\\rajab\\OneDrive\\Desktop\\momo.txt"
content = read_text_file(file_path)

def complementary_dna_sequence(dna_sequence):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C", " ": " "}
    dna_sequence = dna_sequence.upper()
    if not all(base in complement for base in dna_sequence):
        raise ValueError("Invalid DNA sequence. Only A, T, C, and G are allowed.")
    complementary_sequence = "".join(complement[base] for base in reversed(dna_sequence))
    return complementary_sequence
if content:
    complementary_sequence = Seq(complementary_dna_sequence(content))
    print("Original DNA Sequence:      ", content)
    print("Complementary DNA Sequence: ", complementary_sequence)
    protein_sequence= complementary_sequence.translate()
    print("Protein sequence:", protein_sequence)