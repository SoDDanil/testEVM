
def update_data_with_id(session ,url:str,id:int,data:dict):
    session.put(f'{url}/{id}',json = data,timeout = 10)
    