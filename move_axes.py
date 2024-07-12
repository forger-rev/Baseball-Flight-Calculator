import matplotlib.pyplot as plt


def move_axes(ax, fig, subplot_args, remove=False):
    """Move an Axes object from a figure to a new pyplot managed Figure in
    the specified subplot.
    
    ax = the original Axes
    fig = the new figure
    subplot_args = where to put the ax in the new figure, e.g. (nrows, ncols, index)
    """

    # get a reference to the old figure context so we can release it
    old_fig = ax.figure

    # remove the Axes from it's original Figure context
    ax.remove()

    # set the pointer from the Axes to the new figure
    ax.figure = fig

    # add the Axes to the registry of axes for the figure
    fig.axes.append(ax)
    # twice, I don't know why...
    fig.add_axes(ax)

    # then to actually show the Axes in the new figure we have to make
    # a subplot with the positions etc for the Axes to go, so make a
    # subplot which will have a dummy Axes
    dummy_ax = fig.add_subplot(*subplot_args)

    # then copy the relevant data from the dummy to the ax
    ax.set_position(dummy_ax.get_position())

    # then remove the dummy
    dummy_ax.remove()

    # close the figure the original axis was bound to
    if remove:
        plt.close(old_fig)
    else:
        return old_fig