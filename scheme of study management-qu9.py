class Subject:
    def __init__(self, name, subject_code):
        self.name = name
        self.subject_code = subject_code

class Grade:
    def __init__(self, score, grade_letter):
        self.score = score
        self.grade_letter = grade_letter

class Progress:
    def __init__(self, progress_report):
        self.progress_report = progress_report

class Enrollment:
    def __init__(self, student_name, subject):
        self.student_name = student_name
        self.subject = subject
        self.grades = []
        self.progress_reports = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def add_progress(self, progress):
        self.progress_reports.append(progress)

class Study:
    def __init__(self, name, description, start_date, end_date):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.subjects = []
        self.enrollments = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def enroll_student(self, enrollment):
        self.enrollments.append(enrollment)