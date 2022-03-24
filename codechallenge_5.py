file=open("demo.txt",'w')
file.write("I'am Devan Dinesh")
file.close()

file=open("demo.txt",'r')
content=file.read()
print(content)
file.close()

file=open("demo.txt","a")
file.write("\na professional")
file.close()