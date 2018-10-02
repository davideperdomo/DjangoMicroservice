
     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 

# Django + Mongo Microservice on Cloud9

Configure Mongo 

`mkdir data`

`echo 'mongod --bind_ip=$IP --dbpath=data --nojournal --rest "$@"' > mongod`

`chmod a+x mongod`

Activate virtualenv

`cd project`

`source env/bin/activate`  # On Windows use `env\Scripts\activate`

Install dependencies into the virtualenv

`pip install -r requirements.txt`


Sync databases

`cd project`

`python manage.py makemigrations app`

`python manage.py migrate`

Run server on Cloud9

`python manage.py runserver $IP:$PORT`
