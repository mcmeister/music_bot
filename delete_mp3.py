import os
import glob


# Delete Downloaded Files from a Disk

os.chdir("/tmp/")
for file_tmp in glob.glob("*.tmp"):
    if os.path.exists(file_tmp):
        os.remove(file_tmp)
        print('Deleted: ' + str(file_tmp))
    else:
        print("The file does not exist")

for file_mp3 in glob.glob("*.mp3"):
    if os.path.exists(file_mp3):
        os.remove(file_mp3)
        print('Deleted: ' + str(file_mp3))
    else:
        print("The file does not exist")