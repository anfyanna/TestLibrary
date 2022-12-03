import random
import hashlib

from pypinyin import lazy_pinyin


def generate_string(length: str = 6, chars: str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'):
    '''
    隨機字串
    '''
    return ''.join(random.choice(chars) for _ in range(length))


def strB2Q(ustring):
    '''
    半形轉全形
    '''
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 32:                                 #半形空格直接轉化                  
            inside_code = 12288
        elif inside_code >= 32 and inside_code <= 126:        #半形字元（除空格）根據關係轉化
            inside_code += 65248
        rstring += chr(inside_code)
    return rstring


def amt_with_thousandths(amt: str) -> str:
    '''
    數字加上千分位逗號

    Args:
        amt (str): 數字字串

    Returns:
        str: 數字字串
    '''
    try:
        value = int(amt)
        result = format(value, ',')
        return result
    except Exception:
        return amt


def md5_hash(string):
    '''
    MD5加密
    '''
    hl = hashlib.md5()
    hl.update(string.encode('utf-8'))
    return hl.hexdigest()


def get_encoded_str(data: str, fill_str: str = '*', pre_len: int = 1, suf_len: int = 1) -> str:
    '''
    隱藏字串中指定部分

    Args:
        data (str): 原字串
        fill_str (str): 取代隱藏部分的字元
        pre_len (int): 前面保留的字元數量
        suf_len (int): 後面保留的字元數量

    Returns:
        str: 結果字串
    '''
    s = ""
    if len(data) <= 2:
        s = data[:pre_len].ljust(2, fill_str)
    else:
        s = data[:pre_len] + (fill_str*(len(data)-(pre_len+suf_len))) + data[-suf_len:]
    return s


def convert_to_pinyin(word: str) -> str:
    '''
    將中文字轉為拼音

    Args:
        word (str): 中文字串

    Raises:
        TypeError: 傳入類型錯誤

    Returns:
        str: 拼音文字字串
    '''
    if not isinstance(word, str):
        raise TypeError(f"Value should be string, not {type(word)}.")
    converted_word = lazy_pinyin(word)
    return ' '.join(converted_word).title()


if __name__ == '__main__':
    pass
