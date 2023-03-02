

# problems = ["Counting DNA Nucleotides", "Transcribing DNA into RNA"]
problems = {1: "Counting DNA Nucleotides", 2: "Transcribing DNA into RNA"}

for index in range(len(problems)):
    print(f"{index + 1}: {problems[index + 1]}.")

print("")
user_input = input(f"Which problem code output would you like to see? Choose from '1' to '{len(problems)}': ")


# Problem 1 - DNA nucleotide counter
if user_input == "1":

    from problem_1 import problem_1_dataset as data_1
    from problem_1.dna_nucleotides_counter import DNACounter

    print(f"Problem 1: {problems[1]}")
    dna_counter = DNACounter(data_1.dna_sequence)
    result = dna_counter.get_nucleotides_count()
    print(result)

# Problem 2 - Transcribing DNA into RNA
elif user_input == "2":

    from problem_2 import problem_2_dataset as data_2
    from problem_2.transcriber import Transcriber

    print(f"Problem 2: {problems[2]}")

    dna_sequence = data_2.dna_sequence
    transcriber = Transcriber(dna_sequence)
    rna_sequence = transcriber.get_rna_sequence()
    print(rna_sequence)

