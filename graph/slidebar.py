# 작업목표: 먼저 매도호가1 가격 plot를 화면을 적당한 크기(화면당 x축눈금 100개)로 나누어 띄우고, right_key, left_key로 좌우로 왔다갔다하면서 분석할 지점을 찾은 후
# 분석할 지점을 찾으면 마우스를 클릭하여 그 부분을 중점으로 다시 분석용 그래프(채결량, 호가잔량 등을 시각화하여)를 띄워 분석에 돌입한다.

import matplotlib.pyplot as plt
import sqlite3
import pandas as pd
from math import ceil, floor        # 소수점미만 올림 계산
from matplotlib.widgets import Slider
import numpy as np

# con = sqlite3.connect('mh_real.db')
con = sqlite3.connect('../../mh_trader/db/mh.db')
df = pd.read_sql("SELECT * FROM 주식체결", con, index_col=None)
df01 = pd.read_sql("SELECT * FROM 주식호가잔량", con, index_col=None)

# DataFrame 합치기
dfs = pd.concat([df,df01])
# 합친 dataframe sort해서 새로 저장
dfs.sort_values(by=['종목코드', 'index'], inplace=True, ignore_index = True)

## dataframe 행의 null값을 0 또는 특정값으로 대체
# 먼저 column 중 매수체결, 매도체결, 체결강도, 매수도호가직전대비1,2,3 column의 nan 값을 0으로 대체
dfs['체결시간'] = dfs['체결시간'].fillna(0)
dfs['매수체결'] = dfs['매수체결'].fillna(0)
dfs['매도체결'] = dfs['매도체결'].fillna(0)
dfs['체결강도'] = dfs['체결강도'].fillna(0)
dfs['매수호가직전대비1'] = dfs['매수호가직전대비1'].fillna(0)
dfs['매수호가직전대비2'] = dfs['매수호가직전대비2'].fillna(0)
dfs['매수호가직전대비3'] = dfs['매수호가직전대비3'].fillna(0)
dfs['매도호가직전대비1'] = dfs['매도호가직전대비1'].fillna(0)
dfs['매도호가직전대비2'] = dfs['매도호가직전대비2'].fillna(0)
dfs['매도호가직전대비3'] = dfs['매도호가직전대비3'].fillna(0)
dfs['매수호가총잔량직전대비'] = dfs['매수호가총잔량직전대비'].fillna(0)
dfs['매도호가총잔량직전대비'] = dfs['매도호가총잔량직전대비'].fillna(0)

# 나머지 column은 같은 종목코드을 기준으로 (필터링 필요) 직전 row값으로 대체.(호가시간 ; 매수호가1,2,3 ; 매도호가1,2,3 ; 매수호가수량1,2,3 ; 매도호가수량1,2,3 ;매수/매도호가 총잔량)
# ['종목코드']column에서 종목을 추출하여 jongmok 리스트에 저장
jongmok= []
save_row = None
for row in dfs['종목코드']:
    if row != save_row:
        jongmok.append(row)
    save_row = row

# 같은종목별로 그룹화하여 작업시작
# 그룹화를 쉽게하는 함수가 있다. series.groupby() 활용방법은 다음에...
for code in jongmok:
    # 앞방향으로 채우기한 후 맨앞쪽은 뒤방향으로 채우기
    dfs[dfs['종목코드']==code] = dfs[dfs['종목코드']==code].fillna(method='ffill')
    dfs[dfs['종목코드']==code] = dfs[dfs['종목코드']==code].fillna(method='bfill')

# dfs의 column명 ['index']를 ['수신시간']으로 변경
dfs.rename(columns={'index':'수신시간'}, inplace = True)

# todo 여기까지는 확실하게 되었다.
# 이제는 가격변동이 있는 자리를 찾는 것.  ======> 그래프부터 그려보자 어떻게 찾아야 할지 잘 모르겠으니까

# 종목[0]부터 시작하여 끝까지. todo 그룹화하여 작업하는 것이 가능할른지도 검토
# for i in jongmok:
#     code = dfs[dfs['종목코드']==i]

# 테스트 완료할때까지는 당분간 한종목만 한다.
# 먼저 매도호가1 그래프를 보고 스코롤하면서 분석할 자리를 찾는다. # 그래프는 스크롤바를 이용하자.
# 종목별 data를 필터링하여 code 변수에 저장. 일단 테스트
code_data = dfs[dfs['종목코드'] == jongmok[0]]

x = code_data['수신시간']
y = code_data['매도호가1']
y2 = code_data['매수체결']
y3 = code_data['매도체결']
y4 = code_data['체결강도']
y5 = code_data['매도호가수량1']
y6 = code_data['매수호가수량1']
# y7 = code_data['매도호가수량1']


