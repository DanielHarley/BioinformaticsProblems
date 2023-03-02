class Transcriber:

    def __init__(self, dna_nucleotide_sequence: str):
        self.dna_sequence: str = dna_nucleotide_sequence
        self.rna_sequence: str = ''

        self.transcribe()

    def transcribe(self):
        self.rna_sequence = self.dna_sequence.replace("T", "U")

    def get_rna_sequence(self):
        return self.rna_sequence
