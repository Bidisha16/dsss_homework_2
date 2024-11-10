import unittest
from math_quiz import gen_random_num, select_random_op, calc_problem

class TestMathGame(unittest.TestCase):

    def test_gen_random_num(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = gen_random_num(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, 
                            f"Generated number {rand_num} is outside the range [{min_val}, {max_val}]")

    def test_select_random_op(self):
        # Test if the function returns one of the valid operators
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of selections
            op = select_random_op()
            self.assertIn(op, valid_operators, f"Selected operator {op} is not one of the valid operators.")

    def test_calc_problem(self):
        test_cases = [
            (2, 2, '+', '2 + 2', 4),
            (15, 3, '-', '15 - 3', 12),
            (4, 10, '*', '4 * 10', 40),
            (7, 3, '-', '7 - 3', 4)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calc_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem, f"Problem does not match expected problem. Expected: {expected_problem}, got: {problem}")
            self.assertEqual(answer, expected_answer, f"Answer does not match expected answer. Expected: {expected_answer}, got: {answer}")

if __name__ == "__main__":
    unittest.main()
