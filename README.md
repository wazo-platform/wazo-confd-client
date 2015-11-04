XiVO confd client
=================
[![Build Status](https://travis-ci.org/xivo-pbx/xivo-confd-client.svg?branch=master)](https://travis-ci.org/xivo-pbx/xivo-confd-client)

A python library for using [xivo-confd](https://github.com/xivo-pbx/xivo-confd)

Usage
=====

The client exposes each resource through command groups. Each group offers the
same CRUD operations. A list of available resources can be found in the [confd
docs](http://api.xivo.io). Additional operations are documented futher down in
this README.

To start using the library, first configure a new client, then execute an
operation on a resource.

```python
from xivo_confd_client import Client

c = Client('confd.example.com',
           https=True,
           port=9486,
           username='alice',
           password='s3cre7')
c = Client('confd.example.com', port=9486, https=True, token='the-one-ring')

users = c.users.list()
```

Each resource offers the following CRUD operations:

list
----

Return a list of items. You can also pass optional paramters for searching and
sorting such as ```search```, ```sort```, ```order```, ```offset```,
```limit```, etc.  Returns a dict structured as ```{'total': total, 'items':
[item1, item2, item3]}```.

```python
users = c.users.list(search='John')
```

get
---

Return an item for a given ID.

```python
user_id = 42
user = c.users.get(user_id)

user_uuid = '2e752722-0864-4665-887d-a78a024cf7c7'
user = c.users.get(user_uuid)  // users only
```

create
------

Create a new resource item with given parameters.

```python

created_user = c.users.create({'firstname': 'John', 'lastname': 'Doe'})
```

update
------

Update a resource item with given parameters. Only the parameters that need to
be updated should be sent. The parameters dict **MUST** contain the id of the
item that needs to be updated.

```python
user = {'id': 42, 'firstname': 'Johnny'}
c.users.update(user)
```

delete
------

Delete a resource item.

```python
user_id = 42
c.users.delete(user_id)
```

Additional operations
=====================

Some resources also offer additional operations:

devices
-------

Resource for managing devices, such as SIP or SCCP phones

```python

#Reset a device in autoprov mode
c.devices.autoprov(device_id)

#Synchronize the configuratuon of a device
c.devices.synchronize(device_id)
```

funckeys
--------

Resource for manipulating funckey templates and their keys.

```python
#Get the funckey inside a template for a given position
c.funckeys.get_template_funckey(template_id, position)

#Update a funckey inside a template
c.funckeys.update_template_funckey(template_id, position, funckey)

#Remove a funckey from a template
c.funckeys.delete_template_funckey(template_id, position)
```

Resource relations
==================

Certain resources can be associated together in order to offer additional
functionality.  These associations are known as "relations". Each resource
exposes a subset of commands for manipulating relations through the
```relations``` method. Consult the [confd documentaton](http://api.xivo.io) for
a complete list of associations.

```python
#Access relation by using IDs
user_id = 42
line_id = 34
c.users.relations(user_id).add_line(line_id)

user = c.users.get(user_id)
line = c.lines_sip.get(line_id)

#dicts can also be used instead of IDs
c.users.relations(user).add_line(line)

#Calling the command group directly is equivalent to calling .relations()
c.users(user).add_line(line)
```

Here is a list of relations and their methods:

CtiProfile relation
-------------------

Exposed via ```c.cti_profiles.relations(cti_profile_id)```

 * add_user(user)

Extension relation
------------------

Exposed via ```c.extensions.relations(extension_id)```

 * add_line(line)
 * remove_line(line)
 * get_line()

Funckey template relation
----------------

Exposed via ```c.funckeys.relations(template_id)```

 * add_user(user)
 * remove_user(user)

Line relation
-------------

Exposed via ```c.lines.relations(line_id)```

 * add_user(user)
 * remove_user(user)
 * list_users()
 * add_extension(extension)
 * remove_extension(extension)

User relation
-------------

Exposed via ```c.users.relations(user_id)```

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
 * add_cti_profile(cti_profile)
 * disable_cti_profile()
 * get_cti_profile()

Voicemail relation
------------------

Exposed via ```c.voicemails.relations(voicemail_id)```

 * add_user(user)
 * remove_user(user)
 * remove_users()
 * list_users()


Other resources
===============

Some resources do not expose CRUD methods. This section
documents which operations are available for other resources.

infos
-----

```python
#Get information about server
info = c.infos.get()
```

configuration
-------------

```python
#Get status of live reload
live_reload_status = c.configuration.live_reload.get()

#Update live reload configuration
c.configuration.live_reload.update({'enabled': True})
```

queues
------

```python
# Add agent to a queue
c.queues.add_agent(queue_id, agent_id, penalty=0)

#Remove agent from a queue
c.queues.remove_agent(queue_id, agent_id)

#Get membership info for an agent in a queue
c.queues.get_membership(queue_id, agent_id)

#Update penalty for an agent in a queue
c.queues.edit_membership(penalty)
```


Adding new commands
===================

New command groups can be added to the client by sub-classing ```RESTCommand```.
The new class must be added to the entry points in ```setup.py``` under
```confd_client.commands```.  The name of the entry point is used as name for
the group in the client. For example, commands for the ```Foo``` resource would look
like this:

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

Then, your method ```bar``` would be used like this:

```python
c = Client(...)

c.foo.bar()
```


Changelog
=========

1.1.1
-----

* Remove argument auth_method from xivo_confd_client.Client. Auth method is
always digest.
