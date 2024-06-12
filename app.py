from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'

db = SQLAlchemy(app)


class Object_Seeker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_obj = db.Column(db.String(150))
    count_obj = db.Column(db.String(150))
    location_obj = db.Column(db.String(150))
    сomment_obj = db.Column(db.String(150))

    def __init__(self, name_obj,count_obj, location_obj, сomment_obj):
        self.name_obj = name_obj
        self.count_obj = count_obj
        self.location_obj = location_obj
        self.сomment_obj = сomment_obj


with app.app_context():
    db.drop_all()
    db.create_all()


@app.route('/add_info_Object', methods=['POST'])
def add_info_Object():
    name_obj = request.form['name_obj']
    count_obj = request.form['count_obj']
    location_obj = request.form['location_obj']
    сomment_obj = request.form['сomment_obj']
    info_Object = Object_Seeker(name_obj, count_obj, location_obj, сomment_obj)
    db.session.add(info_Object)
    db.session.commit()
    return {"session": "Consumables found at the facility"}


@app.route('/get_info_Object/<int:id>')
def get_info_Object(id):
    info_Object = Object_Seeker.query.get(id)
    if info_Object:
        return jsonify({
            'id': info_Object.id,
            'name_obj': info_Object.name_obj,
            'count_obj': info_Object.count_obj,
            'location_obj': info_Object.location_obj,
            'сomment_obj': info_Object.сomment_obj
        })
    else:
        return {'error': 'There are no consumables at the facility'}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
