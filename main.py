
from depends import Depends, inject_depends
from providers import mysettings1, mysettings2
from typing import Dict

@inject_depends
def myfunc1(s = 5, d:Dict = Depends(mysettings1)):
    print("I got it, d={}".format(d),  f"and s = {s}")


@inject_depends
def myfunc2(a = 1, b:int = Depends(mysettings2)):
    print("I got a={} and b={}".format(a, b))


if __name__ == "__main__":
    myfunc1()
    myfunc2()