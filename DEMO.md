# TaskAI - Demo del Sistema

## 🚀 Características Principales

### 1. **Gestión Inteligente de Tareas**
- Creación de tareas con sugerencias automáticas de IA
- Priorización inteligente basada en patrones de comportamiento
- Predicción de duración óptima para cada tarea
- Sugerencias de horarios ideales para máxima productividad

### 2. **Analytics de Productividad**
- Métricas de rendimiento personalizadas
- Identificación de horas más productivas
- Análisis de patrones de trabajo
- Recomendaciones personalizadas para optimización

### 3. **Arquitectura SOLID**
- **Single Responsibility**: Cada clase tiene una responsabilidad específica
- **Open/Closed**: Extensible sin modificar código existente
- **Liskov Substitution**: Interfaces intercambiables
- **Interface Segregation**: Interfaces específicas y cohesivas
- **Dependency Inversion**: Dependencias inyectadas

## 🛠️ Tecnologías Utilizadas

- **FastAPI**: Framework web moderno y rápido
- **SQLAlchemy**: ORM para manejo de base de datos
- **Scikit-learn**: Machine Learning para predicciones
- **Pydantic**: Validación de datos y serialización
- **JWT**: Autenticación segura
- **Pytest**: Testing automatizado

## 📊 Endpoints Principales

### Tareas
```
POST   /api/tasks              # Crear tarea
GET    /api/tasks              # Listar tareas
GET    /api/tasks/{id}         # Obtener tarea específica
PUT    /api/tasks/{id}         # Actualizar tarea
DELETE /api/tasks/{id}         # Eliminar tarea
POST   /api/tasks/{id}/complete # Completar tarea
```

### IA y Analytics
```
GET    /api/ai/suggestions     # Sugerencias de IA
GET    /api/ai/insights        # Insights de productividad
GET    /api/ai/recommendations # Recomendaciones personalizadas
POST   /api/ai/train          # Entrenar modelo de IA
```

### Analytics
```
GET    /api/tasks/analytics/stats    # Estadísticas de tareas
GET    /api/tasks/overdue            # Tareas vencidas
GET    /api/tasks/due-today         # Tareas del día
```

## 🧠 Características Innovadoras de IA

### 1. **Predicción de Tiempo Óptimo**
```python
# El sistema aprende de tus patrones y sugiere:
optimal_time = ai_service.predict_optimal_time(task, user_id)
# Resultado: "2024-01-15T10:30:00" (tu hora más productiva)
```

### 2. **Estimación Inteligente de Duración**
```python
# Basado en tareas similares completadas:
duration = ai_service.predict_duration(task, user_id)
# Resultado: 45 minutos (basado en tareas similares)
```

### 3. **Priorización Automática**
```python
# Analiza tu comportamiento y sugiere prioridad:
priority = ai_service.suggest_priority(task, user_id)
# Resultado: TaskPriority.HIGH (basado en patrones)
```

### 4. **Insights de Productividad**
```json
{
  "completion_rate": 85.2,
  "most_productive_hour": 10,
  "average_duration": 45.5,
  "recommendations": [
    "Eres más productivo en las mañanas",
    "Considera dividir tareas largas"
  ]
}
```

## 🔧 Instalación y Uso

### 1. **Instalar Dependencias**
```bash
pip install -r requirements.txt
```

### 2. **Configurar Variables de Entorno**
```bash
cp env.example .env
# Editar .env con tus configuraciones
```

### 3. **Ejecutar la Aplicación**
```bash
uvicorn app.main:app --reload
```

### 4. **Acceder a la Documentación**
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 📈 Ejemplo de Uso

### Crear una Tarea con IA
```bash
curl -X POST "http://localhost:8000/api/tasks" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Implementar nueva funcionalidad",
    "description": "Desarrollar API para reportes",
    "category": "work",
    "priority": "medium"
  }'
```

### Respuesta con Sugerencias de IA
```json
{
  "id": 1,
  "title": "Implementar nueva funcionalidad",
  "priority": "high",  // IA sugirió alta prioridad
  "estimated_duration": 120,  // IA predijo 2 horas
  "ai_confidence": 85,  // 85% de confianza
  "optimal_time": "2024-01-15T10:30:00"  // Hora óptima sugerida
}
```

### Obtener Sugerencias de IA
```bash
curl -X GET "http://localhost:8000/api/ai/suggestions" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Respuesta con Insights
```json
{
  "productivity_insights": {
    "completion_rate": 85.2,
    "most_productive_hour": 10,
    "average_duration": 45.5
  },
  "task_suggestions": [
    {
      "task_id": 1,
      "suggested_priority": "high",
      "suggested_duration": 120,
      "optimal_time": "2024-01-15T10:30:00"
    }
  ]
}
```

## 🧪 Testing

### Ejecutar Tests
```bash
pytest
```

### Tests con Cobertura
```bash
pytest --cov=app
```

### Tests Específicos
```bash
pytest tests/test_task_service.py -v
```

## 🏗️ Arquitectura del Proyecto

```
taskai/
├── app/
│   ├── core/           # Configuración y utilidades
│   │   ├── config.py   # Configuración central
│   │   └── database.py  # Configuración de BD
│   ├── models/         # Modelos de datos
│   │   ├── task.py     # Modelo de tareas
│   │   └── user.py     # Modelo de usuarios
│   ├── repositories/   # Acceso a datos
│   │   ├── base_repository.py
│   │   └── task_repository.py
│   ├── services/      # Lógica de negocio
│   │   └── task_service.py
│   ├── ai/            # Módulo de IA
│   │   └── ai_service.py
│   ├── api/           # Endpoints REST
│   │   ├── tasks.py
│   │   ├── ai.py
│   │   └── dependencies.py
│   └── main.py        # Aplicación principal
├── tests/             # Tests unitarios
├── requirements.txt   # Dependencias
└── README.md         # Documentación
```

## 🎯 Beneficios del Diseño SOLID

### 1. **Mantenibilidad**
- Código fácil de entender y modificar
- Cambios aislados sin efectos secundarios
- Testing simplificado

### 2. **Extensibilidad**
- Nuevas funcionalidades sin modificar código existente
- Fácil integración de nuevos algoritmos de IA
- Soporte para múltiples proveedores de datos

### 3. **Testabilidad**
- Interfaces claras para mocking
- Tests unitarios independientes
- Cobertura de código completa

### 4. **Reutilización**
- Componentes reutilizables
- Lógica de negocio desacoplada
- Servicios intercambiables

## 🚀 Próximas Mejoras

1. **Machine Learning Avanzado**
   - Modelos de deep learning
   - Predicciones más precisas
   - Aprendizaje continuo

2. **Integraciones**
   - Calendarios (Google, Outlook)
   - Herramientas de comunicación (Slack, Teams)
   - Sistemas de notificaciones

3. **Analytics Avanzados**
   - Dashboards interactivos
   - Reportes personalizados
   - Métricas de equipo

4. **Mobile App**
   - Aplicación móvil nativa
   - Notificaciones push
   - Sincronización en tiempo real

---

*Este proyecto demuestra la aplicación práctica de principios SOLID en un sistema real con características innovadoras de IA para gestión de tareas.*