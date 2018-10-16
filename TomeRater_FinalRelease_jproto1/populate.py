from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])
                                                                #"Society of Mind"
                                                                 #"Alice In Wonderland"
                                                                  #"Automate the Boring Stuff"

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)       #"Society of Mind"
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)       #"Alice In Wonderland"
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)   #"Automate the Boring Stuff"
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)    #"Computing Machinery and Intelligence"
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)          #"There Will Come Soft Rains"

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)            #"The Diamond Age"
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)           #"There Will Come Soft Rains"
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)    #"There Will Come Soft Rains"


#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.get_most_read_book())

#Test new methods
print("3 most read books:")
print(Tome_Rater.get_n_most_read_books(3))

print("2 most prolific readers:")
print(Tome_Rater.get_n_most_prolific_readers(2))
