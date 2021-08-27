
# 命令行12306火车余票查询器

### 使用到的工具
  - Python3.x
  - requests库，用来请求http
  - prettytable，是信息以更好看的表格呈现出来
  - colorama，用来设置命令行中显示的颜色

  如果提示没有该模块，运行`python3 -m pip install requests`安装模块


## 思路过程
  - 请求URL获取余票信息 `https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2021-08-26&leftTicketDTO.from_station=WHN&leftTicketDTO.to_station=SHH&purpose_codes=ADULT`

  - 分析参数
    `leftTicketDTO.train_date=2021-09-01
    leftTicketDTO.from_station=WHN
    leftTicketDTO.to_station=SHH
    purpose_codes=ADULT`


  - 解析地址和拼音简写 `https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8971`

  - 创建请求，获取session和cookie `https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E5%8C%97%E4%BA%AC,BJP&ts=%E4%B8%8A%E6%B5%B7,SHH&date=' + time.strftime('%Y-%m-%d',time.localtime()) + '&flag=N,N,Y`

  - 格式化返回

  - 增加颜色辨识