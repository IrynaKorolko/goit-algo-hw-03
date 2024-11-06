path = "cats_file.txt"

def get_cats_info(path):
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        cats_info_list = []
        for separate_line in lines:
             id, name, age = separate_line.strip().split(',')
             cats_info_list.append ({"id": id, "name": name, "age": age})
        print (f"Словник {cats_info_list}")
        return cats_info_list
cats_info = get_cats_info(path) 


