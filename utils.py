import numpy
from matplotlib import pyplot
import matplotlib
import seaborn


def show_image(img, img_shape, ax = ()):
    img_formated = numpy.reshape(img,img_shape)
    
    
    if  isinstance(ax, matplotlib.axes._subplots.Axes) :
        axis = ax
    
    elif len(ax) == 2:
        fig, axis = pyplot.subplots(figsize=ax)
    
    else:
        fig, axis = pyplot.subplots(figsize=(2,2))
    
    
    
    seaborn.heatmap(img_formated,
                vmin=0,
                vmax=255,
                cmap="binary",
                cbar=False,
                xticklabels=False,
                yticklabels=False,
                ax=axis)