from typing import Any

from marshmallow import Schema, ValidationError, fields, validates_schema

VALID_CMD_COMMANDS = ('filter', 'unique', 'map', 'limit', 'sort')


class RequestSchema(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str()

    @validates_schema
    def check_all_cmd_valid(self, values: dict[str, str], *args: Any, **kwargs: Any):
        if values['cmd'] not in VALID_CMD_COMMANDS:
            raise ValidationError('"cmd" contains invalid value')


class BatchRequestSchema(Schema):
    queries = fields.Nested(RequestSchema, many=True)