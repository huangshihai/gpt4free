from fastapi import FastAPI

import g4f.api

app: FastAPI = g4f.api.create_app()