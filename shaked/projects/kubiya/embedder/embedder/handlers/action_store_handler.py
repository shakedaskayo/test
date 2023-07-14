from services.embedder import CohereEmbedder
from services.pinecone_handler import PineconeHandler
from handlers.base_handler import BaseHandler

class ActionStoreHandler(BaseHandler):
    def handle_request(self, request):
        embedder = CohereEmbedder()
        pinecone_handler = PineconeHandler()

        for action_name, action in request.actions.items():
            # Create the embeddings
            embedding = embedder.embed_text(action.description)

            # Store the embedding in Pinecone
            pinecone_handler.from_texts([f"{request.name}.{action_name}"], [embedding], [action.description])

