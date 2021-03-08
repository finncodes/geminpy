from typing import Union


class Request:
    """
    A class used to contain the data of an incoming request from a client

    :ivar hostname:         the hostname the client connected to
    :ivar path:             the URI of the requested resource
    :ivar query_parameters: the values extracted from the query string
    """
    def __init__(self, hostname: str, path: str, query_parameters: Union[None, list[str]] = None):
        """ The constructor for the Request class
        :param hostname:            the hostname of the server
        :param path:                the URI of the requested resource
        :param query_parameters:    the query parameters in a list
        """
        if query_parameters is None:
            query_parameters = []
        self.hostname = hostname
        self.path = path
        self.query_parameters = query_parameters
