import requests

def fetch_email(email):
	url = f"https://api.invertexto.com/v1/email-validator/{email}?token=21591|2bQVvbLWHeBAh2qnsAkpcF6kXoTzm4xa" 
	response = requests.get(url)
	
	return response.json() if response.status_code == 200 else response.status_code

resto = fetch_email("andrezinhogame15@gmail.com")

for chave, valor in resto.items():
	print(chave + ":" + str(valor)) 