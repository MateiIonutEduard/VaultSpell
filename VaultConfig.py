import json

class VaultConfig(object):
    def __init__(self, content):
        self.__dict__ = json.loads(content)