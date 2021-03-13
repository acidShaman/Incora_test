# Incora_test
In command line run first "pipenv install" to download and install required packages


Those are db_name and my sql credentials:
        'NAME': 'incora_test',
        'USER': 'root',
        'PASSWORD': 'qazwsxedc',
You also need to create db first and name it 'incora_test'
You may change them to your like so that it would work with your mysqldb. 

Then run:
    python3 manage.py makemigrations
    python3 manage.py migrate
    
To start project run:
    python3 manage.py runserver
