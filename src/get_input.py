import sys


def get_input(msg:str = "Word: ") -> str:
	output = ""
	if not sys.stdin.isatty():
		output = sys.stdin.read().strip()
	else:
		if len(sys.argv) != 2:
			output = input(msg).strip()
		else:
			output = sys.argv[-1].strip()
	return output


if __name__ == "__main__":
	name = get_input()
	print(f"Name: {name}")
