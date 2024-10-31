import numpy as np
import unittest
from linviz import determinant
import math

class TestFunctions(unittest.TestCase):

    A_1 = np.array([
        [4839753,9854],
        [8932983,298374]
    ])
    A_2 = np.array([
        [1,2],
        [3,4]
    ])
    A_3 = np.array([
        [-4,-8493],
        [94035489,0]
    ])
    
    def test_determinant(self):
        real_det_A_1 = np.linalg.det(self.A_1)
        test_det_A_1 = determinant(self.A_1)
        difference = math.floor(abs(real_det_A_1 - test_det_A_1))
        self.assertEqual(difference, 0, f'incorrect determinant. real:{real_det_A_1}, test:{test_det_A_1}')

        real_det_A_2 = np.linalg.det(self.A_2)
        test_det_A_2 = determinant(self.A_2)
        difference = math.floor(abs(real_det_A_2 - test_det_A_2))
        self.assertEqual(difference, 0, f'incorrect determinant. real:{real_det_A_2}, test:{test_det_A_2}')

        real_det_A_3 = np.linalg.det(self.A_3)
        test_det_A_3 = determinant(self.A_3)
        difference = math.floor(abs(real_det_A_1 - test_det_A_1))
        self.assertEqual(difference, 0, f'incorrect determinant. real:{real_det_A_1}, test:{test_det_A_1}')

if __name__ == '__main__':
    unittest.main()
