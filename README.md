## Django Portfolio Template
A simple dynamic portfolio created with the Django framework.

### Installation (Windows)
```
Install Python 3.7 version
```

##### Create Virtual Environment (Recommended)
1) [Download Virtual Enviroment](https://docs.python.org/3/library/venv.html)

2) ##### Clone or download the project
    ```
    git clone https://github.com/HarrysAsi/portfolio.git
    ```
3) ##### Create the virtual enviroment inside your project
    ```
    python3 -m venv /path/to/new/virtual/environment
    ```
4) ##### Activate the enviroment
     ```
     pip install -r requirements.txt
     ```
5) ##### Install all project requirements
    ```
    pip install -r requirements.txt
    ```
6) ##### Register your email in settings.py
    ```
    OWNER_EMAIL = ""
    ```
7) ### Create a mysql database with name (portfolio) and migrate
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
8) ##### With the registered email create a super user (insert email and password)
   ```
   python3 manage.py createsuperuser 
   ```
9) ### Run the project
    ```
    python3 manage.py runserver
    ```
### Configure the UI from the admin panel
```
navigate to yourdomain/admin and login with the superuser you created
```

### Built With

* [Python 3.7](https://www.python.org/downloads/release/python-370/)

### Versioning

We use [github](https://github.com/) for versioning.

### Authors

* **Asimakopoulos Charalampos** - *Initial work* - [HarrysAsi](https://github.com/HarrysAsi)
