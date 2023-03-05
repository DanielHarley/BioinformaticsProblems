from typing import List


class FibonacciSequence:

    def __init__(self, desired_month: int, multiplier: int):
        self.__month = desired_month
        self.__litter = multiplier
        self.__pairs_sequence: List[int] = []

        self.__create_sequence()

    def __create_sequence(self):
        for index in range(self.__month + 1):
            if index == 0 or index == 1:
                self.__pairs_sequence.append(1)
            else:
                number_of_pairs = self.__pairs_sequence[index - 1] + (self.__pairs_sequence[index - 2] * self.__litter)
                self.__pairs_sequence.append(number_of_pairs)

    def get_pairs_number(self):
        return self.__pairs_sequence[self.__month - 1]
