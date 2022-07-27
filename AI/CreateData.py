# Make Dataset
import pandas as pd
import numpy as np
import random
import os
import matplotlib.pyplot as plt

temp, humi = [], []
feat, color = [], []
path = r'D:\1 College study.2-2\新国大暑研\3 Artificial Intelligence of Things\P03 Project\AI\Data\\'

def Return_FeatColor(x):
    if x==1:
        return "x", 'black'
    elif x==2:
        return "f", 'orange'
    elif x==3:
        return "h", 'blue'
    elif x==4:
        return "c", 'red'

def DecideFeature(nowtemp, nowhumi):
    if(nowtemp < 25.0):
        return Return_FeatColor(1)
    elif(nowtemp < 30.0):
        return Return_FeatColor(2)
    elif(nowtemp < 35.0 and nowhumi > 60.0):
        return Return_FeatColor(3)
    else:
        return Return_FeatColor(4)

def RandomDecideFeature(nowtemp, nowhumi):
    num = int(random.uniform(1,5))
    return Return_FeatColor(num)

# 展示
def SHOW(x_, y_, k):
    plt.figure()
    plt.scatter(x_, y_, c=k, s=4)
    plt.xticks(np.arange(0, 50, step=5))
    plt.yticks(np.arange(0, 110, step=10))
    plt.grid(color = 'r', linestyle = '--', linewidth = 0.3)
    plt.legend()
    plt.show()

def main():
    # 限制数据
    for i in range(800):
        nowhumi = random.uniform(0, 100)
        nowtemp = random.uniform(0, 45)
        nowfeat, nowcolor = DecideFeature(nowtemp, nowhumi)
        humi.append(nowhumi)
        temp.append(nowtemp)
        feat.append(nowfeat)
        color.append(nowcolor)
    # 随机数据
    for i in range(200):
        nowhumi = random.uniform(0, 100)
        nowtemp = random.uniform(0, 45)
        nowfeat, nowcolor = RandomDecideFeature(nowtemp, nowhumi)
        humi.append(nowhumi)
        temp.append(nowtemp)
        feat.append(nowfeat)
        color.append(nowcolor)
    # 显示
    SHOW(temp, humi, color)
    # 导出
    
    Data = {'temp': temp, 'humi': humi, 'feat': feat, 'color': color}
    df = pd.DataFrame(Data)
    df.to_csv(path + "data.csv", index=False, sep=',')
    



if __name__ == '__main__':
    main()