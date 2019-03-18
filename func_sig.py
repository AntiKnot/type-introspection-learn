"""
python function signature
"""

from inspect import signature
from inspect import Signature, Parameter


def foo(value):
    return value


# get function signature
foo_sig = signature(foo)
print(f'foo_sig:{foo_sig}')

# get function parameters
foo_params = foo_sig.parameters
print(f'foo_params:{foo_params}')

# build function signature
params = [Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
          Parameter('y', Parameter.POSITIONAL_OR_KEYWORD),
          Parameter('z', Parameter.KEYWORD_ONLY, default=9)]

sig = Signature(params)
print(f'sig:{sig}')

# check if the function parameter matches the signature
bound_args_01 = sig.bind(1, 2, z=3)
print(f'bound_args_01:{bound_args_01}')
bound_args_02 = sig.bind(1, 2)
print(f'bound_args_02:{bound_args_02}')
# bound_args_03 = sig.bind(1)
# print(f'bound_args_03:{bound_args_03}')

"""
Reference

BlackMatrix. (2018, January 16). 浅谈python函数签名.[Web log post]
https://www.cnblogs.com. 
Retrieved March 18, 2019 from https://www.cnblogs.com/blackmatrix/p/8299290.html
"""
