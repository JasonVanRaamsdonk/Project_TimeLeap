import unittest
from unittest.mock import patch

from colorizers.siggraph17 import SIGGRAPHGenerator
from colorizers.eccv16 import ECCVGenerator


class TestEccv16(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # print('set up method')
        cls.model = ECCVGenerator()
        cls.model_not_used = SIGGRAPHGenerator()

    @classmethod
    def tearDownClass(cls):
        ECCVGenerator.instances = {}
        SIGGRAPHGenerator.instances = {}

    # def setUp(self):
    #     self.model = ECCVGenerator()
    #
    # def tearDown(self):
    #     pass

    def test_model_contents_exists(self):
        self.assertIsNotNone(self.model)

    def test_eccv_is_not_eccv(self):
        self.assertIsNot(self.model, self.model_not_used)

    def test_model_instance(self):
        self.assertIsInstance(self.model, ECCVGenerator)

    def test_model_not_instance(self):
        self.assertNotIsInstance(self.model, SIGGRAPHGenerator)

    def test_s3bucket_response(self):
        with patch('colorizers.eccv16.requests.get') as mocked_get:
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
