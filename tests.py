import pytest

from collections_hierarchy.node import Node

from collections_hierarchy.concrete_classes import List, Stack
from collections_hierarchy.base_classes import (
    Sequenceable, Appendable, Pushable, Popable)


def test_sequenceable():
    n1 = Node('X')
    n2 = Node('Y')
    n3 = Node('Z')
    n4 = Node('R')
    
    n1.next = n2
    n2.next = n3
    n3.next = n4

    sequence = Sequenceable()
    assert sequence.get_elements() == []
    # Warning. Violating encapsulation
    sequence.start = n1

    assert sequence.get_elements() == ['X', 'Y', 'Z', 'R']


def test_appendable():
    class TestAppendableSequence(Sequenceable, Appendable):
        pass

    sequence = TestAppendableSequence()
    assert sequence.get_elements() == []

    sequence.append('X')
    assert sequence.get_elements() == ['X']

    sequence.append('Y')
    assert sequence.get_elements() == ['X', 'Y']

    sequence.append('Z')
    assert sequence.get_elements() == ['X', 'Y', 'Z']


def test_popable():
    class TestPopableSequence(Sequenceable, Popable):
        pass

    sequence = TestPopableSequence()
    with pytest.raises(IndexError):
        sequence.pop()

    n1 = Node('X')
    n2 = Node('Y')
    n3 = Node('Z')
    n1.next = n2
    n2.next = n3
    sequence.start = n1

    # Preconditions
    assert sequence.get_elements() == ['X', 'Y', 'Z']

    elem = sequence.pop()
    assert elem == 'X'
    assert sequence.get_elements() == ['Y', 'Z']

    elem = sequence.pop()
    assert elem == 'Y'
    assert sequence.get_elements() == ['Z']

    elem = sequence.pop()
    assert elem == 'Z'
    assert sequence.get_elements() == []

    with pytest.raises(IndexError):
        sequence.pop()


def test_pushable():
    class TestPushableSequence(Sequenceable, Pushable, Appendable):
        pass

    sequence = TestPushableSequence()
    assert sequence.get_elements() == []

    sequence.push('C')
    assert sequence.get_elements() == ['C']

    sequence.push('B')
    assert sequence.get_elements() == ['B', 'C']

    sequence.push('A')
    assert sequence.get_elements() == ['A', 'B', 'C']
    
    sequence.append('D')
    assert sequence.get_elements() == ['A', 'B', 'C', 'D']
