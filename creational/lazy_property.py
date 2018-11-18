from __future__ import print_function
import functools


class lazy_property:
    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __get__(self, obj, type_):
        if obj is None:
            return self
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val


def lazy_property2(fn):
    attr = '_lazy__' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr):
            setattr(self, attr, fn(self))
        return getattr(self, attr)
    return _lazy_property


class Person():
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self.call_count2 = 0

    @lazy_property
    def relatives(self):
        # Get all relatives, let's assume that it costs much time.
        relatives = 'Many relatives.'
        return relatives

    @lazy_property2
    def parents(self):
        self.call_count2 += 1
        return 'Father and mother'


if __name__ == '__main__':
    Jhon = Person('Jhon', 'Coder')
    print('Name: {0}    Occupation: {1}'.format(Jhon.name, Jhon.occupation))
    print('Before we access `relatives`:')
    print(Jhon.__dict__)
    print('Jhon\'s relatives: {0}'.format(Jhon.relatives))
    print('After we\'ve accessed `relatives`:')
    print(Jhon.__dict__)
    print(Jhon.parents)
    print(Jhon.__dict__)
    print(Jhon.parents)
    print(Jhon.call_count2)

### OUTPUT ###
# Name: Jhon    Occupation: Coder
# Before we access `relatives`:
# {'name': 'Jhon', 'occupation': 'Coder', 'call_count2': 0}
# Jhon's relatives: Many relatives.
# After we've accessed `relatives`:
# {'name': 'Jhon', 'occupation': 'Coder', 'call_count2': 0, 'relatives': 'Many relatives.'}
# Father and mother
# {'name': 'Jhon', 'occupation': 'Coder', 'call_count2': 1, 'relatives': 'Many relatives.', '_lazy__parents': 'Father and mother'}
# Father and mother
# 1