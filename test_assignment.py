"""
Program: test_assignment.py
Author: Cody Kelderman
Date: 10/30/23
The first two methods on the test set up and tear downt he object.
The first test checks all required attributes are as they should be.
The second test checks funcitonality when all fields are entered.
The third test checks the string returned from __str__.
The fourth, fifth, sixth, and seventh tests validate the input for last name, first name, major, and gpa.
"""


import unittest
import study as s


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s.Student('Kelderman', 'Cody', 'CIS', 4.0)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Kelderman')
        self.assertEqual(self.student.first_name, 'Cody')
        self.assertEqual(self.student.major, 'CIS')

    def test_object_created_all_attributes(self):
        student = s.Student('Kelderman', 'Cody', 'CIS', 4.0) # this is not self.person from setUp, but local
        assert student.last_name == 'Kelderman'                 # note no self here on person or assert
        assert student.first_name == 'Cody'
        assert student.major == 'CIS'
        assert student.gpa == 4.0

    def test_student_str(self):
        self.assertEqual(str(self.student), "Kelderman, Cody has major CIS with gpa: 4.0")


    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = s.Student('123', 'Cody', 'CIS')

    def test_object_not_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            p = s.Student('Kelderman', '123','CIS', 4.0)
         
    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            p = s.Student('Kelderman', 'Cody', '123', 4.0)

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            p = s.Student('Kelderman', 'Cody', 'CIS', 5.0)

if __name__ == '__main__':
    unittest.main()
