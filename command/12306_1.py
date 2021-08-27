# 12306余票查询

# 查询余票主接口

import requests

if __name__ == "__main__":

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
    response = requests.get(url).text

    print(response)
      