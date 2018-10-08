""" Helpers for Dashboard """
import re
import unidecode

def remove_whitespaces(text) -> str:
	""" Remove Whitespaces """

	# Strip Leading Whitespace
	text = text.lstrip()
	# Strip Trailing Whitespace
	text = text.rstrip()

	return text

def slugify(text) -> str:
    """  helper function that creates slugs for the articles """

    text = unidecode.unidecode(text).lower()

    return re.sub(r'\W+', '-', text)