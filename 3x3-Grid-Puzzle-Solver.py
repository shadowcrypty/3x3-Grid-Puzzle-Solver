import sys


emptyTable=[True,True,True,True,True,True,True,True,True]
targetTable=[]
testTable=[True,True,True,True,True,True,True,True,True]

def ReTurn(a):
    if(a==False):
        return True
    else:
        return False  
    
def basicMove(x):
    if x=="1":
        testTable[0]=ReTurn(testTable[0])
        testTable[1]=ReTurn(testTable[1])
        testTable[3]=ReTurn(testTable[3])
        return testTable
    elif x=="2":
        testTable[0]=ReTurn(testTable[0])
        testTable[1]=ReTurn(testTable[1])
        testTable[2]=ReTurn(testTable[2])
        testTable[4]=ReTurn(testTable[4])
        return testTable
    elif x=="3":
        testTable[2]=ReTurn(testTable[2])
        testTable[1]=ReTurn(testTable[1])
        testTable[5]=ReTurn(testTable[5])
        return testTable
    elif x=="4":
        testTable[0]=ReTurn(testTable[0])
        testTable[4]=ReTurn(testTable[4])
        testTable[3]=ReTurn(testTable[3])
        testTable[6]=ReTurn(testTable[6])
        return testTable
    elif x=="5":
        testTable[4]=ReTurn(testTable[4])
        testTable[1]=ReTurn(testTable[1])
        testTable[3]=ReTurn(testTable[3])
        testTable[5]=ReTurn(testTable[5])
        testTable[7]=ReTurn(testTable[7])
        return testTable
    elif x=="6":
        testTable[4]=ReTurn(testTable[4])
        testTable[5]=ReTurn(testTable[5])
        testTable[2]=ReTurn(testTable[2])
        testTable[8]=ReTurn(testTable[8])
        return testTable
    elif x=="7":
        testTable[6]=ReTurn(testTable[6])
        testTable[3]=ReTurn(testTable[3])
        testTable[7]=ReTurn(testTable[7])
        return testTable
    elif x=="8":
        testTable[6]=ReTurn(testTable[6])
        testTable[7]=ReTurn(testTable[7])
        testTable[4]=ReTurn(testTable[4])
        testTable[8]=ReTurn(testTable[8])
        return testTable
    else:
        testTable[7]=ReTurn(testTable[7])
        testTable[8]=ReTurn(testTable[8])
        testTable[5]=ReTurn(testTable[5])
        return testTable
        
            
        
def targetTabler(x):
    if x=="...":
        targetTable.append(True)
        targetTable.append(True)
        targetTable.append(True)
        
    elif x=="*..":
        targetTable.append(False)
        targetTable.append(True)
        targetTable.append(True)
    elif x=="**.":
        targetTable.append(False)
        targetTable.append(False)
        targetTable.append(True)
    elif x=="***":
        targetTable.append(False)
        targetTable.append(False)
        targetTable.append(False)
    elif x=="..*":
        targetTable.append(True)
        targetTable.append(True)
        targetTable.append(False)
    elif x==".**":
        targetTable.append(True)
        targetTable.append(False)
        targetTable.append(False)
    elif x==".*.":
        targetTable.append(True)
        targetTable.append(False)
        targetTable.append(True)
    elif x=="*.*":
        targetTable.append(False)
        targetTable.append(True)
        targetTable.append(False)
        #print("triple true")
    else:
        print("miss")
    
def firstAttack():
    for i in range(0,10):
        x=str(i)
        global testTable
        #testTable=
        testTable=emptyTable
        test=basicMove(x)
        #target check break
        if targetTable==test:
            print("1")
            targetTable=emptyTable
            
            break
        
        #reset table
    
for line in sys.stdin:
    if "q" == line.rstrip():
        
        break
    targetTabler(line.rstrip())
    #print(len(targetTable))
    if len(targetTable)==9:
        print("Attack Started")
        firstAttack()
    #basicMove(line.rstrip())
    
        
    
##    if(testTable[0]):
  ##      print("a is true")
   ## else:
     ##   print("a is false")
    ##print(f"input: {line}")
    ##print(line)

print("exit")


