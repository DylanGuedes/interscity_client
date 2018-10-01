# InterSCity Client (for Python)

## Installing
```
pip install interscity_client
```

## Usage

**Check if a capability exist**
```python
>>> from interscity_client import platform

>>> conn = platform.connection()
>>> conn.capability_available("temperature")
True
```

**Create new capability**
```python
>>> from interscity_client import platform

>>> conn = platform.connection()
>>> conn.capability_available("temperature")
False
>>> capability_title = "temperature"
>>> description = "São Paulo temperature"
>>> capability_type = "sensor"
>>> conn.create_capability(capability_title, description, capability_type)
True
```

**Get all resources uuids**
```python
>>> from interscity_client import platform

>>> conn = platform.connection()
>>> conn.all_resources_uuid()
["asdf1", "asdf2", "asdf3", ...
```

**Get all resources uuids of specific capability (faster than previous example)**
```python
>>> from interscity_client import platform

>>> conn = platform.connection()
>>> conn.all_resources_uuid(["temperature"])
["temp1", "temp2", "temp3", ...
```

**Get all resources description**
```python
>>> from interscity_client import platform

>>> conn = platform.connection()
>>> conn.all_resources_description(["temperature"])
["Temperatura de Pinheiros", "Temperatura de Vila Madalena", "Temperatura de Consolação", ...
```

**Create a resource**
```python
>>> from interscity_client import platform
>>> conn = platform.connection()
>>> temperature_builder = platform.resource_builder(connection=conn,
    capability="temperature", uniq_key="region")
>>> uniq_sensor = "Pinheiros"
>>> temperature_builder.register(uniq_sensor, "Sensor em "+uniq_sensor, ["temperature"])
>>> temperature_builder.send_data(uniq_sensor, {"temperature": 25})
>>> temperature_builder.send_data(uniq_sensor, {"temperature": 33})
```
