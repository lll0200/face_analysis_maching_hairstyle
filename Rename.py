import os

def change_path(before_path, after_path):
    filelist = os.listdir(before_path)
    j = 0
    for i in filelist:    # 判断该路径下的文件是否为图片
        if i.endswith('.jpg'):
            os.rename(os.path.join(os.path.abspath(before_path), i), os.path.join(os.path.abspath(after_path),
                                                                                  'w' + format(str(j), '0>2s') + '.jpg'))
            j += 1
        elif i.endswith('.jpeg'):
            os.rename(os.path.join(os.path.abspath(before_path), i), os.path.join(os.path.abspath(after_path),
                                                                                  's' + format(str(j), '0>2s') + '.jpg'))
        elif i.endswith('.png'):
            os.rename(os.path.join(os.path.abspath(before_path), i), os.path.join(os.path.abspath(after_path),
                                                                                  'p' + format(str(j), '0>2s') + '.jpg'))

# 图片路径
path = './images'
# 目标文件夹路径
path1 = './images'
change_path(path,path1)

