from src.core.database import engine
from src.auth.hashing import get_password_hash
from src.users.models import User


users = User.__tablename__

name = input('Name>>')
is_active = True

while True:
    password1 = input('Password>>')
    password2 = input('Password again>>')
    if password1 == password2:
        break
    print('Entered passwords are not the same. ')

hashed_password = get_password_hash(password1)


with engine.connect() as connection:
    print(hashed_password)
    # result = connection.execute(users.insert(), {''})
    # for row in result:
    #     print(row)


