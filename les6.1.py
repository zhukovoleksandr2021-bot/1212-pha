file_path = r"C:SHARA//1212//Саша Жуков//1.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
