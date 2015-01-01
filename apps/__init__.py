from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
import os


app = Flask('gach')
app.config.from_object('apps.config.Production')
if __name__ == '__main__':
    app.run()
import controller, models