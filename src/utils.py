from ctypes import windll
from subprocess import run
from requests import get
from .models import WordResponseAPI, word_response_parser
from .visual import prt
# from models import WordResponseAPI, word_response_parser
# from visual import prt
from json import loads
import sys


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


def scroll_page(inpt:str,use_less:bool=True) -> None:
	"""Show the input text using less.exe"""
	if(use_less):
		# Save the current console codepage
		prev_codepage = windll.kernel32.GetConsoleOutputCP()
		# Set the console codepage to UTF-8
		windll.kernel32.SetConsoleOutputCP(65001)
		# Run less.exe
		run("less.exe -R", input=inpt, encoding='utf-8')
		# Restore the previous console codepage
		windll.kernel32.SetConsoleOutputCP(prev_codepage)
	else:
		print(inpt)


if __name__ == "__main__":
	word:WordResponseAPI = get_api_response("Define")
	scroll_page(word.word)
