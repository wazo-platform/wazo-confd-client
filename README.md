# XiVO confd client
[![Build Status](https://jenkins.wazo.community/buildStatus/icon?job=xivo-confd-client)](https://jenkins.wazo.community/job/xivo-confd-client)

A python library for using [xivo-confd](https://github.com/wazo-pbx/xivo-confd)


# Installation

This library requires python version 2.7. Other versions of python have not been
tested.

## Installing in a virtualenv

It is recommended to install the library in a
[virtualenv](https://virtualenv.readthedocs.org).  A virtualenv isolates python
packages from the rest of the system, hence avoiding conflicts with your OS
package manager. On debian based systems, virtualenv can be install with
apt-get:

    sudo apt-get install python-virtualenv

Afterwards create a virtual environment for the library:

    virtualenv -p /usr/bin/python2 confd-client

When opening a new terminal **do not forget to activate your virtualenv**, otherwise
the library will not be available.

    source confd-client/bin/activate

## Dependencies

We recommend installing dependencies via ```pip```. It will already be available
if you are using a virutalenv. Otherwise, it can be installed via apt-get:

    sudo apt-get install python-pip

Afterwards use the ```requirements.txt``` file for installing dependencies:

    pip install -r requirements.txt

# Usage

The client exposes each resource through command groups. Each group offers the
same CRUD operations. A list of available resources can be found in the [confd
docs](http://api.wazo.community). Additional operations are documented futher down in
this README.

To start using the library, first configure a new client, then execute an
operation on a resource.

```python
from xivo_confd_client import Client

c = Client('confd.example.com', port=9486, https=True, token='the-one-ring')

users = c.users.list()
```

Each resource offers the following CRUD operations:

## list

Return a list of items. You can also pass optional parameters for searching and
sorting such as ```search```, ```sort```, ```order```, ```offset```,
```limit```, etc.  Returns a dict structured as ```{'total': total, 'items':
[item1, item2, item3]}```.

```python
users = c.users.list(search='John')
```

## get

Return an item for a given ID.

```python
user_id = 42
user = c.users.get(user_id)

user_uuid = '2e752722-0864-4665-887d-a78a024cf7c7'
user = c.users.get(user_uuid)  // users only
```

## create

Create a new resource item with given parameters.

```python

created_user = c.users.create({'firstname': 'John', 'lastname': 'Doe'})
```

For creation in a specific entity (tenant), add a `tenant_uuid` parameter:

```python

created_user = c.users.create({'firstname': 'John', 'lastname': 'Doe', 'tenant_uuid': 'my-tenant-uuid'})
```

## update

Update a resource item with given parameters. Only the parameters that need to
be updated should be sent. The parameters dict **MUST** contain the id of the
item that needs to be updated.

```python
user = {'id': 42, 'firstname': 'Johnny'}
c.users.update(user)
```

## delete

Delete a resource item.

```python
user_id = 42
c.users.delete(user_id)
```

# Additional operations

Some resources also offer additional operations:

## devices

Resource for managing devices, such as SIP or SCCP phones

```python

#Reset a device in autoprov mode
c.devices.autoprov(device_id)

#Synchronize the configuratuon of a device
c.devices.synchronize(device_id)
```

## funckeys

Resource for manipulating funckey templates and their keys.

```python
#Get the funckey inside a template for a given position
c.funckeys.get_template_funckey(template_id, position)

#Update a funckey inside a template
c.funckeys.update_template_funckey(template_id, position, funckey)

#Remove a funckey from a template
c.funckeys.delete_template_funckey(template_id, position)
```

## users

Resource to check if user exists
```
user_exists = c.users.exist('52d99c78-4f67-47da-90dd-aeba32afd251')
```

Resource for managing user accounts

```
#Mass import users using CSV data
csvdata = """firstname,lastname
John,Smith
"""

c.users.import_csv(csvdata, encoding='utf-8', timeout=300)

#Mass update users using CSV data
csvdata = """uuid,firstname,lastname
52d99c78-4f67-47da-90dd-aeba32afd251,John,Smith
"""

c.users.update_csv(csvdata, encoding='utf-8', timeout=300)

#Mass export users in CSV format
csvdata = c.users.export_csv()

#Get SIP endpoint of main line for a user
user_uuid = '52d99c78-4f67-47da-90dd-aeba32afd251'
endpoint_sip = users.get_main_endpoint_sip(user_uuid)
```


## sounds

Resource for managing files
```
#Get sound file
binary_content = c.sounds.download_file(category, file_name, format=format, language=language)

#Upload sound file
c.sounds.upload_file(category, file_name, binary_content, format=format, language=language)

#Delete sound file
c.sounds.delete_file(category, file_name, format=format, language=language)
```


# Resource relations

Certain resources can be associated together in order to offer additional
functionality.  These associations are known as "relations". Each resource
exposes a subset of commands for manipulating relations through the
```relations``` method. Consult the [confd documentaton](http://api.wazo.community) for
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

## Call Filter Relation

Exposed via ```c.call_filters.relations(call_filter_id)```

 * update_fallbacks(fallbacks)
 * update_user_recipients(users)
 * update_user_surrogates(users)


## Call Pickup Relation

Exposed via ```c.call_pickups.relations(call_pickup_id)```

 * update_group_interceptors(groups)
 * update_group_targets(groups)
 * update_user_interceptors(users)
 * update_user_targets(users)


## Call Permission Relation

Exposed via ```c.call_permissions.relations(call_permission_id)```

 * add_user(user_id)
 * remove_user(user_id)
 * list_users()

## Conference relation

Exposed via ```c.conferences.relations(conference_id)```

 * add_extension(extension)
 * remove_extension(extension)

## Context relation

Exposed via ```c.contexts.relations(context_id)```

 * update_contexts(contexts)

## CtiProfile relation

Exposed via ```c.cti_profiles.relations(cti_profile_id)```

 * add_user(user)

## Device Relation

Exposed via ```c.devices.relations(device_id)```

 * add_line(line_id)
 * remove_line(line_id)
 * list_lines()

## Endpoint SIP relation

Exposed via ```c.endpoints_sip.relations(endpoint_id)```

 * associate_line(line)
 * dissociate_line(line)
 * get_line()
 * get_trunk()

## Endpoint SCCP relation

Exposed via ```c.endpoints_sccp.relations(endpoint_id)```

 * associate_line(line)
 * dissociate_line(line)
 * get_line()

## Endpoint Custom relation

Exposed via ```c.endpoints_custom.relations(endpoint_id)```

 * associate_line(line)
 * dissociate_line(line)
 * get_line()
 * get_trunk()

## Extension relation

Exposed via ```c.extensions.relations(extension_id)```

 * add_line(line)
 * remove_line(line)
 * get_line()
 * list_lines()

## Extension feature relation

Exposed via ```c.extensions_features.relations(extension_id)```

## Funckey template relation

Exposed via ```c.funckeys.relations(template_id)```

 * add_user(user)
 * remove_user(user)

## Group relation

Exposed via ```c.groups.relations(group_id)```

 * add_extension(extension)
 * remove_extension(extension)
 * update_extensions_members(extensions)
 * update_user_members(users)

 * update_fallbacks(fallbacks)
 * list_fallbacks()

 * add_schedule(schedule)
 * remove_schedule(schedule)

 * add_call_permission(call_permission)
 * remove_call_permission(call_permission)

## Incall relation

Exposed via ```c.incalls.relations(incall_id)```

 * add_extension(extension)
 * remove_extension(extension)
 * add_schedule(schedule)
 * remove_schedule(schedule)

## Line relation

Exposed via ```c.lines.relations(line_id)```

 * add_user(user)
 * remove_user(user)
 * list_users()
 * add_extension(extension)
 * remove_extension(extension)
 * list_extensions()
 * add_endpoint_sip(endpoint_sip)
 * remove_endpoint_sip(endpoint_sip)
 * get_endpoint_sip()
 * add_endpoint_sccp(endpoint_sccp)
 * remove_endpoint_sccp(endpoint_sccp)
 * get_endpoint_sccp()
 * add_endpoint_custom(endpoint_custom)
 * remove_endpoint_custom(endpoint_custom)
 * get_endpoint_custom()
 * add_device(device_id)
 * remove_device(device_id)
 * get_device()

## Outcall relation

Exposed via ```c.outcalls.relations(outcall_id)```

 * update_trunks(trunks)
 * add_extension(extension, prefix='123', external_prefix='456', strip_digits=2, caller_id='toto')
 * remove_extension(extension)
 * add_schedule(schedule)
 * remove_schedule(schedule)
 * add_call_permission(call_permission)
 * remove_call_permission(call_permission)

## Paging relation

Exposed via ```c.pagings.relations(paging_id)```

 * update_user_members(users)
 * update_user_callers(users)

## Parking Lot relation

Exposed via ```c.parking_lots.relations(parking_lot_id)```

 * add_extension(extension)
 * remove_extension(extension)


## Queue relation

Exposed via ```c.queues.relations(queue_id)```

 * add_extension(extension)
 * remove_extension(extension)

 * update_fallbacks(fallbacks)
 * list_fallbacks()

 * add_schedule(schedule)
 * remove_schedule(schedule)

 * add_agent_member(agent, priority, penalty)
 * remove_agent_member(agent)
 * add_user_member(agent, priority)
 * remove_user_member(user)


## Register IAX relation

Exposed via ```c.registers_iax.relations(register_iax_id)```


## Register SIP relation

Exposed via ```c.registers_sip.relations(register_sip_id)```


## Switchboard relation

Exposed via ```c.switchboards.relations(switchboard_id)```

 * update_user_members(users)

## Trunk relation

Exposed via ```c.trunks.relations(trunk_id)```

 * add_endpoint_sip(endpoint_sip)
 * remove_endpoint_sip(endpoint_sip)
 * get_endpoint_sip()
 * add_endpoint_iax(endpoint_iax)
 * remove_endpoint_iax(endpoint_iax)
 * add_endpoint_custom(endpoint_custom)
 * remove_endpoint_custom(endpoint_custom)
 * get_endpoint_custom()
 * add_register_sip(register_sip)
 * remove_register_sip(register_sip)
 * add_register_iax(register_iax)
 * remove_register_iax(register_iax)

## User relation

Exposed via ```c.users.relations(user_id)```

 * add_line(line)
 * remove_line(line)
 * list_lines()
 * update_lines(lines)

 * add_call_permission(call_permission)
 * remove_call_permission(call_permission)
 * list_call_permissions()

 * add_voicemail(voicemail)
 * remove_voicemail()
 * get_voicemail()

 * add_funckey(position, funckey)
 * update_funckey(position, funckey)
 * remove_funckey(position, funckey)
 * get_funckey(position)
 * list_funckeys()
 * update_funckeys(funckeys)
 * add_funckey_template(funckey_template)
 * remove_funckey_template(funckey_template)

 * add_cti_profile(cti_profile)
 * disable_cti_profile()
 * get_cti_profile()
 * update_cti_profile(cti_profile, enabled)

 * get_entity()

 * add_agent(agent)
 * remove_agent()
 * get_agent()

 * update_service(service_name, service)
 * get_service(service_name)
 * update_services(services)
 * list_services()

 * update_forward(forward_name, forward)
 * get_forward(forward_name)
 * update_forwards(forwards)
 * list_forwards()

 * get_endpoint_sip(line_id)

 * update_fallbacks(fallbacks)
 * list_fallbacks()

 * update_groups(groups)

 * add_schedule(schedule)
 * remove_schedule(schedule)


## Voicemail relation

Exposed via ```c.voicemails.relations(voicemail_id)```

 * add_user(user)
 * remove_user(user)
 * remove_users()
 * list_users()


# Other resources

Some resources do not expose CRUD methods. This section
documents which operations are available for other resources.

## infos

```python
#Get information about server
info = c.infos.get()
```

## configuration

```python
#Get status of live reload
live_reload_status = c.configuration.live_reload.get()

#Update live reload configuration
c.configuration.live_reload.update({'enabled': True})
```

## timezones

```python
#Get available timezones
timezones = c.timezones.list()
```


## sounds languages

```python
#Get available sounds languages
sounds_languages = c.sounds_languages.list()
```


## voicemail zonemessages

```python
#Get voicemail zonemessages configuration
voicemail_zonemessages = c.voicemail_zonemessages.get()

#Update voicemail zonemessages configuration
c.voicemail_zonemessages.update(voicemail_zonemessages)
```


## voicemail general

```python
#Get Voicemail general configuration
voicemail_general = c.voicemail_general.get()

#Update Voicemail general configuration
c.voicemail_general.update(voicemail_general)
```


## sccp general

```python
#Get SCCP general configuration
sccp_general = c.sccp_general.get()

#Update SCCP general configuration
c.sccp_general.update(sccp_general)
```


## sip general

```python
#Get SIP general configuration
sip_general = c.sip_general.get()

#Update SIP general configuration
c.sip_general.update(sip_general)
```


## iax callnumberlimits

```python
#Get IAX callnumberlimits configuration
iax_callnumberlimits = c.iax_callnumberlimits.get()

#Update IAX callnumberlimits configuration
c.iax_callnumberlimits.update(iax_callnumberlimits)
```


## iax general

```python
#Get IAX general configuration
iax_general = c.iax_general.get()

#Update IAX general configuration
c.iax_general.update(iax_general)
```

## confbridge

```python
#Get ConfBridge wazo_default_bridge configuration
wazo_default_bridge = c.confbridge_wazo_default_bridge.get()

#Update ConfBridge wazo_default_bridge configuration
c.confbridge_wazo_default_bridge.update(wazo_default_bridge)

#Get ConfBridge wazo_default_user configuration
wazo_default_user = c.confbridge_wazo_default_user.get()

#Update ConfBridge wazo_default_user configuration
c.confbridge_wazo_default_user.update(wazo_default_user)
```


## features

```python
#Get Features applicationmap configuration
applicationmap = c.features_applicationmap.get()

#Update Features applicationmap configuration
c.features_applicationmap.update(applicationmap)

#Get Features featuremap configuration
featuremap = c.features_featuremap.get()

#Update Features featuremap configuration
c.features_featuremap.update(featuremap)

#Get Features general configuration
general = c.features_general.get()

#Update Features general configuration
c.features_featuremap.update(general)
```


## wizard

```python
#Pass the wizard
c.wizard.create(wizard)

#Get the Wazo configuration status
configured = c.wizard.get()

#Get informations about the system on which xivo-confd is installed
discover = c.wizard.discover()
```

# Adding new commands

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


# Changelog

## 1.1.1

* Remove argument auth_method from xivo_confd_client.Client. Auth method is
always digest.


# Unit-tests

## Running unit tests

```
apt-get install libpq-dev python-dev libffi-dev libyaml-dev
pip install tox
tox --recreate -e py27
```
