# -*- coding: iso-8859-15 -*-

import re

SAMPLE_RESPONSE = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><chart sYAxisNameFontBold="0" sYAxisNameFontColor="859AA6" labelFontColor="4B4B4B" xAxisNameFontBold="0" yAxisNameFontBold="0" pYAxisNameFontColor="859AA6" xAxisNameFontColor="859AA6" animation="1"  animationDuration="1" tooltipcolor="FFFFFF" yAxisValueDecimals="2" xAxisName="" toolTipBorderColor="FFFFFF" toolTipBgColor="0B74BE" showYAxisValues="1" showValues="0" showPlotBorder="0" showLegend="0" setAdaptiveSYMin="1" sYAxisValueDecimals="0" sNumberSuffix="°F" plotGradientColor="" plotFillAlpha="100" plotBorderThickness="0" numberPrefix="$" numDivLines="5" labelDisplay="NONE" forceDecimals="true" exportEnabled="0" exportAtClient="0" chartRightMargin="2" chartLeftMargin="2" chartBottomMargin="2" canvasBorderColor="DFF3FE" canvasBgColor="DFF3FE" borderThickness="0" borderColor="DFF3FE" bgColor="DFF3FE" anchorRadius="4.5" anchorBorderThickness="2" anchorBorderColor="FFFFFF" anchorBgColor="F4D13F" adjustDiv="0" SYAxisName="Temperature (°F)" SYAxisMinValue="82.0" SYAxisMaxValue="94.0" PYAxisName="Cost ($)" PYAxisMaxValue="5.22"><categories><category label="23{br}F{br}Jun{br}"/><category label="24{br}S{br}{br}"/><category label="25{br}Su{br}{br}"/><category label="26{br}M{br}{br}"/><category label="27{br}Tu{br}{br}"/><category label="28{br}W{br}{br}"/><category label="29{br}Th{br}{br}"/><category label="30{br}F{br}{br}"/><category label="01{br}S{br}{br}"/><category label="02{br}Su{br}{br}"/><category label="03{br}M{br}{br}"/><category label="04{br}Tu{br}{br}"/><category label="05{br}W{br}Jul{br}"/></categories><dataset seriesName="$" parentYAxis="P"><set value="1.83" toolText="Day/Date: Jun. 23, 2017 {br}kWh Usage: 14 kWh {br}Approx. Cost: $1.83 {br}Daily High Temp: 88 °F " link="j-hourlyJs-183732653,2017/06/23T00:00:00,2017/06/23T00:00:00,0574925590,residential,32905,20170623,20170705" color="009900"/><set value="4.0" toolText="Day/Date: Jun. 24, 2017 {br}kWh Usage: 34 kWh {br}Approx. Cost: $4.00 {br}Daily High Temp: 92 °F " link="j-hourlyJs-183732653,2017/06/24T00:00:00,2017/06/24T00:00:00,0574925590,residential,32905,20170623,20170705" color="E99356"/><set value="4.43" toolText="Day/Date: Jun. 25, 2017 {br}kWh Usage: 38 kWh {br}Approx. Cost: $4.43 {br}Daily High Temp: 90 °F " link="j-hourlyJs-183732653,2017/06/25T00:00:00,2017/06/25T00:00:00,0574925590,residential,32905,20170623,20170705" color="E99356"/><set value="4.11" toolText="Day/Date: Jun. 26, 2017 {br}kWh Usage: 35 kWh {br}Approx. Cost: $4.11 {br}Daily High Temp: 90 °F " link="j-hourlyJs-183732653,2017/06/26T00:00:00,2017/06/26T00:00:00,0574925590,residential,32905,20170623,20170705" color="009900"/><set value="3.24" toolText="Day/Date: Jun. 27, 2017 {br}kWh Usage: 27 kWh {br}Approx. Cost: $3.24 {br}Daily High Temp: 89 °F " link="j-hourlyJs-183732653,2017/06/27T00:00:00,2017/06/27T00:00:00,0574925590,residential,32905,20170623,20170705" color="009900"/><set value="3.78" toolText="Day/Date: Jun. 28, 2017 {br}kWh Usage: 32 kWh {br}Approx. Cost: $3.78 {br}Daily High Temp: 87 °F " link="j-hourlyJs-183732653,2017/06/28T00:00:00,2017/06/28T00:00:00,0574925590,residential,32905,20170623,20170705" color="009900"/><set value="3.89" toolText="Day/Date: Jun. 29, 2017 {br}kWh Usage: 33 kWh {br}Approx. Cost: $3.89 {br}Daily High Temp: 87 °F " link="j-hourlyJs-183732653,2017/06/29T00:00:00,2017/06/29T00:00:00,0574925590,residential,32905,20170623,20170705" color="009900"/><set value="4.0" toolText="Day/Date: Jun. 30, 2017 {br}kWh Usage: 34 kWh {br}Approx. Cost: $4.00 {br}Daily High Temp: 87 °F " link="j-hourlyJs-183732653,2017/06/30T00:00:00,2017/06/30T00:00:00,0574925590,residential,32905,20170623,20170705" color="009900"/><set value="4.22" toolText="Day/Date: Jul. 01, 2017 {br}kWh Usage: 36 kWh {br}Approx. Cost: $4.22 {br}Daily High Temp: 85 °F " link="j-hourlyJs-183732653,2017/07/01T00:00:00,2017/07/01T00:00:00,0574925590,residential,32905,20170623,20170705" color="E99356"/><set value="5.19" toolText="Day/Date: Jul. 02, 2017 {br}kWh Usage: 45 kWh {br}Approx. Cost: $5.19 {br}Daily High Temp: 91 °F " link="j-hourlyJs-183732653,2017/07/02T00:00:00,2017/07/02T00:00:00,0574925590,residential,32905,20170623,20170705" color="E99356"/><set value="3.67" toolText="Day/Date: Jul. 03, 2017 {br}kWh Usage: 31 kWh {br}Approx. Cost: $3.67 {br}Daily High Temp: 91 °F " link="j-hourlyJs-183732653,2017/07/03T00:00:00,2017/07/03T00:00:00,0574925590,residential,32905,20170623,20170705" color="009900"/><set value="4.54" toolText="Day/Date: Jul. 04, 2017 {br}kWh Usage: 39 kWh {br}Approx. Cost: $4.54 {br}Daily High Temp: 91 °F " link="j-hourlyJs-183732653,2017/07/04T00:00:00,2017/07/04T00:00:00,0574925590,residential,32905,20170623,20170705" color="E99356"/><set value="3.78" toolText="Day/Date: Jul. 05, 2017 {br}kWh Usage: 32 kWh {br}Approx. Cost: $3.78 {br}Daily High Temp: 84 °F " link="j-hourlyJs-183732653,2017/07/05T00:00:00,2017/07/05T00:00:00,0574925590,residential,32905,20170623,20170705" color="009900"/></dataset><dataset seriesName="Temperature (°F)" parentYAxis="S"><set value="88" toolText="88 °F" color="FD4D4E"/><set value="92" toolText="92 °F" color="FD4D4E"/><set value="90" toolText="90 °F" color="FD4D4E"/><set value="90" toolText="90 °F" color="FD4D4E"/><set value="89" toolText="89 °F" color="FD4D4E"/><set value="87" toolText="87 °F" color="FD4D4E"/><set value="87" toolText="87 °F" color="FD4D4E"/><set value="87" toolText="87 °F" color="FD4D4E"/><set value="85" toolText="85 °F" color="FD4D4E"/><set value="91" toolText="91 °F" color="FD4D4E"/><set value="91" toolText="91 °F" color="FD4D4E"/><set value="91" toolText="91 °F" color="FD4D4E"/><set value="84" toolText="84 °F" color="FD4D4E"/></dataset><styles><definition><style type="animation" start="0" param="_xScale" name="CanvasAnim" duration="1"/><style type="font" name="axisNameStyle" color="859AA6" bold="false"/><style type="font" size="10" name="myToolTipFont" font="Verdana" color="FFFFFF"/></definition><application><apply toObject="Canvas" styles="CanvasAnim"/><apply toObject="ToolTip" styles="myToolTipFont"/><apply toObject="XAXISNAME" styles="axisNameStyle"/><apply toObject="YAXISNAME" styles="axisNameStyle"/></application></styles></chart><ARG>@@2017/07/05T00:00:00@@2017/07/05T00:00:00@@183732653@@0574925590@@32905@@null@@<b>Usage for: </b>Jun. 23, 2017 12:00 AM - Jul. 05, 2017 12:00AM.  &&&&&Average daily usage: </b>$3.90 (33 kWh)@@false@@false@@null@@null@@null@@null@@JUL,2017@@0@@20170623@@20170705@@Empty @@Empty @@true</ARG>FLAGfalse!!!!false!!!!false!!!!!!!!20170623!!!!20170705!!!!null!!!!true"""
DAY_DATE_RE = re.compile("Day/Date: (.*)")
KWH_USAGE_RE = re.compile("kWh Usage: (.*) kWh")
APPROX_COST_RE = re.compile("Approx\. Cost: \$(.*) ")
TEMP_HIGH_RE = re.compile("Daily High Temp: (.*) ")

DAY_DATE ="Day/Date: "
KWH_USAGE = "kWh Usage: "
APPROX_COST = "Approx. Cost: $"
TEMP_HIGH = "Daily High Temp: "

def _parse_date2(raw_date_string):
    searchObj = DAY_DATE_RE.search(raw_date_string)

    if searchObj is not None:
        date_string = searchObj.group(0)
        from datetime import datetime
        datetime_obj = datetime.strptime(date_string, '%b. %d, %Y')
        return datetime_obj

def _parse_number(raw_input_string, field_name_str):
    value = -1
    _, _, parsed_string = raw_input_string.partition(field_name_str)
    if parsed_string:
        parsed_string = parsed_string.replace(',','')
        number_string = parsed_string.split()[0]
        if '.' in number_string:
            value = float(number_string)
        else:
            value = int(number_string)
    return value

def _parse_date(raw_date_string):
    _, _, date_string = raw_date_string.partition(DAY_DATE)
    date_string = date_string.strip()
    date_string = date_string.replace(',', '')
    date_string = date_string.replace('.', '')


    if date_string:
        from datetime import datetime
        datetime_obj = datetime.strptime(date_string, '%b %d %Y')
        return datetime_obj

def _parse_kwh_usage(raw_kwh_string):
    return _parse_number(raw_kwh_string, KWH_USAGE)

def _parse_approx_cost(raw_ac_string):
    return _parse_number(raw_ac_string, APPROX_COST)

def _parse_temp(raw_temp_string):
    return _parse_number(raw_temp_string, TEMP_HIGH)

def parse_response(data):
    from lxml import html

    etree_response = html.fromstring(data)
    data = etree_response.findall('chart/dataset')

    relevant_data = []
    for data_set in data:
        if data_set.attrib['seriesname'] == '$':
            for data_point in data_set:
                date =_parse_date(data_point.attrib['tooltext'].split('{br}')[0])
                usage = _parse_kwh_usage(data_point.attrib['tooltext'].split('{br}')[1])
                cost = _parse_approx_cost(data_point.attrib['tooltext'].split('{br}')[2])
                h_temp = _parse_temp(data_point.attrib['tooltext'].split('{br}')[3])
                relevant_data.append((date, usage, cost, h_temp))
            break
    return relevant_data

if __name__ == "__main__":
    data_range = parse_response(SAMPLE_RESPONSE)
    for data_point in data_range:
        print data_point
