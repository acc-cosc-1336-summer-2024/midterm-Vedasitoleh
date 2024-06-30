#write function tests here, don't add input('') statements here!
import unittest
from src.question_a.question_a import test_config
from src.question_a.question_a import reverse_string
from src.question_d.question_d import get_random_number
#follow this example to add questions b, c, and d for testing including their functions

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    #QUESTION A TESTS
    def test_reverse_string_1(self):
        #test that the function reverses hello correctly
        self.assertEqual('olleh', reverse_string('hello'))
    def test_reverse_string_2(self):
        #test that the function reverses hello world correctly
        self.assertEqual('dlrow olleh', reverse_string('hello world'))

    #QUESTION D TESTS
    def test_get_random_number(self):
        #test the number to make sure it generates number in the range of 1 to 5.
        answer = get_random_number()
        self.assertLessEqual(1,answer)
        self.assertGreaterEqual(5,answer)

