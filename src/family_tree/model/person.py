from family_tree.model.errors import (
    AlreadyMarriedError,
    ChildOlderThanParentError,
    UnderageError,
)


class Person:
    def __init__(
        self,
        name: str,
        age: int,
        spouse=None,
        children: list = None,
    ) -> None:
        self.name = name
        self.age = age
        self.spouse = spouse
        if children is None:
            self.children = []

    def __gt__(self, person):
        if self.age > person.age:
            return True
        return False

    def __ge__(self, person):
        if self.age >= person.age:
            return True
        return False

    def __lt__(self, person):
        if self.age < person.age:
            return True
        return False

    def __le__(self, person):
        if self.age <= person.age:
            return True
        return False

    def __eq__(self, person):
        if self.age == person.age:
            return True
        return False

    def __repr__(self) -> str:
        return f"""name: {self.name}, age: {self.age}"""


class FamilyMember(Person):
    def __init__(
        self,
        name: str,
        age: int,
        spouse: Person = None,
        children: list[Person] = None,
    ) -> None:
        super().__init__(
            name=name,
            age=age,
            spouse=None,
            children=None,
        )
        if children is None:
            children = []
        for child in children:
            self.add_child(child)
        if spouse:
            self.marry(spouse)

    def _married(self, person: Person) -> bool:
        if self.spouse or person.spouse:
            return True
        return False

    def marry(self, person: Person) -> None:
        if self._married(person):
            raise AlreadyMarriedError()
        if person.age >= 18 and self.age >= 18:
            self.spouse = person
            person.spouse = self
        else:
            raise UnderageError()

    def add_child(self, person: Person) -> None:
        if self > person:
            self.children.append(person)
            self.children.sort(reverse=True)
        else:
            raise ChildOlderThanParentError(msg="Child older than parent")
