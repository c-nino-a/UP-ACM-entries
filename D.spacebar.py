import math

def main():
    t=int(input())
    outputs=[]
    for rep in range(t):
        char=input()
        mark=input()
        for i in range(len(char)):
            if char[i].isupper()==True:
                if i>0:
                    if mark[i-1]=="1":
                        outputs.append("not enough spaCe, please Bounce!")
                        break
                if i!=7:
                    if mark[i+1]=="1":
                        outputs.append("not enough spaCe, please Bounce!")
                        break
            if i==7:
                outputs.append("made some spaCe, welcome to the Bar!")
    for i in outputs:
        print(i)
                
    
if __name__=="__main__":
    main()


