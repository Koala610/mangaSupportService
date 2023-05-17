import fastapi
from src.routers.support import router as support_router

app = fastapi.FastAPI(docs_url="/docs")

app.include_router(support_router)