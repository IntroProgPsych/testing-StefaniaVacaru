import unittest
from grading import grade_student


class TestGradeStudent(unittest.TestCase):
    # TODO:
    # - Write tests for typical values:
    #   * 95 -> "A"
    #   * 85 -> "B"
    #   * 75 -> "C"
    #   * 65 -> "D"
    #   * 30 -> "F"
    # - Write tests for boundary values:
    #   * 90 -> "A", 89 -> "B"
    #   * 80 -> "B", 79 -> "C"
    #   * 70 -> "C", 69 -> "D"
    #   * 60 -> "D", 59 -> "F"
    # - Write tests that check ValueError for:
    #   * score < 0
    #   * score > 100
    # - Use assertEqual for grades and assertRaises for invalid scores.
    #
    # write your tests here
    def test_grade_student(self):
        self.assertEqual(grade_student(95), "A")
    def test_grade_student(self):
        self.assertEqual(grade_student(85), "B")
    def test_grade_student(self):
        self.assertEqual(grade_student(75), "C")
    def test_grade_student(self):
        self.assertEqual(grade_student(65), "D")
    def test_grade_student(self):
        self.assertEqual(grade_student(30), "F")
    

if __name__ == "__main__":
    unittest.main()
