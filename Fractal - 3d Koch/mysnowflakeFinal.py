'''
3D SNOWFLAKE
Работу выполнил студент Голев. А.С. 2022</br>
@author: goliksim 
 
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection  # appropriate import to draw 3d polygons
import random


# lambda func to fix unreadable bug of numpy
vecProd = lambda a,b:np.cross(a,b)
    
#first type of generation new sides   
def createNewSideType1(side):
    a = (side[1]+side[0])/2
    b = (side[-1]+side[1])/2
    c = (side[-1]+ side[0])/2
    side_len = np.linalg.norm(a-b,2)
    newSide = [a,b,c]
    pivot = (b + (a+c))/3
    n = vecProd(pivot - newSide[0], newSide[-1]-pivot)
    d = pivot + n/np.linalg.norm(n,2)*side_len*np.sqrt(2/3)
    return np.array([[b,d,a],[b,c,d],[a,d,c]])

#second type of generation new sides
def createNewSideType2(side):
    pivot = (side[1]+side[0]+side[-1])/3
    a = (side[0]+pivot)/2
    b = (side[1]+pivot)/2
    c = (side[-1]+pivot)/2
    side_len = np.linalg.norm(a-b,2)
    newSide = [a,b,c]
    n = vecProd(pivot - b, a-pivot)
    d = pivot + n/np.linalg.norm(n,2)*side_len*np.sqrt(2/3)
    return np.array([[b,d,a],[b,c,d],[a,d,c]])
    
#replace the side with 3 side and hole 
def sideWithHole(side):
    a = (side[1]+side[0])/2
    b = (side[-1]+side[1])/2
    c = (side[-1]+ side[0])/2
    return np.array([[side[0],a,c],[side[1],b,a],[side[-1],c,b]])

#disable matplotlib axis
def disableAxis(ax):
    # убираем фон шкалы
    ax.w_xaxis.set_pane_color((0.56, 1, 0.62, 1.0))
    ax.w_yaxis.set_pane_color((0.56, 1, 0.62, 1.0))
    ax.w_zaxis.set_pane_color((0.56, 1, 0.62, 1.0))

    # убираем шкалу
    ax.w_xaxis.line.set_color((0.56, 1, 0.62, 1.0))
    ax.w_yaxis.line.set_color((0.56, 1, 0.62, 1.0))
    ax.w_zaxis.line.set_color((0.56, 1, 0.62, 1.0))

    # убираем линии
    ax.set_xticks([]) 
    ax.set_yticks([]) 
    ax.set_zticks([])

#func to first type of generation
def recurseFuncType1(data,color, iter, randomBool):
    
    if (iter<=0): return data, color
    result = np.empty(shape=(0,3,3))
    colorResult = np.empty(shape=(0,3))
    for side, color in zip(data,color):
        if ((random.getrandbits(1)==1) & (randomBool)):
            result = np.concatenate([result, [side]], axis=0)
            colorResult = np.concatenate([colorResult, [color]], axis=0)
        else:
            newSides = sideWithHole(side)      #TYPE1
            newSides = np.concatenate([newSides, createNewSideType1(side)], axis=0)
            newColors = np.repeat([color],3, axis=0)   #TYPE1
            newColors = np.concatenate([newColors, np.repeat(np.array([color])+0.03*iter,3, axis=0)], axis=0)
            a, b = recurseFuncType1(newSides,newColors,iter-1,randomBool)
            result = np.concatenate([result, a], axis=0)
            colorResult  = np.concatenate([colorResult, b], axis=0)
    return result, colorResult

#func to second type of generation
def recurseFuncType2(data,color, iter, randomBool):
    
    if (iter<=0): return data, color
    result = np.empty(shape=(0,3,3))
    colorResult = np.empty(shape=(0,3))
    for side, color in zip(data,color):
        if ((random.getrandbits(1)==1) & (randomBool)):
            result = np.concatenate([result, [side]], axis=0)
            colorResult = np.concatenate([colorResult, [color]], axis=0)
        else:
            newSides = np.array([side])         #TYPE2    
            newSides = np.concatenate([newSides, createNewSideType2(side)], axis=0)
            newColors = np.array([color])               #TYPE2
            newColors = np.concatenate([newColors, np.repeat(np.array([color])+0.03*iter,3, axis=0)], axis=0)
            a, b = recurseFuncType2(newSides,newColors,iter-1,randomBool)
            result = np.concatenate([result, a], axis=0)
            colorResult  = np.concatenate([colorResult, b], axis=0)
    return result, colorResult

# work only with random color (i just didnt want to write code for color)
def cycleFunc(data,iter,randomBool):
    for iter in range(iter):
        newSides = np.empty(shape=(0,3,3))
        for side in data:
            if ((random.getrandbits(1)==1) & (randomBool)):
                newSides = np.concatenate([newSides, [side]], axis=0)
            else:
                newSides = np.concatenate([newSides, sideWithHole(side)], axis=0)
                newSides = np.concatenate([newSides, createNewSideType1(side)], axis=0)
        data = newSides
    return data


# main snowflake func
def showSnowflake(iter, randomBool):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # creating first figure
    a = np.array([0, 0, 0])
    b = np.array([0.5, np.sqrt(3)/2, 0])
    c = np.array([1, 0, 0])
    h = np.array([0.5,np.sqrt(3)/2/3,np.sqrt(2/3)])

    data=np.array([[a,b,c], [a,c,h],[a,h,b],[b,h,c]])
    color = np.array([[0,0,0.5], [0,0.5,0],[0.5,0,0],[0.5,0.5,0]])

    #starting recurse
    data, color = recurseFuncType1(data,color,iter,randomBool)
    #data, color = recurseFuncType2(data,color,iter,randomBool)
    #data = data = cycleFunc(data,iter,randomBool)

    #plot
    ax.add_collection3d(Poly3DCollection(data, facecolors=color, linewidths=0, alpha=1))
    disableAxis(ax)
    ax.patch.set_facecolor('xkcd:mint green')
    fig.patch.set_facecolor('xkcd:mint green')
    fig.savefig(f'3dSnowFlake1_{iter}',dpi = 200)
    #plt.show()
    
if __name__ == "__main__":
    showSnowflake(3,False)  #calling func, there 3 - number of iteration, False - disable random mode