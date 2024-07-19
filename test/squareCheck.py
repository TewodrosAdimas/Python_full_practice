import unittest

def square(x):
    return (x*x)

class TestSquare(unittest.TestCase):
    def test__square(self):
        result = square(5)
        self.assertEqual(result,25)

    def test__inputCheck(self):
        result = str(type(square(5)))
        self.assertEqual(result,"<class 'int'>")

unittest.main()