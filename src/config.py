import os

class Config:
    # Configuración base
    SECRET_KEY = os.environ.get("SECRET_KEY", "mi_clave_secreta_predeterminada")  # Clave secreta para sesiones
    DATABASE_URL = os.environ.get("DATABASE_URL", "db/databases.db")  # Ruta de la base de datos
    DEBUG = os.environ.get("DEBUG", True)  # Modo de depuración

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "development"

class ProductionConfig(Config):
    DEBUG = False
    ENV = "production"

# Mapeo de configuraciones
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}