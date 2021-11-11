import random
lower_letter = "abcdefghijklmnopqurtsuvwzyz"
Upper_letter = "ABCDEFGHIJKLMNOPQURTSUVWZYZ"
Number = "0123456789"
Symbols = "()_!@#$%^:."
Password_Enter = int(input("Enter the character limit:"))
all = lower_letter + Upper_letter + Number + Symbols
lenght = Password_Enter
password = "".join(random.sample(all,lenght))
print("your password is:",password)