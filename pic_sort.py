import os
import cv2

from get_face_type import get_face_type
from get_gender import get_gender

path='./images'  #待分类路径
filelist = os.listdir(path)
j=362
for i in filelist:    # 遍历
    pic=os.path.join(os.path.abspath(path), i) #路径
    picture=cv2.imread(pic)
    gender=get_gender(pic)#需传路径
    pic_type=get_face_type(picture)#需传处理后的图片
    target_path=os.path.join(gender+"/"+pic_type)#指定目录
    print(gender,pic_type,pic)
    j+=1
    print(j)
    if gender=="Male":
        if pic_type=="Diamond":
            os.rename(pic, os.path.join(os.path.abspath(target_path),
                                        's' + format(str(j), '0>2s') + '.jpg'))  # 重命名并且移动到指定目录下
        elif pic_type=="Oblong":
            os.rename(pic, os.path.join(os.path.abspath(target_path),
                                        's' + format(str(j), '0>2s') + '.jpg'))  # 重命名并且移动到指定目录下
        elif pic_type=="Oval":
           os.rename(pic, os.path.join(os.path.abspath(target_path),
                                        's' + format(str(j), '0>2s') + '.jpg'))  # 重命名并且移动到指定目录下
        elif pic_type=="Round":
            os.rename(pic, os.path.join(os.path.abspath(target_path),
                                        's' + format(str(j), '0>2s') + '.jpg'))  # 重命名并且移动到指定目录下
        elif pic_type=="Square":
            os.rename(pic, os.path.join(os.path.abspath(target_path),
                                        's' + format(str(j), '0>2s') + '.jpg'))  # 重命名并且移动到指定目录下
        elif pic_type=="Traingle":
            os.rename(pic, os.path.join(os.path.abspath(target_path),
                                        's' + format(str(j), '0>2s') + '.jpg'))  # 重命名并且移动到指定目录下
    elif gender=="Female" :
        if pic_type=="Diamond":
            os.rename(pic, os.path.join(os.path.abspath(target_path),
                                        's' + format(str(j), '0>2s') + '.jpg'))  # 重命名并且移动到指定目录下
        elif pic_type=="Oblong":
            os.rename(pic, os.path.join(os.path.abspath(target_path),
                                        's' + format(str(j), '0>2s') + '.jpg'))  # 重命名并且移动到指定目录下
        elif pic_type=="Oval":
            os.rename(pic, os.path.join(os.path.abspath(target_path),
                                        's' + format(str(j), '0>2s') + '.jpg'))  # 重命名并且移动到指定目录下
        elif pic_type=="Round":
            os.rename(pic, os.path.join(os.path.abspath(target_path),
                                        's' + format(str(j), '0>2s') + '.jpg'))  # 重命名并且移动到指定目录下
        elif pic_type=="Square":
            os.rename(pic, os.path.join(os.path.abspath(target_path),
                                        's' + format(str(j), '0>2s') + '.jpg'))  # 重命名并且移动到指定目录下
        elif pic_type=="Traingle":
            os.rename(pic, os.path.join(os.path.abspath(target_path),
                                        's' + format(str(j), '0>2s') + '.jpg'))  # 重命名并且移动到指定目录下
