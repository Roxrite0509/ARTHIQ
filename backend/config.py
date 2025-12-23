import os

JWT_SECRET = os.getenv("JWT_SECRET", "arthiq-secret")
JWT_ALGO = "HS256"

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

ENV = os.getenv("ENV", "dev")