# now the real code :)
x_tick_ = None
y_tick_ = None
curr_pos = 0
def key_event(e):
    global curr_pos, x_tick_, y_tick_               # 전역변수 값 변경한다.

    if e.key == "right":
        curr_pos = curr_pos + 1
    elif e.key == "left":
        curr_pos = curr_pos - 1

    else:
        return

    # curr_pos = curr_pos % len(plots)
    curr_pos = curr_pos % len(plots)

    # 현재좌표축을 지우는 명령, 즉, 그래프를 새로 그리기 위하여 현재 있는 그래프를 지운다.
    ax.cla()
    x_tick_ = x[plots[curr_pos][0]:plots[curr_pos][1]]
    y_tick_ = y[plots[curr_pos][0]:plots[curr_pos][1]]
    # print('key-event=x축', x_tick_)
    ax.plot(x_tick_, y_tick_, label='hoga1_graph')
    ax.legend()
    ax.set_title("hoga1 graph", fontdict={'size': 18})

    # x축 눈금표시
    ax.set_xticks(x_tick_)
    # x축 눈금에 label표시 및 기울기
    x_label_ = []
    for x_ in x_tick_:
        x_label_.append(x_[11:22])
    ax.set_xticklabels(x_label_, rotation=-90)

    # x축에 대한 label표시
    ax.set_xlabel('timestamp', color='black', fontdict={'size': 15})
    # y축에 대한 label표시
    ax.set_ylabel('sell_hoga1', color='green', fontdict={'size': 15})

    fig.canvas.draw()

def new_plot(x_pos):
    print("new_plot: ",  x_pos)
    start_num = x_pos -25
    end_num = x_pos +25
    x_tick_ = x[start_num:end_num]
    y_tick_ = y[start_num:end_num]
    # print("x값: ", x)
    # print("new_plot x_tick:", x_tick_)
    # print("now_plot y_tick:", y_tick_)
    fig, ax = plt.subplots()
    ax.plot(x_tick_, y_tick_, 'go-')
    ax.set_xticks(x_tick_)
    ax.set_xticklabels(x_tick_, rotation= -90)

    ax2 = ax.twinx()
    y2_tick_ = y2[start_num:end_num]
    y3_tick_ = y3[start_num:end_num]
    y4_tick_ = y4[start_num:end_num]
    y5_tick_ = y5[start_num:end_num]
    y6_tick_ = y6[start_num:end_num]
    ax2.bar(x_tick_, y2_tick_, color='red')
    ax2.bar(x_tick_, y3_tick_, color='blue')
    ax2.plot(x_tick_, y4_tick_, color='black')
    ax2.plot(x_tick_, y5_tick_, color='blue')
    ax2.plot(x_tick_, y6_tick_, color='red')



    # 위와 같이 그려보니 혼란스럽다. 두개를 분리하거나 적어도 매도호가1 그래프는 위에서만 놀고 다른 것들과 겹쳐서는 안되겠다.
    # 한편으로 매수/매도호가수량과 체결량의 상관관계를 잘 살펴볼수 있도록 해야 한다.

    plt.show()


def click(event):
    # 클릭한 x좌표 기준값 찾기
    print("xdata 값: ", event.xdata)
    x_base = floor(event.xdata)

    # todo 아래 공식은 한화면에 보여주는 개수를 조정하면 같이 조정해야 한다.
    x_pos = floor(np.mean(x_tick_.index)-25 + x_base)

    # 기준값을 중심으로 좌우 25 tick을 포함한 그래프 그리기
    new_plot(x_pos)

# define your x and y arrays to be plotted
# 그래프 x축 눈금을 몇개단위(show_ticks)로 표시하는 그래프그리기
cnt = len(code_data['수신시간'])
# 보여줄 눈금개수
show_ticks = 50
# 반복회수 산출
repeat = ceil(cnt / show_ticks)

start_num = 0
end_num = -1

plots =[]
for i in range(1, repeat + 1):
    start_num = end_num + 1
    end_num = i * show_ticks
    plots.append((start_num, end_num))

fig = plt.figure()                     # figure 생성
# 요게 뭐하는 건지가 중요
fig.canvas.mpl_connect('key_press_event', key_event)
fig.canvas.mpl_connect("button_press_event", click)      #  <= 이렇게 하면 마우스버튼을 클릭하면 동작하게 된다.

ax = fig.add_subplot(111)
# 아마도 맨처음에 나타내는 화면아닐까?
x_tick_ = x[plots[0][0]:plots[0][1]]
y_tick_ = y[plots[0][0]:plots[0][1]]
ax.plot(x_tick_, y_tick_, label='hoga1_graph')
ax.legend()
ax.set_title("hoga1 graph", fontdict={'size': 18})

# x축 눈금표시
ax.set_xticks(x_tick_)
# x축 눈금에 label표시 및 기울기
x_label_ =[]
for x_  in x_tick_:
    x_label_.append(x_[11:22])

ax.set_xticklabels(x_label_, rotation=-90)
# x축에 대한 label표시
ax.set_xlabel('timestamp', color='black', fontdict={'size': 15})
# y축에 대한 label표시
ax.set_ylabel('sell_hoga1', color='green', fontdict={'size':15})

plt.show()


