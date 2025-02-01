import os

class Config:
#    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://neondb_owner:GBYUhV93gPwC@ep-wispy-art-a4rjnsko.us-east-1.aws.neon.tech/neondb?sslmode=require')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://uhwtvgcnoburkmaj:6cPBd5hT6j3HSQHgDf34@b0ilsbp5axpf1cdf0y8e-mysql.services.clever-cloud.com:3306/b0ilsbp5axpf1cdf0y8e')	
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)  # or another method to set a secret key
	
	


