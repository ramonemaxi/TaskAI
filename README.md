# TaskAI - Sistema de Gestión de Tareas Inteligente

## 🚀 Descripción

TaskAI es un sistema innovador de gestión de tareas que utiliza inteligencia artificial para aprender de tus patrones de trabajo y sugerir automáticamente cuándo realizar cada tarea. El sistema analiza tu productividad histórica y optimiza tu agenda diaria.

## ✨ Características Innovadoras

- **IA Predictiva**: Aprende de tus patrones de trabajo para sugerir horarios óptimos
- **Priorización Inteligente**: Clasifica automáticamente las tareas por importancia y urgencia
- **Análisis de Productividad**: Proporciona insights sobre tus patrones de trabajo
- **Sugerencias Contextuales**: Recomienda tareas basadas en el contexto actual
- **API RESTful**: Arquitectura moderna con FastAPI

## 🏗️ Arquitectura SOLID

El proyecto implementa los principios SOLID:

- **S** - Single Responsibility: Cada clase tiene una responsabilidad específica
- **O** - Open/Closed: Extensible sin modificar código existente
- **L** - Liskov Substitution: Interfaces intercambiables
- **I** - Interface Segregation: Interfaces específicas y cohesivas
- **D** - Dependency Inversion: Dependencias inyectadas

## 🛠️ Tecnologías

- **Backend**: FastAPI, SQLAlchemy, Alembic
- **IA/ML**: Scikit-learn, Pandas, NumPy
- **Base de Datos**: SQLite (desarrollo) / PostgreSQL (producción)
- **Autenticación**: JWT
- **Testing**: Pytest

## 📁 Estructura del Proyecto

```
taskai/
├── app/
│   ├── core/           # Configuración y utilidades
│   ├── models/          # Modelos de datos (SOLID)
│   ├── services/       # Lógica de negocio
│   ├── repositories/   # Acceso a datos
│   ├── ai/             # Módulo de IA
│   └── api/            # Endpoints REST
├── tests/              # Tests unitarios
├── migrations/         # Migraciones de DB
└── requirements.txt
```

## 🚀 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/ramonemaxi/TaskAI.git
cd TaskAI

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
alembic upgrade head

# Iniciar servidor
uvicorn app.main:app --reload
```

## 📊 Características Técnicas

### Principios SOLID Implementados

1. **Single Responsibility Principle (SRP)**
   - `TaskService`: Solo maneja lógica de tareas
   - `AIService`: Solo maneja predicciones de IA
   - `UserService`: Solo maneja lógica de usuarios

2. **Open/Closed Principle (OCP)**
   - Sistema de plugins para diferentes algoritmos de IA
   - Extensible para nuevos tipos de tareas sin modificar código

3. **Liskov Substitution Principle (LSP)**
   - Interfaces intercambiables para diferentes proveedores de IA
   - Repositorios intercambiables (SQLite/PostgreSQL)

4. **Interface Segregation Principle (ISP)**
   - Interfaces específicas: `ITaskRepository`, `IAIService`
   - No hay dependencias innecesarias

5. **Dependency Inversion Principle (DIP)**
   - Inyección de dependencias en todos los servicios
   - Abstracciones no dependen de detalles

## 🤖 Módulo de IA

El sistema incluye un módulo de IA que:

- **Analiza patrones**: Aprende cuándo eres más productivo
- **Predice horarios**: Sugiere el mejor momento para cada tarea
- **Clasifica tareas**: Prioriza automáticamente según tu comportamiento
- **Optimiza agenda**: Sugiere reorganizaciones inteligentes

## 📈 Métricas y Analytics

- Tiempo promedio de finalización por tipo de tarea
- Patrones de productividad por hora del día
- Efectividad de las sugerencias de IA
- Análisis de tendencias de productividad

## 🔧 API Endpoints

```
GET    /api/tasks              # Listar tareas
POST   /api/tasks              # Crear tarea
PUT    /api/tasks/{id}         # Actualizar tarea
DELETE /api/tasks/{id}         # Eliminar tarea
GET    /api/ai/suggestions     # Obtener sugerencias de IA
GET    /api/analytics          # Obtener analytics
```

## 🧪 Testing

```bash
# Ejecutar tests
pytest

# Tests con cobertura
pytest --cov=app
```

## 📝 Licencia

MIT License - Ver LICENSE para más detalles.

## 👨‍💻 Autor

**Maximiliano Benegas** - Desarrollador Python especializado en IA y arquitecturas limpias.

---

*Este proyecto demuestra la aplicación práctica de principios SOLID en un sistema real con características innovadoras de IA.*