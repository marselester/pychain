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

    def __init__(self, id):
        self._id = id
        self.url = None

    def __repr__(self):
        return '<chain.Webhook {}>'.format(self.id)

    @property
    def id(self):
        return self._id

    def save(self):
        data = {
            'url': self.url
        }
        path = self._api_path_single.format(webhook_id=self.id)
        json_resp = rest('put', path, data=data)
        self.refresh_from(json_resp)

    def delete(self):
        path = self._api_path_single.format(webhook_id=self.id)
        return rest('delete', path)

    def refresh_from(self, attributes):
        self.url = attributes.get('url')

    def refresh(self):
        path = self._api_path_single.format(webhook_id=self.id)
        json_resp = rest('get', path)
        self.refresh_from(json_resp)

    @classmethod
    def construct_from(cls, attributes):
        webhook = cls(id=attributes.get('id'))
        webhook.refresh_from(attributes)
        return webhook

    @classmethod
    def list(cls):
        json_resp = rest('get', cls._api_path_collection)
        for attributes in json_resp:
            yield cls.construct_from(attributes)

    @classmethod
    def create(cls, url, id=None):
        data = {
            'url': url
        }
        if id is not None:
            data['id'] = id
        json_resp = rest('post', cls._api_path_collection, data=data)
        return cls.construct_from(json_resp)


class WebhookEvent(object):
    _api_path_collection = 'webhooks/{webhook_id}/events'

    def __init__(self, id):
        self._id = id
        self._webhook_id = None
        self._event = None
        self._block_chain = None
        self._address = None
        self._confirmations = None

    @property
    def id(self):
        return self._id

    @property
    def webhook_id(self):
        return self._webhook_id

    @property
    def event(self):
        return self._event

    @property
    def block_chain(self):
        return self._block_chain

    @property
    def address(self):
        return self._address

    @property
    def confirmations(self):
        return self._confirmations

    def refresh_from(self, attributes):
        self._webhook_id = attributes.get('webhook_id')
        self._event = attributes.get('event')
        self._block_chain = attributes.get('block_chain')
        self._address = attributes.get('address')
        self._confirmations = attributes.get('confirmations')

    @classmethod
    def construct_from(cls, attributes):
        webhook_event = cls(id=attributes.get('id'))
        webhook_event.refresh_from(attributes)
        return webhook_event

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
        json_resp = rest('post', path, data=data)
        return cls.construct_from(json_resp)
