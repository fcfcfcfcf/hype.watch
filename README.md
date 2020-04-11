![hype.watch logo](https://raw.githubusercontent.com/marshingjay/hype.watch/master/hype_watch_logo.PNG)
This is a hype-play alert service for traders.

#How to use this

Hype.watch is configured to pull ticker data via the Alpaca API (see https://alpaca.markets/). In order to use this service you will need to provide a set of Alpaca API keys (free to obtain for a paper-trading account) and place them into the config.py file. Then, edit 'watchlist.hype' to include the ticker names you would like notifications for. Run the script using 'python3 scan.py' to start recieving notifications for price movements. If you'd like to add a ticker to your watchlist, simply edit the watchlist file and save it, there's no need to restart the script.

This tool exists as a proof of concept and will be greatly expanded in the future.
