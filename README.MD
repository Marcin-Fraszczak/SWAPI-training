# SWAPI - training app for django and API

App available at:

https://marcinfraszczak2.eu.pythonanywhere.com/

Main focus on working with API and data processing using pandas library.

Some additional JS features for displaying data.

Write and read to csv files.

Metadata written to MySQL database.



# How to run it locally:
1. Fork the repository
2. Clone the repository to your local machine, for example:
`git clone <your_repo_url>`
3. Create and activate virtual environment, for example for virtualenv:

`virtualenv -p python3.11 venv`

and then

`source venv/bin/activate`

4. In the main project folder (where manage.py is located), with virtual environment activated, use command:

`bash start.sh`

That will run the script, which does the following:
- installs required packages
- prepares and runs migrations (database file is created in main directory)
- flushes the database, in case script is run for the second time
- runs django development server, by default at http://127.0.0.1:8000/
- creates directories for storing csv files
- tests code with pytest
- saves all the above info to `log.txt` file in the main directory


[//]: # (- populates the database with starting data:)
[//]: # (    - one user)
[//]: # (    - one superuser)
[//]: # (    - couple of instances of all the necessary models)


### In case you run this script multiple times without killing the previous process, you'll get `port already in use` message

One easy way to free this port is:

`sudo lsof -t -i:8000`

or any other port number. This will output ID of the process that is running on this port,

for example `21987`, then

`sudo kill 21987`
