from enum import Enum
from enum import auto


class Status(Enum):
    """ ステータス
    """

    Open = auto()
    Confirm = auto()
    Inprogress = auto()
    Resolve = auto()
    Close = auto()
