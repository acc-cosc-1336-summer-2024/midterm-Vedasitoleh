#write function tests here, don't add input('') statements here!
import unittest
from src.question_a.question_a import test_config
from src.question_a.question_a import reverse_string
from src.question_b.question_b import get_assessment_value
from src.question_b.question_b import get_tax_value
from src.question_c.question_c import is_prime
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

    #QUESTION B TESTS
    def test_get_assessment_value_1(self):
        #Test that 10000 returns 6000
        self.assertEqual(6000,get_assessment_value(10000))

    def test_get_assessment_value_2(self):
        #Test that 20000 returns 12000
        self.assertEqual(12000,get_assessment_value(20000))

    def test_get_tax_value_1(self):
        #Test that 6000 returns 43.2
        self.assertEqual(43.2,get_tax_value(6000))

    def test_get_tax_value_2(self):
        #Test that 10000 returns 72
        self.assertEqual(72,get_tax_value(10000))


    #QUESTION C TESTS
    def test_is_prime_1(self):
        #Test that 4 returns False
        self.assertEqual(False,is_prime(4))
    def test_is_prime_2(self):
        #Test that 5 returns True
        self.assertEqual(True,is_prime(5))
    def test_is_prime_3(self):
        #Test that 11 returns True
        self.assertEqual(True,is_prime(11))
        
    #QUESTION D TESTS
    def test_get_random_number(self):
        #test the number to make sure it generates number in the range of 1 to 5.
        answer = get_random_number()
        self.assertLessEqual(1,answer)
        self.assertGreaterEqual(5,answer)

