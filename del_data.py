def del_all_data( session ,url:str):
    session.delete(url,timeout = 10)
    
def del_bear_with_id(session ,url:str,id:int):
    session.delete(f'{url}/{id}',timeout = 10)