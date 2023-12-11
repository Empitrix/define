#!/usr/bin/env python3
from src.models import WordResponseAPI
from src.utils import get_api_response, scroll_page
from src.visual import prt, get_display_context
from src.flag import check_for_flags, OPT
import subprocess as sp
import sys


# Run less and get the erros
less_return_code:int = sp.run(
	"less --version",
	capture_output=True,
	text=True).returncode

opts:OPT = check_for_flags()
word = opts.word

# # If exit have erros close the CLI
# if less_return_code == 1:
# 	prt('[red]"Less" is NOT installed!')
# 	sys.exit()
# Get the word from user
# word = get_input()
if word == "":
	prt('[red]Enter a valid word!')
	sys.exit()

# Get word's data from API
response:WordResponseAPI = get_api_response(
	word, debug_mode=opts.debug)

# Make the page
context = get_display_context(response)

# Show the text using less
scroll_page(context, use_less=opts.use_less)

