from telnyx.aio.api_resources.abstract import CreateableAPIResource
from telnyx.aio.api_resources.abstract import DeletableAPIResource
from telnyx.aio.api_resources.abstract import ListableAPIResource


class APIKey(CreateableAPIResource, ListableAPIResource, DeletableAPIResource):
    OBJECT_NAME = "api_key"
