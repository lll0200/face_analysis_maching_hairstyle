"""
phash
海明距离
在信息论中，两个等长字符串之间的汉明距离是两个字符串对应位置的不同字符的个数)。如果不相同的数据位数不超过5，就说明两张图像很相似；如果大于10，就说明这是两张不同的图像
步骤:
（1）缩小尺寸：pHash以小图片开始，但图片大于8*8，32*32是最好的。这样做的目的是简化了DCT的计算，而不是减小频率。
（2）简化色彩：将图片转化成灰度图像，进一步简化计算量。
（3）计算DCT：计算图片的DCT变换，得到32*32的DCT系数矩阵。
（4）缩小DCT：虽然DCT的结果是32*32大小的矩阵，但我们只要保留左上角的8*8的矩阵，这部分呈现了图片中的最低频率。
（5）计算平均值：如同均值哈希一样，计算DCT的均值。
（6）计算hash值：这是最主要的一步，根据8*8的DCT矩阵，设置0或1的64位的hash值，大于等于DCT均值的设为”1”，小于DCT均值的设为“0”。组合在一起，就构成了一个64位的整数，这就是这张图片的指纹
"""
import cv2
import numpy as np

#定义感知哈希
def pHash(img):
    #step1：调整大小32x32
    img=cv2.resize(img,(32,32))
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=img.astype(np.float32)
    #step2:离散余弦变换
    img=cv2.dct(img)
    img=img[0:8,0:8]
    Sum=0.
    hash_str=''
    #step3:计算均值
    # avg = np.sum(img) / 64.0
    for i in range(8):
        for j in range(8):
            Sum+=img[i, j]
    avg= Sum / 64
    #step4:获得哈希
    for i in range(8):
        for j in range(8):
            if img[i,j]>avg:
                hash_str += '1'
            else:
                hash_str += '0'
    return hash_str
#计算汉明距离
def hmdistance(phash1, phash2):
    num=0
    assert len(phash1) == len(phash2)
    for i in range(len(phash1)):
        if phash1[i]!=phash2[i]:
            num+=1
    return num

"""path="./test_images/img.png"#待测图片
path1="./test_images/s155.jpg"
user =cv2.imread(path)
user1=cv2.imread(path1)
user_pHash=pHash(user)
user_pHash1=pHash(user1)
print("user:",user_pHash)
print("user1:",user_pHash1)
dict=hmdistance(user_pHash,user_pHash1)
print("user and user1 hmdistance:",dict)"""