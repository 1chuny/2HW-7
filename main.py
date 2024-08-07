from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from my_select import select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9, select_10
from models import Base

DATABASE_URL = "postgresql://postgres:admin@localhost/mydatabase"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# Примеры выполнения запросов
print(select_1(session))
print(select_2(session, 'Math'))
print(select_3(session, 'Math'))
print(select_4(session))
print(select_5(session, 'Teacher Name'))
print(select_6(session, 'Group 1'))
print(select_7(session, 'Group 1', 'Math'))
print(select_8(session, 'Teacher Name'))
print(select_9(session, 'Student Name'))
print(select_10(session, 'Student Name', 'Teacher Name'))

session.close()
