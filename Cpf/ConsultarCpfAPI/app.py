import requests

def fetch_cpf(Cpf):
	url = f"https://api.invertexto.com/v1/validator?token=21591|2bQVvbLWHeBAh2qnsAkpcF6kXoTzm4xa&value={Cpf}&type=cpf" 
	response = requests.get(url)
	
	return response.json() if response.status_code == 200 else response.status_code

cpf = fetch_cpf("875.307.490-48")

for x in cpf:
	print(cpf[x]) 