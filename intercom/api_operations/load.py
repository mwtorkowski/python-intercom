from intercom import Intercom
from intercom import utils


class Load(object):

    @classmethod
    def load(cls, **params):
        collection = utils.resource_class_to_collection_name(cls)
        if 'id' in params:
            response = Intercom.get("/%s/%s" % (collection, params['id']))
        else:
            raise Exception(
                "Cannot load %s as it does not have a valid id." % (cls))
        return cls(**response)