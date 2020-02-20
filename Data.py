
class Data:

    n_books = 0
    n_libraries = 0
    n_days = 0
    book_scores = []
    # [0] n_books
    # [1] n_signup_days
    # [2] n_books_per_days
    # [3] list_of_books_in_the_library
    libraries = []

    #
    library_with_book_id = {}

    def __init__(self, path):
        f = open(path)

        first_line = f.readline()
        split = first_line.split(" ")

        self.n_books = int(split[0])
        self.n_libraries = int(split[1])
        self.n_days = int(split[2])

        second_line = f.readline()
        split = second_line.split(" ")

        self.book_scores = [int(score) for score in split]

        for i in range(self.n_libraries * 2):
            first_line = f.readline()
            split = first_line.split()
            n_books = int(split[0])
            n_signup_days = int(split[1])
            n_books_per_days = int(split[2])

            second_line = f.readline()
            split = second_line.split(" ")
            book_ids = [int(id) for id in split]

            self.libraries.append( (n_books, n_signup_days, n_books_per_days, book_ids) )
            for id in book_ids:
                if id in self.library_with_book_id:
                    self.library_with_book_id[id].append(i)
                else:
                    self.library_with_book_id[id] = [i]
