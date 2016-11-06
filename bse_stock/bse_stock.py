import json

import mechanize
import urllib2
from bs4 import BeautifulSoup
import sys


def getData(item):
	url = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol="
	try:
		url=url+""+item
		br = mechanize.Browser()
		br.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0 (compatible;)'), ('Accept', '*/*')]
		br.set_handle_robots(False)
		br.set_handle_equiv(False)
		response = br.open(url)
		br.select_form(nr=0)  
		html=response.read() 
		soup = BeautifulSoup(html, "lxml")
		dt = soup.find('div', {'id': 'responseDiv'})
		jdata= json.loads(dt.text)
		return jdata
	except:
		print "Error occured... try again after sometime"
		exit(0)
	
def dispQuote(item):
	jdata=getData(item)				
	
	print  "Last Update Time:" + jdata['lastUpdateTime']
	print "Traded Date:" + jdata['tradedDate']
	print "Company Name=" + jdata['data'][0]['companyName']
	print "Symbol=" + jdata['data'][0]['symbol']
	print "Last Price=" + jdata['data'][0]['lastPrice']
	print "Change=" + jdata['data'][0]['change']
	print "Change %=" + jdata['data'][0]['pChange']
	print "Open Price=" + jdata['data'][0]['open']
	print "High=" + jdata['data'][0]['dayHigh']
	print "Low=" + jdata['data'][0]['dayLow']
	print "Close=" + jdata['data'][0]['closePrice']
	print "Previous Close=" + jdata['data'][0]['previousClose']

def getStock(item):
	try:
		jdata=getData(item)
		return "Quote of " + jdata['data'][0]['companyName'] + " updated as on " + jdata['lastUpdateTime'] + " is Rs." + "\n" + jdata['data'][0]['lastPrice'] + " change Rs." + jdata['data'][0]['change'] + " and " + jdata['data'][0]['pChange'] + "%"
	except:
		print "Stock not traded today"
		exit(0)
		
#print getStock('SBIN')
#print getStock('PNB')
#print getStock('ICICI')

