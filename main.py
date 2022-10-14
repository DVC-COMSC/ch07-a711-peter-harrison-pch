import numpy as np
import matplotlib.pyplot as plt

Math = [100, 90]
English = [90, 80]
Physics = [80, 80]
Computer = [80, 90]
x = np.arange(2)
width = 0.15
labels = ['Math', 'English', 'Physics', 'Computer']
names = ['Bill', 'Mary']

# ******************************
# Make your code
# ******************************

fig, ax = plt.subplots()

# number from center, subject list, label of the subject from labels list
def makebarm(num, subj, subname):  
    '''
    num: width distance left from center of block
    subj: the subject specific array used
    subname: the name of the subject from the labels array   
    '''
    return ax.bar(x - width*num, subj, width, label = subname)

# copy of function for making bar right of center to go right, unsure of parsing so unfortunately make a new one with just - -> +
def makebarp(num, subj, subname): 
    '''copy of makebarm but for to the right of center instead of left'''
    return ax.bar(x + width*num, subj, width, label = subname)

#each subjects bars added
s_math = makebarm(1.5, Math, labels[0])
s_eng = makebarm(.5, English, labels[1])
s_phy = makebarp(.5, Physics, labels[2])
s_comp = makebarp(1.5, Computer, labels[3])

# Add some text for labels, title and x-axis tick labels
ax.set_title('Grouped Graph for Scores')
ax.set_xticks(x, names)
ax.legend()

ax.bar_label(s_math, padding=3)
ax.bar_label(s_eng, padding=3)
ax.bar_label(s_phy, padding=3)
ax.bar_label(s_comp, padding=3)

fig.savefig('A11.png')
