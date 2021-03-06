import os 
basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
FLASKY_MAIL_SENDER = 'Kurosawa Geeker <363876315@qq.com>'
#FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
FLASK_POSTS_PER_PAGE = 10 #每个页面的博文最大数目
FLASKY_ADMIN = '363876315@qq.com'
MAIL_SERVER = 'smtp.qq.com'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:YES@localhost/test11'
SQLALCHEMY_TRACK_MODIFICATIONS = False
#MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
#MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_USERNAME = '363876315@qq.com'
MAIL_PASSWORD = 'wyj83152515'
MAIL_USE_TLS = True
MAIL_PORT = 587
""" class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <wuyajungood@126.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:YES@localhost/test2'    #此处应该为不同的数据库

class TestingConfig(Config): 
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:YES@localhost/test2'    #此处应该为不同的数据库

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:YES@localhost/test2'    #此处应该为不同的数据库

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
} """