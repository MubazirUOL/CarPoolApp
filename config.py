class Config:
    SECRET_KEY = 'supersecretkey'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///carpool.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False