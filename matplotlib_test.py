import matplotlib.pyplot as plt

from matplotlib.gridspec import GridSpec


# def format_axes(fig):
#     for i, ax in enumerate(fig.axes):
#         ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
#         ax.tick_params(labelbottom=False, labelleft=False)

fig = plt.figure(layout="constrained")

gs = GridSpec(3, 3, figure=fig)
ax1 = fig.add_subplot(gs[0, :])
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
ax1.set_xlabel('time (s)')
ax1.set_ylabel('current (nA)')
ax1.set_title('Gaussian colored noise')
# identical to ax1 = plt.subplot(gs.new_subplotspec((0, 0), colspan=3))
ax2 = fig.add_subplot(gs[1, :-1])
ax3 = fig.add_subplot(gs[1:, -1])
ax4 = fig.add_subplot(gs[2, 0])
ax5 = fig.add_subplot(gs[2, -2])

fig.suptitle("GridSpec")
# format_axes(fig)

plt.show()