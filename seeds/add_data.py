import random

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Student, Teacher, Grade, Subjects, Group


fake = Faker('uk-UA')
"""Заповніть отриману базу даних випадковими даними (~30-50 студентів, 3 групи, 5-8 предметів, 
3-5 викладачів, до 20 оцінок у кожного студента з усіх предметів)."""


def insert_groups():
    for _ in range(3):
        group = Group(
            group_name=fake.word()
        )
        session.add(group)


def insert_students():
    groups = session.query(Group).all()
    for _ in range(30):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=str(fake.phone_number()),
            address=fake.address(),
            group_id=random.choice(groups).id
        )
        session.add(student)


def insert_teachers():
    for _ in range(5):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
            start_work=fake.date_between(start_date='-3y')
        )
        session.add(teacher)


def insert_subjects():
    teachers = session.query(Teacher).all()
    for _ in range(5):
        subject = Subjects(
            SubjectName=fake.job(),
            TeacherID=random.choice(teachers).id
        )
        session.add(subject)


def insert_grades():
    students = session.query(Student).all()
    subjects = session.query(Subjects).all()
    for student in students:
        for subject in subjects:
            grade = Grade(
                StudentID=student.id,
                SubjectID=subject.id,
                Grade=random.randint(0, 100),
                DateReceived=fake.date_between(start_date='-2y')
            )
            session.add(grade)


if __name__ == '__main__':
    try:
        insert_groups()
        insert_students()
        insert_teachers()
        insert_subjects()
        insert_grades()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()
