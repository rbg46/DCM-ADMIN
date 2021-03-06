from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from ..service.doms_service import get_all_domains, save_domain
from ..util.dto import DomainDto

api = DomainDto.api
user_auth = DomainDto.domain


@api.route('/')
class Domains(Resource):
    """
        Domain Resource
    """
    @api.doc('Get All Domains')
    @api.marshal_list_with(user_auth)
    def get(self):
        return get_all_domains()

    @api.doc('Create/Update Domains')
    @api.response(201, 'User successfully created/updated.')
    @api.expect(user_auth, validate=True)
    @api.marshal_with(user_auth)
    def post(self):
        # get the post data
        post_data = request.json
        return save_domain(data=post_data)