import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# plot barplot with numbers on bars
def put_numbers_on_bar():
    ax = plt.gca()
    for p in ax.patches:
        height = int(p.get_height())
        x = p.get_x() + p.get_width() / 2
        y = p.get_height()
        ax.annotate(f'{height}', (x, y), ha='center', va='bottom')
        
        
if __name__ == "__main__":
    pass