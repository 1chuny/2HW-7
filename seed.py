import random
from datetime import date
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Group, Teacher, Course, Grade

DATABASE_URL = "postgresql://postgres:admin@localhost/mydatabase"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
fake = Faker()

def create_groups():
    groups = [Group(name=f'Group {i}') for i in range(1, 4)]
    session.add_all(groups)
    session.commit()
    return groups

def create_teachers():
    teachers = [Teacher(fullname=fake.name()) for _ in range(5)]
    session.add_all(teachers)
    session.commit()
    return teachers

def create_courses(teachers):
    courses = [Course(name=fake.word().capitalize(), teacher=random.choice(teachers)) for _ in range(8)]
    session.add_all(courses)
    session.commit()
    return courses

def create_students(groups):
    students = [Student(fullname=fake.name(), group=random.choice(groups)) for _ in range(50)]
    session.add_all(students)
    session.commit()
    return students

def create_grades(students, courses):
    for student in students:
        for course in courses:
            grades = [Grade(student=student, course=course, grade=random.uniform(1, 10), date_received=fake.date_this_year()) for _ in range(random.randint(1, 20))]
            session.add_all(grades)
    session.commit()

def main():
    groups = create_groups()
    teachers = create_teachers()
    courses = create_courses(teachers)
    students = create_students(groups)
    create_grades(students, courses)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    main()
