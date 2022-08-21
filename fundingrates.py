import ccxt

ftx = ccxt.ftx()
ftx.load_markets()
symbols = ftx.symbols
symbols_ = []


def funding_rates():
    for symbol in symbols:
        if ':' in symbol:
            if '-' not in symbol:
                symbols_.append(symbol)
    data = {}
    for i in range(len(symbols_)):
        info = ftx.fetch_funding_rate(symbols_[i])
        data[symbols_[i]] = round(info['fundingRate'] * 100, 4)
    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=False)
    return sorted_data
