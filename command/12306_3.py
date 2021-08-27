# 12306余票查询

# 增加出发地目的地汉字转拼音

import requests
import re
import time

if __name__ == "__main__":
    
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }

    #获取城市名称对应的编码,数据为字典形式 {城市：编码}
    name_url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8971'
    name_id = requests.get(url=name_url,headers=headers).text
    name_stations = dict(re.findall(r'([\u4e00-\u9fa5]+).*?([A-Z]+)', name_id))

    #创建session()对象s获取cookie
    s = requests.session()
    s_url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E5%8C%97%E4%BA%AC,BJP&ts=%E4%B8%8A%E6%B5%B7,SHH&date=' + time.strftime('%Y-%m-%d',time.localtime()) + '&flag=N,N,Y'
    s.get(s_url)

    #输入出发地和目的地，并加入异常处理防止输入错误时程序终止
    while True:
        try:
            chufadi = name_stations[input('出发地：')]
            mudidi = name_stations[input('目的地：')]
            riqi = input('日期(yyyy-mm-dd)：')
            if len(riqi) != 10:
                continue
            break
        except:
            pass

    #车次数据的链接的组成
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=' + riqi + '&leftTicketDTO.from_station=' + chufadi +'&leftTicketDTO.to_station=' + mudidi +'&purpose_codes=ADULT'
    response = s.get(url).text

    print(response)
      