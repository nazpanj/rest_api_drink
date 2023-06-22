# Drink Management App

The Drink Management App is a web application built with Flask that allows you to manage a list of drinks. It provides functionality to add, update, get, and delete drinks using a RESTful API.

[RESTful API tutorial](https://www.google.com/search?q=tutorial+restful+api&oq=tutorial+restful+api&aqs=chrome..69i57j0i22i30l9.8227j0j7&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:aed5445a,vid:qbLc5a9jdXo)

## Installation

1. Clone the repository:  
```bash 
git clone https://github.com/nazpanj/rest_api_drinks.git
```


2. Navigate to dir:  
```bash
cd rest_api_drinks
```

3. Create a conda environment and install the requirements:  
```bash
conda create --name your_env_name --file requirements.txt
```

If there is `PackagesNotFoundError`, then run the following command first and then run the above command again:
```bash
conda config --append channels conda-forge
```

4. Activate the conda environment (macOS):  
```bash
conda activate your-env-name
```


## Usage

1. Run the application:
```bash
python run.py
```

2. The above command will start your Flask application and it will be accessible at:  `http://localhost:5000`

3. Use the web interface to add, update, and delete drinks:

- Add a drink: `http://localhost:5000/add_drink`  
- Update a drink: `http://localhost:5000/update_drink`  
- Delete a drink: `http://localhost:5000/delete_drink` 
- Get a list of drinks: `http://localhost:5000/drinks`
- Get a a drink based on id: `http://localhost:5000/drinks/<id>`

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

- Flask: A micro web framework for building web applications.  
- Flask-SQLAlchemy: Integrates SQLAlchemy, an Object-Relational Mapping (ORM) library, with Flask.

