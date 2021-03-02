class Request:
    def __init__(self, hostname, path, query_parameters=None):
        if query_parameters is None:
            query_parameters = []
        self.hostname = hostname
        self.path = path
        self.query_parameters = query_parameters
