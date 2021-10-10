#!/usr/bin/env pypy
import timeit

def main():
    r=int(input())
    w=int(input())
    standard=1/3
    actual=r/w
    # if(actual!=standard):
    #     if(actual>standard):
    #         print("WE NEED MORE WATER.")
    #     else:
    #         print("WE NEED MORE RICE.")
    # else:
    #     print("THE RICE IS RIGHT!")

    res= "THE RICE IS RIGHT!" if actual==standard else "WE NEED MORE WATER" if actual>standard else "WE NEED MORE RICE"
    print(res)
    
if __name__=="__main__":
    main()