import os
import random
import shutil

# getting imagelist from 'training/images'
imageDir = 'data/images'
labelDir = 'data/labels'
imageList = os.listdir(imageDir)


#shuffling images
random.seed(0)
random.shuffle(imageList)

# split ratio 
split = 0.22

# output train path 
trainPath = 'data_split/train'
# otput validate path
validatePath = 'data_split/validate'

if os.path.isdir(trainPath) == False:
    os.makedirs(trainPath)
if os.path.isdir(validatePath) == False:
    os.makedirs(validatePath)

numImages = len(imageList)

print("Images in total: ", numImages)

trainImages = imageList[: int(numImages - (numImages*split))]
validateImages = imageList[int(numImages - (numImages*split)):]

print("Training images: ", len(trainImages))
print("Validation images: ", len(validateImages))

for imgName in trainImages:
    srcImgPath = os.path.join(imageDir, imgName)
    dstImgPath = os.path.join(trainPath, imgName)

    shutil.copyfile(srcImgPath, dstImgPath)

    srcTxtPath = os.path.join(labelDir, imgName.replace('.jpg', '.txt'))
    dstTxtPath = os.path.join(trainPath, imgName.replace('.jpg', '.txt'))

    shutil.copyfile(srcTxtPath, dstTxtPath)

for imgName in validateImages:
    srcImgPath = os.path.join(imageDir, imgName)
    dstImgPath = os.path.join(validatePath, imgName)

    shutil.copyfile(srcImgPath, dstImgPath)

    srcTxtPath = os.path.join(labelDir, imgName.replace('.jpg', '.txt'))
    dstTxtPath = os.path.join(validatePath, imgName.replace('.jpg', '.txt'))

    shutil.copyfile(srcTxtPath, dstTxtPath)


print("Training Data Split Complete! ")
