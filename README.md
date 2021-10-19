# SHORTENER
## _The Best Shorten API in the market_

SHORTENER was born from a coding exercise from the folk at element.io - This API allow users to do what shortener API does best: shorten url, redirect from a shorten url and lookup for an original url. You can also choose the type of serialization that you prefer between 'json' or 'xml'. 


## Features

- Create a shorten url (for any type of url)
- Lookup for an original URL by using the identifier found in the shorten URL
- Redirect to the original URL
- Choose between the 2 following serialization: 'json' or 'xml'
- Easy to deploy thanks to the inlude docker-compose.yaml file

The above features come out the box with this first version. It is easy to add new feature, to make sure that this fantastic could go toe to with the leader of the shortener market (naming: bit.ly 😃)
As [Mike] once said:

> If you have a great product, there no reason 
> that people won't use it.

## Tech

SHORTENER uses a number of open source projects to work properly:
 [Python] - One of the best coding language out there
- [Flask] - Flask is a micro web framework written in Python. (Make it easy to create APIs)
- [GUNICORN] - The Gunicorn "Green Unicorn" is a Python Web Server Gateway Interface HTTP server.
- [Docker] - The number 1 container runtime. Allow to build, share and run any app easily.
- [Docker-compose] - A great tool to spin a set of containers in one go
- [Git] - Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. 
- [MongoDB] - A NoSQL database that has proved it woth. Used by million and loved by million. One of the best reliable NoSQL and fast Databases out there.
- [Python-simplexml] - A tool that make it easy to return xml serialization format

And of course SHORTENER is an open-source project, anyone can participate on the success of this great product.

## Installation

To start using SHORTNER, you will need docker and docker-compose to be installed in the machine that will run the app.

To start using SHORTNER, you will need to do the following:

(use the available public image: milguad/shorten:v0.1.0)

1 - Clone this project and edit the docker-compose.yaml file with your the values of the environment variables that you want:
```
MONGO_INITDB_ROOT_USERNAME: <choose_an_admin_username>
MONGO_INITDB_ROOT_PASSWORD: <choose_an_admin_password>
FLASK_ENV : <run_either_in_production_or_in_developement_mode> "production" or "developement"
SECRET_KEY : <add_a_secret_key_here>
MONGOHOST : 'db'
MONGOPORT : '27017'
MONGOUSER : '<use_same_admin_user>'
MONGOPASSWORD : '<use_same_admin_user_password>'
RESPONSE_FORMAT : 'json'
```

For production environments...
It is advisable to use a .env file to avoid leaking secret such as password to the docker-compose file.
```
MONGOUSER : '<create_a_separate_user_from_admin>'
MONGOPASSWORD : '<create_a_separate_user_from_admin>'
```
To start the app, use docker-compose with the following command:
```
$ docker-compose up -d
```
if no error, the app will be available on the URL connected to your server such as on a local machine:
```
 http://localhost:5050
```

## Start using the app

Here are the following routes available to you:

- To shorten a url:
```
$ <BASE_URL>/api/v1/shorten [POST]
```
You can shorten a url by doing a POST call to the above route as follow:
```
$ curl -XPOST http://localhost:5050/api/v1/shorten \
    -H "Content-Type: application/json" \ 
    -d '{"url":"<url_to_shorten>"}'
```

Reply from the API (json example):
```
{
  "status_code": "200", 
  "url_shorten": "http://localhost:5050/sekKBjo"
}
```

- To find the original url from the identifier:
```
$ <BASE_URL>/api/v1/lookup/<identifier> [GET]
```
For example:
```
$ curl -XGET http://localhost:5050/api/v1/lookup/<short_url_identifier>
```
Reply from the API (json example):
```
{
  "original_url": "https://google.com", 
  "status_code": 200
}
```


- To be redirected:

Go to your browser and insert the short URL to the navigation bar.
You will then be redirected to the original website

```
$ localhost:5050/sekKBjo
```

Et voila!