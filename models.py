from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class WeatherSearch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    temp = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<Search {self.city}>'