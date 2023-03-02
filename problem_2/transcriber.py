from typing import List


class Transcriber:

    def __init__(self, dna_nucleotide_sequence: str):
        self.dna_nucleotide_list: List[str] = list(dna_nucleotide_sequence)
        self.rna_nucleotide_list: List[str] = []
        self.rna_sequence: str = ''

        self.transcribe()

    def transcribe(self):
        for index in range(len(self.dna_nucleotide_list)):
            dna_nucleotide = self.dna_nucleotide_list[index]

            if dna_nucleotide == "T":
                self.rna_nucleotide_list.append("U")
            else:
                self.rna_nucleotide_list.append(dna_nucleotide)

        self.rna_sequence = ''.join(self.rna_nucleotide_list)

    def get_rna_sequence(self):
        return self.rna_sequence
