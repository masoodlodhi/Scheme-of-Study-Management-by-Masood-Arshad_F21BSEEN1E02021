import unittest
from app import create_study, create_subject, enroll_student, add_grade, get_progress

class TestApp(unittest.TestCase):

    def test_create_study(self):
        # Test data
        study_name = "Study Plan A"
        study_description = "Description for Study Plan A"
        start_date = "2022-01-01"
        end_date = "2022-12-31"

        # Test method
        study = create_study(study_name, study_description, start_date, end_date)

        # Check if the study was created correctly
        self.assertEqual(study.name, study_name)
        self.assertEqual(study.description, study_description)
        self.assertEqual(study.start_date, start_date)
        self.assertEqual(study.end_date, end_date)

    # Add more test cases for other functions

if __name__ == "__main__":
    unittest.main()