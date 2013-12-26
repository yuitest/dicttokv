# DictToKeyValue

```
pip install dictokv
```

## make flatten nested dictionary or list

```
$ python
>>> from dicttokv import from_object
>>> list(from_object({'a': 'b', 'c': {'d': {'e': {'f': [0, 1, 2]}}}}))
[
    (('a',), 'b'),
    (('c', 'd', 'e', 'f', 0), 0),
    (('c', 'd', 'e', 'f', 1), 1),
    (('c', 'd', 'e', 'f', 2), 2)
]
>>> 
```

## If you need tsv

```
$ python -m dicttokv.main <<< '{"a": 1, "b": {"c": 2}}'
a       1
b.c     2
```
