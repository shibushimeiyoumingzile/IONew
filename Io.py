import os
#os.mkdir("Ten")
f = open("D:/python/Io/Ten/ten.text",'w+')
for i in range(1,11):
     f.write("人们把难言的爱都埋入土壤里")
     f.write("\n")

f.seek(0)
a = f.readlines()
f.close()

f = open("D:/python/Io/Ten/ten2.text",'w+')
for i in a:
    f.write(i)

f.close()
