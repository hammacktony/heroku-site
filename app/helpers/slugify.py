""" Transform title to slug """
import re
import unidecode

def remove_whitespaces(text):
	""" Remove Whitespaces """

	# Strip Leading Whitespace
	text = text.lstrip()
	# Strip Trailing Whitespace
	text = text.rstrip()

	return text

def slugify(text):
    """  helper function that creates slugs for the articles """

    text = unidecode.unidecode(remove_whitespaces(text)).lower()

    return re.sub(r'\W+', '-', text)