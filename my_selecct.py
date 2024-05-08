from sqlalchemy import func
from conf.db import session
from conf.models import Student, Grade, Subjects, Teacher, Group


def select_1():
    top_students = session.query(
        Student.id,
        Student.fullname,
        func.round(func.avg(Grade.Grade), 2).label('average_grade')
    ).join(
        Grade
    ).group_by(
        Student.id
    ).order_by(
        func.avg(Grade.Grade).desc()
    ).limit(5).all()
    return top_students


def select_2(subject_name):
    best_student_subject = session.query(
        Student.id,
        Student.fullname,
        Subjects.SubjectName,
        func.round(func.avg(Grade.Grade), 2).label('average_grade')
    ).select_from(Student).join(
        Grade
    ).join(
        Subjects
    ).filter(
        Subjects.SubjectName == subject_name
    ).group_by(
        Student.id, Subjects.SubjectName
    ).order_by(
        func.avg(Grade.Grade).desc()
    ).first()
    return best_student_subject


def select_3(subject_name):
    average_grade_by_group = (session.query(
        Group.group_name,
        Subjects.SubjectName,
        func.avg(Grade.Grade).label('average_grade')
    ).join(
        Student,
        Student.group_id == Group.id
    ).join(
        Grade
    ).join(
        Subjects
    ).filter(
        Subjects.SubjectName == subject_name
    ).group_by(
        Group.group_name, Subjects.SubjectName
    ).all())
    return average_grade_by_group


def select_4():
    average_grade_overall = session.query(
        func.avg(Grade.Grade).label('average_grade')
    ).scalar()
    return average_grade_overall


def select_5(teacher_id):
    courses_taught_by_teacher = session.query(
        Teacher.fullname,
        Subjects.SubjectName
    ).join(
        Teacher
    ).filter(
        Teacher.id == teacher_id
    ).all()
    return courses_taught_by_teacher


def select_6(group_id):
    students_in_group = session.query(
        Group.group_name,
        Student.fullname
    ).join(
        Group
    ).filter(
        Student.group_id == group_id
    ).all()
    return students_in_group


def select_7(group_id, subject_name):
    grades_in_group_for_subject = session.query(
        Student.fullname,
        Grade.Grade
    ).join(
        Grade
    ).join(
        Subjects
    ).filter(
        Student.group_id == group_id,
        Subjects.SubjectName == subject_name
    ).all()
    return grades_in_group_for_subject


def select_8(teacher_id):
    average_grade_by_teacher = session.query(
        func.avg(Grade.Grade).label('average_grade')
    ).join(
        Subjects
    ).filter(
        Subjects.TeacherID == teacher_id
    ).scalar()
    return average_grade_by_teacher


def select_9(student_id):
    courses_attended_by_student = session.query(
        Subjects.SubjectName
    ).join(
        Grade
    ).join(
        Student
    ).filter(
        Student.id == student_id
    ).distinct().all()
    return courses_attended_by_student


def select_10(student_id, teacher_id):
    courses_taught_to_student_by_teacher = session.query(
        Subjects.SubjectName
    ).join(
        Grade
    ).join(
        Student
    ).join(
        Teacher
    ).filter(
        Student.id == student_id,
        Teacher.id == teacher_id
    ).distinct().all()
    return courses_taught_to_student_by_teacher


if __name__ == "__main__":
    print(select_1())

    print(select_2("Стоматолог"))

    print(select_3("Стоматолог"))

    print(select_4())

    print(select_5(17))

    print(select_6(11))

    print(select_7(11, "Філолог"))

    print(select_8(17))

    print(select_9(102))

    print(select_10(101, 17))
