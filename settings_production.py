from settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG


DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',
        'NAME': '/var/EoSGP201011/database.db',
    }
}

ADMINS = (
	('EoSGP Admins', 'eos.gospelpartnership@gmail.com'),
)
