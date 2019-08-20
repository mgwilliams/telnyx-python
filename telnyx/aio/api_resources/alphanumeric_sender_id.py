from telnyx.aio.api_resources.abstract import CreateableAPIResource
from telnyx.aio.api_resources.abstract import DeletableAPIResource
from telnyx.aio.api_resources.abstract import UpdateableAPIResource
from telnyx.aio.api_resources.abstract import ListableAPIResource


class AlphanumericSenderId(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "alphanumeric_sender_id"
