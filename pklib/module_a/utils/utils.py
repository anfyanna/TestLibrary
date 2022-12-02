from pklib.constants.banks import bank_list

def get_bank_info(bk: str) -> dict:
    '''
    取得銀行資訊

    Args:
        bk (str): 銀行代號

    Returns:
        dict: 銀行資訊
        example:
            {'code': '005', 'name': '臺灣土地銀行', 'remark': ['eACH', 'eDDA'], 'description': '網銀驗證'}
    '''
    return next((item for item in bank_list if item["code"] == bk), {})


def get_bank_name(bk: str) -> str:
    '''
    取得銀行名稱

    Args:
        bk (str): 銀行代號

    Returns:
        str: 銀行名稱
    '''
    return get_bank_info(bk).get('name', '')