from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from os import get_terminal_size
from rich.align import AlignMethod
from .models import WordResponseAPI
from rich.table import Table
from rich.layout import Layout
from rich.text import Text


_cnsl = Console()


def prt(inpt:str) -> None:
	"""Print on terminal by colors"""
	_cnsl.print(inpt)


def __divider(padding=4) -> str:
	return "─" * (get_terminal_size().columns - padding)


def __column(children:list, equal=True, expand=True, align:AlignMethod='center') -> Columns:
	return Columns(children, equal=equal, expand=expand, align=align)


def get_display_context(rs:WordResponseAPI) -> str: 
	
	speech = Table()
	speech.add_column("Part of Speech", justify="right", style="cyan", no_wrap=True)

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
		)

		# Updating Layouts
		layout["upper"]["right"].update(
			Panel(
				__column([
				], expand=False, align="left"),
				title="Examples"
			)
		)
		layout["upper"]["left"]["up"].update(
			Panel(
				Text(
					f"{rs.phonetic}\n"
				),
				title="Pronunciation",
			)
		)
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
