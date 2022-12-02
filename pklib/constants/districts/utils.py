from constants.districts.zip_code import zip_code

def getpath(nested_dict, value, prepath=()):
    '''
    以郵遞區號取得縣市、鄉鎮區域
    '''
    for k, v in nested_dict.items():
        path = prepath + (k,)
        if v == value: # found value
            return path
        elif hasattr(v, 'items'): # v is a dict
            p = getpath(v, value, path) # recursive call
            if p is not None:
                return p

def get_path_by_zipcode(value):
    return getpath(zip_code, value)
