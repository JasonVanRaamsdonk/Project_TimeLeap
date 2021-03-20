
from mock_base_color import *

import requests


class SIGGRAPHGenerator(BaseColor):
    def __init__(self, norm_layer=0, classes=529):
        super(SIGGRAPHGenerator, self).__init__()


    def forward(self, input_A, input_B=None, mask_B=None):
        pass

    def model_state_from_s3bucket(self):
        response = requests.get('https://siggraphs3jvr.s3-eu-west-1.amazonaws.com/siggraph17.pth')
        if response.ok:
            return response.test
        else:
            return 'Bad Response!'

def siggraph17(pretrained=True):
    # model = SIGGRAPHGenerator()
    pass

    return model
