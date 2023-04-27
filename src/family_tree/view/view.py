import abc
import json

import drawsvg as draw

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


class SVGView(View):
    WIDTH = 1000
    HEIGHT = 1000

    def _member(self, d: draw.Drawing, person: Person, x0: int, y0: int):
        MEMBER_WIDTH = 150
        MEMBER_HEIGHT = 50
        STROKE_W = 2
        r = draw.Rectangle(
            x0,
            y0,
            MEMBER_WIDTH,
            MEMBER_HEIGHT,
            stroke_width=STROKE_W,
            stroke="black",
            fill="white",
        )
        text = [f"{person}"]
        if person.spouse:
            text.append(f"{person.spouse}")
        t = draw.Text(
            text,
            15,
            x0 + 10,
            y0 + 20,
        )
        d.append(r)
        d.append(t)
        for idx, child in enumerate(person.children):
            self._member(
                d,
                child,
                x0 + MEMBER_WIDTH + 20,
                y0 + MEMBER_HEIGHT * idx,
            )
        return r

    def visualize(self, person: Person):
        d = draw.Drawing(self.WIDTH, self.HEIGHT)
        self._member(d, person, 500, 50)
        d.save_svg("test.svg")
