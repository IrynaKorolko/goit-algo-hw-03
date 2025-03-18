import pickle 

class Person:
    def __init__ (self, name, email, phone, favorite):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

class AddressBook:
    def __init__(self):
        self.contacts = []
    def add_contact (self, person):
        self.contacts.append (person)
    def __str__ (self):
        return "\n".join([f"{contact.name} - {contact.phone}" for contact in self.contacts])
                         
    def save_data(self,filename= "addressbook.pkl"):
        with open (filename, "wb") as f:
            pickle.dump (self, f)

    @classmethod
    def load_data(cls, filename = "addressbook.pkl"):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)  
        except (FileNotFoundError, EOFError):
            return cls()
def main():
        book = AddressBook.load_data()
        if not book.contacts:
            person1 = Person("John Doe", "john@example.com", "123-456-7890", True)
            person2 = Person("Jane Smith", "jane@example.com", "987-654-3210", False)
            book.add_contact(person1)
            book.add_contact(person2)
            book.save_data ()

        print("Address Book:")
        print(book)

if __name__ == "__main__":
    main()
