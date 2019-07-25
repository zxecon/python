################################################
#python for data analysis study codes and notes#
################################################
'''
Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython 2nd Edition
Visual Studio Code w/ Jupyter Environment
'''

#####
#2.2#
#####

#%%
pip install numpy

#%%
import numpy as np
data = {i : np.random.randn() for i in range(7)}
data

#Introspection
#%%
b = [1, 2, 3]
b?

#%%
print?

#%run command
#ipython_script_test.py
'''
def f(x, y, z):
    return (x + y) / z

a = 5
b = 6
c = 7.5

result = f(a, b, c)
'''
#%run ipython_script_test.py

#Magic Commands
#%%
a = np.random.randn(100, 100)
%timeit np.dot(a, a)

#Matplotlib
#%%
pip install matplotlib #if matplotlib is not installed

#%%
%matplotlib inline
import matplotlib.pyplot as plt 
plt.plot(np.random.randn(50).cumsum())


#####
#2.3#
#####

#%%
for x in array:
    if x < pivot:
        less.append(x)
    else:
        greater.append(x)

#%%
a = [1, 2, 3]
b = a
a.append(4)
b

#%%
a = 5
type(a)
b = "foo"
type(b)

#%%
if x < 0:
    print('It's negative')
elif x == 0:
    print('Equal to zero')
elif 0 < x < 5:
    print('Positive but smaller than 5')
else:
    print('Positive and larger than or equal to 5')

