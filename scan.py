# JACOB MARSHALL 2020 :)

from datetime import datetime
import time
import csv
from config import *
from pathlib import Path
import alpaca_trade_api as alpaca

def set_watchlist(my_list, filename):
    my_list.clear()
    my_watchlist = open(filename, 'r')
    for symbol in my_watchlist:
        my_list.add(symbol.replace('\n', ''))


# set up API
api = alpaca.REST(API_KEY, SECRET_KEY, ENDPOINT_URL)
clock = api.get_clock()

# set up watchlist
watchlist = set()
previous_size = Path('watchlist.hype').stat().st_size
set_watchlist(watchlist, 'watchlist.hype')

# book-keeping
next_cycle = False
last_minute = datetime.now().minute
cur_size = 0

#check if market is open
if not clock.is_open:
    print('market is closed!')

#main loop
while True:
    #check if file has been changed
    cur_size = Path("watchlist.hype").stat().st_size
    if cur_size != previous_size:
        previous_size = cur_size
        set_watchlist(watchlist, 'watchlist.hype')

    symbols_to_report = set()

    #do price comparisons on each stock
    for symbol in watchlist:
        data = api.get_barset(symbol, 'day', limit=1)
        yesterday_close = data[symbol][0].c
        data = api.get_barset(symbol, 'minute', limit=1)
        cur_price = data[symbol][0].c
        if cur_price >= 1.15 * yesterday_close:
            print(symbol + ' has increased by ' + str(cur_price / float(yesterday_close)) + '%% and is now at ' + str(cur_price) + ' (closed yesterdat at ' + str(yesterday_close) + ')')
        print(yesterday_close)
        print(cur_price)
    #wait until exactly a minute has passed since the last loop began and then go again
    while last_minute == datetime.now().minute:
        time.sleep(1)
    last_minute = datetime.now().minute



