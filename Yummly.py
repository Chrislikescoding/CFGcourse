import requests

url = "https://yummly2.p.rapidapi.com/feeds/auto-complete"

querystring = {"q":"chicken soup"}

headers = {
	"X-RapidAPI-Host": "yummly2.p.rapidapi.com",
	"X-RapidAPI-Key": "dea20e96efmshbc1cad7aa88cc06p1721cejsn9e24c754945b"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)