# Twitter Talk

An implementation of the [eliza chatbot](http://www.nltk.org/_modules/nltk/chat/eliza.html) which i've wrapped in a modified version of Andy Pipers twitter [sample-python-autoreply](https://github.com/twitterdev/sample-python-autoreply) and dockerized it for ease of deployment.

## Getting Started

Nothing magical required, if the docker section is complete you would just need docker on your system and be able to run docker commands you're good to go.

### Prerequisites

* docker installed on your system
* twitter app account
	* api & secret keys from this account
* (optional) a heroku account 

### Built with

* Python 3.6
* NLTK
* Docker

### Install / Build

pull the repo

```bash
$ git clone https://URL-TO-THIS-REPO/twittertalk.git
```

*required or the app wont build properly:*
edit the `twitter_settings.py` file and put your twitter account api and secret keys:

for example:
```
MY_CONSUMER_KEY = ‘XXXXXXXXXXXXXXXXXXXXXXXXX’
MY_CONSUMER_SECRET = ‘XXXXXXXXXXXXXXXXXXXXXXX’
MY_ACCESS_TOKEN_KEY = ‘XXXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXX’
MY_ACCESS_TOKEN_SECRET = ‘XXXXXXXXXXXXXXXXXXXXXXXXXX’
RULE = ‘bot_account_name’
SCREEN_NAME = ‘bot_screen_name’
USER_ID = ‘bot_account_name’
```

build it

```bash
$ docker build -t twittertalk .
```


### Run

docker run the app

```bash
$ docker run -t twittertalk
```

### Test?

sorry, haven't written any tests (really need to get my test-writing game up!) but just go and talk to your bot account and watch it respond with some sh!t.


### TODO:

* heroku deploy automation (maybe?)
* a Makefile under /app for ease of re-building
* easy way to turn DEBUG on/off

### Credits

thanks to Andy Pipers python work saved me time figuring that part out.