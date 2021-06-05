import pickle
import dlib
import cv2
from imutils import face_utils
from sklearn import neighbors


def predict_face(imgpath,datapath,targetpath,shape_predictor_path):

    data_file = open(datapath, 'rb')  # rb for read byte
    target_file = open(targetpath, 'rb')

    # load for read
    train_data = pickle.load(data_file)
    train_target = pickle.load(target_file)
    #KNeighborsClassifier是实现K近邻算法的一个类
    clsfr = neighbors.KNeighborsClassifier()
    clsfr.fit(train_data, train_target)#数据预处理
    face_detector = dlib.get_frontal_face_detector()
    # 预测人脸标记点
    landmarks_detector = dlib.shape_predictor(shape_predictor_path)
    # 灰度处理
    gray = cv2.cvtColor(imgpath, cv2.COLOR_BGR2GRAY)
    #预测人脸框
    rect = face_detector(gray)
    imgpath[0:][0:30] = [0, 255, 0]
    points = landmarks_detector(gray, rect[0])
    points = face_utils.shape_to_np(points)  # converting the 68 points into a numpy array

    face_dic={0:'Diamond',1:'Oblong',2:'Oval',3:'Round',4:'Square',5:'Traingle'}
    point7=[0 for x in range(7)]
    point7[0]=points[2][0]
    point7[1]=points[3][0]
    point7[2]=points[4][0]
    point7[3]=points[5][0]
    point7[4]=points[6][0]
    point7[5]=points[7][0]
    point7[6]=points[8][0]

    d1=point7[6]-point7[0]
    d2=point7[6]-point7[1]
    d3=point7[6]-point7[2]
    d4=point7[6]-point7[3]
    d5=point7[6]-point7[4]
    d6=point7[6]-point7[5]

    D1=d2/float(d1)*100
    D2=d3/float(d1)*100
    D3=d4/float(d1)*100
    D4=d5/float(d1)*100
    D5=d6/float(d1)*100

    results=clsfr.predict([[D1,D2,D3,D4,D4]])
    result=results[0]
    return face_dic[result]