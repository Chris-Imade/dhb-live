from django.utils.crypto import get_random_string


def random_string():
	unique_char = get_random_string(length=15)
	return unique_char