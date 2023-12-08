from rich.console import Console


def prt(inpt:str) -> None:
	"""Print on terminal by colors"""
	Console().print(inpt)


if __name__ == "__main__":
	prt("[green]Working!")
	prt("[red]sth bad!")
