from rich import style
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from os import get_terminal_size
from rich.align import AlignMethod
from .models import WordResponseAPI
from rich.table import Table
from rich.style import Style
from rich.text import Text


_cnsl = Console()

def prt(inpt:str) -> None:
	"""Print on terminal by colors"""
	_cnsl.print(inpt)


def __divider(padding=4) -> str:
	return "─" * (get_terminal_size().columns - padding)

# def __column(children:list, equal=True, expand=True, align:AlignMethod='center') -> Columns:
# 	return Columns(children, equal=equal, expand=expand, align=align)

def __column(children:list, equal=True, expand=True, align:AlignMethod='center') -> Columns:
	return Columns(children, equal=equal, expand=expand, align=align)


def get_display_context(rs:WordResponseAPI) -> str: 
	
	# table = Table(title="Examples")
	# table.add_column("Released", justify="right", style="cyan", no_wrap=True)
	# table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")
	
	speech = Table()
	speech.add_column("Part of Speech", justify="right", style="cyan", no_wrap=True)
	speech.add_row(rs.part_of_speech.upper())

	with _cnsl.capture() as capture:
		# _cnsl.print(Panel(__column([
		# 	# Text("Awesome", style=""),
		# 	speech,
		# ])))
		_cnsl.print(Panel(__column([speech]), title=rs.word.title()))
		# _cnsl.print(Panel(__column([speech])))
	return capture.get()


def __test():
	prt("[green]Working!")
	prt("[red]Something bad!")
	_cnsl.print(Panel(__column([
		__divider(),
	])))



if __name__ == "__main__":
	__test()
