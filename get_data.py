
def get_all_data( session ,url:str) -> str:
    result = session.get(url,timeout = 10)
    return result.text

def get_data_with_id(session ,url:str,id:int):
    result = session.get(f'{url}/{id}',timeout = 10)
    return result.json()

def get_all_bear_id_data( session ,url:str) -> str:
    result = session.get(url,timeout = 10)
    arrId = sorted([x['bear_id'] for x in result.json()])
    return arrId


def get_all_bear_type_data( session ,url:str) -> str:
    result = session.get(url,timeout = 10)
    arrId = [x['bear_type'] for x in result.json()]
    return arrId