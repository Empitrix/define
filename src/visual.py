from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from os import get_terminal_size
from rich.align import AlignMethod
from .models import WordResponseAPI
from rich.table import Table
from rich.align import Align
# from rich.layout import Layout
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

	# layout = Layout()

	with _cnsl.capture() as capture:
		# Spliting
		# layout.split_column(
		# 	Layout(name="top"),
		# 	Layout(name="middle"),
		# 	Layout(name="bottom"))
		# layout["bottom"].size = 5
		# layout["top"].size = 2
		# layout["middle"].split_row(
		# 	Layout(name="left"),
		# 	Layout(name="right"))

		# Updating
		# layout["top"].update(Text(rs.phonetic, style="yellow"))
		
		# top = Align(__column([Align(Text(rs.phonetic, style="yellow"), align="left")], expand=False), align="left")
		top = Align(__column([Text(rs.phonetic, style="yellow")], expand=False), align="left")
		# layout["middle"]["right"].update(Panel("", title="Right"))
		# layout["middle"]["left"].update(Panel("", title="Left"))
		
		# layout["middle"]["right"].update(Panel(__column([
		# 	Text(f'{mean.part_of_speech + ""}') for mean in rs.meanings
		# ]), title="Phonetics"))
		# # layout["middle"].size = None
		# # layout["middle"].ratio = 2
		# layout["middle"]["left"].size = 10
		# layout["middle"]["right"].size = 10
		middle_left:Panel = Panel(__column([
			__column(
				[
					Text(mean.part_of_speech.upper(), style="red"),
				] + [
						__column([
							Text(f'{d.definition}' + ENDLINE, style="cyan"),
							Text(f'{d.example}'+ENDLINE, style="yellow"),
							Text(f'{d.antonyms}'+ENDLINE, style="red"),
							Text(f'{d.antonyms}'+ENDLINE, style="blue"),
						], expand=False, align="left") for d in mean.definitions 
				] + [
					
				] + [
					Text(DIVIDER * int(get_terminal_size().columns / 2 - 6), style="bright_black")
				],
			expand=False, align="left") for mean in rs.meanings], expand=False, align="left"),
		title="Meanings", width=int(get_terminal_size().columns / 2) - 1, expand=True)
		# layout["middle"]["left"].update(Panel(__column([
		# 	__column(
		# 		[
		# 			Text(mean.part_of_speech.upper(), style="red"),
		# 		] + [
		# 				__column([
		# 					Text(f'{d.definition}' + ENDLINE, style="cyan"),
		# 					Text(f'{d.example}'+ENDLINE, style="yellow"),
		# 					Text(f'{d.antonyms}'+ENDLINE, style="red"),
		# 					Text(f'{d.antonyms}'+ENDLINE, style="blue"),
		# 				], expand=False, align="left") for d in mean.definitions 
		# 		] + [
		# 			
		# 		] + [
		# 			Text(DIVIDER * int(get_terminal_size().columns / 2 - 6), style="bright_black")
		# 		],
		# 	expand=False, align="left") for mean in rs.meanings
		# ], expand=False, align="left"), title="Meanings", height=100))



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
		# layout["bottom"].update(
		# 	Panel(Align(
		# 		__column([
		# 				__column([
		# 					Text("License: "),
		# 					Text(f"{rs.file_license.name}", style=f"link {rs.file_license.url}"),
		# 				], expand=False, align="left"),
		# 				Text(__divider(padding=8), style="bright_black")
		# 			] + [
		# 				Text(f"[LINK-{idx+1}]", style=f"link {link}") for idx, link in enumerate(rs.source_urls)
		# 			], expand=False, align="left"
		# 		),
		# 	align="left"), title="Source(s)")
		# )



		# Spliting
		# layout.split_column(
		# 	Layout(name="upper"),
		# 	Layout(name="lower"))
		# layout["upper"].split_row(
		# 	Layout(name="left"),
		# 	Layout(name="middle"),
		# 	Layout(name="right"))
		# layout["lower"].split_row(
		# 	Layout(name="left"),
		# 	Layout(name="right"))
		# # layout["upper"]["left"].split_column(
		# # 	Layout(name="up"),
		# # 	Layout(name="down"))

		# # Updating Layouts
		# # layout["upper"]["left"]["up"].update(
		# # 	Panel(
		# # 		Text(f"{rs.phonetic}\n"),
		# # 		title="Phonetic",
		# # 	))
		# layout["upper"]["left"].update(
		# 	Panel(
		# 		Text(f"{rs.phonetic}\n"),
		# 		title="Phonetic",
		# 	))
		# layout["upper"]["left"].update(
		# 	Panel(
		# 		# # Text(f"{rs.phonetics}\n"),
		# 		__column([
		# 			# __column([
		# 			# 	Text(f'{i.text}, {i.audio}, {i.file_license if isinstance(i, LicenseAPI) else ""}') for i in rs.phonetics
		# 			# ]),
		# 			# __divider(),
		# 			# Text(f'{i.text}, {i.audio[3::] if isinstance(i.audio, str) else ""}, {i.file_license.name if isinstance(i, LicenseAPI) else ""}') for i in rs.phonetics
		# 		]),
		# 		title="Phonetic",
		# 	))

		# _cnsl.print(Panel(layout, title=rs.word.title()))
		_cnsl.print(__column([
			top,
			middle_left,
			bottom
			# Panel("", title=rs.word.title(), width=int(get_terminal_size().columns / 2) - 1),
			# Panel("", title=rs.word.title(), width=int(get_terminal_size().columns / 2) - 1),
		]))
		# _cnsl.print(layout)
		
		# _cnsl.print(Panel(layout, title=f"{rs.word.title()}{rs.phonetic}"))
	return capture.get()


def __test():
	prt("[green]Working!")
	prt("[red]Something bad!")
	_cnsl.print(Panel(__column([
		__divider(),
	])))


if __name__ == "__main__":
	__test()
