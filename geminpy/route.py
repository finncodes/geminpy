from pathlib import PurePath


class Route:

    def __init__(self, path, func):
        self.path = PurePath(path)
        self.func = func

    def path_matches(self, path):
        return self.path == PurePath(path)
