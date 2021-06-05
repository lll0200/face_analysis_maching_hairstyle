import time

from skimage import io
import os
import cv2
from face_matching import hmdistance, pHash
from face_swap import swap_face
from get_face_type import get_face_type
from get_gender import get_gender

if __name__ == '__main__':
   a=time.time()
   # path="test_images/img.png"#待测图片
   path="test_images/test1.jpg"#待测图片

   user =cv2.imread(path)
   user_type=get_face_type(user)
   gender=get_gender(path)
   user_pHash=pHash(user)
   matching_path=os.path.join(gender+"/"+user_type)#根据性别，脸型，获取对应的路径
   Distance = []
   filelist = os.listdir(matching_path)
   for i in filelist:  # 判断该路径下的文件是否为图片
       pic = os.path.join(os.path.abspath(matching_path), i)  # 路径
       picture = cv2.imread(pic)
       pHash_pic=pHash(picture)
       distance=hmdistance(user_pHash,pHash_pic)
       Distance.append(distance)
   r = 0  # 找到匹配图片的序号r+1
   for i in range(len(filelist)):
      if Distance[i] < Distance[r]:
         r = i
   m=0
   img_matching=""
   for i in filelist:  #寻找相匹配照片的路径
       pic = os.path.join(os.path.abspath(matching_path), i)  # 路径
       m+=1
       if m==r+1:
          img_matching=pic
   swap_face(img_matching, path)
   out_path="./output/output.jpg"
   output=cv2.imread(out_path)
   height, width = output.shape[:2]  # 获取原图像的水平方向尺寸和垂直方向尺寸。
   # img1 = cv2.resize(output, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_NEAREST)  # 这里设置的是，宽和高都减少一
   # cv2.imshow("outpu", img1)
   pic = cv2.resize(output, (400, 400), interpolation=cv2.INTER_CUBIC)
   cv2.imshow("output",pic)
   b=time.time()
   print(b-a)
   cv2.waitKey(0)
   cv2.destroyAllWindows()