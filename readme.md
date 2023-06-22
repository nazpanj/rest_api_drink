# Drink Management App

The Drink Management App is a web application built with Flask that allows you to manage a list of drinks. It provides functionality to add, update, get, and delete drinks using a RESTful API.

## Installation

1. Clone the repository:  
```bash 
git clone https://github.com/nazpanj/rest_api_drinks.git
```


2. Navigate to dir:  
```bash
cd rest_api_drinks
```

3. Create a conda environment:  
```bash
conda create --name your-env-name python=3.9
```

4. Activate the conda environment (macOS):  
```bash
conda activate your-env-name
```

5. Install the required dependencies from the requirements.txt file:  
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python run.py
```

2. The above command will start your Flask application and it will be accessible at:   http://localhost:5000

3. Use the web interface to add, update, and delete drinks.

4. Use the API endpoints to interact with the drink data programmatically:

Add a drink: `POST /drinks`  
Update a drink: `PUT /drinks/<id>`  
Delete a drink: `DELETE /drinks/<id>`  

## Project Structure
The project follows a standard Flask application structure:

`app/`: Directory containing the Flask application files.  
`__init__.py`: Initializes the Flask app, configures database and creates tables, defines the app's routes.  
`models.py`: Defines the database models, including the Drink model.  
`routes.py`: Defines the app's routes and API endpoints.  
`templates/`: Directory containing the HTML templates for the web interface.  
`add_drink.html`: Template for adding a new drink.  
`update_drink.html`: Template for updating an existing drink.  
`delete_drink.html`: Template for deleting a drink.  
`run.py`: Script for running the application

## Dependencies
The project's dependencies are listed in the requirements.txt file. They include:

Flask: A micro web framework for building web applications.  
Flask-SQLAlchemy: Integrates SQLAlchemy, an Object-Relational Mapping (ORM) library, with Flask.

