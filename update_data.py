import json
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd
import yfinance as yf

SYMBOLS = {'SPY':'USA · S&P 500','QQQ':'USA · Nasdaq 100','VT':'Mondo · Azionario globale','VGK':'Europa','EWI':'Italia','EWG':'Germania','EWJ':'Giappone','MCHI':'Cina','INDA':'India','VWO':'Emergenti','VEA':'Sviluppati ex USA'}
OUT = Path(__file__).parent / 'data' / 'history.json'

def series(ticker):
    frame = yf.download(ticker, start='2000-01-01', auto_adjust=True, progress=False, threads=False)
    if frame.empty: raise ValueError(f'Nessun dato per {ticker}')
    close = frame['Close']
    if isinstance(close, pd.DataFrame): close = close.iloc[:,0]
    result = []
    for date, price in close.dropna().items():
        if float(price) > 0: result.append([date.strftime('%Y-%m-%d'),round(float(price),6)])
    if not result: raise ValueError(f'Nessun prezzo valido per {ticker}')
    return result

existing = {}
if OUT.exists():
    try: existing = json.loads(OUT.read_text(encoding='utf-8'))
    except (ValueError,OSError): pass
prices = {}
errors = {}
for symbol in [*SYMBOLS,'EURUSD=X']:
    try:
        prices[symbol] = series(symbol)
        print(symbol,len(prices[symbol]))
    except Exception as exc:
        errors[symbol] = str(exc)
        if existing.get('prices',{}).get(symbol): prices[symbol] = existing['prices'][symbol]
        print('WARNING',symbol,str(exc))
if not prices: raise SystemExit('Nessuna serie disponibile; file precedente conservato')
OUT.parent.mkdir(exist_ok=True)
OUT.write_text(json.dumps({'updated_at':datetime.now(timezone.utc).isoformat(),'labels':SYMBOLS,'prices':prices,'errors':errors},separators=(',',':')),encoding='utf-8')
