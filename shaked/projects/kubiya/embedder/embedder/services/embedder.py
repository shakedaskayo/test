from utils.secrets import SecretsManagerService

class CohereEmbedder:
    def __init__(self):
        self.cohere_api_key = SecretsManagerService.get_secret_value("COHERE_API_KEY")

    def embed_text(self, text):
        # Embedding logic
        pass

