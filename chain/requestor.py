"""
chain.requestor
~~~~~~~~~~~~~~~

This module provides REST request abstraction layer.

"""
from urlparse import urljoin
import json

import requests

from . import conf
from .exceptions import (
    APIConnectionError, APIError, AuthError, InvalidRequestError
)

session = requests.Session()


def rest(method, path, query_params=None, data=None):
    """Makes JSON API request and returns response as dictionary.

    Usage example::

        >>> rest('post', 'webhooks', data={'url': 'https://example.com'})

    """
    headers = {
        'Content-Type': 'application/json'
    }
    if data is not None:
        data = json.dumps(data)
    try:
        resp = session.request(
            method=method,
            url=_api_url(path),
            params=query_params,
            data=data,
            headers=headers,
            auth=(conf.api_key, conf.api_secret)
        )
    except requests.RequestException as exc:
        raise APIConnectionError(exc)

    try:
        json_resp = resp.json()
    except ValueError as exc:
        raise APIError(exc, resp.content, resp.status_code)

    if resp.status_code == 200:
        return json_resp

    error_msg = json_resp.get('message') or json_resp.get('error')
    if resp.status_code in (401, 403):
        raise AuthError(error_msg, resp.content, resp.status_code)
    if resp.status_code in (400, 404):
        raise InvalidRequestError(error_msg, resp.content, resp.status_code)
    raise APIError(error_msg, resp.content, resp.status_code)


def _api_url(path):
    path = path.lstrip('/')
    return urljoin(conf.api_base, path)
