from hms_softforge import database, app
from hms_softforge.models import Usuario, Tarefa, Quarto

with app.app_context():
    database.create_all()