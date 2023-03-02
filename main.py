from collections import Counter
import dataset as data
from dna_nucleotides_counter import DNACounter

problems = ["Counting DNA Nucleotides"]

print(f"Problem 1: {problems[0]}")
user_input = input(f"Which problem code output would you like to see? Choose from '1' to '{len(problems)}':\n")


# Problem 1 - DNA nucleotide counter
print(f"Problem 1: {problems[0]}")
dna_counter = DNACounter(dna_sequence_string=data.dna_sequence)
dna_counter.get_nucleotides_count()
