import requests
from response_parser import parse_response

query_params = { 'premiseNumber' : '183732653',
'startDate' : '20170623',
'endDate' : '20170705',
'accountNumber' : '0574925590',
'accountType' : 'null',
'zipCode' : '32905',
'consumption' : '0.0',
'usage' : '0.0',
'isMultiMeter' : 'false',
'lastAvailableDate' : '2017/07/05',
'isAmiMeter' : 'true',
'userType' : 'EXT',
'currentReading' : '57379',
'isResidential' : 'true',
'isTouUser' : 'false',
'showGroupData' : 'false',
'isNetMeter' : 'false',
'certifiedDate' : '2017/06/23',
'userId' : 'jaguilar@aguilarstiller.com',
'acctNetMeter' : 'false',
'tempType' : 'max',
'viewType' : 'dollar',
'ecDayHumType' : 'NoHum',
'ecHasMoveInRate' : 'true',
'ecMoveInRateVal' : '',
'lastAvailableIeeDate' : '20170705'}

query_params_2 = { 'premiseNumber':'743019753',
'startDate':'20170417',
'endDate':'20170518',
'isAmiMeter':'true',
'accountNumber':'5720511046',
'accountType':'residential',
'zipCode':'32904',
'consumption':'0.0',
'usage':'0.0',
'isMultiMeter':'false',
'lastAvailableDate':'2017/07/05',
'userType':'EXT',
'currentReading':'43031',
'certifiedDate':'2014/05/31',
'userId':'jaguilar@aguilarstiller.com',
'isResidential':'true',
'acctNetMeter':'false',
'tempType':'max',
'viewType':'dollar',
'ecDayHumType':'NoHum',
'ecHasMoveInRate':'false',
'ecMoveInRateVal':'',
'lastAvailableIeeDate':'20170706' }

http_proxy  = "http://127.0.0.1:3128"
https_proxy = "https://127.0.0.1:3128"

proxyDict = {
              "http"  : http_proxy,
              "https" : https_proxy,
            }

import requests

def make_fpl_request():
    r = requests.get(url='https://app.fpl.com/wps/PA_ESFPortalWeb/getDailyConsumption.do',
                     proxies = proxyDict,
                     params=query_params_2,
                     verify=False)
    return r.content

if '__main__' == __name__:
    print make_fpl_request()
    data_range = parse_response(make_fpl_request())
    for data_point in data_range:
        print data_point