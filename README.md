XiVO confd client
=================
[![Build Status](https://travis-ci.org/xivo-pbx/xivo-confd-client.svg?branch=master)](https://travis-ci.org/xivo-pbx/xivo-confd-client)

A python library to connect to xivo-confd.

Usage:

```python
from xivo_confd_client import Client

c = Client('confd.example.com', port=9486, version='1.1', username='alice', password='s3cre7', timeout=3)

users = c.users.list()

templates = c.funckeys.list_templates()
template = c.funckeys.get_template(id)
c.funckeys.create_template(data)
c.funckeys.delete_template(id)

fk = c.funckeys.get_template_funckey(template_id, position)
c.funckeys.delete_template_funckey(template_id, position)
c.funckeys.update_template_funckey(template_id, position, data)
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
