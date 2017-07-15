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
'ecmonthHumType':'NoHum',
'ecHasMoveInRate' : 'true',
'ecMoveInRateVal' : '',
'lastAvailableIeeDate' : '',
'dailyStartDate':'20170623',
'dailyEndDate':'20170713',
'dailyUsage':'',
'ecShowMinTab':'true'
}

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
    r = requests.get(**kwargs)
    return r.content

def make_fpl_query(url, proxy, **kwargs):
    current_query = base_query
    current_query.update(kwargs)

    request_dict = {'url': url,
                    'params' : current_query}

    if proxy:
        request_dict['proxies'] = proxy
        request_dict['verify'] = False

    response = make_http_request(**request_dict)

    return response


def fpl_request_daily_usage(premise_no, start_date, end_date, zip_code, acct_no, proxy):
    from response_parser import parse_daily_usage

    response = make_fpl_query(DAILY_CONSUMPTION_URL,
                              proxy,
                              premiseNumber = premise_no,
                              startDate= start_date,
                              endDate = end_date,
                              zipCode = zip_code,
                              accountNumber = acct_no)
    data_range = parse_daily_usage(response)
    return data_range

#Requests to FPL can only be done ina  per day basis, ranges exceeding one day will return nothing
def fpl_request_hourly_usage(premise_no, start_date, end_date, zip_code, acct_no, proxy):
    from response_parser import parse_hourly_usage

    response = make_fpl_query(HOURLY_CONSUMPTION_URL,
                              proxy,
                              premiseNumber = premise_no,
                              startDate= start_date,
                              endDate = end_date,
                              zipCode = zip_code,
                              accountNumner = acct_no)
    data_range = parse_hourly_usage(response)
    return data_range

def get_usage(premise_no, start_date, end_date, zip_code, acct_no='', hourly=True):
    pass


if '__main__' == __name__:
    data_range = fpl_request_daily_usage(premise_no='743019753',
                                         start_date='20170101',
                                         end_date='20170201',
                                         zip_code='32904',
                                         acct_no='5720511046',
                                         proxy=proxyDict)
    for data_point in data_range:
        print data_point

    data_range = fpl_request_hourly_usage(premise_no='183732653',
                                          start_date='2017-06-30T00:00:00',
                                          end_date='2017-06-30T00:00:00',
                                          zip_code='32905',
                                          acct_no='5720511046',
                                          proxy=proxyDict)

    for data_point in data_range:
        print data_point