from collections import Counter
from typing import List


class DnaGCCounter:

    def __init__(self):
        self.dna_dictionary_list: List[dict] = []
        self.highest_gc_percentage_dna = {}
        self.__read_fasta_file(file_path="problem_5/dna_sequences.fasta")
        self.__rank_dna()

    def __read_fasta_file(self, file_path) -> None:
        sequences = []
        with open(file_path, 'r') as fasta:
            sequence_name = ''
            sequence = ''
            for line in fasta:
                if line.startswith('>'):
                    # save previous sequence and start new one
                    if sequence_name and sequence:
                        # calculate GC percentage
                        gc_count = sequence.count('G') + sequence.count('C')
                        total_count = len(sequence)
                        gc_percentage = gc_count / total_count * 100
                        sequences.append({"name": sequence_name, "sequence": sequence, "gc_percentage": gc_percentage})
                    sequence_name = line.strip()[1:]
                    sequence = ''
                else:
                    sequence += line.strip()
            # save the last sequence
            if sequence_name and sequence:
                # calculate GC percentage
                gc_count = sequence.count('G') + sequence.count('C')
                total_count = len(sequence)
                gc_percentage = gc_count / total_count * 100
                sequences.append({"name": sequence_name, "sequence": sequence, "gc_percentage": gc_percentage})
        self.dna_dictionary_list = sequences

    def __rank_dna(self) -> None:
        highest_gc_percentage = 0.0

        for index in range(len(self.dna_dictionary_list)):
            dna = self.dna_dictionary_list[index]
            if dna["gc_percentage"] > highest_gc_percentage:
                highest_gc_percentage = dna["gc_percentage"]
                self.highest_gc_percentage_dna = dna

    def get_highest_gc_percent_dna(self) -> dict:
        return self.highest_gc_percentage_dna

