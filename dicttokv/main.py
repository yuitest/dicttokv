# coding: utf-8
from __future__ import unicode_literals, print_function


class DictToKeyValue(object):

    @classmethod
    def from_object(cls, target, prefixes=()):
        if isinstance(target, dict):
            for key, value in target.iteritems():
                for i in cls.from_object(value, prefixes + (key, )):
                    yield i

        elif isinstance(target, (list, tuple)):
            for index, value in enumerate(target):
                for i in cls.from_object(value, prefixes + (index, )):
                    yield i

        else:
            yield (prefixes, target)

    @classmethod
    def keys_to_keystr(cls, keys, delimiter='.', ignore_number=False):
        if ignore_number:
            keys = (unicode(key) for key in keys if not isinstance(key, int))
        else:
            keys = (unicode(key) for key in keys)
        return delimiter.join(keys)

    @classmethod
    def to_tsvlines(cls, target, delimiter='.', ignore_number=False):
        for keys, v in cls.from_object(target):
            yield '{}\t{}'.format(
                cls.keys_to_keystr(keys, delimiter, ignore_number), v)

if __name__ == '__main__':
    import sys
    import json
    obj = json.load(sys.stdin)
    for line in DictToKeyValue.to_tsvlines(obj):
        print(line)
