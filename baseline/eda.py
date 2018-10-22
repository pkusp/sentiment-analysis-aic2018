# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: eda.py
@time: 2018/10/22 下午4:01

这一行开始写关于本文件的说明与解释
"""
import time
from baseline import config
from baseline.data_process import load_data_from_csv

t_start = time.time()


def eda():
    print("\n")
    print(config.project_path)
    print("\n")
    print(config.train_data_path)
    print("\n")

    train_df = load_data_from_csv(config.train_data_path)
    valid_df = load_data_from_csv(config.validate_data_path)
    test_df = load_data_from_csv(config.test_data_path)
    print("\ncolumns:\n", len(train_df.columns))
    print("\ntrain data:\n", train_df.iloc[2])
    print("\nvalidation data:\n", valid_df.iloc[1])
    print("\ntest data:\n", test_df.iloc[1])
    train_nums = len(train_df)
    valid_nums = len(valid_df)
    test_nums = len(test_df)
    print("\ntrain amount:\n", train_nums)
    print("valid amount:\n", valid_nums)
    print("test amount:\n", test_nums)
    print("train ratio:\n", train_nums / (train_nums + valid_nums))


eda()
t_end=time.time()
print("\nrun {}s".format(round(t_end-t_start,4)))


'''

columns:
 22

train data:
 id                                                                                          2
content                                     "4人同行 点了10个小吃\n榴莲酥 榴莲味道不足 松软 奶味浓\n虾饺 好吃 两颗大虾仁\...
location_traffic_convenience                                                               -2
location_distance_from_business_district                                                   -2
location_easy_to_find                                                                      -2
service_wait_time                                                                          -2
service_waiters_attitude                                                                    0
service_parking_convenience                                                                -2
service_serving_speed                                                                       1
price_level                                                                                 0
price_cost_effective                                                                       -2
price_discount                                                                              1
environment_decoration                                                                     -2
environment_noise                                                                          -2
environment_space                                                                           1
environment_cleaness                                                                       -2
dish_portion                                                                                0
dish_taste                                                                                  1
dish_look                                                                                  -2
dish_recommendation                                                                        -2
others_overall_experience                                                                   0
others_willing_to_consume_again                                                            -2
Name: 2, dtype: object

validation data:
 id                                                                                          1
content                                     "趁着国庆节，一家人在白天在山里玩耍之后，晚上决定吃李记搅团。\n东门外这家店门口停车太难了...
location_traffic_convenience                                                               -2
location_distance_from_business_district                                                   -2
location_easy_to_find                                                                      -1
service_wait_time                                                                          -2
service_waiters_attitude                                                                   -2
service_parking_convenience                                                                -1
service_serving_speed                                                                      -2
price_level                                                                                 1
price_cost_effective                                                                       -2
price_discount                                                                              0
environment_decoration                                                                     -2
environment_noise                                                                          -2
environment_space                                                                          -2
environment_cleaness                                                                       -2
dish_portion                                                                                1
dish_taste                                                                                  1
dish_look                                                                                   1
dish_recommendation                                                                         1
others_overall_experience                                                                   1
others_willing_to_consume_again                                                             1
Name: 1, dtype: object

test data:
 id                                                                                          1
content                                     "终于开到心心念念的LAB loft。第一次来就随便点也一些～【香辣虾意面】蛮辣的，但其实一...
location_traffic_convenience                                                              NaN
location_distance_from_business_district                                                  NaN
location_easy_to_find                                                                     NaN
service_wait_time                                                                         NaN
service_waiters_attitude                                                                  NaN
service_parking_convenience                                                               NaN
service_serving_speed                                                                     NaN
price_level                                                                               NaN
price_cost_effective                                                                      NaN
price_discount                                                                            NaN
environment_decoration                                                                    NaN
environment_noise                                                                         NaN
environment_space                                                                         NaN
environment_cleaness                                                                      NaN
dish_portion                                                                              NaN
dish_taste                                                                                NaN
dish_look                                                                                 NaN
dish_recommendation                                                                       NaN
others_overall_experience                                                                 NaN
others_willing_to_consume_again                                                           NaN
Name: 1, dtype: object

train amount:
 105000
valid amount:
 15000
test amount:
 15000
train ratio:
 0.875
'''
