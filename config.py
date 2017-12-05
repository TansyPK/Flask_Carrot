import os
SECRET_KEY = '\xe2\xae\xd7\xef\xc8\x0e\xff\xed\x0c\xbf\xbf\x8e\xe0\x9d'
UPLOADED_PHOTOS_DEST=os.getcwd() + '/Blog/static/Koiphotos_static/photos'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:SmileGirl@123@localhost:3306/flask_blog?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# MAIL_SERVER = 'smtp.163.com'
# MAIL_PORT = '465'
# MAIL_USE_SSL = True
# MAIL_USE_TLS = False
# MAIL_USERNAME = 'koicarrot@163.com'
# MAIL_PASSWORD = 'KoiCarrot123'
# MAIL_DEFAULT_SENDER = 'koicarrot@163.com'
