from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from os import get_terminal_size
from rich.align import AlignMethod
from .models import WordResponseAPI
# from .utils import get_random_color
# import .utils as utils
from . import utils as u
# from .utils import get_color
# from .utils import get_random_color
from rich.table import Table
from rich.layout import Layout
from rich.text import Text


_cnsl = Console()

def prt(inpt:str) -> None:
	"""Print on terminal by colors"""
	_cnsl.print(inpt)


def __divider(padding=4) -> str:
	return "─" * (get_terminal_size().columns - padding)

# def __column(children:list, equal=True, expand=True, align:AlignMethod='center') -> Columns:
#	return Columns(children, equal=equal, expand=expand, align=align)

def __column(children:list, equal=True, expand=True, align:AlignMethod='center') -> Columns:
	return Columns(children, equal=equal, expand=expand, align=align)


def get_display_context(rs:WordResponseAPI) -> str: 
	
	speech = Table()
	speech.add_column("Part of Speech", justify="right", style="cyan", no_wrap=True)
	speech.add_row(rs.part_of_speech.upper())


	layout = Layout()

	with _cnsl.capture() as capture:
		# Spliting
		layout.split_column(
			Layout(name="upper"),
			Layout(name="lower")
		)
		layout["upper"].split_row(
			Layout(name="left"),
			Layout(name="middle"),
			Layout(name="right")
		)
		layout["lower"].split_row(
			Layout(name="left"),
			Layout(name="right")
		)
		layout["upper"]["left"].split_column(
			Layout(name="up"),
			Layout(name="down")
			# Panel(__column([ex for ex in rs.phonetics]), title="Examples")
		)

		# Updating
		layout["upper"]["right"].update(
			Panel(
				# Text( "".join([i.example+"\n" for i in rs.definitions]) ),
				__column([
					Text(i.example, style=u.get_random_color()) for i in rs.definitions
					# Text( "".join([i.example+"\n" for i in rs.definitions]) ),
				], expand=False, align="left"),
				title="Examples"
			)
		)
		layout["upper"]["left"]["up"].update(
			Panel(
				Text(
					f"{rs.get_pronunciation().text}\n"
					f'{rs.get_pronunciation().audio if rs.get_pronunciation().audio != "" else "NO VOICE LINK"}'
				),
				title="Pronunciation",
			)
		)
		# Updating
		# layout["lower"]["right"].update(
		# 	# Panel(__column([ex for ex in rs.phonetics]), title="Examples")
		# )
		_cnsl.print(Panel(layout, title=rs.word.title()))
	return capture.get()


def __test():
	prt("[green]Working!")
	prt("[red]Something bad!")
	_cnsl.print(Panel(__column([
		__divider(),
	])))



if __name__ == "__main__":
	__test()
