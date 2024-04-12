import unittest
from Student import Student

class RunningTests(unittest.TestCase, Student):

    def setUp(self):
        self.distance = 0

    def test_walk(self):
        student = Student("John")
        for _ in range(10):
            student.walk()
        self.assertEqual(student.distance, 500, "Дистанции не равны" + str(student.distance) + "!= 500")

    def test_run(self):
        student1 = Student("Max")
        for _ in range(10):
            student1.run()
        self.assertGreater(student1.distance, 1000, "Дистанции не равны" + str(student1.distance) + "!=1000")

    def test_sravnenie(self):
        student = Student("John")
        student1 = Student("Max")
        if student1 > student:
            self.assertLess(student1.distance, 1000, "должен преодолеть дистанцию больше, чем", student.distance, 500)


if __name__ == '__main__':
    unittest.main()