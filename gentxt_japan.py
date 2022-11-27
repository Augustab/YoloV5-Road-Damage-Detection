import os

image_files = []
for filename in os.listdir("../../../projects/vc/courses/TDT17/2022/open/RDD2022/Japan/train/images/"):
    if filename.endswith(".jpg"):
        image_files.append(filename[:-4])

with open("txt_japan.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
        