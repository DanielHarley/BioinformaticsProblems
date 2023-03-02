from typing import List


class DNAPolymerase:

    def __init__(self, dna_nucleotide_sequence: str):
        self._dna_sequence: List[str] = list(dna_nucleotide_sequence)
        self._new_dna_strand: List[str] = []
        self._new_dna_sequence: str = ''

        self._replicate()

    def _replicate(self):
        self._dna_sequence = self._dna_sequence[::-1]

        for index in range(len(self._dna_sequence)):
            dna_nucleotide = self._dna_sequence[index]
            if dna_nucleotide == "A":
                self._new_dna_strand.append("T")
            elif dna_nucleotide == "T":
                self._new_dna_strand.append("A")
            elif dna_nucleotide == "C":
                self._new_dna_strand.append("G")
            elif dna_nucleotide == "G":
                self._new_dna_strand.append("C")

        self._new_dna_sequence = ''.join(self._new_dna_strand)

    def get_new_dna_sequence(self):
        return self._new_dna_sequence
