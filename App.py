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

            self.libraries.append( (i, n_signup_days, n_books_per_days, book_ids) )
            for id in book_ids:
                if id in self.library_with_book_id:
                    self.library_with_book_id[id].append(i)
                else:
                    self.library_with_book_id[id] = [i]


if __name__ == '__main__':
    data = Data("/mnt/886c2f0d-8fd6-4d89-867f-29c7952c1d9d/project/HashCode2020/b_read_on.txt")
    # [0] n_books
    # [1] n_signup_days
    # [2] n_books_per_days
    # [3] list_of_books_in_the_library
    data.sorted_libraries = sorted(data.libraries, key=lambda x: x[1])

    current_day = -1

    result = []

    for (id, signup_days, n_book_per_days, list_of_book) in data.sorted_libraries:
        current_day += signup_days
        remaining_days = data.n_days - current_day
        if current_day <= data.n_days:
            n_book_to_be_shipped = min(n_book_per_days * remaining_days, len(list_of_book))
            shipped_book = list_of_book[0:n_book_to_be_shipped]
            result.append((
                id,
                n_book_to_be_shipped,
                shipped_book
            ))

    # f = open("/mnt/886c2f0d-8fd6-4d89-867f-29c7952c1d9d/project/HashCode2020/b_result.txt", "w+")
    # f.write(f"{len(result)}\n")
    # for (id, n, books) in result:
    #     f.write(f"{id} {n}\n")
    #     for b in books:
    #         f.write(f"{b} ")
    #     f.write("\n")
    #     print(id)
    #     print(books)


    f = open("/mnt/886c2f0d-8fd6-4d89-867f-29c7952c1d9d/project/HashCode2020/b_result.txt", "w+")
    print(f"{len(result)}\n", end="")
    for (id, n, books) in result:
        if n > 0:
            print(f"{id} {n}\n", end="")
            for b in books:
                print(f"{b} ", end="")
            print("\n", end="")

