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
PADDING:int = 3
_cnsl = Console()

is_used = False
def __get_top_line() -> Text:
	global is_used
	if is_used:
		# Before base pannel it was '6'
		return Text("\n" + DIVIDER * int(get_terminal_size().columns / 2 - 7), style="bright_black")
	is_used = True
	return Text("")

is_used_down = False
def __get_down_line() -> Text:
	global is_used_down
	if is_used_down:
		return Text("\n" + DIVIDER * int(get_terminal_size().columns / 2 - 7), style="bright_black")
	is_used_down = True
	return Text("")


def prt(inpt:str) -> None:
	"""Print on terminal by colors"""
	_cnsl.print(inpt)


def __divider(padding=4) -> str:
	return DIVIDER * (get_terminal_size().columns - padding)


def __flexable(children:list, equal=True, expand=True, align:AlignMethod='center') -> Columns:
	return Columns(children, equal=equal, expand=expand, align=align)


def get_display_context(rs:WordResponseAPI) -> str: 
	
	speech = Table()
	speech.add_column("Part of Speech", justify="right", style="cyan", no_wrap=True)

	with _cnsl.capture() as capture:
		"""TOP: phonetic(pronunciation)"""
		top = Align(__flexable([Text(rs.phonetic, style="yellow")], expand=False), align="left")

		"""MIDDLE-LEFT: Meanings"""
		middle_left:Panel = Panel(__flexable([
			__flexable(
				[
					__get_top_line(),
				] + [
					Text(f"{DIVIDER} {mean.part_of_speech.upper()} {DIVIDER}", style="red"),
				] + [
						__flexable([
							# ► ⦿ •
							Text(f'• {d.definition}' + ENDLINE, style="cyan"),
							Text(f'⦿ {d.example.strip()}'+ ENDLINE, style="yellow") if d.example != "" else "",
							Text(f'Antonyms: {d.antonyms}'+ ENDLINE, style="red") if d.antonyms != [] else "",
							Text(f'Synonyms: {d.synonyms}'+ ENDLINE + "\n", style="blue") if d.synonyms != [] else "",
						], expand=False, align="left") for d in mean.definitions 
				] + [
						Panel(__flexable([
							Text(f"Antonyms: {mean.antonyms}" + ENDLINE, style="steel_blue") if mean.antonyms != [] else "",
							Text(f"Synonyms: {mean.synonyms}" + ENDLINE, style="steel_blue") if mean.synonyms != [] else "",
						], expand=False, align="left"), expand=True) if mean.synonyms != [] and mean.antonyms != [] else ""
				],
			expand=False, align="left") for mean in rs.meanings], expand=False, align="left"),
		title="Meanings", width=int(get_terminal_size().columns / 2) - PADDING, expand=True)


		"""MIDDLE-RIGHT: Phonetics"""
		middle_right:Panel = Panel(__flexable([
			__flexable([
					__get_down_line(),
				] + [
				__flexable([
					Text(p.text[1:-2:]),
					Text("  "),
					Text("Audio", style=f"link {p.audio}") if p.audio != "" and p.audio != None else "",
					Text("  "),
					Text(f"{p.file_license.name}", style=f"link {p.file_license.url}") if p.file_license != None else "",

				], expand=False, align="left"),
				# Text(ENDLINE)
				# Text("\n" + DIVIDER * int(get_terminal_size().columns / 2 - 6), style="bright_black")
			], expand=False, align="left") for p in rs.phonetics
		]), title="Phonetics", width=int(get_terminal_size().columns / 2) - PADDING)

		"""BOTTOM: Source(s)"""
		bottom:Panel = Panel(Align(
			__flexable([
					__flexable([
						Text("License: "),
						Text(f"{rs.file_license.name}", style=f"link {rs.file_license.url}"),
					], expand=False, align="left"),
					Text(__divider(padding=8), style="bright_black")
				] + [
					__flexable([
						Text(f"[LINK-{idx+1}]", style=f"link {link}") for idx, link in enumerate(rs.source_urls)
					], expand=False)
				], expand=False, align="left"
			),
		align="left"), title="Source(s)")

		#  Capture all of the data (save with capture)
		_cnsl.print(
			Panel(
				__flexable([
					top,
					__flexable([middle_left, middle_right]),
					bottom
				]),
				title=rs.word.title(),
				title_align="left",
				expand=True,
			)
		)

	return capture.get()


def __test():
	prt("[green]Working!")
	prt("[red]Something bad!")
	_cnsl.print(Panel(__flexable([
		__divider(),
	])))


if __name__ == "__main__":
	__test()
