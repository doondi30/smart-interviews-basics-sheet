n=input()
text=[]
text2=[]
for i,char in enumerate(n):
    if i % 2==0:
        text.append(char)
    else:
        text2.append(char)
print(''.join(text2)+''.join(text))
