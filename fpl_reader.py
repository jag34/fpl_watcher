# Needed for the query to work:
# zipCode
# accountNumber: Not being there, affects the estimated cost. Different account #s return different approx cost values.
# startDate, endDate; for the query
# lastAvailableDate: Needs to be there, but doesn't actually need a valid value.
# certifiedDate: Doesn't need to be accurate, just needs to be there

# Everything else should be kept the same over other requests.
# A lot of these values might be necessary for providing echo's back for the front
# end library to properly fill out fields in the page.

# TODO: There is a bug where the first day on the query is really large.

base_query = { 'premiseNumber' : '',
'startDate' : '',
'endDate' : '',
'accountNumber' : '',
'accountType' : 'null',
'zipCode' : '',
'consumption' : '0.0',
'usage' : '0.0',
'isMultiMeter' : 'false',
'lastAvailableDate' : '1970/01/01',
'isAmiMeter' : 'true',
'userType' : 'EXT',
'currentReading' : '',
'isResidential' : 'true',
'isTouUser' : 'false',
'showGroupData' : 'false',
'isNetMeter' : 'false',
'certifiedDate' : '1970/01/01',
'userId' : '',
'acctNetMeter' : 'false',
'tempType' : 'max',
'viewType' : 'dollar',
'ecDayHumType' : 'NoHum',
'ecHasMoveInRate' : 'true',
'ecMoveInRateVal' : '',
'lastAvailableIeeDate' : '20170705'}

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
'userId' : '',
'acctNetMeter' : 'false',
'tempType' : 'max',
'viewType' : 'dollar',
'ecDayHumType' : 'NoHum',
'ecHasMoveInRate' : 'true',
'ecMoveInRateVal' : '',
'lastAvailableIeeDate' : '20170705'}

query_params_2 = { 'premiseNumber':'743019753',
'startDate':'20170101',
'endDate':'20170201',
'isAmiMeter':'true',
'accountNumber':'5720511046',
'accountType':'residential',
'zipCode':'32904',
'consumption':'0.0',
'usage':'0.0',
'isMultiMeter':'false',
'lastAvailableDate':'2017/06/23',
'userType':'EXT',
'currentReading':'',
'certifiedDate':'2014/05/31',
'userId':'',
'isResidential':'true',
'acctNetMeter':'false',
'tempType':'max',
'viewType':'dollar',
'ecDayHumType':'NoHum',
'ecHasMoveInRate':'false',
'ecMoveInRateVal':'',
'lastAvailableIeeDate':'20170623' }

DAILY_CONSUMPTION_URL = 'https://app.fpl.com/wps/PA_ESFPortalWeb/getDailyConsumption.do'
HOURLY_CONSUMPTION_URL = 'https://app.fpl.com/wps/PA_ESFPortalWeb/getHourlyConsumption.do'
START_END_DATE_FORMAT = '%Y%m%d'

# only for use when there's a corporate proxy
proxyDict = {
              "http"  : "http://127.0.0.1:3128",
              "https" : "https://127.0.0.1:3128",
            }


def validate_date(date, expected):
    from datetime import datetime
    return datetime.strptime(date, expected)


def make_http_request(**kwargs):
    import requests
    print kwargs['params']
    r = requests.get(**kwargs)
    return r.content


def request_daily_usage(premise_no, start_date, end_date, zip_code, acct_no='', proxy=None):
    from response_parser import parse_daily_usage
    #from datetime import datetime
    #start_date_datetime = datetime.strptime(start_date, START_END_DATE_FORMAT)
    #end_date_datetime = datetime.strptime(end_date, START_END_DATE_FORMAT)
    current_query = base_query

    current_query['premiseNumber'] = premise_no
    current_query['startDate'] = start_date
    current_query['endDate'] = end_date
    current_query['zipCode'] = zip_code
    current_query['accountNumber'] = acct_no

    request_dict = {'url': DAILY_CONSUMPTION_URL,
                    'params' : current_query}

    if proxy:
        request_dict['proxies'] = proxy
        request_dict['verify'] = False

    response = make_http_request(**request_dict)
    data_range = parse_daily_usage(response)

    return data_range


if '__main__' == __name__:
    data_range = request_daily_usage(premise_no='743019753',
                                     start_date='20170101',
                                     end_date='20170201',
                                     zip_code='32904',
                                     acct_no='5720511046',
                                     proxy=proxyDict)

    for data_point in data_range:
        print data_point