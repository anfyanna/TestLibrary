import random


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


if __name__ == '__main__':
    pass
