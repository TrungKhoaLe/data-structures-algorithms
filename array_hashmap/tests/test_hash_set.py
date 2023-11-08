from ..data_structure.hash_set import HashSet
import pytest


@pytest.fixture
def hashset_instance():
    return HashSet()


def test_add_and_contains(hashset_instance):
    hashset_instance.add(1)
    hashset_instance.add(2)

    assert hashset_instance.contains(1)
    assert hashset_instance.contains(2)
    assert not hashset_instance.contains(3)


def test_remove(hashset_instance):
    hashset_instance.add(1)
    hashset_instance.add(2)

    hashset_instance.remove(2)
    assert hashset_instance.contains(1)
    assert not hashset_instance.contains(2)


def test_remove_nonexistence_key(hashset_instance):
    hashset_instance.add(1)
    hashset_instance.add(2)

    with pytest.raises(KeyError):
        hashset_instance.remove(3)
