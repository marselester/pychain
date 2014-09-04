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

Webhook
-------

Creating a webhook
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    webhook = chain.Webhook.create('https://your-server-url.com')

Retrieving a webhook
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    webhook = chain.Webhook.retrieve('FFA21991-5669-4728-8C83-74DEC4C93A4A')

Updating a webhook
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    webhook = chain.Webhook('FFA21991-5669-4728-8C83-74DEC4C93A4A')
    webhook.url = 'https://your-new-url.com'
    webhook.save()

Deleting a webhook
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    webhook = chain.Webhook('FFA21991-5669-4728-8C83-74DEC4C93A4A')
    webhook.delete()

.. _Chain.com: https://chain.com
