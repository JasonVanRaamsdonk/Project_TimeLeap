

from mock_base_color import *

import requests


class ECCVGenerator(BaseColor):
    def __init__(self, norm_layer=0):
        super(ECCVGenerator, self).__init__()

    def forward(self, input_l):
        pass

    def model_state_from_s3bucket(self):
        response = requests.get('https://siggraphs3jvr.s3-eu-west-1.amazonaws.com/siggraph17.pth')
        if response.ok:
            return response.test
        else:
            return 'Bad Response!'

def eccv16(pretrained=False):
	# model = ECCVGenerator()
    # print(model)
    # print("*" * 10)
	# if(pretrained):
	# 	import torch.utils.model_zoo as model_zoo
	# 	model.load_state_dict(model_zoo.load_url('https://colorizers.s3.us-east-2.amazonaws.com/colorization_release_v2-9b330a0b.pth',map_location='cpu',check_hash=True))
    #
    #     print(model)
	return model
