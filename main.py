class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def rate_hw(self, lecturer, course, grade):
        # Студент выставляет оценку лектору. Лектор должен вести именно тот курс, на котором учится данный студент.

        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):

        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Создаем лекторов и закрепляем их за курсом
best_lecturer_1 = Lecturer('Sergey', 'Sergeev')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Miron', 'Fedorov')
best_lecturer_2.courses_attached += ['React']

best_lecturer_3 = Lecturer('Andrey', 'Smirnov')
best_lecturer_3.courses_attached += ['Python']

# Создаем проверяющих и закрепляем их за курсом
cool_reviewer_1 = Reviewer('Igor', 'Denisov')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['React']

cool_reviewer_2 = Reviewer('Vasiliy', 'Semenov')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['React']

# Создаем студентов и определяем для них изучаемые и завершенные курсы
student_1 = Student('Oleg', 'Sokolov')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Основы программирования']

student_2 = Student('Ivan', 'Kukushkin')
student_2.courses_in_progress += ['React']
student_2.finished_courses += ['Основы программирования']

student_3 = Student('Petr', 'Orlov')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Основы программирования']

# Выставляем оценки лекторам за лекции
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)

student_1.rate_hw(best_lecturer_2, 'Python', 5)
student_1.rate_hw(best_lecturer_2, 'Python', 7)
student_1.rate_hw(best_lecturer_2, 'Python', 8)

student_1.rate_hw(best_lecturer_1, 'Python', 7)
student_1.rate_hw(best_lecturer_1, 'Python', 8)
student_1.rate_hw(best_lecturer_1, 'Python', 9)

student_2.rate_hw(best_lecturer_2, 'React', 10)
student_2.rate_hw(best_lecturer_2, 'React', 8)
student_2.rate_hw(best_lecturer_2, 'React', 9)

student_3.rate_hw(best_lecturer_3, 'Python', 5)
student_3.rate_hw(best_lecturer_3, 'Python', 6)
student_3.rate_hw(best_lecturer_3, 'Python', 7)

# Выставляем оценки студентам за домашние задания
cool_reviewer_1.rate_hw(student_1, 'Python', 8)
cool_reviewer_1.rate_hw(student_1, 'Python', 9)
cool_reviewer_1.rate_hw(student_1, 'Python', 10)

cool_reviewer_2.rate_hw(student_2, 'React', 8)
cool_reviewer_2.rate_hw(student_2, 'React', 7)
cool_reviewer_2.rate_hw(student_2, 'React', 9)

cool_reviewer_2.rate_hw(student_3, 'Python', 8)
cool_reviewer_2.rate_hw(student_3, 'Python', 7)
cool_reviewer_2.rate_hw(student_3, 'Python', 9)
cool_reviewer_2.rate_hw(student_3, 'Python', 8)
cool_reviewer_2.rate_hw(student_3, 'Python', 7)
cool_reviewer_2.rate_hw(student_3, 'Python', 9)

print(f'Выставление оценок лекторам:')
print('Лектор 1:', f'{best_lecturer_1.name} {best_lecturer_1.surname}', '\n', 'Оценка за лекции:',
      f'{best_lecturer_1.grades}')
print('Лектор 2:', f'{best_lecturer_2.name} {best_lecturer_2.surname}', '\n', 'Оценка за лекции:',
      f'{best_lecturer_2.grades}')
print('Лектор 3:', f'{best_lecturer_3.name} {best_lecturer_3.surname}', '\n', 'Оценка за лекции:',
      f'{best_lecturer_3.grades}')
print()
print(f'Выставление оценок студентам:')
print('Студент 1:', f'{student_1.name} {student_1.surname}', '\n', 'Оценка за лекции:', f'{student_1.grades}')
print('Студент 2:', f'{student_2.name} {student_2.surname}', '\n', 'Оценка за лекции:', f'{student_2.grades}')
print('Студент 3:', f'{student_3.name} {student_3.surname}', '\n', 'Оценка за лекции:', f'{student_3.grades}')
