import pandas as pd
import numpy as np

if __name__ == "__main__":

    # Here are the different ways to check the python environment

    # Method 1
    # import sys
    # print(sys.prefix)

    # Method 2
    import os
    if 'VIRTUAL_ENV' in os.environ:
        print('Your python environment is from %s' % os.environ['VIRTUAL_ENV'])
    else:
        print("Not using a virtual environment")
        
# function to print the python environment
def print_env():
    import os
    if 'VIRTUAL_ENV' in os.environ:
        print('Your python environment is from %s' % os.environ['VIRTUAL_ENV'])
    else:
        print("Not using a virtual environment")