import os
from zipfile import ZipFile

projects = '/Users/andrew.gonzalez4/Desktop/Labs/Lab4-030/'
dirname = '/Users/andrew.gonzalez4/Desktop/Labs/Unzipped/'
extension = '.zip'
os.chdir(projects)
dirlist = []


for subdir, dirs, files in os.walk(projects):
   sd = subdir.split("Lab4-030/")[-1]
   dirlist.append(sd)
del(dirlist[0])

# # del(dirlist[0])
# os.chdir(dirname)
# for item in dirlist:
#     os.mkdir(item)

i = 0
for folders in os.listdir(projects):
    try:
        for files in os.listdir(os.getcwd() + '/' + folders ):
            with ZipFile(os.getcwd() + '/' + folders +'/' + files, 'r') as zipObj:
                zipObj.extractall(dirname + dirlist[i])
        i = i + 1
    except:
        print("?")\









