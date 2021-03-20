import unittest

import sys # added!
sys.path.append(".") # added!

from TimeLeap.time_leap.colorization.colorizers.base_color import BaseColor
from TimeLeap.time_leap.colorization.colorizers.siggraph17 import SIGGRAPHGenerator
from TimeLeap.time_leap.colorization.colorizers.eccv16 import ECCVGenerator

class TestBaseColor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # print('set up method')
        cls.util_class = BaseColor()

    @classmethod
    def tearDownClass(cls):
        BaseColor.instances = {}

    # def setUp(self):
    #     self.model = BaseColor()
    #
    # def tearDown(self):
    #     pass

    def test_model_contents_exists(self):
        self.assertIsNotNone(self.util_class)

    def test_model_instance(self):
        self.assertNotIsInstance(self.util_class, SIGGRAPHGenerator)

    def test_model_not_instance(self):
        self.assertNotIsInstance(self.util_class, ECCVGenerator)


if __name__ == '__main__':
    unittest.main()
