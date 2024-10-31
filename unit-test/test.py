import numpy as np
import unittest
from ../"Linear-Algebra-Visualizer" import determinant

class TestFunctions(unittest.TestCase):

    A_1 = np.array(
        [4839753,9854],
        [8932983,298374]
    )
    A_2 = np.array(
        [1,2],
        [3,4]
    )
    A_3 = np.array(
        [-4,-8493],
        [94035489,0]
    )
    
    def test_determinant(self):
        real_det_A_1 = np.linalg.det(A_1)
        test_det_A_1 = determinant(A_1)
        self.assertEqual(real_det_A_1, test_det_A_1)

        real_det_A_2 = np.linalg.det(A_2)
        test_det_A_2 = determinant(A_2)
        self.assertEqual(real_det_A_2, test_det_A_2)

        real_det_A_3 = np.linalg.det(A_3)
        test_det_A_3 = determinant(A_3)
        self.assertEqual(real_det_A_3, test_det_A_3)

if __name__ == '__main__':
    unittest.main()
