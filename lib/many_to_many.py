class Author:
    all = []
    def __init__(self,name):
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        #return list of realted contracts
        my_contracts = []
        for contract in Contract.all:
            if contract.author is self:
                my_contracts.append(contract)
        return my_contracts
    
    def books(self):
        my_books = []
        for contract in self.contracts():
            my_books.append(contract.book)
        return my_books
    
    def sign_contract(self, book,date, royalties):
        new_contract = Contract(self,book,date,royalties)
        return new_contract
    
    def total_royalties(self):
        my_royalties = 0
        for contract in self.contracts():
            my_royalties += contract.royalties
        return my_royalties


class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        my_contracts = []
        for contract in Contract.all:
            if contract.book is self:
                my_contracts.append(contract)
        return my_contracts
    
    def authors(self):
        my_authors = []
        for contract in self.contracts():
            my_authors.append(contract.author)
        return my_authors



class Contract:
    all = []
    def __init__(self,author,book,date,royalties):

        self._author = None
        self._book = None
        self._date = None
        self._royalties = None


        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,new_author):
        if isinstance(new_author,Author):
            self._author = new_author
        else:
            raise Exception("wrong type")

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self,new_book):
        if isinstance(new_book,Book):
            self._book = new_book
        else:
            raise Exception("wrong type")
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self,new_date):
        if isinstance(new_date,str):
            self._date = new_date
        else:
            raise Exception("wrong type")

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self,new_royalties):
        if isinstance(new_royalties,int):
            self._royalties = new_royalties
        else:
            raise Exception("wrong type")

    
    @classmethod
    def contracts_by_date(cls,date):
        my_contracts = []
        for contract in cls.all:
            if contract.date == date:
                my_contracts.append(contract)
        return my_contracts
