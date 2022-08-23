import uuid

from qiita_given_when_then.status import Status


class Task:
    """ タスク
    """

    __id: str
    __name: str
    __current_status: Status

    __status_transition_rules: dict[Status, Status] = {
        Status.Open: Status.Confirm,        # Open → Confirm
        Status.Confirm: Status.Inprogress,  # Confirm → Inprogress
        Status.Inprogress: Status.Resolve,  # Inprogress → Resolve
        Status.Resolve: Status.Close,       # Resolve → Close
    }

    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def status(self) -> Status:
        return self.__current_status

    def __init__(self, id: str, name: str, status: Status) -> None:
        self.__id = id
        self.__name = name
        self.__current_status = status

    @classmethod
    def create(cls, name: str) -> "Task":
        if name is None:
            raise ValueError()

        return Task(str(uuid.uuid4()), name, Status.Open)

    def next_status(self) -> None:

        if self.__current_status == Status.Close:
            raise Exception()

        next_status = self.__status_transition_rules[self.__current_status]
        self.__current_status = next_status
