study = Study("Study Plan A", "Description for Study Plan A", "2022-01-01", "2022-12-31")

math = Subject("Mathematics", "MATH101")
study.add_subject(math)

alice = Enrollment("Alice", math)
study.enroll_student(alice)

grade_1 = Grade(90, "A")
alice.add_grade(grade_1)

progress_1 = Progress("Good progress so far")
alice.add_progress(progress_1)

print(study.subjects) # prints [<__main__.Subject object at 0x7f43240402a0>]
print(study.enrollments) # prints [<__main__.Enrollment object at 0x7f43240403a0>]
print(alice.grades) # prints [<__main__.Grade object at 0x7f43240404a0>]
print(alice.progress_reports) # prints [<__main__.Progress object at 0x7f43240405a0>]