# 종목별로 매도호가1을 나타내는 그래프를 그리는 함수
# def doGraph(start_num, end_num):
#     x = code['index'][start_num:end_num]  # todo column name 변경해야한다. 진짜 index(0,1,2,3...)와 헷갈린다.
#     y = code['매도호가1'][start_num:end_num]
#
#     # x축 label이 너무 길어서 시분초.밀리세컨드2자리로로 표시
#     xlabel = []
#     # for i in code['index']
#     for i in x:
#         xlabel.append(i[11:22])
#
#     fig, ax = plt.subplots()
#
#     # x, y 그래프 label은 범례(별도로 ax.legend() 명령 필요.
#     ax.plot(x, y, label='sell_hoga1')
#     # 범례 표시
#     ax.legend()
#
#     # 제목표시, 한글로 표시하려면 다른 장치 필요
#     ax.set_title("hoga1 graph", fontdict={'size': 18})
#
#     # x축 눈금표시
#     ax.set_xticks(x)
#     # x축 눈금에 label표시 및 기울기
#     ax.set_xticklabels(xlabel, rotation=-90)
#     # x축에 대한 label표시
#     ax.set_xlabel('timestamp', color='black', fontdict={'size': 15})
#     # y축에 대한 label표시
#     ax.set_ylabel('sell_hoga1', color='green', fontdict={'size':15})
#
#     # y축 눈금표시 (호가단위에 따라 한칸씩 표시하는것이 나을 듯
#     plt.show()


# 그래프 x축 눈금을 몇개단위(show_ticks)로 표시하는 그래프그리기
# cnt = len(code['index'])
# # 보여줄 눈금개수
# show_ticks = 50
# # 반복회수 산출
# repeat = ceil(cnt / show_ticks)
#
# start_num = 0
# end_num = -1
# y= []
# for i in range(1, repeat+1):
#     start_num = end_num +1
#     end_num = i * show_ticks
#     # y[i] =start_num
#
#
#     doGraph(start_num, end_num)
#

# 다음은 찾은 자리를 기준으로 xlim(min,max)하여 분석한다. 그래프 외에 숫자로도 분석을 병행한다


# 드디어 그래프를 그리는 순서


# df['index'] = pd.to_datetime(df['index'])
# df01['index'] = pd.to_datetime(df01['index'])
#
#
#
# code = df[df['종목코드'].isin(['352820'])]
# code01 = df01[df01['종목코드'].isin(['352820'])]
#
# # print(df)
# # print(df01)
#
# x = code['index']
# y = code['매수체결']
#
# x1 = code['index']
# y1 = code['매도체결']
#
# x2 = code['index']
# y2 = code['체결강도']
#
# x11 = code01['index']
# y11 = code01['매도호가1']
#
#
# # fig, ax = plt.subplots()
# fig = plt.figure()
#
# ax = fig.add_subplot(212)
# ax.bar(x, y, width=0.2, color='red', label='buy_sign')
# ax.bar(x1, y1, width=0.1,  color='blue')
#
# # plt.show()
# # input()
#
#
# # xv =[]
# # for d in code['index']:
# #     xv.append(d[11:21])
# # end = len(xv)-1
#
# ax.set_xticks(x)
# ax.set_xticklabels(x, rotation=-90)
#
# ax.set_xlabel('timestamp', color='black', fontdict={'size': 15})
# ax.set_ylabel('buy_sign', color='green', fontdict={'size':15})
# # ax.legend("buy_sign")
# # ax.legend()
# ax.legend(loc="center right", bbox_to_anchor=(0.5,0.97))
# # plt.tick_params(direction = 'in')
# ax.grid(True, color='gray', alpha=0.2, linestyle='-')
#
# # plt.show()
# # input()
#
# '''
# # ax10 = fig.add_subplot(211, sharex=ax)
# ax10 = fig.add_subplot(211)
# ax10.plot(x11, y11)
# ax10.set_xticks(x11)
# ax10.set_xticklabels(x11,rotation=-90)
# ax10.grid(True, color='gray', alpha=0.2, linestyle='-')
#
# # plt.xticks(color='w')
# # ax10.axes.xaxis.set_ticklabels([])
# # ax10.axes.xaxis.set_visible(False)
# '''
#
#
# ax2 =ax.twinx()
# ax2.plot(x,y2, color='black', label='sign_strength')
# ax2.set_ylabel('sign_strength', color='black', fontdict={'size':15})
# ax2.legend(loc="center left", bbox_to_anchor=(0.5,0.97))
# ax.set_xticks(x)
# ax.set_xticklabels(x, rotation=-90)
# # plt.tick_params(direction = 'in')
#
#
# plt.show()
# input()
#
#
# def slidebar(pos):
#     ax.set_xlim(pos - 1, pos + showbars + 1)
#     # plt.set_xlim(pos - 1, pos + showbars + 1)
#
# showbars = 50
#
# slidebarpos = plt.axes([0.01, 0.01, 0.7, 0.02], facecolor="skyblue")
# slider = Slider(slidebarpos, '', 0, len(x) - showbars, valinit=0)
# slider.on_changed(slidebar)
# slidebar(0)
#
#
# plt.show()
#


