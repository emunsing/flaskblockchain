class Config(object):
	HEROKU = False
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	ETHNETWORK = False

class HerokuConfig(Config):
	HEROKU      = True
	DEVELOPMENT = False
	DEBUG       = False
	ETHEREUM    = False
	ETHNETWORK  = False

class LocalNoEthereum(Config):
	DEVELOPMENT = True
	DEBUG       = True
	ETHEREUM    = False
	ETHNETWORK  = False

class LocalEthereumNoNetwork(Config):
	DEVELOPMENT = True
	DEBUG       = True
	ETHEREUM    = True
	ETHNETWORK  = False

class LocalEthereumNetwork(Config):
	DEVELOPMENT = True
	DEBUG       = True
	ETHEREUM    = True
	ETHNETWORK  = True