x=(0,1,2,3,"Devan","Dinesh")
y=list(x)
y.insert(10,"kumily")
y.append("idukki")
print(y)
x=tuple(y)
print(x)
index=x.index("kumily")
print("The index number is=",index)