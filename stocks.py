import requests
import json
import time

# 查询接口
def getGegu(gu_code):
    header = {'Referer':'https://finance.sina.com.cn/'}
    gegu = requests.get('http://hq.sinajs.cn/list=' + gu_code, headers=header)
    gegu_status = gegu.status_code
    if gegu_status != 200:
        return False
    allinfo = gegu.text.split('"')[1].split(',')
    gegu_name = allinfo[0]
    # 今开
    gegu_jinkai = allinfo[1]
    # 昨收
    gegu_zuoshou = allinfo[2]
    # 现价
    gegu_xianjia = allinfo[3]
    # 成交数
    gegu_chengjiaoshu = allinfo[8]
    # 成交额
    gegu_chengjiaoe = allinfo[9]
    # 日期
    gegu_date = allinfo[30]
    # 时间
    gegu_time = allinfo[31]
    res_info = {'gegu_name': gegu_name, 'gegu_jinkai': gegu_jinkai, 'gegu_zuoshou': gegu_zuoshou, 'gegu_xianjia': gegu_xianjia,\
            'gegu_chengjiaoshu':gegu_chengjiaoshu, 'gegu_chengjiaoe':gegu_chengjiaoe, 'gegu_date':gegu_date,'gegu_time':gegu_time}
    return res_info


sh = getGegu('sh000001')
sz = getGegu('sz399001')

sh_offset = (float(sh['gegu_xianjia']) - float(sh['gegu_zuoshou'])) / float(sh['gegu_zuoshou'])
sz_offset = (float(sz['gegu_xianjia']) - float(sz['gegu_zuoshou'])) / float(sz['gegu_zuoshou'])

def format_money(x):
    return str.format('%.2f' % (float(x) / 100000000.)) + u'亿'

def format_percent(x):
    if (x >= 0):
        return '\033[31m' + str.format('%.2f' % (x * 100)) + '%\033[0m'
    else:
        return '\033[36m' + str.format('%.2f' % (x * 100)) + '%\033[0m'

print('')
print('-' * 30)
print(time.ctime())
print('\033[44m' + '[SH]' + '\033[0m')
print('| NOW:' + sh['gegu_xianjia'] + '\tVOT:' + format_money(sh['gegu_chengjiaoe']) + '\tRANGE:' + format_percent(sh_offset) + ' |')
print('\033[44m' + '[SZ]' + '\033[0m')
print('| NOW:' + sz['gegu_xianjia'] + '\tVOT:' + format_money(sz['gegu_chengjiaoe']) + '\tRANGE:' + format_percent(sz_offset) + ' |')
print('\033[44m' + u'综合' + '\033[0m')
print('| VOT:' + format_money(float(sh['gegu_chengjiaoe']) + float(sz['gegu_chengjiaoe'])) + '\tRANGE:' + format_percent((sh_offset + sz_offset) / 2.0) + ' |')
print('-' * 30)
print('')
