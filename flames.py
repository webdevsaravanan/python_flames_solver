try:
    print("enter first name")
    name1=input()
    print("enter second name")
    name2=input()
except ValueError:
    print("Name is mandatory")
flames='flames'
currentPos=0
its=1
for i in name1:
    index=name2.find(i)
    if(index!=-1):
        name1=name1[:currentPos]+'#'+name1[(currentPos+1):]
        name2=name2[:index]+'$'+name2[(index+1):]
    currentPos+=1;   
dif=(len(name2)-name2.count('$'))+(len(name1)-name1.count('#'))
while(its<6):
    index=dif%len(flames)
    if(index!=0):
            flames=flames[index:]+flames[:index-1]
    else:
            flames=flames[len(flames):]+flames[:len(flames)-1]
    its+=1
print(flames)
    
