#  File: TomeRster.py   
#    by: John Prokop | jproto1/_at_/verizon.net
# Notes: Book rating skeleton for Codecademy course: Programming 
#         with Python - Intensive 10/2018
################################################################################
from collections import Counter 

debug = False

# ===== Debug Utilities
def dbg_print(s):
    if debug == True:
        print(s)


# ========= User: name, email
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        if '@' in address:
            self.email = address
            print("Email address has been updated")

    def __repr__(self):
        l=0
        if self.books != None:
            l = len(self.books)
        return("{} has read {} books.".format(self.name, l))

    def __eq__(self, other_user):
        return( self.name == other_user.name and 
            self,email == other_user.email )

    # Additional Methods

    def read_book(self, book, rating=None):
        self.books[book] = rating
        #book.add_rating(rating)
    
    # Avg of all Books rated by User
    def get_average_rating(self):
        total_ratings=0
        num_ratings=0
        b_list = self.books.keys()
        for b in b_list:
            rate = self.books[b]
           # for rate in bv:
            if(rate != None):
                num_ratings += 1
                total_ratings += rate
        if(num_ratings > 0):
            return total_ratings/num_ratings 
        else:
            return 0;

    # My Added methods
    # Return user email, book count for user
    def get_user_book_ct(self):
        l=0
        if self.books != None:
            l = len(self.books)
        return(self.email, l)


# ========= Book: title, isbn 
class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("Book's ISBN has been updated.\n")

    def add_rating(self, rating):
        if (rating != None) and (rating>=0 and rating<5):
            self.ratings.append(rating)
    
    def __eq__(self, other):
        return( self.get_title() == other.get_title() and
                self.isbn == other.isbn)

    # Additional Methods

    # Avg of all ratings of Book
    def get_average_rating(self):
        sum_ratings = 0
        num_ratings = len(self.ratings)
        if num_ratings == 0:
            return 0
        for r in self.ratings:
            sum_ratings+=r
        return sum_ratings/num_ratings

    # Massage into Hashability
    def __hash__(self):
        return hash((self.title, self.isbn))

    # My Added methods
    def __repr__(self):
        return ("\'{}\' ISBN: {}".format(self.get_title(), self.get_isbn())) 

# ========= Fiction: title, author, isbn
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    # Added ISBN to repr string
    def __repr__(self):
        return ("\'{}\' by {}   ISBN: {}".format(self.get_title(), self.get_author(), self.get_isbn())) 

# ========= Non_Fiction: title, subject, level, isbn
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    # Added ISBN to repr string
    def __repr__(self):
        return("\'{}\', a {} manual on {}   ISBN: {}".format(self.get_title(), 
            self.get_level(), self.get_subject(), self.get_isbn()))


# ========= TomeRater
class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email not in self.users:
            print("No user with email {}!".format(email))
        else:
            u = self.users[email]
            u.read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books:
                self.books[book] = 1 
                dbg_print("{} added for {}".format( book.title, email))
            else:
                self.books[book] += 1 
                dbg_print("(+1) {} incremented for {} -> {}".format( book.title, email, self.books[book]))
                 

    def add_user(self, name, email, user_books = None):
        u = User(name, email)
        dbg_print("adding user {}:{}".format(name, email))
        self.users[email] = u
        if user_books != None:
            for b in user_books:
                dbg_print("+++ adding book {} to {}".format(b.title, name))
                self.add_book_to_user(b, email)

    def print_catalog(self):
        print("Current Catalog of all Books =========")
        b_list = self.books.keys()
        for b in b_list:
            print(b)
        print("")

    def print_users(self):
        print("All Current Users --------")
        user_list = self.users.values()
        for u in user_list:
            print(u)
        print("")

    def most_read_book(self):
        max_read = 0
        book_list = self.books.keys()
        max_book = None
        for b in book_list:
            r = self.books[b]
            if r > max_read:
                max_read = r
                max_book = b
        return max_book

    # populate.py test driver called 'get_most_read_book()', so I added pass through wrapper:
    def get_most_read_book(self):
        return self.most_read_book()

    def highest_rated_book(self):
        max_rating = 0
        b_list = self.books.keys()
        max_book = None
        for b in b_list:
            b_rating = b.get_average_rating()
            if b_rating > max_rating:
                max_rating = b_rating
                max_book = b
        return max_book

    def most_positive_user(self):
        max_rating = -1
        max_user = None
        user_emails = self.users.keys()
        for u in user_emails:
            r = self.users[u].get_average_rating()
            if r > max_rating:
                max_user = u
                max_rating = r
        return self.users[max_user].name

    # My Added methods
    def get_n_most_read_books(self, n=3, q_print=False):
        ct = Counter(dict(self.books)).most_common(n)
        if q_print == True:
            print("{} Most Read Books--------".format(n))
            for c in ct:
                print("{} has been read {} times.".format(c[0], c[1]))
        else:
            return ct

    def get_n_most_prolific_readers(self, x=3, q_print=False):
        u_num_dict = {}
        u_list = self.users.values()
        for u in u_list:
            e,n = u.get_user_book_ct()
            u_num_dict[e] = n
        #print(u_num_dict)
        ct = Counter(dict(u_num_dict)).most_common(x)
        if q_print == True:
            print("{} Most Prolific Readers --------".format(x))
            for c in ct:
                print("{} has read {} books.".format(self.users[c[0]].name, c[1]))
        else:
            return ct


