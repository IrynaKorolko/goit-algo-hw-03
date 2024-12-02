from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
		pass

class Phone(Field):
	def __init__(self, value):
        if not value.isdigit() or len (value) != 10:
            raise ValueError
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone (self, phone):
            self.phones.append (Phone (phone))

    def remove_phone (self, phone):
            for p in self.phones:
                if p.value == phone:
                    self.phones.remove(p)
                    return 
            raise ValueErroralueError (f"Phone {phone} not found")
    
    def edit_phone (self, old_phone, new_phone):
            for p in self.phones:
                if p.value == old_phone:
                        self.phones.remove(p)
                        self.add_phone(new_phone)
                        return
            raise ValueError (f"Phone {old_phone} not found")
    
    def find_phones (self, phone):
            for p in self.phones:
                    if p.value == phone:
                            return p
                    return NotImplemented
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict): 
	def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError(f"Record with name {name} not found")
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
    
              