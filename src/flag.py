import sys
from . import logs
from . import get_input
# import logs


class OPT:
	def __init__(self, debug:bool=False, use_less:bool=True, word:str="") -> None:
		self.debug = debug
		self.use_less = use_less
		self.word = word


def check_for_flags() -> OPT:
	# Check for only filename
	args = sys.argv.copy()
	clear_arg = sys.argv.copy()
	clear_arg.pop(0)  # Removing file name

	opt:OPT = OPT()

	if len(args) == 1:
		opt.word = get_input.get_input()
		return opt

	if len(args) > 1:
		for ord in args:
			arg = ord.strip().lower()
			
			# Options
			if arg == "-nl" or arg == "--no-less":
				opt.use_less = False
				clear_arg.remove(ord)
			if arg == "-d" or arg == "--debug":
				opt.debug = True
				clear_arg.remove(ord)

			# Auto
			if arg == "-v" or arg == "--version":
				print(logs.LOGs.version)
				sys.exit()
			if arg == "-h" or arg == "--help":
				print(logs.LOGs.help)
				sys.exit()


	if len(clear_arg) == 1:
		opt.word = clear_arg.pop()
	else:
		word = get_input.get_input_sys()
		if word.strip() == "":
			opt.word = input("Word: ")
	return opt


if __name__ == "__main__":
	out:OPT = check_for_flags()

