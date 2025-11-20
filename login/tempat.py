from auth import *

text = login()


if text == "admin":
    print("Menu Admin!")
elif text == "staff":
    print("Menu staff")