import os

FOLDER = '2016-07-23'
INPUT_FOLDER = '/home/kelvin/Documents/Betfair/Data/' + FOLDER + '/'
UPLOAD_FOLDER = '/home/kelvin/Documents/Betfair/Data/'

for root, dirs, filenames in os.walk(INPUT_FOLDER):
    for f in filenames:
        new_file_path = ''
        file_path = INPUT_FOLDER + f
        if 'marketIndicators' not in f \
           and 'matches' not in f \
           and 'orders' not in f \
           and 'tradeDetail' not in f \
           and 'tradeSummary' not in f \
           and 'MarketKeys' not in f:
            with open(file_path, 'r') as o:
                market_id = o.readline().split(',')[2]
                new_file_name = market_id + '_marketdata.csv'
                new_file_path = UPLOAD_FOLDER + 'market_data/' + new_file_name

        elif 'marketIndicators' in f:
            with open(file_path, 'r') as o:
                market_id = o.readline().split(',')[2]
                new_file_name = market_id + '_marketindicators.csv'
                new_file_path = UPLOAD_FOLDER + 'market_indicators/' + new_file_name

        elif 'tradeDetail' in f:
            with open(file_path, 'r') as o:
                market_id = o.readline().split(',')[7]
                new_file_name = market_id + '_tradedetail.csv'
                new_file_path = UPLOAD_FOLDER + 'trade_detail/' + new_file_name

        elif 'tradeSummary' in f:
            with open(file_path, 'r') as o:
                market_id = o.readline().split(',')[1]
                new_file_name = market_id + '_tradesummary.csv'
                new_file_path = UPLOAD_FOLDER + 'trade_summary/' + new_file_name

        elif 'matches' in f:
            with open(file_path, 'r') as o:
                market_id = o.readline().split(',')[3]
                new_file_name = market_id + '_marketmatches.csv'
                new_file_path = UPLOAD_FOLDER + 'market_matches/' + new_file_name

        elif 'orders' in f:
            with open(file_path, 'r') as o:
                market_id = o.readline().split(',')[3]
                new_file_name = market_id + '_marketorders.csv'
                new_file_path = UPLOAD_FOLDER + 'market_orders/' + new_file_name

        elif 'MarketKeys' in f:
            new_file_path = UPLOAD_FOLDER + 'market_keys/' + str(FOLDER)[0:4] + \
            str(FOLDER)[5:7] + str(FOLDER)[8:10] + '_marketkeys.csv' 

        if len(new_file_path) > 0:
            os.rename(file_path, new_file_path)
            print(new_file_path)
