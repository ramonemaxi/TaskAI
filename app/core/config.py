"""
Configuración central del sistema TaskAI
Implementa el principio de responsabilidad única (SRP)
"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Configuración centralizada del sistema"""
    
    # Configuración de la aplicación
    app_name: str = "TaskAI"
    app_version: str = "1.0.0"
    debug: bool = False
    
    # Configuración de base de datos
    database_url: str = "sqlite:///./taskai.db"
    database_echo: bool = False
    
    # Configuración de autenticación
    secret_key: str = "your-secret-key-here"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Configuración de IA
    ai_model_path: str = "./models/"
    prediction_threshold: float = 0.7
    
    class Config:
        env_file = ".env"


# Instancia global de configuración
settings = Settings()