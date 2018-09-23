# Item Catalog 


## About
A multi-page application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users have the ability to add, edit and delete their own items.

## Tech Stack
* HTML
* CSS
* Python
* Flask
* OAuth2
* SQLAlchemy


## Getting Started
1. Download and install [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
2. Clone the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)
3. Launch the Vagrant VM (vagrant up) in your terminal.
4. Download the project or clone this repository.
5. Open your terminal and run the database_catalog_setup.py to create the tables (User, Category and Item). 
6. Step #5 will create a database - catalog.db in the project.
7. To populate the catalog.db with items, run the file database_populate_items.py.
8. Run your application within the VM (python /vagrant/Item-Catalog-Project/catalog_backend.py).
9. Access and test your application by visiting http://localhost:5000 locally.
10. The homepage displays all current categories along with the all the items.
11. Selecting a specific category shows you all the items available for that category.
12. After logging in, a user has the ability to add, update, or delete item info.
13. The application provides a JSON endpoint - /category/<int:category_id>/<int:item_id>/JSON
Returns the id, name and description on an item.

![Sample View of the Application]()


## Using Google Login
To get the Google login working there are a few additional steps:

1. Go to Google Dev Console
2. Sign up or Login if prompted
3. Go to Credentials
4. Select Create Crendentials > OAuth Client ID
5. Select Web application
6. Enter name 'Item-Catalog-Project'
7. Authorized JavaScript origins = 'http://localhost:5000'
8. Authorized redirect URIs = 'http://localhost:5000/login' && 'http://localhost:5000/gconnect'
9. Select Create
10. Copy the Client ID and paste it into the data-clientid in login.html
11. On the Dev Console Select Download JSON
12. Rename JSON file to client_secrets.json
13. Place JSON file in item-catalog directory that you cloned from here
14. Run application using python /Item-Catalog-Project/catalog_backend.py


## My Learnings
1. Developed a RESTful web application using the Python framework Flask along with implementing third-party OAuth authentication. 
2. Used the various HTTP methods available to you and how these methods relate to CRUD (create, read, update and delete) operations.

## Reference materials
TBD
