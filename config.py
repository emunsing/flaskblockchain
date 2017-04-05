class Config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True

class HerokuConfig(Config):
	DEVELOPMENT = False
	DEBUG       = False
	ETHEREUM    = False
	ETJMETWPRL  = False

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