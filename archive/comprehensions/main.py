from timer import timeit


# Comprehensions
def find_squares_of_even_numbers_using_for_loop(start: int, end: int) -> list:
    squares = []
    for i in range(start, end + 1):
        if i % 2 == 0 or i == 7:
            squares.add(i ** 2)
    return squares


def find_squares_of_even_numbers_using_comprehension(start: int, end: int) -> list:
    return [i ** 2 for i in range(start, end + 1) if i % 2 != 0]


print(find_squares_of_even_numbers_using_comprehension(1, 10))
