import re

def main():
    t=int(input())
    outputs=[]
    for rep in range(t):
        q=input()
        spc=[m.start() for m in re.finditer(' ', q)]
        spc.append(None)
        st=0
        placeholder=""
        for i in spc:
            if re.search('([A-Z])', q[st:i]) != None:
                placeholder+=q[st:i].upper()
            else:
                placeholder+=q[st:i]
            st=i
        outputs.append(placeholder)
                   
    for i in outputs:
        print(i)
                
    
if __name__=="__main__":
    main()



