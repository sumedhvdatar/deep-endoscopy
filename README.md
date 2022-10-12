# deep-endoscopy

This repository contains the entire dataset of the endoscopic images. The dataset has the following components

a. Data
b. Pre-processing
c. Training


a. Data - The data folder has the following components

1. Annotations - The annotation folder contains a collection of JSON files for both polp and ulcer. Every image has a separate annotation.json file. The format of the annotation is following the stabdard Coco format.
2. Crops - This folder has all the crops and its mainly created to quickly recognition tasks
3. Data_set - This folder has the entire curated dataset with train and test split for easy plug and play training
4. raw_images - This folder contains raw images for the respective labels.


b. Pre-processing - This folder contains python files which help in pre-processing raw images and integrating annotation files with raw images.

c. Training - This folder contains training python files for image recognition tasks.
