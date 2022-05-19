
n=input("数字:")
s=[]
for a in range(1,int(n),1):
  if a==1 or a==2:
    s.append(1)
  else:
    c=s[a-3]+s[a-2]
    s.append(c)
print(s)
e=0
for d in s:
  e+=d
print(e)