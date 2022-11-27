from shutil import copyfile

with open('txt_japan.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        #fName = line.split('/')[-1]
        #fName = fName.split('.')[0]
        srcLbl = 'data_copy/labels/' + line + '.txt'
        destLbl = 'data_copy/labels/train/' + line + '.txt'
        print(srcLbl + " " + destLbl)

        copyfile(srcLbl, destLbl)

# with open('train.txt', 'r') as f:
#     for line in f:
#         line = line.rstrip()
#         #fName = line.split('/')[-1]
#         #fName = fName.split('.')[0]
#         srcLbl = 'data_copy/labels/' + line + '.txt'
#         destLbl = 'data_copy/labels/train/' + line + '.txt'
#         print(srcLbl + " " + destLbl)

#         copyfile(srcLbl, destLbl)

# with open('val.txt', 'r') as f:
#     print("TEST")
#     for line in f:
#         line = line.rstrip()
#         #fName = line.split('/')[-1]
#         #fName = fName.split('.')[0]
#         fName = line

#         srcLbl = 'data/labels/' + fName + '.txt'
#         destLbl = 'data/labels/valid/' + fName + '.txt'
#         print(srcLbl + " " + destLbl)


#         copyfile(srcLbl, destLbl)
