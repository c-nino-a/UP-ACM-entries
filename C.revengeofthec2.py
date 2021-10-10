#!/usr/bin/env pypy
import math

def main():
    t=int(input())
    outputs=[]
    for rep in range(t):
        ai=list(map(int,input().split()))
        ci=list(map(int,input().split()))
        A=abs(math.prod(ai)) // math.gcd(ai[0],ai[1]*ai[2])
        amt=[A/a for a in ai]
        perp=[amtt * cost for amtt, cost in zip(amt, ci)]
        outputs.append(perp.index(min(perp))+1)
    for i in outputs:
        print(i)
    
    
if __name__=="__main__":
    main()