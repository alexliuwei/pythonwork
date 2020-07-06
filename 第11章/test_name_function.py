import  unittest
from  name_function import get_name

class Name_Test(unittest.TestCase):
    def test_name_func(self):
        name = get_name('alex','liu')
        self.assertEqual(name,'Alex Liu')


if __name__ == '__main__':
    unittest.main()
