import requests
from add_data import set_data
from del_data import del_all_data
from const_data import ARR_TYPE_BEAR,URL

data_for_add = {
    1: {
        "bear_type":ARR_TYPE_BEAR[0],
        "bear_name":"mikhail",
        "bear_age":17.5},
    2: {
        "bear_type":ARR_TYPE_BEAR[2],
        "bear_name":"tolik",
        "bear_age":20},
    3: {
        "bear_type":ARR_TYPE_BEAR[3],
        "bear_name":"danil",
        "bear_age":27},
    4: {
        "bear_type":ARR_TYPE_BEAR[1],
        "bear_name":"bobik",
        "bear_age":20},
    }
SESSION = requests.Session()

del_all_data(session=SESSION,url=URL)


for i in data_for_add.keys():
    set_data(data=data_for_add[i],session=SESSION,url = URL )

