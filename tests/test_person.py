from pytest import raises

from family_tree.model.errors import (
    AlreadyMarriedError,
    ChildOlderThanParentError,
    UnderageError,
)
from family_tree.model.person import FamilyMember, Person


def test_create_person():
    p1 = FamilyMember(name="person1", age=36)
    p2 = FamilyMember(name="person2", age=35, spouse=p1)

    assert p1.spouse is p2
    assert p2.spouse is p1
    assert p1.name == "person1"
    assert p1.age == 36
    assert len(p2.children) == 0


def test_merriage():
    p1 = FamilyMember(name="person1", age=36)
    p2 = FamilyMember(name="person2", age=35)
    p2.marry(p1)

    assert p2.spouse is p1
    assert p1.spouse is p2


def test_marriage_fail():
    p1 = FamilyMember(name="person1", age=16)
    p2 = FamilyMember(name="person2", age=35)
    with raises(UnderageError):
        p2.marry(p1)

    assert p2.spouse is None
    p4 = Person(name="xxx", age=22)
    p3 = Person(name="nnn", age=22, spouse=p4)
    with raises(AlreadyMarriedError):
        p2.marry(p3)

    assert p2.spouse is None


def test_resolve_hierarchy():
    p1 = FamilyMember(name="person1", age=16)
    p2 = FamilyMember(name="person2", age=35)

    assert p1 < p2
    assert p1 <= p2
    assert p2 > p1
    assert p2 >= p1
    assert p2 != p1


def test_add_children():
    father = FamilyMember(name="father", age=35)
    child1 = FamilyMember(name="child1", age=10)
    child2 = FamilyMember(name="child2", age=8)
    father.add_child(child1)
    father.add_child(child2)

    assert father.children == [child1, child2]


def test_add_children_fail():
    father = FamilyMember(name="father", age=35)
    child1 = FamilyMember(name="child1", age=50)

    with raises(ChildOlderThanParentError):
        father.add_child(child1)
    assert len(father.children) == 0
