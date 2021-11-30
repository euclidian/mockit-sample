# Github Module
from .services.open_library.get_by_isbn import GetByIsbn

def get_by_isbn(isbn):
    return GetByIsbn(isbn).perform()
