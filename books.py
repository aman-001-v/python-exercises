class Book:

    def __init__(self , title , author , pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __repr__(self):
        return "Book({} , {} , {})".format(self.title , self.author , self.pages)
    
    def __str__(self):
        return "{} by {} ({})".format(self.title , self.author , self.pages)
    
    def __len__(self):
        return self.pages

    def __add__(self , other):
        return self.pages + other.pages

    def __eq__(self , other):
        if self.title == other.title and self.author == other.author and self.pages == other.pages:
            return True
        else:
            return False
    
    def __lt__(self , other):
        if self.pages == other.pages:
            print("EQUAL")
        elif self.pages > other.pages:
            print("{} has more pages".format(self.title))
        else:
            print("{} has more pages.".format(other.title))

    def __call__(self):
        print("Reading {}....".format(self.title))
            
    # @property
    # def title(self , title):
    #     self.title = title
    
    # @property
    # def author(self , author):
    #     self.author = author

    @property
    def description(self):
        return("{} by {}".format(self.title , self.author))
    
    @description.setter
    def description(self , info):
        self.title , self.author = info.split(" by ")
        print(self.title)
        print(self.author)

    # @title.setter
    # def title(self , title):
    #     self.title = title

    @description.deleter
    def description(self):
        self.title = None
        self.author = None

        print(self.title)
        print(self.author)


book1 = Book("Atomic Habits", "James Clear", 320)
book2 = Book("Python Crash Course", "Eric Matthes", 550)

print(book1)
print(repr(book1))

print(len(book1))

print(book1 + book2)

print(book1 == book2)

print(book1 < book2)

book1()

print(book1.description)

book1.title = "Deep Work"

print(book1.description)

book1.description = "Clean Code by Robert Martin"

print(book1.title)
print(book1.author)

del book1.description

print(book1.title)
print(book1.author)