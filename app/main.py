import asyncio
import os

from dotenv import load_dotenv
from fastapi import FastAPI

from app.bots.classes.bots import DumdBot
from app.config import openapi_config
from app.initializer import init
from app.ml.classes.sberbank import SmallGPT3


def start():
    app = FastAPI(
        title=openapi_config.name,
        version=openapi_config.version,
        description=openapi_config.description,
    )

    load_dotenv()
    token_choir = os.getenv('TOKEN_SCARLET_CHOIR')

    scarlet_choir_model = SmallGPT3('Nicki/scarlet-choir')

    scarlet_choir_bot = DumdBot(token_choir, scarlet_choir_model)

    loop = asyncio.get_event_loop()

    loop.create_task(scarlet_choir_bot())

    init(app)
    return app
