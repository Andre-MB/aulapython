import requests

def fetch_cep(endpoint):
	url = f"https://viacep.com.br/ws/{endpoint}/json" 
	response = requests.get(url)
	
	return response.json() if response.status_code == 200 else response.status_code

# cep = fetch_cep('01026010')

cep = input("Qual o cep quer buscar ? ")
cep = fetch_cep(cep)

for x in cep:
	print(x +": "+ cep[x])