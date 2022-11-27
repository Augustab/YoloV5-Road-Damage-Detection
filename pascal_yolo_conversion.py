import glob
import os
import pickle
import xml.etree.ElementTree as ET
from os import listdir, getcwd
from os.path import join


def getImagesInDir(dir_path):
    image_list = []
    for filename in glob.glob(dir_path + '*.xml'):
        image_list.append(filename)

    return image_list


def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


def convert_annotation(dir_path, output_path, image_path):
    basename = os.path.basename(image_path)
    basename_no_ext = os.path.splitext(basename)[0]

    in_file = open(dir_path + basename_no_ext + '.xml')
    out_file = open(output_path + basename_no_ext + '.txt', 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        try:
            try:
                difficult = obj.find('difficult').text
            except:
                difficult = 0
            cls = obj.find('name').text
            if cls not in classes or int(difficult)==1:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bb = convert((w,h), b)
            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
        except:
            pass
            print("Image problem: ", image_path)


dir_path = 'data_copy/labels/'
classes = ['D00', 'D10', 'D20', 'D40']

def main():
    count = 0
    cwd = getcwd()

    full_dir_path = cwd + '/' + dir_path
    print("full_dir_path: ", full_dir_path)
    output_path =  full_dir_path
    print("output_path: ", output_path)

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    image_paths = getImagesInDir(full_dir_path)
    list_file = open(full_dir_path + '.txt', 'w')

    for image_path in image_paths:
        list_file.write(image_path + '\n')
        convert_annotation(full_dir_path, output_path, image_path)
        count = count + 1
        print("Image Converted: ", count, ":", image_path)
    list_file.close()

    print("Finished processing: " + dir_path)


if __name__ == '__main__':
    main()
