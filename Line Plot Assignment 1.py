# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 23:17:57 2023

@author: Kinza Ijaz
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sunshine_in_2021 = [41.3, 75.1, 76.4, 197.1, 141.0, 156.0, 153.1, 111.9, 77.0, 43.9, 22.2, 20.7]
sunshine_in_2022 = [19.5, 47.0, 154.0, 120.8, 112.6, 169.2, 105.7, 131.7, 88.7, 62.2, 40.6, 21.0]
sunshine_in_2023 = [22.7, 47.7, 93.4, 166.7, 159.1, 226.0, 118.4, 117.8, 118.8, 68.4, 30.0, 22.5]

plt.plot(months, sunshine_in_2021, label='Sunshine in 2021', marker='o',markerfacecolor='green')
plt.plot(months, sunshine_in_2022, label='Sunshine in 2022', marker='o',markerfacecolor='green')
plt.plot(months, sunshine_in_2023, label='Sunshine in 2023', marker='o',markerfacecolor='green')

plt.xlabel('months')
plt.ylabel('sunshine')

plt.title('Sunshine comparison in past 3 years')

plt.legend()

plt.show()