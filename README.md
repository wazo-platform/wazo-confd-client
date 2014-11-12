XiVO confd client
=================

A python library to connect to xivo-confd

Usage:

```python
from xivo_confd_client import Client

c = Client('confd.example.com', port=9487, version='1.1')

users = c.users.list()
```
