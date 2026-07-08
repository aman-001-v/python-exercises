class book:
    total_books = 0
    def __init__(self , title , author , pages):
        self.title = title
        self.author = author
        self.pages = pages
        book.total_books += 1
    
    def description(self):
        print("{} by {} ({})".format(self.title , self.author , self.pages))
    def is_long_book(self):
        if self.pages > 300:
            return True
        else:
            return False
    def change_pages(self ,  new_pages):
        self.pages = new_pages