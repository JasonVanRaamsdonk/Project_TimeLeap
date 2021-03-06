import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

import matplotlib.pyplot as plt

from .models import *

# parser = argparse.ArgumentParser()
# parser.add_argument('--use_gpu', action='store_true', help='whether to use GPU')
# parser.add_argument('-o','--save_prefix', type=str, default='saved', help='will save into this file with {eccv16.png, siggraph17.png} suffixes')
# opt = parser.parse_args()
ran = False

# load models
colouriser_main = colouriser(pretrained=True).eval()


# if(opt.use_gpu):
# 	colorizer_eccv16.cuda()
# 	colorizer_siggraph17.cuda()

# default size to process images is 256x256
# grab L channel in both original ("orig") and resized ("rs") resolutions
def colourise_image(img):
    img = load_img(img)
    (tens_l_orig, tens_l_rs) = preprocess_img(img, HW=(256, 256))
    # if(opt.use_gpu):
    # 	tens_l_rs = tens_l_rs.cuda()

    # colorizer outputs 256x256 ab map
    # resize and concatenate to original L channel
    img_bw = postprocess_tens(tens_l_orig, torch.cat((0 * tens_l_orig, 0 * tens_l_orig), dim=1))
    # out_img_eccv16 = postprocess_tens(tens_l_orig, colorizer_eccv16(tens_l_rs).cpu())
    out_img_siggraph17 = postprocess_tens(tens_l_orig, colouriser_main(tens_l_rs).cpu())
    # print('%s_eccv16.png'%opt.save_prefix)
    # plt.imsave('static/images/eccv16.png', out_img_eccv16)
    plt.imsave('static/images/siggraph17.png', out_img_siggraph17)

    return int(os.path.getsize('static/images/siggraph17.png') / 1024)
    ran = True
# plt.imsave('%s_siggraph17.png'%opt.save_prefix, out_img_siggraph17)
