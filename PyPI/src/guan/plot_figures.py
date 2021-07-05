# plot figures

import numpy as np

def plot(x, y, xlabel='x', ylabel='y', title='', filename='a', show=1, save=0, type='', y_min=None, y_max=None): 
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.20, left=0.18) 
    ax.plot(x, y, type)
    ax.grid()
    ax.set_title(title, fontsize=20, fontfamily='Times New Roman')
    ax.set_xlabel(xlabel, fontsize=20, fontfamily='Times New Roman') 
    ax.set_ylabel(ylabel, fontsize=20, fontfamily='Times New Roman') 
    if y_min!=None or y_max!=None:
        if y_min==None:
            y_min=min(y)
        if y_max==None:
            y_max=max(y)
        ax.set_ylim(y_min, y_max)
    ax.tick_params(labelsize=20) 
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    [label.set_fontname('Times New Roman') for label in labels]
    if save == 1:
        plt.savefig(filename+'.jpg', dpi=300) 
    if show == 1:
        plt.show()
    plt.close('all')

def plot_3d_surface(x, y, matrix, xlabel='x', ylabel='y', zlabel='z', title='', filename='a', show=1, save=0, z_min=None, z_max=None): 
    import matplotlib.pyplot as plt
    from matplotlib import cm
    from matplotlib.ticker import LinearLocator
    matrix = np.array(matrix)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    plt.subplots_adjust(bottom=0.1, right=0.65) 
    x, y = np.meshgrid(x, y)
    if len(matrix.shape) == 2:
        surf = ax.plot_surface(x, y, matrix, cmap=cm.coolwarm, linewidth=0, antialiased=False) 
    elif len(matrix.shape) == 3:
        for i0 in range(matrix.shape[2]):
            surf = ax.plot_surface(x, y, matrix[:,:,i0], cmap=cm.coolwarm, linewidth=0, antialiased=False) 
    ax.set_title(title, fontsize=20, fontfamily='Times New Roman')
    ax.set_xlabel(xlabel, fontsize=20, fontfamily='Times New Roman') 
    ax.set_ylabel(ylabel, fontsize=20, fontfamily='Times New Roman') 
    ax.set_zlabel(zlabel, fontsize=20, fontfamily='Times New Roman') 
    ax.zaxis.set_major_locator(LinearLocator(5)) 
    ax.zaxis.set_major_formatter('{x:.2f}')  
    if z_min!=None or z_max!=None:
        if z_min==None:
            z_min=matrix.min()
        if z_max==None:
            z_max=matrix.max()
        ax.set_zlim(z_min, z_max)
    ax.tick_params(labelsize=15) 
    labels = ax.get_xticklabels() + ax.get_yticklabels() + ax.get_zticklabels()
    [label.set_fontname('Times New Roman') for label in labels] 
    cax = plt.axes([0.80, 0.15, 0.05, 0.75]) 
    cbar = fig.colorbar(surf, cax=cax)  
    cbar.ax.tick_params(labelsize=15)
    for l in cbar.ax.yaxis.get_ticklabels():
        l.set_family('Times New Roman')
    if save == 1:
        plt.savefig(filename+'.jpg', dpi=300) 
    if show == 1:
        plt.show()
    plt.close('all')

def plot_contour(x, y, matrix, xlabel='x', ylabel='y', title='', filename='a', show=1, save=0):  
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2, right=0.75, left = 0.16) 
    x, y = np.meshgrid(x, y)
    contour = ax.contourf(x,y,matrix,cmap='jet') 
    ax.set_title(title, fontsize=20, fontfamily='Times New Roman')
    ax.set_xlabel(xlabel, fontsize=20, fontfamily='Times New Roman') 
    ax.set_ylabel(ylabel, fontsize=20, fontfamily='Times New Roman') 
    ax.tick_params(labelsize=15) 
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    [label.set_fontname('Times New Roman') for label in labels] 
    cax = plt.axes([0.78, 0.17, 0.08, 0.71])
    cbar = fig.colorbar(contour, cax=cax) 
    cbar.ax.tick_params(labelsize=15) 
    for l in cbar.ax.yaxis.get_ticklabels():
        l.set_family('Times New Roman')
    if save == 1:
        plt.savefig(filename+'.jpg', dpi=300) 
    if show == 1:
        plt.show()
    plt.close('all')