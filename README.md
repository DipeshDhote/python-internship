## What I did ?
#### Step - 1 create a function using "psycopg2" to connect to the postgresSQL database.To connect to database there are 5 main variables i used those are 
- db_name
- user
- password
- host
- port
#### Step - 2 Create a main app.py file using flask in which i create following endpoints
- "/" methods = "GET"
- "/employees" methods = "GET"
- "/employee" methods = "POST"
- "/employee/<int:id>" methods = "PUT"
- "/employee/<int:id>" methods = "DELETE"

#### Step - 3 Create a public_api in which i used public_api = "Cat Facts" than get the data about cat facts than save into table name "cat_fact" which was created using postgres SQL inside the "InternDB" Database.
