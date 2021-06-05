import cv2

from train.Face_Type_Detection import predict_face
datapath = "./train/train_data.pickle"
targetpath = "./train/train_target.pickle"
shape_predictor_path="./shape_predictor_68_face_landmarks.dat"
def get_face_type(img):
    re=predict_face(img,datapath,targetpath,shape_predictor_path)
    return re

# path="test_images/img.png"#待测图片
# user =cv2.imread(path)
# user_type=get_face_type(user)
# print("face_type:",user_type)
# # cv2.imshow("gender:%s"%user_type,cv2.imread(path))
# cv2.imshow("gender:%s"%user_type,cv2.imread(path))
#
# cv2.waitKey(0)