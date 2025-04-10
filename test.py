import requests
from add_data import set_data
from get_data import get_data_with_id, get_all_bear_id_data, get_all_bear_type_data
from del_data import del_bear_with_id
from update_data import update_data_with_id
from const_data import ARR_TYPE_BEAR,URL
from main import preparing_data

preparing_data()

class TestClass:
    SESSION = requests.Session()
    def test_one_check_id(self):
        arrId = get_all_bear_id_data(session=self.SESSION,url=URL)
        assert len(arrId)==4

    def test_two_chek_type(self):
        arrType = get_all_bear_type_data(session=self.SESSION,url=URL)
        assert sorted(set(arrType))==sorted(ARR_TYPE_BEAR)

    def test_three_add_new_bear(self):
        dataBearForAdd = {
            "bear_type":ARR_TYPE_BEAR[0],
            "bear_name":"NEW_BEAR_TEST",
            "bear_age":100
        }
        set_data(data=dataBearForAdd,session=self.SESSION,url=URL)
        lastId =  get_all_bear_id_data(session=self.SESSION,url=URL)[-1]
        dataLastBear = get_data_with_id(session=self.SESSION,url=URL,id=lastId)
        assert dataLastBear['bear_type']==dataBearForAdd['bear_type'] and dataLastBear['bear_name']==dataBearForAdd['bear_name'] and dataLastBear['bear_age']==dataBearForAdd['bear_age']

    def test_four_uodate_name_bear(self):
        lastId =  get_all_bear_id_data(session=self.SESSION,url=URL)[-1]
        dataLastBear = get_data_with_id(session=self.SESSION,url=URL,id=lastId)
        dataForUpdate = {
            "bear_type":dataLastBear['bear_type'],
            "bear_name":"UPDATE_DANIL",
            "bear_age":dataLastBear['bear_age']
        }        
        update_data_with_id(session=self.SESSION,url=URL,id= lastId,data=dataForUpdate)
        dataLastBear = get_data_with_id(session=self.SESSION,url=URL,id=lastId)
        assert dataLastBear['bear_name']==dataForUpdate['bear_name']
        

    def test_five_delete_bear_with_id(self):
        arr_id = get_all_bear_id_data(session=self.SESSION,url=URL)
        idForDelete = get_all_bear_id_data(session=self.SESSION,url=URL)[-2]
        del_bear_with_id(session=self.SESSION,url=URL,id= idForDelete)
        assert len(arr_id)==len(get_all_bear_id_data(session=self.SESSION,url=URL))+1


