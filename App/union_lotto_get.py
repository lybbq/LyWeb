import requests
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.0.0',
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control':'max-age=0',
        'Connection': 'keep-alive',
        'Sec-Ch-Ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': "Windows",
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests':'1'
}
# 遍历所有可能性的页数-url,目前最大30
def web_traverse_url(max_page=30):
        list_page_url = []
        prefix_url = 'https://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&'
        suffix_url = '&pageSize=30&systemType=PC'
        middle_url = 'pageNo='
        for loop in range(1, max_page):
                url = prefix_url + middle_url + str(loop) + suffix_url
                list_page_url.append(url)
        # print(list_page_url)
        return list_page_url

# param: 返回url数据 -
# return: dict
def web_get_url_data(url, head):
        response_data = []
        session = requests.session()
        for loop_url in url:
                response = session.get(url=loop_url, headers=head)
                data = split_date_red_bule_str(response.text)
                response_data.extend(data)

        return response_data
def split_date_red_bule_str(data_str):
        # 首次切割
        date_str = re.findall(r"date\":.*?,", data_str) # date:
        red_str = re.findall(r"red\":.*?\",", data_str)
        bule_str = re.findall(r"blue\":.*?\",", data_str)

        # 二次切割成数据
        data = []
        length = len(date_str)
        for loop in range(length):
                date = date_str[loop].strip("date:\"").strip(",\"")
                redBalls = red_str[loop].strip("red:\"").strip("\",").split(",")

                blue = int(bule_str[loop].strip("blue:\"").strip("\","))
                redBalls = [int(red) for red in redBalls] # 转为整数

                temp = [date] + redBalls + [blue]
                data.append(temp)
        return data

if __name__ == '__main__':
        url = web_traverse_url(max_page=30)
        save_data = web_get_url_data(url, head)

        df = pd.DataFrame(save_data)
        df.columns = ['Date', 'red1', 'red2', 'red3', 'red4', 'red5', 'red6', 'blue']
        print(df)
        df.to_csv('data.csv', index=False, header=True)


