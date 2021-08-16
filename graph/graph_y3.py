# 한 figure에 y축을 왼쪽 2개, 오른쪽 한개 도합 3개를 설정하는 방법
import matplotlib.pyplot as plt
def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)
fig, host= plt.subplots()
fig.subplots_adjust(left=0.25)
par1= host.twinx()
par2= host.twinx()
# Offset the right spine of par2.  The ticks and label have already been
# placed on the right by twinx above.
par2.spines["left"].set_position(("axes", -0.2))
par2.yaxis.tick_left()
par2.yaxis.set_label_position("left")
# Having been created by twinx, par2 has its frame off, so the line of its
# detached spine is invisible.  First, activate the frame but make the patch
# and spines invisible.
make_patch_spines_invisible(par2)
# Second, show the right spine.
par2.spines["left"].set_visible(True)
p1,= host.plot([0, 1, 2], [0, 1, 2], "b-", label="Density")
p2,= par1.plot([0, 1, 2], [0, 3, 2], "r-", label="Temperature")
p3,= par2.plot([0, 1, 2], [50, 30, 15], "g-", label="Velocity")
host.set_xlim(0, 2)
host.set_ylim(0, 2)
par1.set_ylim(0, 4)
par2.set_ylim(1, 65)
host.set_xlabel("Distance")
host.set_ylabel("Density")
par1.set_ylabel("Temperature")
par2.set_ylabel("Velocity")
host.yaxis.label.set_color(p1.get_color())
par1.yaxis.label.set_color(p2.get_color())
par2.yaxis.label.set_color(p3.get_color())
tkw= dict(size=4, width=1.5)
host.tick_params(axis='y', colors=p1.get_color(), **tkw)
par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
host.tick_params(axis='x', **tkw)
lines= [p1, p2, p3]
host.legend(lines, [l.get_label() for l in lines])
plt.show()