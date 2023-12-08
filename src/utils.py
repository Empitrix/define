import sys
from requests import get
from models import WordResponseAPI, word_response_parser
from visual import prt
from json import loads


def get_api_response(word:str) -> WordResponseAPI:
	"""Get the input word data from server"""
	word = word.strip().lower()  # Convert word to lowercase
	try:
		response = get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word.strip()}')
		if(response.status_code == 200):
			data = loads(response.text)[0]
			return word_response_parser(data)
		else:
			prt("[red]Error on API")
			sys.exit()
	except(Exception,) as error:
		prt("[red]Something is Wrong, try again later!")
		prt(f"[red]ERROR: [yellow]{error}")
		sys.exit()


if __name__ == "__main__":
	word:WordResponseAPI = get_api_response("Define")
	print(word.word)

