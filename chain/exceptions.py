class ChainException(Exception):
    """Base PyChain exceptions class."""


class APIConnectionError(ChainException):
    """Network communication errors."""


class AuthError(ChainException):
    """Authentication and authorization errors."""
    def __init__(self, message, http_content=None, http_status_code=None):
        super(AuthError, self).__init__(message)
        self.http_content = http_content
        self.http_status_code = http_status_code


class APIError(ChainException):
    """API server errors, for example, invalid response object."""
    def __init__(self, message, http_content, http_status_code):
        super(APIError, self).__init__(message)
        self.http_content = http_content
        self.http_status_code = http_status_code


class InvalidRequestError(ChainException, ValueError):
    """Invalid request param errors."""
    def __init__(self, message, http_content=None, http_status_code=None):
        super(InvalidRequestError, self).__init__(message)
        self.http_content = http_content
        self.http_status_code = http_status_code
