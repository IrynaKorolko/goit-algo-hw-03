path = "salary_file.txt"
developer_count = 0
total_salary = 0

def calculate_salary (path):
     global developer_count, total_salary
     with open(path, "r", encoding="utf-8") as file:
          lines = file.readlines()
          for separate_line in lines:
              name, salary = separate_line.split(",")
              salary = int (salary)
              total_salary += salary
              developer_count += 1
     if developer_count > 0:
        average_salary = total_salary /developer_count
        return total_salary, average_salary
     else: 
        return 0, 0
total, average = calculate_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
