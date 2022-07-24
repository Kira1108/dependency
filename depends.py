from typing import Dict
import inspect
from typing import Callable
from functools import wraps

class Depends:
    """Depends is injected into other functions, when calling, get the values back
    Args:
        dependency: the function that is injected, which returns something
                    provided to the required function
    """

    def __init__(self, dependency):
        if not isinstance(dependency, Callable):
            raise ValueError("Dependency must be callable")
        self.dependency = dependency

    def __call__(self):
        return self.dependency()

def inject_depends(f):
    dependencies = {
            name: signature.default.dependency
            for name, signature in inspect.signature(f).parameters.items() 
            if isinstance(signature.default, Depends)
        }
    @wraps(f)
    def dec(*args, **kwargs):
        # retrieve funtion call args
        callargs = inspect.getcallargs(f, *args, **kwargs)

        # filter call args no depends
        callargs = {k:v for k,v in callargs.items() if not isinstance(v, Depends)}

        # retrieve required depends
        depends_kwargs = {k: v()for k, v in dependencies.items() if k not in callargs}

        return f(**callargs, **depends_kwargs)
    return dec