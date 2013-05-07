class DatabaseConfig(object):
	MONGOALCHEMY_DATABASE = 'FTS-Flask'
	MONGOALCHEMY_SERVER_AUTH = False
	MONGOALCHEMY_USER = 'jerry'
	MONGOALCHEMY_PASSWORD = 'seinfeld'
	MONGOALCHEMY_SERVER = 'linus.mongohq.com'
	MONGOALCHEMY_PORT = 10066

class FlaskConfig(object):
    APP_NAME='FTS_FLASK'
    DEBUG='TRUE'
