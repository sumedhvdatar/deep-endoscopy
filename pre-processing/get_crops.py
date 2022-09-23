import cv2
import os
import json
import time
base_path = "C:\\sumedh\\NeurIPS\\ENDOSCOPY\\deep-endoscopy\\data"

annotation_folder =  base_path+"\\annotations"
crop_folder = base_path+"\\crops"
raw_image_folder = base_path+"\\raw_images"

for label in os.listdir(annotation_folder):

    meta_data = annotation_folder+"\\"+label

    for annotation in os.listdir(meta_data):

        try:

            json_path = meta_data+"\\"+annotation

            f = open(json_path)
            data = json.load(f)

            image_path = raw_image_folder+"\\"+label+"\\"+data["asset"]["name"]

            region_dict = data["regions"][0]
            class_name = region_dict["tags"][0]

            left = int(region_dict["boundingBox"]["left"])
            top = int(region_dict["boundingBox"]["top"])

            w = int(region_dict["boundingBox"]["width"])
            h = int(region_dict["boundingBox"]["height"])

            img = cv2.imread(image_path)
            cropped_image = img[top:top + h, left:left + w]

            crop_label_path = crop_folder+"\\"+label

            if not os.path.isdir(crop_label_path):
                os.mkdir(crop_label_path)
            print(time.time())
            epoch = str(time.time())
            crop_image_name = crop_label_path+"\\"+epoch.split(".")[0]+"_" +data["asset"]["name"]
            cv2.imwrite(crop_image_name,cropped_image)
        except Exception as e:
            print(str(e))


