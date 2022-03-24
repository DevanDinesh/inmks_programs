# result=[]
# for i in "inmakes":
#     result.append(i)
# print(result)

# result=[i for i in "inmakes"]
# print(result)

result=["python","django","flask",'people']
# new=[]
# for i in result:
#     if 'p' in i:
#         new.append(i)
# print(new)

# new=[i for i in result if 'p' in i]
# print(new)

# new=[i for i in range(10)]
# print(new)

# new=["inmakes" for i in result]
# print(new)

new=[i.upper() for i in result]
print(new)