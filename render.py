from eralchemy2 import render_er
from src.models import db

# Renderiza el modelo de SQLAlchemy directamente desde el código Python
render_er(db.Model, 'diagram.png')
print("¡Diagrama actualizado con éxito!")