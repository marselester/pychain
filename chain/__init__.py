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
    _api_path_collection = 'webhooks'
    _api_path_single = 'webhooks/{webhook_id}'

    def __init__(self, id_):
        self.id_ = id_
        self.url = None

    def save(self):
        data = {
            'url': self.url
        }
        path = self._api_path_single.format(webhook_id=self.id_)
        return rest('put', path, data=data)

    def delete(self):
        path = self._api_path_single.format(webhook_id=self.id_)
        return rest('delete', path)

    @classmethod
    def create(cls, url, id_=None):
        data = {
            'url': url
        }
        if id_ is not None:
            data['id'] = id_
        return rest('post', cls._api_path_collection, data=data)


class WebhookEvent(object):
    _api_path_collection = 'webhooks/{webhook_id}/events'

    @classmethod
    def create(cls, webhook_id, event, block_chain, address, confirmations=None):
        data = {
            'webhook_id': webhook_id,
            'event': event,
            'block_chain': block_chain,
            'address': address
        }
        if confirmations is not None:
            data['confirmations'] = confirmations
        path = cls._api_path_collection.format(webhook_id=webhook_id)
        return rest('post', path, data=data)
