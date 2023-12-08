class WordResponseAPI:
	def __init__(self, word:str, pronunciation:str,
			  definition:str, examples:list[str]) -> None:
		self.word = word
		self.pronunciation = pronunciation
		self.definition = definition
		self.examples = examples

