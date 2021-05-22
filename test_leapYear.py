import unittest
from unittest.mock import patch
import leapYear
import io
import sys

class testCase_leapYear(unittest.TestCase):
    #Testing if userinput as a string
    numberInput = '2012'
    @patch('builtins.input', return_value = numberInput)
    def test_string_of_ints(self, mock_input):
        self.assertRaises(TypeError, leapYear.checkLeapYear())

    #Inputting an integer as the userInput and is a leap year
    numberInput = 2012
    @patch('builtins.input', return_value = numberInput)
    def test_number_isLeap(self, mock_input):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        leapYear.checkLeapYear()
        result = capturedOutput.getvalue()
        self.assertEqual(result, "2012 is a leap year.\n")

    #Inputting an integer as the userInput and isnt a leap year
    numberInput = 20013
    @patch('builtins.input', return_value = numberInput)
    def test_number_notLeap(self, mock_input):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        leapYear.checkLeapYear()
        result = capturedOutput.getvalue()
        self.assertEqual(result, "20013 is not a leap year.\n")

    #Inputting a negative number
    numberInput = -2012
    @patch('builtins.input', return_value = numberInput)
    def test_number_neg(self, mock_input):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        leapYear.checkLeapYear()
        result = capturedOutput.getvalue()
        self.assertEqual(result, "-2012 is a leap year.\n")

    #Testing negative edge case
    numberInput = -500
    @patch('builtins.input', return_value = numberInput)
    def test_number_neg_edge(self, mock_input):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        leapYear.checkLeapYear()
        result = capturedOutput.getvalue()
        self.assertEqual(result, "-500 is not a leap year.\n")

    #Testing negative edge case
    numberInput = -400
    @patch('builtins.input', return_value = numberInput)
    def test_number_neg_edge2(self, mock_input):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        leapYear.checkLeapYear()
        result = capturedOutput.getvalue()
        self.assertEqual(result, "-400 is a leap year.\n")



if __name__ == '__main__':
    unittest.main()
