from flask import Blueprint
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher
from .schema import TeachersSchema


principal_teachers_resources = Blueprint('principal_teachers_resources', __name__)

@principal_teachers_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of teachers"""
    teachers_resources = Teacher.get_all_teachers()
    teachers_resources_dump = TeachersSchema().dump(teachers_resources, many=True)
    return APIResponse.respond(data=teachers_resources_dump)