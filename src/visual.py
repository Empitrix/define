from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from os import get_terminal_size
from rich.align import AlignMethod
from .models import WordResponseAPI
from rich.table import Table
from rich.align import Align
from rich.text import Text

DIVIDER:str = "─"
ENDLINE:str = (" " * 100)
_cnsl = Console()


def prt(inpt:str) -> None:
	"""Print on terminal by colors"""
	_cnsl.print(inpt)


def __divider(padding=4) -> str:
	return DIVIDER * (get_terminal_size().columns - padding)


def __column(children:list, equal=True, expand=True, align:AlignMethod='center') -> Columns:
	return Columns(children, equal=equal, expand=expand, align=align)


def get_display_context(rs:WordResponseAPI) -> str: 
	
	speech = Table()
	speech.add_column("Part of Speech", justify="right", style="cyan", no_wrap=True)

	with _cnsl.capture() as capture:
		top = Align(__column([Text(rs.phonetic, style="yellow")], expand=False), align="left")

		middle_left:Panel = Panel(__column([
			__column(
				[
					Text(f"{DIVIDER} {mean.part_of_speech.upper()} {DIVIDER}", style="red"),
				] + [
						__column([
							Text(f'{d.definition}' + ENDLINE, style="cyan"),
							Text(f'{d.example}'+ ENDLINE, style="yellow"),
							Text(f'Antonyms: {d.antonyms}'+ ENDLINE, style="red"),
							Text(f'Synonyms: {d.synonyms}'+ ENDLINE, style="blue"),
						], expand=False, align="left") for d in mean.definitions 
				] + [
						Panel(__column([
							Text(f"Antonyms: {mean.antonyms}", style="steel_blue"),
							Text(f"Synonyms: {mean.synonyms}", style="steel_blue"),
						], expand=False, align="left"))
				] + [
					Text(DIVIDER * int(get_terminal_size().columns / 2 - 6), style="bright_black")
				],
			expand=False, align="left") for mean in rs.meanings], expand=False, align="left"),
		title="Meanings", width=int(get_terminal_size().columns / 2) - 1, expand=True)

		middle_right:Panel = Panel("", title=rs.word.title(), width=int(get_terminal_size().columns / 2) - 1)


		bottom:Panel = Panel(Align(
			__column([
					__column([
						Text("License: "),
						Text(f"{rs.file_license.name}", style=f"link {rs.file_license.url}"),
					], expand=False, align="left"),
					Text(__divider(padding=8), style="bright_black")
				] + [
					__column([
						Text(f"[LINK-{idx+1}]", style=f"link {link}") for idx, link in enumerate(rs.source_urls)
					], expand=False)
				], expand=False, align="left"
			),
		align="left"), title="Source(s)")
		


		# _cnsl.print(Panel(layout, title=rs.word.title()))
		_cnsl.print(__column([
			top,
			__column([middle_left, middle_right]),
			bottom
		]))

	return capture.get()


def __test():
	prt("[green]Working!")
	prt("[red]Something bad!")
	_cnsl.print(Panel(__column([
		__divider(),
	])))


if __name__ == "__main__":
	__test()
