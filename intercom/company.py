from intercom.user import Resource
from intercom.api_operations.all import All
from intercom.api_operations.count import Count
from intercom.api_operations.find import Find
from intercom.api_operations.load import Load
from intercom.api_operations.save import Save
from intercom.extended_api_operations.users import Users


class Company(Resource, Count, Find, All, Save, Load, Users):
    update_verb = 'post'
    identity_vars = ['id', 'company_id']
