"""
PyChain API library
~~~~~~~~~~~~~~~~~~~

Usage example::

    >>> import chain
    >>> chain.conf.api_key = 'YOUR-KEY'
    >>> chain.conf.api_secret = 'YOUR-SECRET'
    >>> chain.Webhook.create('https://your-server-url.com')

"""
from .requestor import rest
from .exceptions import (
    ChainException, APIConnectionError, APIError, AuthError,
    InvalidRequestError
)


class Webhook(object):
    _api_path = 'webhooks'

    @classmethod
    def create(cls, url, id_=None):
        data = {
            'url': url
        }
        if id_ is not None:
            data['id'] = id_
        return rest('post', cls._api_path, data=data)
