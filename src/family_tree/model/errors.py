class PersonError(Exception):
    def __init__(self, msg=None, *args: object) -> None:
        super().__init__(*args)
        self.msg = msg


class AlreadyMarriedError(PersonError):
    pass


class UnderageError(PersonError):
    pass


class ChildOlderThanParentError(PersonError):
    pass
