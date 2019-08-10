from __future__ import absolute_import, division, print_function

from telnyx import util
from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods(
    "alphanumeric_sender_id", path="alphanumeric_sender_id", operations=["create"]
)
@nested_resource_class_methods(
    "number_pool", path="number_pool", operations=["create"]
)
class Message(CreateableAPIResource):
    OBJECT_NAME = "message"

    @classmethod
    def send_from_alphanumeric_sender_id(cls, **params):
        params = util.rewrite_reserved_words(params)
        return Message.create_alphanumeric_sender_id(None, **params)

    @classmethod
    def send_using_number_pool(cls, **params):
        params = util.rewrite_reserved_words(params)
        return Message.create_number_pool(None, **params)
