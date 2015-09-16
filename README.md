XiVO confd client
=================
[![Build Status](https://travis-ci.org/xivo-pbx/xivo-confd-client.svg?branch=master)](https://travis-ci.org/xivo-pbx/xivo-confd-client)

A python library for using [xivo-confd](https://github.com/xivo-pbx/xivo-confd)

Usage
=====

The client exposes each resource through groups of commands. Each command group offers the
same basic CRUD operations. A list of available resources can be found in the [confd
docs](http://api.xivo.io). Additional operations are documented futher down in this
README.

To start using the library, first configure a new client, then execute an operation on a
resource.

```python
from xivo_confd_client import Client

c = Client('confd.example.com', https=True, port=9486,
           username='alice', password='s3cre7', auth_method='digest')

users = c.users.list()
```

Each resource offers the following CRUD operations:

list
----

Return a list of items for a resource. You can also pass optional paramters for searching
and sorting such as ```search```, ```sort```, ```order```, ```skip```, ```limit```, etc.
Returns a dict structured as ```{'total': total, 'items': [item1, item2, item3]}```.

```python
users = c.users.list(search='John')
```

get
---

Return a resource item for a given ID.

```python
user_id = 42
user = c.users.get(user_d)
```

create
------

Create a new resource with given parameters.

```python

created_user = c.users.create({'firstname': 'John', 'lastname': 'Doe'})
```

update
------

Update a resource with new parameters. Only the parameters that have changed should be
sent.

```python
user = {'id': 42, 'firstname': 'Johnny'}
c.users.update(user)
```

delete
------

Delete a resource.

```python
user_id = 42
c.users.delete(user_id)
```

Additional operations
=====================

Some resources also offer additional operations:

funckeys
--------

Resource for manipulating funckey templates and their keys.

 * get_template_funckey(template_id, position)
 * update_template_funckey(template_id, position, funckey)
 * delete_template_funckey(template_id, position)

Resource relations
==================

Certain resources can be associated together in order to offer additional functionality.
These associations are known as "relations" in the client. Each resource exposes a subset
of commands for manipulating relations through the ```relations``` method. Consult the
[documentaton](http://api.xivo.io) for a complete list of associations.

```python
#Access relation by using IDs
user_id = 42
line_id = 34
c.users.relations(user_id).add_line(line_id)

#Resource dicts can also be used instead
user = c.users.get(user_id)
line = c.lines_sip.get(line_id)
c.users.relations(user).add_line(line)

#Calling the command group directly is equivalent to .relations()
c.users(user).add_line(line)
```

Here is a list of relations and their methods:

Extension relation
------------------

 * add_line(line)
 * remove_line(line)
 * get_line()

Funckey template relation
----------------

 * add_user(user)
 * remove_user(user)

Line relation
-------------

 * add_user(user)
 * remove_user(user)
 * add_extension(extension)
 * remove_extension(extension)

User relation
-------------

 * add_line(line)
 * remove_line(line)
 * list_lines()
 * add_voicemail(voicemail)
 * remove_voicemail(voicemail)
 * get_voicemail()
 * add_funckey(position, funckey)
 * remove_funckey(position, funckey)
 * get_funckey(position)
 * list_funckeys()
 * add_funckey_template(funckey_template)
 * remove_funckey_template(funckey_template)

Voicemail relation
------------------

 * add_user(user)
 * remove_user(user)
 * remove_users()
 * list_users()


Adding new commands
===================

New command groups can be added to the client by sub-classing ```RESTCommand```.  The new
class must be added to the entry points in setup.py under confd_client.commands.  The name
of the entry point is used as the group name on the client.  For example, commands for the
```Foo``` resource would look like this:

```python
from xivo_lib_rest_client import RESTCommand

class FooCommands(RESTCommand):

    resource = 'foo'

    def bar(self):
        url = "{}/bar".format(self.base_url)
        response = self.session.get(url)

        if response.status_code != 200:
            self.raise_from_response(response)

        return response.json()


#in setup.py

entry_points={
    'confd_client.commands': [
        'foo = package.to.foo:FooCommands'
    ]
}
```

Then, your method ```bar``` would be accessible from the client like this:

```python
c = Client(...)

c.foo.bar()
```
