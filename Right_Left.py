# todo 좌우화살표키를 이용하여 그래프를 왔다갔다하는 로직

import numpy as np
import matplotlib.pyplot as plt

# define your x and y arrays to be plotted
t = np.linspace(start=0, stop=2*np.pi, num=100)    # x값
y1 = np.cos(t)
y2 = np.sin(t)
y3 = np.tan(t)
plots = [(t,y1), (t,y2), (t,y3)]

# now the real code :)
curr_pos = 0

def key_event(e):
    global curr_pos               # 전역변수 선언

    if e.key == "right":
        curr_pos = curr_pos + 1
    elif e.key == "left":
        curr_pos = curr_pos - 1
    else:
        return

    curr_pos = curr_pos % len(plots)

    # 현재좌표축을 지우는 명령, 즉, 그래프를 새로 그리기 위하여 현재 있는 그래프를 지운다.
    ax.cla()

    # plots라는 리스트에 (x,y)축 여러개를 듀플로 저장해 두고 번갈아서 띄운다. 번갈아서 띄운다. 여기서 index값은 듀플내의 x축값[0], y축값[1]이다. plots내 plot값이 아니다.
    ax.plot(plots[curr_pos][0], plots[curr_pos][1])

    # canvas update하는 함수
    fig.canvas.draw()

fig = plt.figure()                     # figure 생성
# 요게 뭐하는 건지가 중요
fig.canvas.mpl_connect('key_press_event', key_event)
# fig.canvas.mpl_connect("button_press_event", click)        <= 이렇게 하면 마우스버튼을 클릭하면 동작하게 된다.

ax = fig.add_subplot(111)
# 아마도 맨처음에 나타내는 화면아닐까?
ax.plot(t,y1)
plt.show()
