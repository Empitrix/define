from requests import get

def get_api_response(word:str) -> dict:
	"""Get the input word data from server"""
	response = get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word.strip()}')
	if(response.status_code == 200):
		return response.json();
	return {}
