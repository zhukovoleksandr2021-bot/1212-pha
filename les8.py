import sqlite3 as sl3

connection = sl3.connect("academy.sl3")

cursor = connection.cursor()

cursor.execute("""
    create table IF NOT EXISTS STUDENT(
       id integer primary key,
       full_name text,
       age integer,
       email text,
      phone text,
      avg_score real,
       crystals integer,
       coins integer 
   );
""")

# cursor.execute("""
# INSERT INTO students (id, full_name, age, email, phone, avg_score, crystals, coins) VALUES
#         (1, 'Іваненко Іван', 20, 'ivanenko@gmail.com', '+380671234567', 10.5, 10, 150),
#         (2, 'Петренко Олена', 19, 'petrenko@gmail.com', '+380681112233', 11.8, 15, 200),
#         (3, 'Сидоренко Андрій', 21, 'sydorenko@gmail.com', '+380631234999', 7.2, 5, 90),
#         (4, 'Коваленко Марія', 22, 'kovalenko@gmail.com', '+380991112244', 12.0, 20, 300),
#         (5, 'Шевченко Дмитро', 20, 'shevchenko@gmail.com', '+380501234888', 9.1, 8, 120),
#         (6, 'Мельник Наталія', 19, 'melnyk@gmail.com', '+380671110000', 10.8, 12, 180),
#         (7, 'Ткаченко Олексій', 23, 'tkachenko@gmail.com', '+380931234777', 6.5, 4, 70),
#         (8, 'Бондар Юлія', 21, 'bondar@gmail.com', '+380661234666', 11.0, 14, 210),
#         (9, 'Гриценко Владислав', 20, 'grytsenko@gmail.com', '+380981234555', 8.7, 9, 140),
#         (10, 'Олійник Софія', 18, 'oliinyk@gmail.com', '+380731234444', 11.5, 18, 250);
# """)


score = input("score:")
age = input("age:")
cursor.execute(f"select * from students where avg_score >= {score}")
cursor.execute(f"select * from students where age == {age}")
connection.commit()

for student in cursor.fetchall():
    print(student)

connection.close()