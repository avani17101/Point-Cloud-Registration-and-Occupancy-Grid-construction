import os
path = "./01/"
#()for file in enumerate(os.listdir(path)):
for i in range(9, -1, -1):
    print(i)
    src = "./01/00000" + str(i) + ".bin"
    dst = "./01/0000" + str(i + 10) + ".bin"
    os.rename(src, dst)
