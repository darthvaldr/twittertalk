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
$ git clone https://github.com/darthvaldr/twittertalk.git
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
