#!/usr/bin/env pypy
import math

def main():
    n=int(input())
    b=int(input())
    gi=list(map(int,input().split()))
    pi=list(map(int,input().split()))

    servingcost = sum([g * p for g, p in zip(gi, pi)])

    print(int(b/servingcost))
    
    
if __name__=="__main__":
    main()