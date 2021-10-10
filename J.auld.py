
def main():
    outputs=[]
    for i in range(int(input())):
        k=int(input())
        first=list(map(int,input().split()))
        current=list(map(int,input().split()))
        if first==current:
            outputs.append(0)
        else:
            pos=current.index(first[0])
            outputs.append(k-pos)

    for i in outputs:
        print(i)
if __name__=="__main__":
    main()



