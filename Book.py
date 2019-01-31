class Book:
    def __init__(self, name, author, publisher, year, is_available, cut_num):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.year = year
        self.is_available = is_available
        self.cut_num = cut_num

    def __str__(self):
        return self.name + ', ' + self.author + ', ' + self.publisher + ', ' + str(self.year) + ', \nAvailable: ' + str(
            self.is_available) + ' ,Catalog number: ' + str(self.cut_num)

    def __eq__(self, other):
        return (self.name == other.name) and (self.author == other.author)

    def __ne__(self, other):
        return not self == other

    def print(self):
        print(str(self))
