import unittest
import numpy.testing as npt

import os
import numpy as np
import numpy.testing as npt
from skimage import io


class TestResultImage(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        module_dir = os.path.dirname(os.path.dirname(__file__))
        cls.sol_dir = os.path.join(module_dir, "docs")
        cls.res_dir = os.path.join(module_dir, "res")
        cls.img_coords = np.load(
            os.path.join(cls.sol_dir, "img_coords.npy"),
        )
        return super().setUpClass()

    def test_stored_files(self):
        files = os.listdir(self.res_dir)
        self.assertTrue("result.png" in files and "image_coords.npy" in files)

    def test_image_coords(self):
        img_coords = np.load(os.path.join(self.res_dir, "image_coords.npy"))
        npt.assert_allclose(img_coords, self.img_coords, rtol=1e-5, atol=1e-5)


if __name__ == "__main__":
    unittest.main()
