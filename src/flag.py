import sys
# from . import logs
import logs


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

	otp:OPT = OPT()

	if len(args) == 1:
		return OPT()
	
	not_word:list[str] = []
	if len(args) > 1:
		for ord in args:
			arg = ord.strip().lower()
			
			# Options
			if arg == "-nl" or arg == "--no-less":
				otp.use_less = False
				clear_arg.remove(ord)
			if arg == "-d" or arg == "--debug":
				otp.debug = True
				clear_arg.remove(ord)

			# Auto
			if arg == "-v" or arg == "--version":
				print(logs.LOGs.version)
				sys.exit()
			if arg == "-h" or arg == "--help":
				print(logs.LOGs.help)
				sys.exit()


	print("CLEAR LOG LENGTH: ", len(clear_arg))
	return OPT()


if __name__ == "__main__":
	out:OPT = check_for_flags()

