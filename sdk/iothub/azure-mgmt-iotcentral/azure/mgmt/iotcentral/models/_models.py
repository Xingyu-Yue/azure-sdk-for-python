# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class Resource(msrest.serialization.Model):
    """The common properties of an ARM resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The ARM resource identifier.
    :vartype id: str
    :ivar name: The ARM resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :param location: Required. The resource location.
    :type location: str
    :param tags: A set of tags. The resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True, 'pattern': r'^(?![0-9]+$)(?!-)[a-zA-Z0-9-]{2,99}[a-zA-Z0-9]$'},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = kwargs['location']
        self.tags = kwargs.get('tags', None)


class App(Resource):
    """The IoT Central application.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The ARM resource identifier.
    :vartype id: str
    :ivar name: The ARM resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :param location: Required. The resource location.
    :type location: str
    :param tags: A set of tags. The resource tags.
    :type tags: dict[str, str]
    :param sku: Required. A valid instance SKU.
    :type sku: ~azure.mgmt.iotcentral.models.AppSkuInfo
    :ivar application_id: The ID of the application.
    :vartype application_id: str
    :param display_name: The display name of the application.
    :type display_name: str
    :param subdomain: The subdomain of the application.
    :type subdomain: str
    :param template: The ID of the application template, which is a blueprint that defines the
     characteristics and behaviors of an application. Optional; if not specified, defaults to a
     blank blueprint and allows the application to be defined from scratch.
    :type template: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True, 'pattern': r'^(?![0-9]+$)(?!-)[a-zA-Z0-9-]{2,99}[a-zA-Z0-9]$'},
        'type': {'readonly': True},
        'location': {'required': True},
        'sku': {'required': True},
        'application_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'AppSkuInfo'},
        'application_id': {'key': 'properties.applicationId', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'subdomain': {'key': 'properties.subdomain', 'type': 'str'},
        'template': {'key': 'properties.template', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(App, self).__init__(**kwargs)
        self.sku = kwargs['sku']
        self.application_id = None
        self.display_name = kwargs.get('display_name', None)
        self.subdomain = kwargs.get('subdomain', None)
        self.template = kwargs.get('template', None)


class AppAvailabilityInfo(msrest.serialization.Model):
    """The properties indicating whether a given IoT Central application name or subdomain is available.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name_available: The value which indicates whether the provided name is available.
    :vartype name_available: bool
    :ivar reason: The reason for unavailability.
    :vartype reason: str
    :ivar message: The detailed reason message.
    :vartype message: str
    """

    _validation = {
        'name_available': {'readonly': True},
        'reason': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AppAvailabilityInfo, self).__init__(**kwargs)
        self.name_available = None
        self.reason = None
        self.message = None


class AppListResult(msrest.serialization.Model):
    """A list of IoT Central Applications with a next link.

    :param next_link: The link used to get the next page of IoT Central Applications.
    :type next_link: str
    :param value: A list of IoT Central Applications.
    :type value: list[~azure.mgmt.iotcentral.models.App]
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[App]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AppListResult, self).__init__(**kwargs)
        self.next_link = kwargs.get('next_link', None)
        self.value = kwargs.get('value', None)


class AppPatch(msrest.serialization.Model):
    """The description of the IoT Central application.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param tags: A set of tags. Instance tags.
    :type tags: dict[str, str]
    :param sku: A valid instance SKU.
    :type sku: ~azure.mgmt.iotcentral.models.AppSkuInfo
    :ivar application_id: The ID of the application.
    :vartype application_id: str
    :param display_name: The display name of the application.
    :type display_name: str
    :param subdomain: The subdomain of the application.
    :type subdomain: str
    :param template: The ID of the application template, which is a blueprint that defines the
     characteristics and behaviors of an application. Optional; if not specified, defaults to a
     blank blueprint and allows the application to be defined from scratch.
    :type template: str
    """

    _validation = {
        'application_id': {'readonly': True},
    }

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'AppSkuInfo'},
        'application_id': {'key': 'properties.applicationId', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'subdomain': {'key': 'properties.subdomain', 'type': 'str'},
        'template': {'key': 'properties.template', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AppPatch, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.sku = kwargs.get('sku', None)
        self.application_id = None
        self.display_name = kwargs.get('display_name', None)
        self.subdomain = kwargs.get('subdomain', None)
        self.template = kwargs.get('template', None)


class AppSkuInfo(msrest.serialization.Model):
    """Information about the SKU of the IoT Central application.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the SKU. Possible values include: "F1", "S1", "ST0", "ST1",
     "ST2".
    :type name: str or ~azure.mgmt.iotcentral.models.AppSku
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AppSkuInfo, self).__init__(**kwargs)
        self.name = kwargs['name']


class AppTemplate(msrest.serialization.Model):
    """IoT Central Application Template.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar manifest_id: The ID of the template.
    :vartype manifest_id: str
    :ivar manifest_version: The version of the template.
    :vartype manifest_version: str
    :ivar name: The name of the template.
    :vartype name: str
    :ivar title: The title of the template.
    :vartype title: str
    :ivar order: The order of the template in the templates list.
    :vartype order: float
    :ivar description: The description of the template.
    :vartype description: str
    :ivar industry: The industry of the template.
    :vartype industry: str
    :ivar locations: A list of locations that support the template.
    :vartype locations: list[~azure.mgmt.iotcentral.models.AppTemplateLocations]
    """

    _validation = {
        'manifest_id': {'readonly': True},
        'manifest_version': {'readonly': True},
        'name': {'readonly': True},
        'title': {'readonly': True},
        'order': {'readonly': True},
        'description': {'readonly': True},
        'industry': {'readonly': True},
        'locations': {'readonly': True},
    }

    _attribute_map = {
        'manifest_id': {'key': 'manifestId', 'type': 'str'},
        'manifest_version': {'key': 'manifestVersion', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'order': {'key': 'order', 'type': 'float'},
        'description': {'key': 'description', 'type': 'str'},
        'industry': {'key': 'industry', 'type': 'str'},
        'locations': {'key': 'locations', 'type': '[AppTemplateLocations]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AppTemplate, self).__init__(**kwargs)
        self.manifest_id = None
        self.manifest_version = None
        self.name = None
        self.title = None
        self.order = None
        self.description = None
        self.industry = None
        self.locations = None


class AppTemplateLocations(msrest.serialization.Model):
    """IoT Central Application Template Locations.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The ID of the location.
    :vartype id: str
    :ivar display_name: The display name of the location.
    :vartype display_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'display_name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AppTemplateLocations, self).__init__(**kwargs)
        self.id = None
        self.display_name = None


class AppTemplatesResult(msrest.serialization.Model):
    """A list of IoT Central Application Templates with a next link.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param next_link: The link used to get the next page of IoT Central application templates.
    :type next_link: str
    :ivar value: A list of IoT Central Application Templates.
    :vartype value: list[~azure.mgmt.iotcentral.models.AppTemplate]
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[AppTemplate]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AppTemplatesResult, self).__init__(**kwargs)
        self.next_link = kwargs.get('next_link', None)
        self.value = None


class CloudErrorBody(msrest.serialization.Model):
    """Details of error response.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The target of the particular error.
    :vartype target: str
    :param details: A list of additional details about the error.
    :type details: list[~azure.mgmt.iotcentral.models.CloudErrorBody]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[CloudErrorBody]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CloudErrorBody, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = kwargs.get('details', None)


class Operation(msrest.serialization.Model):
    """IoT Central REST API operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Operation name: {provider}/{resource}/{read | write | action | delete}.
    :vartype name: str
    :param display: The object that represents the operation.
    :type display: ~azure.mgmt.iotcentral.models.OperationDisplay
    :ivar origin: The intended executor of the operation.
    :vartype origin: str
    :ivar properties: Additional descriptions for the operation.
    :vartype properties: str
    """

    _validation = {
        'name': {'readonly': True},
        'origin': {'readonly': True},
        'properties': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.display = kwargs.get('display', None)
        self.origin = None
        self.properties = None


class OperationDisplay(msrest.serialization.Model):
    """The object that represents the operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar provider: Service provider: Microsoft IoT Central.
    :vartype provider: str
    :ivar resource: Resource Type: IoT Central.
    :vartype resource: str
    :ivar operation: Name of the operation.
    :vartype operation: str
    :ivar description: Friendly description for the operation,.
    :vartype description: str
    """

    _validation = {
        'provider': {'readonly': True},
        'resource': {'readonly': True},
        'operation': {'readonly': True},
        'description': {'readonly': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = None
        self.resource = None
        self.operation = None
        self.description = None


class OperationInputs(msrest.serialization.Model):
    """Input values.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the IoT Central application instance to check.
    :type name: str
    :param type: The type of the IoT Central resource to query.
    :type type: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationInputs, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.type = kwargs.get('type', "IoTApps")


class OperationListResult(msrest.serialization.Model):
    """A list of IoT Central operations. It contains a list of operations and a URL link to get the next set of results.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param next_link: The link used to get the next page of IoT Central description objects.
    :type next_link: str
    :ivar value: A list of operations supported by the Microsoft.IoTCentral resource provider.
    :vartype value: list[~azure.mgmt.iotcentral.models.Operation]
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[Operation]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.next_link = kwargs.get('next_link', None)
        self.value = None