from typing import List

problems = {
    1: "Counting DNA Nucleotides",
    2: "Transcribing DNA into RNA",
    3: "Complementing a Strand of DNA",
    4: "Rabbits and Recurrence Relations",
    5: "Computing GC Content",
}

should_continue = True

while should_continue:
    for index in range(len(problems)):
        print(f"{index + 1}: {problems[index + 1]}.")

    print("")
    user_input = int(input(f"Which problem code output would you like to see? Choose from '1' to '{len(problems)}': "))
    print("")

    if user_input < 1 or user_input > len(problems):

        print("You chose a wrong number. Please, try again.")

    # Problem 1 - DNA nucleotide counter
    elif user_input == 1:

        from problem_1 import dataset as data_1
        from problem_1.dna_nucleotides_counter import DNACounter

        print(f"Problem 1: {problems[1]}")

        dna_counter = DNACounter(data_1.dna_sequence)
        nucleotides_count = dna_counter.get_nucleotides_count()

        print(nucleotides_count)

    # Problem 2 - Transcribing DNA into RNA
    elif user_input == 2:

        from problem_2 import dataset as data_2
        from problem_2.transcriber import Transcriber

        print(f"Problem 2: {problems[2]}")

        dna_sequence = data_2.dna_sequence
        transcriber = Transcriber(dna_sequence)
        rna_sequence = transcriber.get_rna_sequence()

        print(rna_sequence)

    # Problem 3 - Complementing a Strand of DNA
    elif user_input == 3:

        from problem_3 import dataset as data_3
        from problem_3.dna_polymerase import DNAPolymerase

        print(f"Problem 3: {problems[3]}")

        dna_polymerase = DNAPolymerase(data_3.dna_sequence)
        complementary_dna_sequence = dna_polymerase.get_new_dna_sequence()

        print(complementary_dna_sequence)

    # Problem 4 - Rabbits and Recurrence Relations
    elif user_input == 4:

        from problem_4 import dataset as data_4
        from problem_4.fibonacci_sequence import FibonacciSequence

        print(f"Problem 4: {problems[4]}")

        fibonacci_sequence = FibonacciSequence(desired_month=data_4.month_number, multiplier=data_4.born_rabbits)
        rabbit_pairs = fibonacci_sequence.get_pairs_number()

        print(rabbit_pairs)

    # Problem 5 - Computing GC Content
    elif user_input == 5:

        from problem_5.dna_gc_counter import DnaGCCounter

        print(f"Problem 5: {problems[5]}")

        dna_gc_counter = DnaGCCounter()
        highest_gc_dna = dna_gc_counter.get_highest_gc_percent_dna()

        print(f"{highest_gc_dna.get('name')}\n{highest_gc_dna.get('gc_percentage')}")

    print("")
    user_choice = input("Would you like to see more bioinformatics problems? Type 'y' or 'n': ").lower()

    if user_choice == "n":
        print("Ending program.")
        should_continue = False
