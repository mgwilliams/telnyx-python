from telnyx.aio.api_resources.abstract import UpdateableAPIResource
from telnyx.aio.api_resources.abstract import ListableAPIResource


class ShortCode(ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "short_code"
