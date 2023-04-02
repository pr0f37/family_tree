from family_tree.model.person import FamilyMember
from family_tree.view.view import JsonView


def test_visualize():
    father = FamilyMember(name="father", age=35)
    mother = FamilyMember(name="mother", age=30)
    child1 = FamilyMember(name="child1", age=10)
    child2 = FamilyMember(name="child2", age=8)
    child3 = FamilyMember(name="child3", age=4)
    father.marry(mother)
    father.add_child(child1)
    father.add_child(child2)
    child1.add_child(child3)
    view = JsonView()
    assert isinstance(view.visualize(father), str)
