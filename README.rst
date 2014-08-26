=======
PyChain
=======

PyChain is a Python API client for Chain.com_.

Usage example:

.. code-block:: python

    import chain

    chain.conf.api_key = 'YOUR-KEY'
    chain.conf.api_secret = 'YOUR-SECRET'
    try:
        webhook = chain.Webhook.create('https://your-server-url.com')
    except chain.ChainException as exc:
        print exc

.. _Chain.com: https://chain.com
