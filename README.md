# Dependency Injection


**Some commond depends is injected to a function**        
`fn` is a depended function, which returns a dictionary    
`myfunc` has a parameter d, which is the result of function `fn`     
`myfunc` expliciyly depends on `fn`    

```python
from typing import Dict
from depends import Depends, inject_depends

def fn() -> Dict:
    print("Call Dependencies function")
    return {"a":1}

@inject_depends
def myfunc(s = 5, d:Dict = Depends(fn)):
    print("I got it, d={}".format(d),  f"and s = {s}")


myfunc()
>>> Call Dependencies function
>>> I got it, d={'a': 1} and s = 3
```