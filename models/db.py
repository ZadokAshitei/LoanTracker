from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth
from gluon.tools import Crud
configuration = AppConfig(reload=True)

db= DAL("sqlite://storage.sqlite")
crud = Crud(db)
crud.settings.controller = 'default'
auth = Auth(db)
auth.settings.login_next = URL('index')
auth.settings.logout_next = URL('login')
auth.settings.login_url = URL('login')
auth.settings.register_next = URL('login')


auth.define_tables()

db.define_table('loans',
                Field('loaneeName'),
                Field('loaneeContact', 'integer'),
                Field('amountLoaned', 'float'),
                Field('loaneeAddress'),
                Field('dueDate', 'date'),
                auth.signature
                )
