
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def display_info(self):
        print(f"Title: {self.title}",f"Author: {self.author}",f"Pages: {self.pages}" )
        

#instance
book1 = Book("God is Great", "Vivianritah", 50)
book1.display_info() #displaying



#(iii)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_title_and_author(self):
        return f"Title: {self.title} - Author: {self.author}"

book = Book("God is Great", "Vivianritah")
print(book.get_title_and_author()) 


#(iv)
#Class refers to the blue print for creating objects.
#object is the data field with unique attributes.