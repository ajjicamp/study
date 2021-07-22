# 정말 귀한 자료이다. list, [콤마]형태를 배우고 그래프에서 클릭한 값을 이용하여 클래스에서 실행하는 방법까지 ...
from matplotlib import pyplot as plt

class LineBuilder:
    def __init__(self, line):
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self) #여기서 cid는 의미없다.

    def __call__(self, event):
        print('click', event)
        if event.inaxes!=self.line.axes: return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs, self.ys)      # self.xs == x축값, self.ys == y축값을 의미,
                                                    # 클릭이 되면 self.xs / ys값의 요소가 하나씩 추가된다.
        self.line.figure.canvas.draw()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('click to build line segments')
line, = ax.plot([0], [0])  # empty line
print('line', line)
print(type(line))

linebuilder = LineBuilder(line)

plt.show()

