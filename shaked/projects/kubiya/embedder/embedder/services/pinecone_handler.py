from utils.secrets import SecretsManagerService

class PineconeHandler:
    def __init__(self):
        self.pinecone_api_key = SecretsManagerService.get_secret_value("PINECONE_API_KEY")

    def from_texts(self, texts, embeddings, metadata):
        # Interaction with Pinecone logic
        pass

