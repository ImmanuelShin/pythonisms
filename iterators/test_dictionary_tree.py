import pytest
from dictionary_tree import Treectionary

@pytest.fixture
def tree_dict():
    return Treectionary()

def test_setitem_and_getitem(tree_dict):
    tree_dict['root'] = 10
    assert tree_dict['root'] == 10

def test_delitem(tree_dict):
    tree_dict['root'] = 10
    del tree_dict['root']
    with pytest.raises(KeyError):
        tree_dict['root']

def test_iter(tree_dict):
    tree_dict['root'] = 10
    tree_dict['child1'] = 5
    tree_dict['child2'] = 8

    expected_result = [('root', 10), ('child1', 5), ('child2', 8)]
    assert list(iter(tree_dict)) == expected_result

def test_keys(tree_dict):
    tree_dict['root'] = 10
    tree_dict['child1'] = 5
    tree_dict['child2'] = 8

    expected_keys = ['root', 'child1', 'child2']
    assert tree_dict.keys() == expected_keys

def test_values(tree_dict):
    tree_dict['root'] = 10
    tree_dict['child1'] = 5
    tree_dict['child2'] = 8

    expected_values = [10, 5, 8]
    assert tree_dict.values() == expected_values

def test_pop(tree_dict):
    tree_dict['root'] = 10
    popped_value = tree_dict.pop('root')
    assert popped_value == 10
    with pytest.raises(KeyError):
        tree_dict['root']

def test_pop_with_default(tree_dict):
    default_value = tree_dict.pop('nonexistent_key', 999)
    assert default_value == 999

def test_setdefault(tree_dict):
    tree_dict['root'] = 10
    default_value = tree_dict.setdefault('nonexistent_key', 999)
    assert default_value == 999

def test_setdefault_existing_key(tree_dict):
    tree_dict['root'] = 10
    existing_value = tree_dict.setdefault('root', 999)
    assert existing_value == 10

def test_clear(tree_dict):
    tree_dict['root'] = 10
    tree_dict['child1'] = 5
    tree_dict['child2'] = 8

    tree_dict.clear()
    with pytest.raises(KeyError):
        tree_dict['root']
    assert not tree_dict.keys()
    assert not tree_dict.values()
