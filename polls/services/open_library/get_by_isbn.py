from .base import Base
from .connection import mockit

class GetByIsbn(Base):
    def __init__(self, isbn):
        self.isbn = isbn

    def perform(self):
        s = mockit()
        return 'hello' + self.config + self.isbn + s
