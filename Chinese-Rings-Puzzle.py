#!/usr/bin/python

def lift(n):
    if n == 1:
        print("1")

    elif n == 2:
        print("1")
        print("2")

    else:
        lift(n-1)
        drop(n-2)
        print("2")
        lift(n-2)

def drop(n):
    if n == 1:
        print("1")

    elif n == 2:
        print("2")
        print("1")

    else:
        drop(n - 2)
        print("2")
        lift(n - 2)
        drop(n - 1)

n = int(input("How many seals? \n"))
drop(n)