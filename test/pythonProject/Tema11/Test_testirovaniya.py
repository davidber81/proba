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
        self.assertEqual(student1.distance, 1000, "Дистанции не равны" + str(student1.distance) + "!=1000")

    def test_sravnenie(self):
        student = Student("John")
        student1 = Student("Max")
        for _ in range(10):
            student1.run()
            student.walk()
        if student1.distance > student.distance:
            self.assertLess(student1.distance, student.distance,  "бегун должен преодолеть дистанцию больше, чем пешком")

    def test_sravnenie2(self):
        student = Student("John")
        student1 = Student("Max")
        for _ in range(10):
            student1.run()
            student.walk()
        if not student.distance > student1.distance:
            self.assertGreater(student.distance, student1.distance, "бегун должен преодолеть дистанцию больше, чем пешком")


if __name__ == '__main__':
    unittest.main()
