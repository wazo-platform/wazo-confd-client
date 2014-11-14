XiVO confd client
=================

A python library to connect to xivo-confd

Usage:

```python
from xivo_confd_client import Client

c = Client('confd.example.com', port=9487, version='1.1')

users = c.users.list()
```


## How to implement a new command

Someone trying to implement a new command to the client would have to implement
a new class sub-classing the BaseHTTPCommand. The new class must be in the
setup.py in the entry points under confd_client.commands. The name of the entry
point is used as the handle on the client. For example, if you new entry point
entry looks like this:

```python
entry_points={
    'confd_client.commands': [
        'foo = package.to.foo:FooCommand'
    ]
}
```

your command will be accessible from the client like this:

```python
c = Client(...)

c.foo.bar()  # bar is a method of the FooCommand class
```

Each method of a command will receive a *requests* session and the *args and
**kwargs. The method is responsible of doing the HTTP request on the session
unserialize the response and handle error cases.
