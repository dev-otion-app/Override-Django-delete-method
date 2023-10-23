This repository demonstrates what is explained in https://dev-otion.com/en/entry/how-to-correctly-override-the-delete-method-in-a-model

In order to install the minimal requirements to use this example, create a virutial environment with Python 3.11.4 and run `pip install -r requirements.txt`

You can find some images to carry out your tests in the `img` folder. The SQlite database provided in the repository contains the AppModel used in the example, if you want to modify the models remember to carry out the migrations. An admin user is already defined:
    - ID: admin
    - Password: 123456
You can create as many admins as you need by running `python manage.py createsuperuser`