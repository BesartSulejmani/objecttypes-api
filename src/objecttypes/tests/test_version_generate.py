from django.test import TestCase

from objecttypes.core.models import ObjectVersion
from objecttypes.core.tests.factories import ObjectTypeFactory, ObjectVersionFactory

JSON_SCHEMA = {
    "type": "object",
    "title": "Tree",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "required": ["diameter"],
    "properties": {"diameter": {"type": "integer", "description": "size in cm."}},
}


class GenerateVersionTests(TestCase):
    def test_generate_version_for_new_objecttype(self):
        object_type = ObjectTypeFactory.create()

        object_version = ObjectVersion.objects.create(
            json_schema=JSON_SCHEMA, object_type=object_type
        )

        self.assertEqual(object_version.version, 1)

    def test_generate_version_for_objecttype_with_existed_version(self):
        object_type = ObjectTypeFactory.create()
        ObjectVersionFactory.create(object_type=object_type, version=1)

        object_version = ObjectVersion.objects.create(
            json_schema=JSON_SCHEMA, object_type=object_type
        )

        self.assertEqual(object_version.version, 2)
