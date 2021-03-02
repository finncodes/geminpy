import re
from .request import Request

# matches hostname and subsequent path
REQUEST_PATTERN = r"gemini://([^/]+)(/.*)*\r\n"


def build_parser(server_hostname):
    def parse_request(data):
        match = re.match(REQUEST_PATTERN, data)

        if match is None:
            return None

        (hostname, path) = match.groups()

        if hostname != server_hostname:
            return None

        return Request(hostname, path)

    return parse_request
