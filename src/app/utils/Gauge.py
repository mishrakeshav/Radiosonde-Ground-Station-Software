"""
This module was used to generate the gauge images and is not actually 
used in the software
"""



import os, sys
import matplotlib
from matplotlib import cm
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Wedge, Rectangle

def degree_range(n): 
    start = np.linspace(0,180,n+1, endpoint=True)[0:-1]
    end = np.linspace(0,180,n+1, endpoint=True)[1::]
    mid_points = start + ((end-start)/2.)
    return np.c_[start, end], mid_points

def rot_text(ang): 
    rotation = np.degrees(np.radians(ang) * np.pi / np.pi - np.radians(90))
    return rotation

def gauge(N,colors='jet_r', arrow=1, title='',fname=None): 
    
    """
    some sanity checks first
    
    """
    
    if arrow > N: 
        raise Exception("\n\nThe category ({}) is greated than \
        the length\nof the labels ({})".format(arrow, N))
 
    
    """
    if colors is a string, we assume it's a matplotlib colormap
    and we discretize in N discrete colors 
    """
    
    if isinstance(colors, str):
        cmap = cm.get_cmap(colors, N)
        cmap = cmap(np.arange(N))
        colors = cmap[::-1,:].tolist()
    if isinstance(colors, list): 
        if len(colors) == N:
            colors = colors[::-1]
        else: 
            raise Exception("\n\nnumber of colors {} not equal \
            to number of categories{}\n".format(len(colors), N))

    """
    begins the plotting
    """
    
    fig, ax = plt.subplots()
    ang_range, mid_points = degree_range(N)

    
    """
    plots the sectors and the arcs
    """
    patches = []
    for ang, c in zip(ang_range, colors): 
        # sectors
        patches.append(Wedge((0.,0.), .4, *ang, facecolor='w', lw=2))
        # arcs
        patches.append(Wedge((0.,0.), .4, *ang, width=0.10, facecolor=c, lw=2, alpha=1))
    
    [ax.add_patch(p) for p in patches]

    
    """
    set the bottom banner and the title
    """
    r = Rectangle((-0.4,-0.1),0.8,0.1, facecolor='w', lw=2)
    ax.add_patch(r)
    
    ax.text(0.5,0.0, title , horizontalalignment='center', \
         verticalalignment='bottom', fontsize=14, fontweight='bold', transform = ax.transAxes)

    """
    plots the arrow now
    """
    
    pos = mid_points[abs(arrow - N)]
    
    ax.arrow(0, 0, 0.225 * np.cos(np.radians(pos)), 0.225 * np.sin(np.radians(pos)), \
                 width=0.04, head_width=0.09, head_length=0.1, fc='k', ec='k')
    
    ax.add_patch(Circle((0, 0), radius=0.02, facecolor='k'))
    ax.add_patch(Circle((0, 0), radius=0.01, facecolor='w', zorder=11))

    """
    removes frame and ticks, and makes axis equal and tight
    """
    
    ax.set_frame_on(False)
    ax.axes.set_xticks([])
    ax.axes.set_yticks([])
    ax.axis('equal')

    plt.tight_layout()
    if fname:
        fig.savefig(fname, dpi=200)

def update_gauge(arrow, number):
        """
        Updates the gauges
        """
        gauge(number, colors = 'cool', arrow = arrow, title=f'Pressure hPa', fname=f"images/pressure/{arrow}.png")
        gauge(number, colors = 'autumn',arrow = arrow, title=f'Temp {chr(176)}C',fname=f"images/temperature/{arrow}.png")
        gauge(number, colors='summer',arrow=arrow, title=f'Humidity %',fname=f"images/humidity/{arrow}.png")
        gauge(number, colors = 'copper',arrow=arrow, title=f'Speed m/s',fname=f"images/wind_speed/{arrow}.png")
        gauge(number, colors = 'PuOr',arrow=arrow, title=f'Direction {chr(176)}',fname=f"images/wind_direction/{arrow}.png")
        gauge(number, colors = 'coolwarm',arrow=arrow, title=f'Altitude m',fname=f"images/altitude/{arrow}.png")

if __name__ == '__main__':
    for i in range(1, 101):
        update_gauge(i, 100)

