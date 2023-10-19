import os

def get_folder_size(path):
    sz = 0
    for item in os.listdir(path):
        itempath = os.path.join(path, item)
        if os.path.isfile(itempath):
            sz += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            sz += get_folder_size(itempath)
    return sz


path = "D:\\BMW\\tickets\\"
for item in os.listdir(path):
    itempath = os.path.join(path, item)
    if os.path.isdir(itempath):
        sz = get_folder_size(itempath) // (1024*1024)
        print(item + "\t\t\t" + str(sz) + "MB")
        
print("Total: " + str(get_folder_size(path) // (1024*1024)) + "MB")
