class Config(object):
	CSRF_ENABLED = True
	SECRET_KEY = '1324'
class Production(Config):
	debug = True
	CSRF_ENABLED = False
	#ADMIN = "zeros19861@gmail.com"
	SQLALCHEMY_DATABASE_URL = "mysql://owen:Sksdhdnps86!@gach.cqesbxxoyeoo.us-west-2.rds.amazonaws.com/gach"
	migration_directory = 'mig'