import pytest
from Source.school import Classroom, Teacher, Student, TooManyStudents

### 🧙 Fixtures ###

@pytest.fixture
def hogwarts_teacher():
    return Teacher("Minerva McGonagall")

@pytest.fixture
def transfiguration_students():
    return [Student(name) for name in [
        "Hermione Granger", "Harry Potter", "Ron Weasley", "Neville Longbottom"
    ]]

@pytest.fixture
def full_class_students():
    return [Student(f"Student {i}") for i in range(11)]

@pytest.fixture
def transfiguration_class(hogwarts_teacher, transfiguration_students):
    return Classroom(hogwarts_teacher, transfiguration_students, "Transfiguration")


### 🧪 Tests ###

def test_add_student_success(transfiguration_class):
    new_student = Student("Luna Lovegood")
    transfiguration_class.add_student(new_student)
    assert new_student in transfiguration_class.students
    assert len(transfiguration_class.students) == 5

def test_add_student_raises_if_too_many():
    prof_flitwick = Teacher("Filius Flitwick")
    students = [Student(f"Student {i}") for i in range(11)]
    charms_class = Classroom(prof_flitwick, students, "Charms")
    
    with pytest.raises(TooManyStudents):
        charms_class.add_student(Student("Extra Student"))

@pytest.mark.parametrize("student_name", [
    "Hermione Granger",
    "Ron Weasley",
])
def test_remove_student(transfiguration_class, student_name):
    transfiguration_class.remove_students(student_name)
    names = [student.name for student in transfiguration_class.students]
    assert student_name not in names

def test_change_teacher(transfiguration_class):
    new_teacher = Teacher("Albus Dumbledore")
    transfiguration_class.change_teacher(new_teacher)
    assert transfiguration_class.teacher.name == "Albus Dumbledore"

@pytest.mark.slow
def test_large_class_behavior():
    teacher = Teacher("Severus Snape")
    students = [Student(f"Slytherin {i}") for i in range(10)]
    potions_class = Classroom(teacher, students, "Potions")
    new_student = Student("Draco Malfoy")
    
    # Should succeed when adding 11th student only if limit not yet hit
    potions_class.add_student(new_student)
    assert new_student in potions_class.students
    assert len(potions_class.students) == 11

    # Now it should raise an error
    with pytest.raises(TooManyStudents):
        potions_class.add_student(Student("Crabbe"))


### Extra test: Removing a non-existent student ###
def test_remove_nonexistent_student_does_nothing(transfiguration_class):
    before = transfiguration_class.students.copy()
    transfiguration_class.remove_students("Draco Malfoy")  # Not in list
    after = transfiguration_class.students
    assert before == after
