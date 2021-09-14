tup=(12,"Rajat",10,5.2,6,True,6,51,3,"hello",False)
string=0
integer=0
flot=0
ui=0
boolean=0
for i in tup:
    if type (i) ==int:
        integer+=1
    elif type (i) ==str:
        string+=1
    elif type (i)==float:
        flot+=1
    elif type (i)==bool:
        boolean+=1
    else:
        ui+=1
print (tup)
print ("integer elements",integer)
print ("float elements",flot)
print ("boolean elements",boolean)
print ("string elements",string)
if ui>0:
    print("unidentify elements",ui)
