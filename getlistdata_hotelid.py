#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

#通过酒店id 获取gethoteldata接口的数据
def get_hoteldata(hotelid):
    url = 'https://xapi.elong.com/xcxdetail/gethoteldata/'
    data = {
        "indate": "2018-07-21",
        "outdate": "2018-07-22",
        "hotelid": hotelid,
        "usercityid": "0101",
        "httpAgentInfo": {"tcOpenId":"o498X0ZhjY4H7gEAMiYuaTBYz7r4","wxSource":"tcqb_xcx","ct":5,"bns":3,"hoff":1001}
    }

    r = requests.post(url,data)
    return r.json()


#通过酒店名字  获取getlistdata接口的数据
def get_listdata(hotelname):
    url = 'https://xapi.elong.com/newxcxlist/getlistdata/'
    data = {
        "city": "0101",
        "indate": "2018-07-21",
        "outdate": "2018-07-22",
        "keywords": hotelname,
        "page": "10",
        "pageindex": "0",
        "AB":"A",
        "httpAgentInfo":{"tcOpenId":"o498X0ZhjY4H7gEAMiYuaTBYz7r4","wxSource":"tcqb_xcx","ct":5,"bns":3,"hoff":1001}
    }

    r = requests.post(url,data)
    return r.json()


def read_file(path):
    hotel_ids=[]
    with open(path,'r') as f:
        for line in f.readlines():
            hotel_ids.append(line.strip())

    return hotel_ids


if __name__ =='__main__':
    hotel_ids=read_file('/Users/user/Documents/demo/hotelid.txt')
    for hotelid in hotel_ids:
        hotelname=get_hoteldata(hotelid)['hotelName']
        #print(get_listdata(hotelname)['hotelList'][0])
        print(get_listdata(hotelname)['hotelList'][0]['bargainPrice'])

















