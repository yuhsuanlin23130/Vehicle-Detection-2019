'''XML檔生成Annotations/Main底下之檔案'''
# ˋ轉成VOCdevkit格式
import os
from xml.dom import minidom
# 步骤1：读取train.txt文件获取训练图片
# 获取训练txt文件

def _GetImageSet():
        # txt路径
        image_set_path = 'D:/VOC2007/ImageSets/Main/test.txt'
        with open(image_set_path, 'r') as f:
            return [line.split()[0] for line in f.readlines()]

# 训练图片合集
img_set = _GetImageSet()

# 步骤2：读取对应的xml文件
# xml标注文件路径

annotation='D:/VOC2007/Annotations'

# 构建xml列表

xml = []
for img in img_set:
        xml_path = os.path.join(annotation,img + '.xml')
        xml.append(xml_path)

# 步骤3：根据xml中的<name>项，判定图片中是否存在该类别。读取<name>项之后，一定通过set()函数，清除其中的重复类别名称，否则会出现标签重复的情况
# 类别

VOC_CLASSES = ['ambulance', 'compact car', 'firetruck', 'garbage truck','minibus', 'minivan', 'mountain bike', 'motor scooter', 'moving van', 'police car', 'taxi', 'tow truck', 'trailer truck']

for x in xml:    ### 每張照片
    # 获取每个name的地址
    elem_list = minidom.parse(x).getElementsByTagName('name')
    name = []

    # 读取每个地址的内容
    for elem in elem_list:
        cat_name = elem.firstChild.data
        # 获取name
        name.append(cat_name)

        # 删除重复标记
        name = list(set(name))

    # 根据类别写入标签文件
    for cls in VOC_CLASSES:  ### 每個類別
        txt = 'D:/VOC2007/ImageSets/Main/%s_test.txt' % cls

        if cls in name:
            file_write_obj = open(txt, 'a')
            gt = x[-10:-4] + ' ' +' '+ '1'
            file_write_obj.writelines(gt)
            file_write_obj.write('\n')

        else:
            file_write_obj = open(txt, 'a')
            gt = x[-10:-4] + ' '  + '-1'
            file_write_obj.writelines(gt)
            file_write_obj.write('\n')
