path = input("path: ")

try:
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
except FileNotFoundError as fnfe:
    print(f"File {path} not")