import mysql.connector
from tkinter import*

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="mydatabase"
)
mycursor = mydb.cursor()

class User:
    def __init__(self, name, surname, nickname, password, email, country):
        self.name = name
        self.surname = surname
        self.nickname = nickname
        self.password = password
        self.email = email
        self.country = country

#correct
def add_user() -> None:

    print("Please insert some info down below")
    name_ = input("What's your name: ")
    surname_ = input("What's your surname: ")
    nickname_ = input("What's is your desired nickname: ")
    password_ = input("Insert your new password to protect your data: ")
    email_ = input("In case of an emergency give us your e-mail: ")
    country_ = input("Where do You live: ")

    new_user = User(name_, surname_, nickname_, password_, email_, country_)


    sql_values = (str(new_user.name), str(new_user.surname),
                  str(new_user.nickname), str(new_user.password),
                  str(new_user.email), str(new_user.country))

    sql_insert = "INSERT INTO users (name, surname, nickname, password," \
                 " email, country) VALUES (%s, %s, %s, %s, %s, %s)"

    mycursor.execute(sql_insert, sql_values)
    mydb.commit()


#correct
def delete_an_account() -> None:
    print("Please insert a nickname of an account that You want to delete")
    nickname_ = input("Nickname is: ")
    password_ = input("Assure us with your password: ")
    values = (nickname_, password_)
    mycursor.execute("DELETE FROM users WHERE nickname = %s \
     AND password = %s", values)
    mydb.commit()


#corrrect
def get_id(nickname_: str, password_: str) -> int:
    values = (nickname_, password_)
    mycursor.execute("SELECT id FROM users WHERE nickname =%s \
     AND password =%s", values)
    result = mycursor.fetchone()
    return result[0]


#correct
def update_password(nickname_: str) -> None:
    old_password = input("Your current password is: ")
    new_password = input("Your new password is: ")
    values = (new_password, nickname_, old_password)
    mycursor.execute("UPDATE users SET password = %s WHERE nickname = %s \
     AND password = %s", values)
    mydb.commit()


#correct
def update_email(nickname_: str, password_: str):
    new_email = input("Give us your new email: ")
    values = (new_email, nickname_, password_)
    mycursor.execute("UPDATE users SET email = %s WHERE nickname = %s \
     AND password = %s", values)
    mydb.commit()

