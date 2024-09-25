from marshmallow import Schema, EXCLUDE, fields, post_load
from core.models.teachers import Teacher

class TeachersSchema(Schema):
    class Meta:
        model = Teacher
        unknown = EXCLUDE
        include_relationships = True

    id = fields.Integer(required=True, allow_none=False)
    user_id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    @post_load
    def initiate_class(self, data_dict, many, partial):
        # pylint: disable=unused-argument,no-self-use
        return Teacher(**data_dict)

