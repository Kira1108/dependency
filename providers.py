from typing import Dict
import random

def mysettings1() -> Dict:
    """Some boring settings"""
    print("Call Dependencies function mysettings1")
    return {"a":1}


def mysettings2() -> int:
    """Some boring settings too"""
    print("Call Dependencies function mysettings2")
    return random.randint(1,100)

