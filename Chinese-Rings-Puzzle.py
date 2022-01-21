#!/usr/bin/python

def lift(n):
    if n == 1:
        print("Lift the 1 seal")

    elif n == 2:
        print("Lift the 2 seal")
        print("Lift the 1 seal")

    else:
        lift(n-1)
        drop(n-2)
        print("lift the {} seal".format(n))
        lift(n-2)

def drop(n):
    if n == 1:
        print("Drop the 1 seal")

    elif n == 2:
        print("Drop the 2 seal")
        print("Drop the 1 seal")

    else:
        drop(n - 2)
        print("Drop the {} seal".format(n))
        lift(n - 2)
        drop(n - 1)

n = int(input("How many seals? \n"))
drop(n)