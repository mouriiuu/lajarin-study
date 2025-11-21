from auth import login

role = login()

if role == "admin":
    print('kamu admnin')
elif role == "staff":
    print('kamu staff')
else:
    print('tidak ada')