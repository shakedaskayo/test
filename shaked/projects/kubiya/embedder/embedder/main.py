from fastapi import FastAPI

from handlers.action_store_handler import ActionStoreHandler

app = FastAPI()

@app.post("/process_action_store")
def process_action_store(action_store: ActionStore):
    handler = ActionStoreHandler()
    return handler.handle_request(action_store)

