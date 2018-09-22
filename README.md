
     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 

# Django Microservice

Activate virtualenv

`$ source env/bin/activate`  # On Windows use `env\Scripts\activate`

Install Django and Django REST framework into the virtualenv

`$ pip install django`

`$ pip install djangorestframework`

Sync databases

`python manage.py makemigrations app`

`$ python manage.py migrate`

Run server on Cloud9

`$ python manage.py runserver $IP:$PORT`

Users: https://djangoquickstart-daeperdomocr.c9users.io/users/

Teams: https://djangoquickstart-daeperdomocr.c9users.io/teams/