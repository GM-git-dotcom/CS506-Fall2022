class Library:
    def __init__(self, name, location, n_floors):
        self.name = name
        self.location = location
        self.n_floors = n_floors

    def __repr__(self):
        s_name = "Name of library: {}".format(self.name)
        s_location = "Location of library: {}".format(self.location)
        s_n_floors = "Number of floors in library: {}".format(self.n_floors)
        combined_str = s_name+"\n"+s_location+"\n"+s_n_floors
        return combined_str
        

class Book(Library):
    def __init__(self, title, author, n_pages, floor, name, location, n_floors):
        self.title = title
        self.author = author
        self.n_pages = n_pages
        self.floor = floor
        super().__init__(name, location, n_floors)

    def __repr__(self):
        s_title = "Title of book: {}".format(self.title)
        s_author = "Name of author: {}".format(self.author)
        s_n_pages = "Number of pages: {}".format(self.n_pages)
        s_floor = "Located on floor: {}".format(self.floor)
        combined_str = s_title+"\n"+s_author+"\n"+s_n_pages+"\n"+s_floor
        print(super().__repr__())
        print()
        return combined_str


#mugar = Library("Mugar", "650 Comm Ave", 5)
b1 = Book("The Da Vinci Code", "Dan Brown", 450, 2, "Mugar", "650 Comm Ave", 5)
b2 = Book("A room on the roof", "Ruskin Bond", 300, 2, "Mugar", "650 Comm Ave", 5)


print(b1)
print(b2)
    

    


def draw_library():
    print("library not found")
    return
