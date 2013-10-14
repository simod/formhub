
from geonode_formhub.formhub.views import form_save

from restservice.RestServiceInterface import RestServiceInterface


class ServiceDefinition(RestServiceInterface):
    id = u'geonode'
    verbose_name = u'GeoNode save'

    def send(self, url, parsed_instance):

        instance_dict = parsed_instance.to_dict_for_mongo()

        form_save(instance_dict)