from django.core.management import setup_environ
import analysis.settings as settings
setup_environ(settings)
from bs4 import BeautifulSoup
from core.models import DailyTradeData, ListedCompany
import eventlet
import datetime
import sys
from dateutil import parser
import os
from eventlet.green import urllib2


request = eventlet.import_patched('requests')
key_columns = ["traded_date", "open_value", "high_value", "low_value",
               "ltp_value", "close_value", "volume", "turn_over"]
short_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def load_company_database():
    f = open(settings.RESOURCES_COMPANY_LIST, 'r')
    companies_text = f.read()
    for company in companies_text.split('\n'):
        if company:
            company_pair = company.split('\t')
            company_obj , listed = ListedCompany.objects.get_or_create(
                name = company_pair[0],
                symbol = company_pair[1]
            )
            print company_pair


def parse_data(html_data):
    soup = BeautifulSoup(html_data)
    data = []
    for el in soup.findAll('tr'):
        data_row = {}
        i = 0
        for each_data in el.findAll('td'):
            data_row[key_columns[i]] = each_data.get_text().strip().replace(',', '')
            i = i + 1
        data.append(data_row)
    return data


def fetch_url(url):
    #response = request.get(url)
    #return parse_data(response.content)
    crawled_data = urllib2.urlopen(url).read()
    return parse_data(crawled_data)
    
def crawl_data(company, from_date, to_date, date_period):
    mapped_data_list = fetch_url(
        settings.CRAWL_DATA_URL % {"symbol": company.symbol,
                                   "from_date": from_date,
                                   "to_date": to_date,
                                   "date_period": date_period})
    for mapped_data in mapped_data_list:
        if mapped_data:
            traded_data, created = DailyTradeData.objects.get_or_create(
                listed_company = company,
                traded_date = parser.parse(mapped_data["traded_date"]))
            if created:
                traded_data.listed_company = company
                traded_data.company_symbol = company.symbol
                traded_data.traded_date = parser.parse(mapped_data["traded_date"])
                traded_data.open_value = mapped_data["open_value"]
                traded_data.high_value = mapped_data["high_value"]
                traded_data.low_value = mapped_data["low_value"]
                traded_data.ltp_value = mapped_data["ltp_value"]
                traded_data.close_value = mapped_data["close_value"]
                traded_data.volume = mapped_data["volume"]
                traded_data.turn_over = mapped_data["turn_over"]
                traded_data.save()
            """
            traded_data, created = DailyTradeData.objects.get_or_create(
                listed_company = company,
                company_symbol = company.symbol,
                traded_date = parser.parse(mapped_data["traded_date"]),
                open_value = mapped_data["open_value"],
                high_value = mapped_data["high_value"],
                low_value = mapped_data["low_value"],
                ltp_value = mapped_data["ltp_value"],
                close_value = mapped_data["close_value"],
                volume = mapped_data["volume"],
                turn_over = mapped_data["turn_over"],
            )
            if created:
                traded_data.save()
            """
def get_company_data(company):
    print "crawling: " + company.name
    today = datetime.date.today()
    crawl_data(
        company, "01-Jan-2001",
        str(today.day)+"-"+short_months[today.month]+"-"+str(today.year),
        "")
    

def get_historical_data(symbol):
    if symbol:
        companies = ListedCompany.objects.filter(symbol=symbol)
    else:
        companies = ListedCompany.objects.all()[:10]
    print "loading" + str(companies)
    pool = eventlet.GreenPool(5)
    pile = eventlet.GreenPile(pool)
    for company in companies:
        print company
        pile.spawn(get_company_data, company)
    

def main():
    if len(sys.argv) < 2:
        sys.exit("Must provide an option")
    else:
        if sys.argv[1] == 'history':
            if len(sys.argv) > 2:
                get_historical_data(sys.argv[2])
            else:
                get_historical_data(None)
        elif sys.argv[1] == 'load_companies':
            load_company_database()
            

if __name__ == "__main__":
    main()
    #crawl('http://nseindia.com/live_market/dynaContent/live_watch/get_quote/getHistoricalData.jsp?symbol=ASIANPAINT&fromDate=&toDate=&datePeriod=3months')