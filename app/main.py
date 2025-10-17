"""
Aplicación principal TaskAI - Implementa principios SOLID
Single Responsibility: Solo maneja la configuración de la aplicación
Open/Closed: Extensible para nuevos endpoints y funcionalidades
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.core.config import settings
from app.api import tasks, ai
from app.core.database import engine, Base

# Crear tablas de base de datos
Base.metadata.create_all(bind=engine)

# Crear aplicación FastAPI
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Sistema de Gestión de Tareas Inteligente con IA",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(tasks.router)
app.include_router(ai.router)


@app.get("/")
async def root():
    """
    Endpoint raíz con información de la API
    """
    return {
        "message": "TaskAI - Sistema de Gestión de Tareas Inteligente",
        "version": settings.app_version,
        "docs": "/docs",
        "features": [
            "Gestión inteligente de tareas",
            "Predicciones de IA para optimización",
            "Analytics de productividad",
            "API RESTful moderna",
            "Arquitectura SOLID"
        ],
        "endpoints": {
            "tasks": "/api/tasks",
            "ai_suggestions": "/api/ai/suggestions",
            "analytics": "/api/tasks/analytics/stats",
            "documentation": "/docs"
        }
    }


@app.get("/health")
async def health_check():
    """
    Endpoint de salud para monitoreo
    """
    return {
        "status": "healthy",
        "app_name": settings.app_name,
        "version": settings.app_version,
        "database": "connected"
    }


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """
    Manejador global de excepciones HTTP
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "status_code": exc.status_code,
            "path": str(request.url)
        }
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """
    Manejador global de excepciones generales
    """
    return JSONResponse(
        status_code=500,
        content={
            "error": "Error interno del servidor",
            "detail": str(exc),
            "path": str(request.url)
        }
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug
    )