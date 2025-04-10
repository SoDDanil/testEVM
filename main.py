import requests
from add_data import set_data
from del_data import del_all_data
from const_data import ARR_TYPE_BEAR,URL

def preparing_data():
    #тестовые данные для проверки работоспособности
    dataForAdd = {
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
    #очистим данные для добавления только 4 медведей
    del_all_data(session=SESSION,url=URL)

    #добавим всех 4 медведей
    for i in dataForAdd.keys():
        set_data(data=dataForAdd[i],session=SESSION,url = URL )

