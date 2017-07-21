#-*- coding: utf-8 -*-
import os
import sys
from PIL import Image, ImageOps
reload(sys)
sys.setdefaultencoding('utf-8')


def circular(ofile='', output='', mask=''):
    alpha = Image.open(mask).convert('L')
    im = Image.open(ofile.decode('utf8'))
    outputimg = ImageOps.fit(im, alpha.size, centering=(0.5, 0.5))
    outputimg.putalpha(alpha)
    outputimg.save(output)
    return outputimg
#
# imagePath = unicode("C:\\Users\\simo\\Pictures\\thumbnail_한글.png","euc-kr").encoding('utf-8')
#
# os.makedirs(os.path.dirname(imagePath))
# imagePath2 = "C:\\Users\\simo\\Pictures\\test34_00.png"
# mask = 'D:\\Dev_project\\wormhole\\python\\testProject\\PyQtTest\\image\\mask.png'

#thumbnail = circular(ofile=imagePath, output=imagePath2, mask=mask)

