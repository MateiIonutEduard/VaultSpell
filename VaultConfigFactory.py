import VaultConfig as vault

class VaultConfigFactory:
    def __init__(self):
        with open('vault.config.json', 'r') as content_file:
            content = content_file.read()
            self.vaultConfig = vault.VaultConfig(content)