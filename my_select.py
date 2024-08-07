from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from models import Student, Grade, Course, Teacher, Group

def select_1(session: Session):
    return session.query(
        Student.fullname,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

def select_2(session: Session, course_name: str):
    return session.query(
        Student.fullname,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade).join(Course).filter(Course.name == course_name).group_by(Student.id).order_by(desc('avg_grade')).limit(1).first()

def select_3(session: Session, course_name: str):
    return session.query(
        Group.name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Student).join(Grade).join(Course).filter(Course.name == course_name).group_by(Group.id).all()

def select_4(session: Session):
    return session.query(
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).first()

def select_5(session: Session, teacher_name: str):
    return session.query(
        Course.name
    ).join(Teacher).filter(Teacher.fullname == teacher_name).all()

def select_6(session: Session, group_name: str):
    return session.query(
        Student.fullname
    ).join(Group).filter(Group.name == group_name).all()

def select_7(session: Session, group_name: str, course_name: str):
    return session.query(
        Student.fullname,
        Grade.grade
    ).join(Group).join(Grade).join(Course).filter(Group.name == group_name, Course.name == course_name).all()

def select_8(session: Session, teacher_name: str):
    return session.query(
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Course).join(Teacher).filter(Teacher.fullname == teacher_name).group_by(Teacher.id).first()

def select_9(session: Session, student_name: str):
    return session.query(
        Course.name
    ).join(Grade).join(Student).filter(Student.fullname == student_name).all()

def select_10(session: Session, student_name: str, teacher_name: str):
    return session.query(
        Course.name
    ).join(Grade).join(Student).join(Teacher).filter(Student.fullname == student_name, Teacher.fullname == teacher_name).all()
