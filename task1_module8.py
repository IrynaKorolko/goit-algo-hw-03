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
    def add_contacts (self, person):
        self.contacts.append (person)
    def __str__ (self):
        return "\n".join([f"{contact.name} - {contact.phone}" for contact in self.contacts])
                         
    def save_data (book,filename= "addressbook.pkl"):
        with open (filename, "wb") as f:
            pickle.dump (book, f)

    def load_data (filename = "addressbook.pkl"):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)  
        except FileNotFoundError:
            return AddressBook()
def main():
        book = AddressBook.load_data()
if __name__ == "__main__":
    main()
