import requests
# import json
import json_data as jd

API_KEY = 'bb3395030b8015c69bbb'

# curr_url =  f'https://free.currconv.com/api/v7/currencies'
# countries_url = 'https://free.currconv.com/api/v7/countries'


# NEED TO UNCOMMENT FINALLY
# res = requests.get(curr_url, params={'apiKey': API_KEY})
# currencies_data = res.json()['results']


# res = requests.get(curr_url, params={'apiKey': API_KEY})
# data = res.json()
# print(json.dumps(data, indent=4))
currencies_data = jd.curr['results']

# cc = jd.curr['results']

# Countries Currency details
def get_currency_details():
	cc = jd.cc_data['results'].items()
	res = []
	for k, v in cc:
		temp = {
			# 'country': f'Country : {v["name"]}',
			'country': v["name"],
			# 'curr': f'Currency : {v["currencyName"]} ~ {v["currencyId"]}'
			'currency': f'{v["currencyName"]} ~ {v["currencyId"]}'
		}
		res.append(temp)
	return res
		# print(f'Country : {v["name"]}')
		# print(f'Currency : {v["currencyName"]} ~ {v["currencyId"]}')
		# print()

def get_exchange_rate(fc, tc):
	q = f'{fc}_{tc}'
	exchange_rate_url = 'https://free.currconv.com/api/v7/convert'
	params = {
	'apiKey': API_KEY,
	'q': q
	}
	res = requests.get(exchange_rate_url, params=params)
	data = res.json()
	# print(data)
	if data['query']['count'] == 0:
		return None
	
	fc = currencies_data[fc]
	tc = currencies_data[tc]

	return data['results'][q]['val'], fc, tc

