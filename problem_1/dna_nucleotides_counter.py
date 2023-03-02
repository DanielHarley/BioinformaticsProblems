from collections import Counter
from typing import List


class DNACounter:

    def __init__(self, dna_sequence_string):
        self.thymine_total = None
        self.adenine_total = None
        self.cytosine_total = None
        self.guanine_total = None

        self.dna_string = dna_sequence_string
        self.nucleotide_list: List[str] = list(self.dna_string)
        self.counter = Counter(self.nucleotide_list)

        self.count_nucleotides()

    def count_nucleotides(self):
        self.counter = Counter(self.nucleotide_list)

        self.thymine_total = self.counter.get("T")
        self.adenine_total = self.counter.get("A")
        self.cytosine_total = self.counter.get("C")
        self.guanine_total = self.counter.get("G")

    def get_nucleotides_count(self):
        result = f"{self.adenine_total} {self.cytosine_total} {self.guanine_total} {self.thymine_total}"
        return result

