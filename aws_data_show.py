#json python 利用
#plot image
#js front
#aws iot grass dataフォーマット
import json
import math
from matplotlib import pyplot

#
def json_read():
    f = open("data\myu_s.json", 'r')

    json_data = json.load(f) #JSON形式で読み込む

    name_list = ["honoka","eri","kotori","umi","rin","maki","nozomi","hanayo","niko"]
    for name in name_list:
        print("{0:6s} 身長：{1}cm BWH: ".format(name,json_data[name]["height"]),end="\t")
        for i in range(len(json_data[name]["BWH"])):
            print("{}".format(json_data[name]["BWH"][i]),end="\t")
        print()


def makegraf1() :
    datas = [
        [1,1.000649,1.000649,1.000649],
        [10,1.000648,1.001081,1.000648],
        [100,1.005793,1.008796,0.997640],
        [1000,1.005395,1.128072,0.961838],
        [10000,1.003097,1.763680,0.706436],
        [100000,1.000356,1.986330,0.364987],
        [1000000,1.000036,2.793968,0.356083],
        [10000000,1.000003,1.874999,0.375001],
    ]
    
    # xyデータに再マッピング
    x = []
    y1 = []
    y2 = []
    y3 = []
    for data in datas:
        x.append( math.log(data[0], 10) )
        y1.append(data[1])
        y2.append(data[2])
        y3.append(data[3])
    
    
    # グラフ内容設定
    pyplot.xlim([ x[0], x[len(x)-1] ])
    pyplot.xlabel("data cnt(10**n)")
    pyplot.ylabel("used memory rate")
    
    pyplot.title('redis decrease used memory test')
    pyplot.plot(x, y1, label = "hset")
    pyplot.plot(x, y2, label = "json")
    pyplot.plot(x, y3, label = "compressed json")
    pyplot.legend()

    # 表示
    pyplot.show()









if __name__=='__main__':
    json_read()
    
    makegraf1()
    
#