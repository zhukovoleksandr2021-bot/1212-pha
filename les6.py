# try:
#     a = int(input("input number a: "))
#     print(a)
# except ValueError as ve:
#     print("a must be a number")





# try:
#     a = int(input("input number a: "))
#     print(f"1 / {a}={1/a:.2f}")
# except ValueError as ve:
#     print("a має бути число")
# except ZeroDivisionError as zde:
#     print("1 бал за рік з алгебри")






users = {
    "admin": "18-23",
    "admin0.5": "14-18",
    "admin2": "23-30",
    "bot": "10-14",
    "bot0.5": "0-10"
}
l = input("Login: ")

try:
   print(users[l])
except KeyError as ke:
    print("неправильний логін")