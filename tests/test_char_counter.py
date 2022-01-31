import unittest
from python_core_exercise import PythonCoreExercise

class PythonCoreExerciseCharCounterTests(unittest.TestCase):
    testInput = "P@#yn26at^&i5ve"

    @classmethod
    def setUpClass(cls):
        cls.func = PythonCoreExercise()
    
    def test_char_counter(self):
        self.assertEqual(self.func.char_counter(self.testInput), (8, 3, 4))


if __name__ == '__main__':
    unittest.main()