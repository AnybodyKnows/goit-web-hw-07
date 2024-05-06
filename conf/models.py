
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120))
    last_name = Column(String(120))
    email = Column(String(100))
    phone = Column('cell_phone', String(100))
    address = Column(String(100))
    start_work = Column(Date, nullable=False)

    @hybrid_property
    def fullname(self):
        return self.first_name + " " + self.last_name


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120))
    last_name = Column(String(120))
    email = Column(String(100))
    phone = Column('cell_phone', String(100))
    address = Column(String(100))
    group_id = Column(Integer, ForeignKey('groups.id', ondelete='CASCADE', onupdate='CASCADE'))

    @hybrid_property
    def fullname(self):
        return self.first_name + " " + self.last_name


class Subjects (Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    SubjectName = Column(String(255), nullable=False)
    TeacherID = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE', onupdate='CASCADE'))


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    StudentID = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'))
    SubjectID = Column(Integer, ForeignKey('subjects.id', ondelete='CASCADE'))
    Grade = Column(Integer, nullable=False)
    DateReceived = Column(Date, nullable=False)


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    group_name = Column(String, nullable=False)




