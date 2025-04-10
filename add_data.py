
def set_data(data:dict, session ,url:str):
    session.post(url,json = data,timeout = 10)
    