from typing import Optional, Union


def __phonetic_detection(name:str, data:dict) -> Optional[Union[str, dict]]:
	if name in list(data.keys()):
		if data[name] != "":
			return data[name]
	return None


class LicenseAPI:
	def __init__(self, name:str, url:str) -> None:
		self.name = name
		self.url = url


def __parse_license(inpt:Optional[dict]) -> Optional[LicenseAPI]:
	"""Parse Json to LincenseAPI"""
	if inpt == None:
		return None
	if "name" not in inpt.keys() and "url" in inpt.keys():
		return None
	if inpt["name"] == "": return None
	if inpt["url"] == "": return None
	return LicenseAPI(name=inpt["name"], url=inpt["name"])


class Definition:
	def __init__(self,
			example:str, definition:str,
			synonyms:list[str], antonyms:list[str]) -> None:
		self.definition = definition
		self.synonyms = synonyms
		self.antonyms = antonyms
		self.example = example


def __parse_defenation(inpt:dict) -> Definition:
	return Definition(
		definition=inpt["definition"],
		synonyms=inpt["synonyms"],
		antonyms=inpt["antonyms"],
		example=inpt["example"] if "example" in list(inpt.keys()) else "")


class Pronunciation:
	def __init__(self, text:Optional[str],
			audio:Optional[str]) -> None:
		self.text = text
		self.audio = audio

class Phonetic:
	def __init__(self, text:str, audio:Optional[str], source_url:Optional[str],
			file_license:Optional[LicenseAPI]) -> None:
		self.text = text
		self.audio = audio
		self.source_url = source_url
		self.file_license = file_license

def __parse_phonetic(inpt:dict) -> Phonetic:
	"""Convert json:dict to Phonetic"""
	lc = __phonetic_detection("license", inpt)
	txt = __phonetic_detection("audio", inpt)
	url = __phonetic_detection("sourceUrl", inpt)
	return Phonetic(
		text=inpt["text"],
		audio=txt if isinstance(txt, str) else None,
		source_url=url if isinstance(url, str) else None,
		file_license=__parse_license(lc if isinstance(lc, dict) else None)
	)


class Meaning:
	def __init__(self, part_of_speech:str,definitions:list[Definition],
			  synonyms:list[str], antonyms:list[str]) -> None:
		self.part_of_speech = part_of_speech
		self.definitions = definitions
		self.synonyms = synonyms
		self.antonyms = antonyms


class WordResponseAPI:
	def __init__(self, word:str, phonetics:list[Phonetic],
			  source_urls:list[str], file_license:LicenseAPI,
			  phonetic:str, meanings:list[Meaning]) -> None:
		self.word = word
		self.phonetic = phonetic
		self.phonetics = phonetics
		self.source_urls = source_urls
		self.file_license = file_license
		self.meanings = meanings


def word_response_parser(inpt:dict) -> WordResponseAPI:
	"""Convert JSON file into WordResponseAPI"""
	phonetics:list[Phonetic] = []
	# definitions:list[Definition] = []
	# for df in inpt["meanings"][0]["definitions"]:
	# 	definitions.append(Definition(
	# 		definition = df["definition"],
	# 		synonyms = df["synonyms"],
	# 		antonyms = df["antonyms"],
	# 		example = df["example"] if "example" in list(df.keys()) else "",
	# 	))
	# Get all the meanings
	all_meanings:list[Meaning] = []
	for m in inpt["meanings"]:
		all_meanings.append(Meaning(
			part_of_speech=m["partOfSpeech"],
			synonyms=m["synonyms"], antonyms=m["antonyms"],
			definitions= [__parse_defenation(i) for i in m["definitions"]]
		))

	# Searching for Phonetic
	for p in inpt["phonetics"]:
		phonetics.append(__parse_phonetic(p))

	return WordResponseAPI(
		word=inpt["word"],
		# phonetic=inpt["phonetic"],
		phonetic=inpt["phonetic"][1:-2:],
		phonetics=phonetics,
		# phonetics=phonetics[1::-2],
		meanings=all_meanings,
		source_urls=inpt["sourceUrls"],
		file_license=LicenseAPI(
			name=inpt["license"]["name"],
			url=inpt["license"]["url"]),  # License
	)
