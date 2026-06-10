# file = open("filename.txt","x")


# with open("filename.txt","a") as file:
#      file.write("New file content inserted")
#      file.write("Content changed")
#      file.write("New more content")
#      file.write("New more")
#      file.write("New more")
#      content = file.read()
#      print(content)


# with open("filename.txt","a+") as file:
#     file.write("New content added\n")

#     content = file.read()
#     print(content)
import os
with open("filename.txt","r+") as file:
    line1  = file.readline()
    line = file.readlines()\
    
    print(line[1])
