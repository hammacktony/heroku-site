""" Helpers for PostsController """


def convert_slug_to_category(slug: str) -> str:
	''' Helper function to convert category slug into category

	args
			slug: str - slug of category

	returns
			category: str - category 
	'''
	
	category = slug.replace('-', ' ')
	return category.title()
