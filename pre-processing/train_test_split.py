import os
from sklearn.model_selection import train_test_split
import cv2

polyp_crops = "C:\\sumedh\\NeurIPS\\ENDOSCOPY\\deep-endoscopy\\data\\crops\\polyps"
ulcer_crops = "C:\\sumedh\\NeurIPS\\ENDOSCOPY\\deep-endoscopy\\data\\crops\\ulcer"
data_set_path = "C:\\sumedh\\NeurIPS\\ENDOSCOPY\\deep-endoscopy\\data\\data_set"
polyp_collection = os.listdir(polyp_crops)
ulcer_collection = os.listdir(ulcer_crops)

train_set_polyp,test_set_polyp = train_test_split(polyp_collection,test_size=0.2, shuffle=False)

train_set_ulcer,test_set_ulcer = train_test_split(ulcer_collection,test_size=0.2, shuffle=False)

for img in train_set_polyp:
    img_path = polyp_crops+"\\"+img
    im = cv2.imread(img_path)
    cv2.imwrite(data_set_path+"\\train\\polyps\\"+img,im)

for img in test_set_polyp:
    img_path = polyp_crops+"\\"+img
    im = cv2.imread(img_path)
    cv2.imwrite(data_set_path+"\\test\\polyps\\"+img,im)

for img in train_set_ulcer:
    img_path = ulcer_crops+"\\"+img
    im = cv2.imread(img_path)
    cv2.imwrite(data_set_path+"\\train\\ulcer\\"+img,im)

for img in test_set_ulcer:
    img_path = ulcer_crops+"\\"+img
    im = cv2.imread(img_path)
    cv2.imwrite(data_set_path+"\\test\\ulcer\\"+img,im)
