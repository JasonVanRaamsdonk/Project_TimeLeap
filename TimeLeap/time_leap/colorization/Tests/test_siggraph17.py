import unittest
from unittest.mock import patch

import sys # added!
sys.path.append(".") # added!

from colorizers.siggraph17 import SIGGRAPHGenerator
from colorizers.eccv16 import ECCVGenerator


class TestSiggraph17(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # print('set up method')
        cls.model = SIGGRAPHGenerator()
        cls.model_not_used = ECCVGenerator()

    @classmethod
    def tearDownClass(cls):
        SIGGRAPHGenerator.instances = {}
        ECCVGenerator.instances = {}

    # def setUp(self):
    #     self.model = SIGGRAPHGenerator()
    #
    # def tearDown(self):
    #     pass

    def test_model_contents_exists(self):
        self.assertIsNotNone(self.model)

    def test_siggraph_is_not_eccv(self):
        self.assertIsNot(self.model, self.model_not_used)

    def test_model_instance(self):
        self.assertIsInstance(self.model, SIGGRAPHGenerator)

    def test_model_not_instance(self):
        self.assertNotIsInstance(self.model, ECCVGenerator)

    def test_s3bucket_response(self):
        with patch('requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.test = 'Success'

            s3bucket = self.model.model_state_from_s3bucket()
            mocked_get.assert_called_with('https://siggraphs3jvr.s3-eu-west-1.amazonaws.com/siggraph17.pth')
            self.assertEqual(s3bucket, 'Success')

            mocked_get.return_value.ok = False

            s3bucket = self.model.model_state_from_s3bucket()
            mocked_get.assert_called_with('https://siggraphs3jvr.s3-eu-west-1.amazonaws.com/siggraph17.pth')
            self.assertEqual(s3bucket, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
