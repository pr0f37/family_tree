import abc
import json

from family_tree.model.person import Person


class View(abc.ABC):
    @abc.abstractmethod
    def visualize(person: Person):
        pass


class JsonView(View):
    def to_dict(self, person: Person) -> dict():
        dictionary = {"name": person.name, "age": person.age, "spouse": None}
        if person.spouse:
            dictionary["spouse"] = {
                "name": person.spouse.name,
                "age": person.spouse.age,
                "children": [self.to_dict(child) for child in person.spouse.children],
            }
        dictionary["children"] = [self.to_dict(child) for child in person.children]
        return dictionary

    def visualize(self, person: Person):
        dict_person = self.to_dict(person)
        return json.dumps(dict_person, indent=4)
