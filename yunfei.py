# -*- coding: utf-8 -*-

import pandas as pd


def yunda_biaozhun(input_sheng='江苏', input_weight=0.0, flag_hebei=False):
    """
    注意河北
    是不是河北的承德 唐山 张家口
    flag_hebei = False
    """
    data = pd.read_csv('yunda_biaozhun.txt', sep='\s+', header=None)
    sheng_list = data.iloc[:, 0].values.tolist()
    for x in sheng_list:
        if input_sheng in x:
            hang_index = sheng_list.index(x)

    fei_1 = data.iloc[:, 1].values
    fei_3 = data.iloc[:, 2].values
    fei_x = data.iloc[:, 3].values
    fei_y = data.iloc[:, 4].values

    # 纠正
    if hang_index == 1:
        if flag_hebei:
            hang_index = 2

    if input_weight <= 1:
        if hang_index == 9:
            FY = 18
        else:
            FY = fei_1[hang_index].item()
    elif input_weight <= 3:
        if hang_index == 9:
            FY = 18 + (input_weight - 1) * 15
        else:
            FY = fei_3[hang_index].item()
    else:
        FY = fei_x[hang_index].item() + (input_weight - 1) * fei_y[hang_index].item()

    return FY


def yunda_ky(input_sheng='江苏', input_weight=0.0):
    """
    if FY == 12345678:
        print("不给送！")
    """
    data = pd.read_csv('yunda_kuaiyun.txt', sep='\s+', header=None)
    sheng_list = data.iloc[:, 0].values.tolist()
    sheng_list_index = sheng_list.index(input_sheng)

    f1 = data.iloc[:, 1].values
    f2 = data.iloc[:, 2].values
    f3 = data.iloc[:, 3].values
    fei_low20 = data.iloc[:, 4].values
    fei_30_150 = data.iloc[:, 5].values
    fei_150_300 = data.iloc[:, 6].values
    fei_300 = data.iloc[:, 7].values

    if input_weight <= 10:
        if sheng_list_index >= 24:
            FY = 12345678
        else:
            FY = f1[sheng_list_index].item()
    elif input_weight <= 15:
        if sheng_list_index >= 24:
            FY = 12345678
        else:
            FY = f2[sheng_list_index].item()
    elif input_weight <= 20:
        if sheng_list_index >= 24:
            FY = 12345678
        else:
            FY = f3[sheng_list_index].item()
    elif input_weight <= 30:
        FY = fei_low20[sheng_list_index].item()
    elif input_weight <= 150:
        FY = fei_30_150[sheng_list_index].item() * input_weight
        if FY <= fei_low20[sheng_list_index].item():
            FY = fei_low20[sheng_list_index].item()
    elif input_weight <= 300:
        FY = fei_150_300[sheng_list_index].item() * input_weight
    else:
        FY = fei_300[sheng_list_index].item() * input_weight

    return FY


def wudi_ZT(input_sheng='江苏', input_weight=0.0):
    """
    不送西藏新疆
    FY, sx, js = wudi_ZT('江苏'， 56)
    """
    data = pd.read_csv('wudizhongtong.txt', sep='\s+', header=None)
    sheng_list = data.iloc[:, 0].values.tolist()
    for x in sheng_list:
        if input_sheng in x:
            hang_index = sheng_list.index(x)
    fei_1_15 = data.iloc[:, 1].values
    fei_16_30 = data.iloc[:, 2].values
    fei_31_100 = data.iloc[:, 3].values
    fei_101_500 = data.iloc[:, 4].values
    fei_501 = data.iloc[:, 5].values
    shixiao = data.iloc[:, 6].values.tolist()
    jiashouqu = data.iloc[:, 7].values.tolist()

    if input_weight <= 15:
        FY = fei_1_15[hang_index].item()
    elif input_weight <= 30:
        FY = fei_16_30[hang_index].item()
    elif input_weight <= 100:
        FY = fei_31_100[hang_index].item() * input_weight
    elif input_weight <= 500:
        FY = fei_101_500[hang_index].item() * input_weight
    else:
        FY = fei_501[hang_index].item() * input_weight

    sx = shixiao[hang_index]
    js = jiashouqu[hang_index]

    return FY, sx, js


def jisuan_w(cd, tiao):
    if cd == '28':
        meitiao = 0.2 / 100
    if cd == '30':
        meitiao = 0.3 / 100
    if cd == '40':
        meitiao = 0.35 / 100
    if cd == '50':
        meitiao = 0.45 / 100
    if cd == '60':
        meitiao = 0.5 / 100

    weight = meitiao * tiao

    return weight
