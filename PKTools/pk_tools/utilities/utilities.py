from ..constants.districts import full_data, zip_code
from ..constants.banks import bank_list


def get_zip_code(city: str, district: str) -> str:
    '''
    取得郵遞區號(三碼)

    Args:
        city (str): 縣市
        district (str): 區域、鄉鎮

    Returns:
        str: 郵遞區號(三碼)
    '''
    zc = zip_code.get(city, {}).get(district, '')
    if zc:
        return zc
    else:
        _result = list(filter(lambda x: x['city'] == city and x['district'] == district, full_data))
        result = _result[0] if len(_result) > 0 else {}
        return result.get('zip_code', '')


def get_full_district_info(zip_code: str) -> dict:
    '''
    以郵遞區號取得詳細鄉鎮區域資訊

    Args:
        zip_code (str): 郵遞區號

    Returns:
        dict: 詳細區域資訊
    '''
    _result = list(filter(lambda x: x['zip_code'] == zip_code, full_data))
    result = _result[0] if len(_result) > 0 else {}
    return result


def get_district_info(zip_code: str):
    '''
    以郵遞區號取得縣市、鄉鎮區域

    Args:
        zip_code (str): 郵遞區號

    Returns:
        (str, str): 縣市, 鄉鎮區域
    '''
    r = get_full_district_info(zip_code)
    return r.get('city', ''), r.get('district', '')


def get_bank_info(code: str) -> dict:
    '''
    取得銀行資訊

    Args:
        code (str): 銀行代號

    Returns:
        dict: 銀行資訊
    '''
    for bank in bank_list:
        if bank.get('code', '') == code:
            return bank
    return {}


def get_bank_name(code: str) -> str:
    '''
    取得銀行名稱

    Args:
        code (str): 銀行代號

    Returns:
        str: 銀行名
    '''
    return get_bank_info(code).get('name')