class Config(object):
	CSRF_ENABLED = True
	SECRET_KEY = '1324'
class Production(Config):
	debug = True
	CSRF_ENABLED = False
	ADMIN = "zeros19861@gmail.com"
	SQLALCHEMY_DATABASE_URL = "'mysql+gaerdbms:///accusation?instance=owenahn:owen'"
	migration_directory = 'mig'