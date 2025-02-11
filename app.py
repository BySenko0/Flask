from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.getcwd(), 'estudiantes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definir el modelo de Estudiante
class Estudiante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    primer_parcial = db.Column(db.Float, nullable=False)
    segundo_parcial = db.Column(db.Float, nullable=False)
    tercer_parcial = db.Column(db.Float, nullable=False)

# Crear la base de datos y agregar datos de prueba
with app.app_context():
    db.create_all()
    
    if not Estudiante.query.first():  # Si la base de datos está vacía, agrega datos de prueba
        estudiantes_prueba = [
            Estudiante(nombre="Kevin", primer_parcial=8.5, segundo_parcial=7.0, tercer_parcial=9.0),
            Estudiante(nombre="Ana", primer_parcial=9.0, segundo_parcial=8.2, tercer_parcial=7.5),
            Estudiante(nombre="Luis", primer_parcial=6.5, segundo_parcial=7.8, tercer_parcial=8.1)
        ]
        db.session.add_all(estudiantes_prueba)
        db.session.commit()

# Ruta para mostrar la tabla de estudiantes
@app.route('/')
def home():
    estudiantes = Estudiante.query.all()
    return render_template('index.html', estudiantes=estudiantes)

if __name__ == '__main__':
    app.run(debug=True)
