# import datetime
# import hashlib
# import base64
# import logging
# import requests

# # from django.utils.timezone import localtime, now
# # from django.apps import apps
# # from django.conf import settings
# # from django.core.cache import cache
# # from django.forms.models import model_to_dict

# from io import BytesIO

# from random import randint

# from nanoid import generate

# from PIL import Image

# from pypinyin import lazy_pinyin

# from constants import bank_list

# logger = logging.getLogger(__name__)


# def generate_string(length, with_str='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'):
#     '''
#     隨機字串
#     '''
#     return generate(with_str, length)


# # def _gen_mgm():
# #     return generate_string(5, settings.MGM_CHARACTERS)


# # def gen_mgm() -> str:
# #     '''
# #     生成MGM
# #     會確保不會重複

# #     Returns:
# #         str: MGM個人推薦碼
# #     '''
# #     mgm = _gen_mgm()
# #     UserAccountStatus =  apps.get_model('user', 'UserAccountStatus')
# #     if UserAccountStatus.objects.filter(mgm=mgm).exists():
# #         return gen_mgm()
# #     else:
# #         return mgm


# def strB2Q(ustring):
#     '''
#     半形轉全形
#     '''
#     rstring = ""
#     for uchar in ustring:
#         inside_code=ord(uchar)
#         if inside_code == 32:                                 #半形空格直接轉化                  
#             inside_code = 12288
#         elif inside_code >= 32 and inside_code <= 126:        #半形字元（除空格）根據關係轉化
#             inside_code += 65248
#         rstring += chr(inside_code)
#     return rstring


# # def get_zip_code(city, district):
# #     '''
# #     取得郵遞區號(三碼)
# #     '''
# #     zc = zip_code.get(city, {}).get(district)
# #     if not zc:
# #         res = requests.get(f"http://api.opencube.tw/twzipcode?city={city}&district={district}")
# #         if res.status_code == 200:
# #             logger.info("check opencube zip_code: ", res.json())
# #             search_res = res.json().get('data', [])
# #             if len(search_res) > 0:
# #                 zc = search_res[0].get('zip_code')
# #     return zc


# def get_bank_name(code) -> str:
#     for bank in bank_list:
#         if bank['code'] == code:
#             return bank['name']
#     return '查無此銀行'


# def get_random_with_N_digits(n):
#     '''
#     隨機數字
#     '''
#     range_start = 10**(n-1)
#     range_end = (10**n)-1
#     return randint(range_start, range_end)


# def amt_with_thousandths(amt:str)->str:
#     '''
#     數字加上千分位逗號
#     '''
#     try:
#         value = int(amt)
#         result = format(value,',')
#         return result
#     except Exception:
#         return '金額有誤'

 
# def md5_hash(string):
#     '''
#     MD5加密
#     '''
#     hl = hashlib.md5()
#     hl.update(string.encode('utf-8'))
#     return hl.hexdigest()


# def get_encoded_str(data, fill_str: str, pre_len: int, suf_len: int):
#     '''
#     隱藏字串中指定部分
#     fill_str 取代隱藏部分的字元
#     pre_len 前面保留的字元數量
#     suf_len 後面保留的字元數量
#     '''
#     s = "-"
#     if len(data) <= 2:
#         s = data[:pre_len].ljust(2, fill_str)
#     else:
#         s = data[:pre_len] + (fill_str*(len(data)-(pre_len+suf_len))) + data[-suf_len:]
#     return s


# # def time_to_string(_datetime:datetime.datetime=localtime(now()),datetime_string:str=None,output_format:str="%Y/%m/%d",input_format:str="%Y%m%d"):
# #     '''
# #     時間轉指定格式時間字串，或時間字串轉指定格式時間字串
# #     '''
# #     try:
# #         if datetime_string:
# #             _datetime = datetime.datetime.strptime(datetime_string,input_format)
# #         return datetime.datetime.strftime(_datetime,output_format)
# #     except Exception as e:
# #         return '無此日期'


# def get_client_ip(request):
#     '''
#     取得client的IP
#     '''
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip


# def convert_to_pinyin(word: str) -> str:
#     '''
#     將中文字轉為拼音

#     Args:
#         word (str): 中文字串

#     Raises:
#         TypeError: 傳入類型錯誤

#     Returns:
#         str: 拼音文字字串
#     '''
#     if not isinstance(word, str):
#         raise TypeError(f"Value should be string, not {type(word)}.")
#     converted_word = lazy_pinyin(word)
#     return ' '.join(converted_word).title()


# def get_model_verbose_name(model) -> dict:
#     '''
#     取得model的欄位名+中文對照表

#     Args:
#         model (Model): model class

#     Returns:
#         dict: {<欄位名>: <中文欄位名>}
#     '''
#     user_dict = model._meta.fields
#     return {ud.name:ud.verbose_name for ud in user_dict}


# # def get_system_settings():
# #     key = "system_settings"
# #     if not cache.has_key(key):
# #         UserSystemSettings = apps.get_model('system_settings', 'UserSystemSettings')
# #         _sys_settings, _ = UserSystemSettings.objects.get_or_create(active=True)
# #         sys_settings = model_to_dict(_sys_settings)
# #         cache.set(key, sys_settings, timeout=None) 
# #         logger.info("set cache system_settings")   
# #     else:
# #         logger.info("get cached system_settings")  
# #     return cache.get(key)


# def get_bank_name(code) -> str:
#     for bank in bank_list:
#         if bank['code'] == code:
#             return bank['name']
#     return '查無此銀行'


# def convert_to_img(base64_string, name="", ):
#     '''
#     base64 string 轉圖片
#     '''
#     if base64_string:
#         try:
#             im1 = Image.open(BytesIO(base64.b64decode(base64_string)))
#             return im1
#         except Exception as e:
#             logger.info(f"{name} convert_to_img error: {str(e)}")
#             return None
#     else:
#         return None

