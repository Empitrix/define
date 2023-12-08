#!/usr/bin/env python3
from src.get_input import get_input
from src.visual import prt
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


print(f"All Fine!, Input Word: {word}")



