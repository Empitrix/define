class LicenseAPI:
	def __init__(self, name:str, url:str) -> None:
		self.name = name
		self.url = url


class Definition:
	def __init__(self,
			example:str, definition:str,
			synonyms:list[str], antonyms:list[str]) -> None:
		self.definition = definition
		self.synonyms = synonyms
		self.antonyms = antonyms
		self.example = example


class Pronunciation:
	def __init__(self, text:str, audio:str) -> None:
		self.text = text
		self.audio = audio 


class Phonetic:
	def __init__(self, audio:str, source_url:str, file_license:LicenseAPI) -> None:
		self.audio = audio
		self.source_url = source_url
		self.file_license = file_license


class WordResponseAPI:
	def __init__(self, word:str, pronunciation:Pronunciation, phonetics:list[Phonetic],
			  part_of_speech:str, source_urls:list[str], file_license:LicenseAPI,
			  synonyms:list[str], antonyms:list[str],
			  definitions:list[Definition]) -> None:
		self.word = word
		self.pronunciation = pronunciation,
		self.phonetics = phonetics
		self.definitions = definitions
		self.part_of_speech = part_of_speech
		self.source_urls = source_urls
		self.file_license = file_license
		self.synonyms = synonyms
		self.antonyms = antonyms

	def get_pronunciation(self) -> Pronunciation:
		return self.pronunciation[0]


def word_response_parser(inpt:dict) -> WordResponseAPI:
	"""Convert JSON file into WordResponseAPI"""
	definitions:list[Definition] = []
	pronunciation:Pronunciation = Pronunciation(text="", audio="")
	# global pronunciation
	# pronunciation:Pronunciation
	phonetics:list[Phonetic] = []

	for df in inpt["meanings"][0]["definitions"]:
		definitions.append(Definition(
			definition = df["definition"],
			synonyms = df["synonyms"],
			antonyms = df["antonyms"],
			example = df["example"] if "example" in list(df.keys()) else "",
		))
	for p in inpt["phonetics"]:
		if len(list(p.keys())) == 2:
			if pronunciation.text == "":
				pronunciation = Pronunciation(
					text=p["text"],
					audio=p["audio"])
			else: continue
		elif len(list(p.keys())) == 3:
			phonetics.append(Phonetic(
				audio=p["audio"],
				source_url=p["sourceUrl"],
				file_license = LicenseAPI(
					name=p["license"]["name"],
					url=p["license"]["url"])
			))
		else: continue

	return WordResponseAPI(
		word=inpt["word"],
		pronunciation=pronunciation,
		phonetics=phonetics,
		definitions=definitions,
		part_of_speech=inpt["meanings"][0]["partOfSpeech"],
		synonyms=inpt["meanings"][0]["synonyms"],
		antonyms=inpt["meanings"][0]["antonyms"],
		source_urls=inpt["sourceUrls"],
		file_license=LicenseAPI(
			name=inpt["license"]["name"],
			url=inpt["license"]["url"]),  # License
	)

