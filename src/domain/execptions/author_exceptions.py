#    _____ __                __           ____
#   / ___// /_  ____  ____  / /____  ____/ __ \___  _   __
#   \__ \/ __ \/ __ \/ __ \/ __/ _ \/ __/ / / / _ \| | / /
#  ___/ / / / / /_/ / /_/ / /_/  __/ / / /_/ /  __/| |/ /
# /____/_/ /_/\____/\____/\__/\___/_/ /_____/\___/ |___/
# __project__: lib_mangacollec
# __author__: ShooterDev
# __filename__: author_exceptions.py
# __directory__: src
"""


"""
from domain.execptions.base_exeptions import MangacollecException


class AuthorNotFoundException(MangacollecException):
    def __init__(self, author_id: str):
        super().__init__(f"Author with ID '{author_id}' not found.")