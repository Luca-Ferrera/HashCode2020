import numpy as np


class Data:
    n_books = 0
    n_libraries = 0
    n_days = 0
    book_scores = []
    # [0] library_id
    # [1] n_signup_days
    # [2] n_books_per_days
    # [3] list_of_books_in_the_library
    libraries = []

    #
    library_with_book_id = {}

    def __init__(self, path):
        f = open(path)

        first_line = f.readline()[:-1]
        split = first_line.split(" ")

        self.n_books = int(split[0])
        self.n_libraries = int(split[1])
        self.n_days = int(split[2])

        second_line = f.readline()[:-1]
        split = second_line.split(" ")

        self.book_scores = [int(score) for score in split]

        for i in range(self.n_libraries):
            first_line = f.readline()[:-1]
            split = first_line.split(" ")
            n_books = int(split[0])
            n_signup_days = int(split[1])
            n_books_per_days = int(split[2])

            second_line = f.readline()[:-1]
            split = second_line.split(" ")
            book_ids = [int(id) for id in split]

            self.libraries.append((i, n_signup_days, n_books_per_days, book_ids, 0))
            for id in book_ids:
                if id in self.library_with_book_id:
                    self.library_with_book_id[id].append(i)
                else:
                    self.library_with_book_id[id] = [i]


if __name__ == '__main__':
    # data = Data("/mnt/886c2f0d-8fd6-4d89-867f-29c7952c1d9d/project/HashCode2020/d_tough_choices.txt")
    data = Data("c_incunabula.txt")
    # [0] id
    # [1] n_signup_days
    # [2] n_books_per_days
    # [3] list_of_books_in_the_library

    gain = []

    for (id, signup_days, x, books, _) in data.libraries:
        scores = [data.book_scores[book] for book in books]
        total_scores = sum(scores)
        gain.append((
            id,
            total_scores / signup_days)
        )
        data.libraries[id] = (id, signup_days, x, books, total_scores / signup_days)

    # gain_sorted = sorted(gain, key=lambda x: x[1])[::-1]

    data.sorted_libraries = sorted(data.libraries, key=lambda x: x[4])[::-1]

    current_day = -1

    result = []

    while True:
        (id, signup_days, n_book_per_days, list_of_book, _) = data.sorted_libraries[0]
        current_day += signup_days
        remaining_days = data.n_days - current_day
        if remaining_days < 0:
            remaining_days = 0
            break
        if current_day <= data.n_days:
            n_book_to_be_shipped = min(n_book_per_days * remaining_days, len(list_of_book))
            shipped_book = list_of_book[0:n_book_to_be_shipped]
            if n_book_to_be_shipped > 0:
                result.append((
                    id,
                    n_book_to_be_shipped,
                    shipped_book
                ))
            for book in shipped_book:
                libraries = data.library_with_book_id[book]
                for id_lib in libraries:
                    data.libraries[id_lib][3].remove(book)
            # Recalculting the gain after removing the book
            gain = []

            for (id, signup_days, x, books, _) in data.libraries:
                scores = [data.book_scores[book] for book in books]
                total_scores = sum(scores)
                gain.append((
                    id,
                    total_scores / signup_days)
                )
                data.libraries[id] = (id, signup_days, x, books, total_scores / signup_days)
            data.sorted_libraries = sorted(data.libraries, key=lambda x: x[4])[::-1]

    # f = open("/mnt/886c2f0d-8fd6-4d89-867f-29c7952c1d9d/project/HashCode2020/d_result.txt", "w+")
    print(f"{len(result)}\n", end="")
    for (id, n, books) in result:
        print(f"{id} {n}\n", end="")
        for b in books:
            print(f"{b} ", end="")
        print("\n", end="")
