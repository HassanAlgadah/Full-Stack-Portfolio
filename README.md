# Full-Stack CapStone Final Project

## API Portfolio

API Portfolio is a fully functional api based Portfolio that lets you add, modify and delete projects on the database the website will show all the project provided by the API and allow visitors to send messages that can only be seen by the admin role,
the reason that I choose this idea as my final project in udacity's full-stack developer nanodgree is that I needed a portfolio since im graduating soon and need a website to showcase my projects in the way I wanted and have a full control over it,
the frontend was build from the ground up using bootstrap and I had to change a lot of the javascript to fit an API model,
the back end is fully Flask framework with all the endpoints and for the database postgres with SQLAlchemy as the ORM, all the models can be found in models.py,
for the authorization I went for auth0 as seen in auth.py,
a fully working unit test cases for all the endpoints can be found in app_test.py 




#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```


## Running the server

From within the Portfolio API directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```



Endpoints

GET '/'

GET '/admin'

GET '/projects'

GET '/project/id'

GET '/messages'

POST '/project'

POST '/messages'

PATCH '/project/id'

DELETE '/project/id'


**GET '/'**
- Request Arguments: None
- Returns: the home html page 

**GET '/admin'**
- Request Arguments: None
- Returns: the admin html page 


**GET '/projects'**
- Fetches a dictionary of all the projects in the database
- Request Arguments: None
- Returns: a json list of all the projects 
```
{
    'success': True,
    'projects': [{
        'id': 1,
        'name': project1,
        'image': www.ex.com,
    }]
}

```
**GET '/project/id'**
- Fetches a dictionary of for a project by the id 
- Request Arguments: the project's id
- Returns: a json object of the required project 
```
{
    'id': 1,
    'name': project1,
    'description': self.description,
    'image': www.ex.com,
    'link': www.github.com
}
```


**GET '/messages'**
- Fetches a dictionary of all messages
- Request Arguments: none
- Authorization requires admin role authorization
- Returns: a json list of all the messages
```
{
    'success': True,
    'projects': [{
          'id': 1,
          'name': name,
          'description': description,
          'image': image,
          'link': link
    }]
}
```
**POST '/project'**
- add a new project to the projects database 
- Request Arguments: string 'name', string 'description', string 'image', string 'link'
- Authorization requires admin role authorization
- Returns: redirect to the homepage 


**POST '/message'**
- Fetches add a new message to the messages database
- Request Arguments: string 'name', string 'phone', string 'email', string 'message' 
- Returns: redirect to the homepage 


**PATCH '/projects'**
- Fetches update a project based on the id of the project
- Request Arguments:  string 'name', string 'description', string 'image', string 'link'
- Returns:  a json object of the updated project 
```
{
    'id': 1,
    'name': project1,
    'description': self.description,
    'image': www.ex.com,
    'link': www.github.com
}
```


**DELETE '/project/id'**
- delete a project based on the project id
- Request Arguments: the project's id
- Returns: none



## Testing
To run the tests, run
```
python app_test.py
```