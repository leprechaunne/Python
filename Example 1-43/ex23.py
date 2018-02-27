import sys
script, encodingType, error = sys.argv

def main(f, encoding, errors):
	line = f.readline()

	# first 'if' and its recursive. That's a weird concept to skip
	if line:
		println(line, encoding, errors)
		return main(f, encoding, errors)

def println(line, encoding, errors):
	lang = line.strip()
	raw = lang.encode(encoding, errors=errors)
	cooked = raw.decode(encoding, errors=errors)

	print(raw, "<===>", cooked)

# store the file object and specify encoding
languages = open("languages.txt", encoding="utf-8")
# start the recursive reading
main(languages, encodingType, error)