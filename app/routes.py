from flask import render_template, jsonify, request
from app.models import Drink
from app import app, db


# Route to serve the add_drink.html file
@app.route('/add_drink', methods=['GET'])
def serve_add_drink_form():
    return render_template('add_drink.html')


# Route to serve the delete_drink.html file
@app.route('/delete_drink', methods=['GET'])
def serve_delete_drink_form():
    return render_template('delete_drink.html')


# Route to serve the update_drink.html file
@app.route('/update_drink', methods=['GET'])
def serve_update_drink_form():
    return render_template('update_drink.html')

# Route to landing page
@app.route('/', methods=['GET']) 
def index():
    return 'Welcome to the Drinks app! This app gives you bunch of drinks and their descriptions.'


# Route to get all drinks
@app.route('/drinks', methods=['GET'])
def get_drinks():
	drinks = Drink.query.all()
	drink_list = []

	for drink in drinks:
		drink_data = {
			'id': drink.id,
			'name': drink.name,
			'description': drink.description
		}
		drink_list.append(drink_data)

	return jsonify({'drinks': drink_list})

# Route to get a drink based on id
@app.route('/drinks/<id>', methods=['GET'])
def get_drink(id):
	drink = Drink.query.get_or_404(id)
	
	return jsonify({
		'name': drink.name,
		'description': drink.description
	})

# Route to add a drink
@app.route('/add_drink', methods=['POST'])
def add_drink():
	drink = Drink(name=request.json['name'], description=request.json['description'])
	db.session.add(drink)
	db.session.commit()

	return {'id': drink.id}

# Route to delete a drink
@app.route('/delete_drink/<id>', methods=['DELETE'])
def delete_drink(id):
	drink = Drink.query.get(id)
	if drink is None:
		return {"error": "not found"}
	drink_name = drink.name
	drink_desc = drink.description
	db.session.delete(drink)
	db.session.commit()
	return {'name': drink_name, 
			'description': drink_desc}


# Route to update a drink
@app.route('/update_drink', methods=['PUT'])
def update_drink():
    drink_id = request.json['id']
    new_name = request.json['name']
    new_description = request.json['description']

    drink = Drink.query.get(drink_id)
    if drink is None:
        return {"error": "Drink not found"}

    drink.name = new_name
    drink.description = new_description
    db.session.commit()

    return {"id": drink_id}

