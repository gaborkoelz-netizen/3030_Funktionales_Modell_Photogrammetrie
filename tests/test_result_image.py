import unittest
import numpy.testing as npt

import os
import numpy as np
from skimage import io

class TestResultImage(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.img_F = io.imread("docs/F_result.png")
        cls.img_N = io.imread("docs/N_result.png")
        return super().setUpClass()

    def test_stored_file(self):
        files = os.listdir("res")
        self.assertTrue("result.png" in files)

    def test_img_content(self):
        img = io.imread("res/result.png")
        diff1 = img - self.img_F
        diff2 = img - self.img_N
        self.assertTrue(np.allclose(diff1, np.zeros(img.shape)) or np.allclose(diff2, np.zeros(img.shape)))


if __name__ == "__main__":
    unittest.main()
