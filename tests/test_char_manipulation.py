import unittest
from python_core_exercise import PythonCoreExercise

class PythonCoreExerciseCharCounterTests(unittest.TestCase):
    testInput1 = ["geek", "gesek"]
    testInput2 = ["cut", "cat"]
    testInput3 = ["sunday", "saturday"]

    @classmethod
    def setUpClass(cls):
        cls.func = PythonCoreExercise()
    
    def test_char_manipulation1(self):
        self.assertEqual(self.func.char_manupilation(self.testInput1[0], self.testInput1[1]), "gesek")
    
    def test_char_manipulation2(self):
        self.assertEqual(self.func.char_manupilation(self.testInput2[0], self.testInput2[1]), "cat")
    
    def test_char_manipulation3(self):
        self.assertEqual(self.func.char_manupilation(self.testInput3[0], self.testInput3[1]), "saturday")


if __name__ == '__main__':
    unittest.main()