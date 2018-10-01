from unittest import TestCase

from interscity_client import platform, exceptions


class TestPlatform(TestCase):
    def test_resource_builder_happy_path(self):
        conn = platform.connection()
        builder = platform.resource_builder(connection=conn,
            capability="temperature", uniq_key="region")
        self.assertTrue(builder.resources == {})
        builder.register("Pinheiros", "Sensor em Pinheiros", ["temperature"])
        self.assertTrue("Pinheiros" in builder.resources.keys())
        builder.send_data("Pinheiros", {"temperature": 25})


    def test_resource_send_data_without_registering(self):
        conn = platform.connection()
        builder = platform.resource_builder(connection=conn,
            capability="temperature", uniq_key="region")
        self.assertTrue("PinheirosZZ" not in builder.resources.keys())
        with self.assertRaises(exceptions.ResourceDoesNotExistLocally):
            builder.send_data("PinheirosZZ", {"temperature": 25})
        with self.assertRaises(exceptions.ResourceDoesNotExistRemotelly):
            resource = {
                "uniq_key": "PinheirosZZ",
                "description": "My sensor",
                "capabilities": ["temperature"],
                "lat": -23,
                "lon": -46,
                "status": "active"
            }
            builder.register_locally(resource)
            builder.send_data("PinheirosZZ", {"temperature": 25})


    def test_resource_without_capability(self):
        conn = platform.connection()
        builder = platform.resource_builder(connection=conn,
            capability="myweirdcap", uniq_key="region")
        with self.assertRaises(exceptions.CapabilityDoesNotExist):
            builder.register("Pinheiros", "Sensor em Pinheiros", ["myweirdcap"])
