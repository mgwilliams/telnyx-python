from telnyx.aio.api_resources.abstract import UpdateableAPIResource
from telnyx.aio.api_resources.abstract import ListableAPIResource


class MessagingPhoneNumber(ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "messaging_phone_number"
