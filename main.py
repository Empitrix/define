#!/usr/bin/env python3
from src.models import WordResponseAPI
from src.get_input import get_input
from src.utils import get_api_response, scroll_page
from src.visual import prt, get_display_context
import subprocess as sp
import sys


# Run less and get the erros
less_return_code:int = sp.run(
	"less --version",
	capture_output=True,
	text=True).returncode

# If exit have erros close the CLI
if less_return_code == 1:
	prt('[red]"Less" is NOT installed!')
	sys.exit()


# Get the word from user
word = get_input()
if word == "":
	prt('[red]Enter a valid word!')
	sys.exit()


# Get word's data from internter
response:WordResponseAPI = get_api_response(word)

# Make the page
context = get_display_context(response)

# Show the text using less
scroll_page(context, use_less=False)

