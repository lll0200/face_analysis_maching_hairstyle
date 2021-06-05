import io

import cv2
genderProto_path= "./gender_deploy.prototxt"
genderModel_path= "./gender_net.caffemodel"
def get_gender(imgpath):
    #要减去的均值
    MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)
    genderList=['Male','Female'] #男 女

    # 用于进行SSD网络的caffe框架的加载
    # 参数说明:prototxt表示caffe网络的结构文本，model表示已经训练好的参数结果
    genderNet=cv2.dnn.readNet(genderModel_path,genderProto_path)
    face=cv2.imread(imgpath)
    '''
    blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size, mean, swapRB=True，crop=False,ddepth = CV_32F )
    1.image，这是传入的，需要进行处理的图像。
    2.scalefactor，执行完减均值后，需要缩放图像，默认是1，需要注意，scalefactor = 1 / \sigma,这是真正乘上的值。 
    3.size,这是神经网络，真正支持输入的值。
    4.mean,这是我们要减去的均值，可以是R,G,B均值三元组，或者是一个值，每个通道都减这值。如果执行减均值，通道顺序是R、G、B。 如果，输入图像通道顺序是B、G、R，那么请确保swapRB = True，交换通道。
    5.swapRB，OpenCV认为图像 通道顺序是B、G、R，而减均值时顺序是R、G、B，为了解决这个矛盾，设置swapRB=True即可。
    6.crop,如果crop裁剪为真，则调整输入图像的大小，使调整大小后的一侧等于相应的尺寸，另一侧等于或大于。然后，从中心进行裁剪。如果“裁剪”为“假”，则直接调整大小而不进行裁剪并保留纵横比。
    7.ddepth, 输出blob的深度，选则CV_32F or CV_8U。
    cv2.dnn.blobFromImage函数返回的blob是我们输入图像进行随意从中心裁剪，减均值、缩放和通道交换的结果。
    '''
    blob=cv2.dnn.blobFromImage(face, 1.0, (227,227), MODEL_MEAN_VALUES, swapRB=False)
    # blob输入网络进行性别的检测
    genderNet.setInput(blob)
    # 性别检测进行前向传播
    genderPreds=genderNet.forward()
    # 分类  返回性别类型
    Gender=genderList[genderPreds[0].argmax()]
    return Gender
"""path="test_images/img.png"#待测图片
gender=get_gender(path)
print("gender:",gender)
cv2.imshow("gender:%s"%gender,cv2.imread(path))
cv2.waitKey(0)"""