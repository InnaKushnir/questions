#### Questions

RESTful API for Questions  progects.

 #### Features
* Users can register, login  in the Questions  using username and password.
* The API allows for manage and store pdf files.
* The API allows create questions.
* The API allows to get answers using LangChain.


#### Installation
##### Python3 must be already installed.
```
git clone https://github.com/InnaKushnir/questions
cd questions
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```
* Copy .env.sample -> .env and populate with all required data.

#### Run the following necessary commands
```
python manage.py migrate
```

#### Test user

* Email: `admin@gmail.com`
* Password: `12345admin`

* Register on the website using the link.

`http://127.0.0.1:8000/api/user/register/`

* Get the token using the link. 

`http://127.0.0.1:8000/api/user/login/`


