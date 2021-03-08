import re
from typing import Union

from .request import Request

# matches hostname and subsequent path
REQUEST_PATTERN = r"gemini://([^/]+)(/.*)*\r\n"


def parse_request(data: bytes) -> Union[Request, None]:
    """Parses the bytes of an incoming request from a client's socket
    :param      data: the bytes received from the client
    :return:    a Request object if successfully parsed, None if not
    """
    data_string = data.decode('utf-8')
    match = re.match(REQUEST_PATTERN, data_string)

    if match is None:
        return None

    (hostname, path) = match.groups()

    return Request(hostname, path)
