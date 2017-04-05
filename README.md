# SETUP

## Setting up Heroku (one-time)
This assumes that you're using the command line:
- Create app with `$ heroku create myawesomeapp` where your actual app name replaces `myawesomeapp`
- Set buildpack with `$heroku buildpacks:set heroku/python`


## Local setup

- Clone github repository into a newly created folder: `$ git clone https://github.com/emunsing/flaskblockchain.git` 
- Create virtual environment by running `$ virtualenv env`
- Set environment variables by running  `$ source .env`
- Install required Python packages with `$ pip install -r requirements.txt
- Associate heroku repository by running`$ git remote add stage git@heroku.com:myawesomapp.git`
- Run a local server with `$ python myaweseomapp.py`
- Go to http://localhost:5000 and see results!