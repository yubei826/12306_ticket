# 12306余票查询

# 查询携带cookie，防止查询错误

import requests
import time

if __name__ == "__main__":

    #创建session()对象s获取cookie
    s = requests.session()
    s_url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E5%8C%97%E4%BA%AC,BJP&ts=%E4%B8%8A%E6%B5%B7,SHH&date=' + time.strftime('%Y-%m-%d',time.localtime()) + '&flag=N,N,Y'
    s.get(s_url)

    #输入出发地和目的地，并加入异常处理防止输入错误时程序终止
    while True:
        try:
            chufadi = input('出发地：')
            mudidi = input('目的地：')
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
      