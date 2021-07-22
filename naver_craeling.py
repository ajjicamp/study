import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

code = '005930'

# 기업개요: naver 크롤링
url = f'https://finance.naver.com/item/coinfo.nhn?code={code}'
source = requests.get(url).text
html = BeautifulSoup(source, 'lxml')
html.select('.summary_info')
gugy_result = ''
titles = html.select('.summary_info')
for title in titles:
    title = title.get_text()
    # title = re.sub('\n', '', title)
    title = re.sub('\n', '', title)     # title문자열의 줄바꿈(\n)을 없앤다. ''
    gugy_result = gugy_result + title
if '기업개요' in gugy_result:
    gugy_result = gugy_result.strip('기업개요')
gugy_result = gugy_result.replace('.', '. ')
print('기업개요\n', gugy_result)
# self.windowQ.put([0, gugy_result])

# 기업공시 crawling
date_result = []
jbjg_result = []
gygs_result = []
for i in [1, 2, 3]:
    url = f'https://finance.naver.com/item/news_notice.nhn?code={code}&page={i}'
    source = requests.get(url).text
    html = BeautifulSoup(source, 'lxml')
    dates = html.select('.date')
    date_result = date_result + [date.get_text() for date in dates]
    infos = html.select('.info')
    jbjg_result = jbjg_result + [info.get_text() for info in infos]
    titles = html.select('.title')
    for title in titles:
        title = title.get_text()
        title = re.sub('\n', '', title)
        gygs_result.append(title)

print('기업공시내용:\n', date_result, jbjg_result, gygs_result)

# try:
#     df = pd.DataFrame({'일자': date_result, '정보제공': jbjg_result, '공시': gygs_result})
# except Exception as e:
#     self.windowQ.put([1, f'WebCrawling 기업공시 {e}'])
# else:
#     self.windowQ.put([ui_num['기업공시'], df])

'''
def WebCrawling(self, cmd, code):
    if cmd == '기업개요':
        url = f'https://finance.naver.com/item/coinfo.nhn?code={code}'
        source = requests.get(url).text
        html = BeautifulSoup(source, 'lxml')
        html.select('.summary_info')
        gugy_result = ''
        titles = html.select('.summary_info')
        for title in titles:
            title = title.get_text()
            title = re.sub('\n', '', title)
            gugy_result = gugy_result + title
        if '기업개요' in gugy_result:
            gugy_result = gugy_result.strip('기업개요')
        gugy_result = gugy_result.replace('.', '. ')
        self.windowQ.put([0, gugy_result])
    elif cmd == '기업공시':
        date_result = []
        jbjg_result = []
        gygs_result = []
        for i in [1, 2, 3]:
            url = f'https://finance.naver.com/item/news_notice.nhn?code={code}&page={i}'
            source = requests.get(url).text
            html = BeautifulSoup(source, 'lxml')
            dates = html.select('.date')
            date_result = date_result + [date.get_text() for date in dates]
            infos = html.select('.info')
            jbjg_result = jbjg_result + [info.get_text() for info in infos]
            titles = html.select('.title')
            for title in titles:
                title = title.get_text()
                title = re.sub('\n', '', title)
                gygs_result.append(title)
        try:
            df = pd.DataFrame({'일자': date_result, '정보제공': jbjg_result, '공시': gygs_result})
        except Exception as e:
            self.windowQ.put([1, f'WebCrawling 기업공시 {e}'])
        else:
            self.windowQ.put([ui_num['기업공시'], df])
    elif cmd == '종목뉴스':
        date_result = []
        title_result = []
        ulsa_result = []
        for i in [1, 2]:
            url = f'https://finance.naver.com/item/news_news.nhn?code={code}&page={i}'
            source = requests.get(url).text
            html = BeautifulSoup(source, 'lxml')
            dates = html.select('.date')
            date_result = date_result + [date.get_text() for date in dates]
            infos = html.select('.info')
            ulsa_result = ulsa_result + [info.get_text() for info in infos]
            titles = html.select('.title')
            for title in titles:
                title = title.get_text()
                title = re.sub('\n', '', title)
                title_result.append(title)
        try:
            df = pd.DataFrame({'일자': date_result, '언론사': ulsa_result, '제목': title_result})
        except Exception as e:
            self.windowQ.put([1, f'WebCrawling 종목뉴스 {e}'])
        else:
            self.windowQ.put([ui_num['기업뉴스'], df])
    elif cmd == '재무제표':
        url = f'https://finance.naver.com/item/main.nhn?code={code}'
        source = requests.get(url)
        soup = BeautifulSoup(source.content, 'html.parser')

        html = soup.select('div.section.cop_analysis div.sub_section')[0]
        text_list = [item.get_text().strip() for item in html.select('th')]
        num_list = [item.get_text().strip() for item in html.select('td')]
        num_list = num_list[:130]
        data1 = {}
        data2 = {}
        columns = ['구분'] + text_list[3:13]
        k = 0
        for i, column in enumerate(columns):
            if i < 5:
                if column == '구분':
                    data1[column] = text_list[-16:-3]
                else:
                    data1[column] = [num for j, num in enumerate(num_list) if j % 10 == k]
                    k += 1
            else:
                data2[column] = [num for j, num in enumerate(num_list) if j % 10 == k]
                k += 1
        df1 = pd.DataFrame(data=data1)
        df2 = pd.DataFrame(data=data2)

        try:
            html = soup.select('div.section.trade_compare')[0]
        except IndexError:
            df3 = pd.DataFrame(columns=columns_jb)
        else:
            text_list = [item.get_text().strip() for item in html.select('th')]
            num_list = [item.get_text().strip() for item in html.select('td')]
            columns = text_list[1:6]
            ccount = 0
            for i, column in enumerate(columns):
                try:
                    columns[i] = self.dict_name[column[-6:]]
                except KeyError:
                    del columns[i]
                else:
                    ccount += 1
            if ccount == 5:
                columns = ['구분'] + columns
            else:
                columns = ['구분'] + columns + ['']
            for i, num in enumerate(num_list):
                if '상향\n\t\t\t\t+' in num:
                    num_list[i] = num.split('상향\n\t\t\t\t')[1]
                elif '상향\n\t\t\t\t' in num:
                    num_list[i] = '+' + num.split('상향\n\t\t\t\t')[1]
                if '하향\n\t\t\t\t-' in num:
                    num_list[i] = num.split('하향\n\t\t\t\t')[1]
                elif '하향\n\t\t\t\t' in num:
                    num_list[i] = '-' + num.split('하향\n\t\t\t\t')[1]
                if '보합' in num:
                    num_list[i] = num.split('보합')[1]
            data3 = {}
            k = 0
            for i, column in enumerate(columns):
                if column == '구분':
                    data3[column] = text_list[ccount + 1:]
                elif column == '':
                    data3[column] = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
                else:
                    data3[column] = [num for j, num in enumerate(num_list) if j % ccount == k]
                    k += 1
            df3 = pd.DataFrame(data=data3)

        self.windowQ.put([ui_num['재무년도'], df1])
        self.windowQ.put([ui_num['재무분기'], df2])
        self.windowQ.put([ui_num['동업종비교'], df3])

WebCrawling(self, '기업개요', '003950')

'''