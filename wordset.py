import tokenize
from io import StringIO
count = 0

word=[]
same=False
count=0
splitted=[]
inp=" "

while inp!="":
    inp=input("Enter a word: ")
    if(inp==""):
        print("Termination!")
        break
    file1 = open('text1.txt', 'r') 
    while True:     
    
        line = file1.readline() 
       
        if not line: 
            break
        name=str(line.strip())
        splitted =  tokenize.generate_tokens(StringIO(name).readline)
        for x in splitted :
            if x.string :
                word.append(x.string)
    file1.close() 

    for a in word:
        if a==inp:
            print("Error...The input word is already exit.")
            same=False
            break
        else:
            same=True
            continue

    if(same==True):
        file1=open('text1.txt','a')
        file1.write(inp)
        file1.write("     ")
        if(count>=6):
            file1.write("\n")
            count=0
        
        file1.close()
        count+=1
        print("Finish Insertion")
