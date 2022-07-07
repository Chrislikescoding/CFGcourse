import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/products/classify"

querystring = {"locale":"en_us"}

payload = {
	"plu_code": "",
	"title": "flour",
	"upc": ""
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
	"X-RapidAPI-Key": "dea20e96efmshbc1cad7aa88cc06p1721cejsn9e24c754945b"
}

response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

print(response.text)