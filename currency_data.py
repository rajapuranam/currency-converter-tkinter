import requests
import json_data as jd

API_KEY = <ENTER_API_KEY>

currencies_data = jd.curr['results']

def get_currency_details():
	cc = jd.cc_data['results'].items()
	res = []
	for k, v in cc:
		temp = {
			'country': v["name"],
			'currency': f'{v["currencyName"]} ~ {v["currencyId"]}'
		}
		res.append(temp)
	return res

def get_exchange_rate(fc, tc):
	q = f'{fc}_{tc}'
	exchange_rate_url = 'https://free.currconv.com/api/v7/convert'
	params = {
		'apiKey': API_KEY,
		'q': q
	}
	res = requests.get(exchange_rate_url, params=params)
	data = res.json()
	
	if data['query']['count'] == 0:
		return None
	
	fc = currencies_data[fc]
	tc = currencies_data[tc]

	return data['results'][q]['val'], fc, tc
