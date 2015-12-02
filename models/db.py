# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

## app configuration made easy. Look inside private/appconfig.ini
from gluon.contrib.appconfig import AppConfig
## once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)


if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL(myconf.take('db.uri'), pool_size=myconf.take('db.pool_size', cast=int), check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## choose a style for forms
response.formstyle = myconf.take('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.take('forms.separator')


## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
## (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=True, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.take('smtp.server')
mail.settings.sender = myconf.take('smtp.sender')
mail.settings.login = myconf.take('smtp.login')

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

from gluon.tools import Auth
auth = Auth(db, hmac_key=Auth.get_or_create_key())
auth_table = auth.settings.table_user




NE = IS_NOT_EMPTY()
db.define_table(
    'car',
    Field('location_'),
    Field('destination'),
    Field('name'),
    Field('phone_number', 'string'),
    Field('monday','boolean',default=False),
    Field('tuesday','boolean',default=False),
    Field('wednesday','boolean',default=False),
    Field('thursday','boolean',default=False),
    Field('friday','boolean',default=False),
    Field('saturday','boolean',default=False),
    Field('sunday','boolean',default=False),    
    Field('comments','text'),
    Field('created_by', 'reference auth_user', default=auth.user_id),
    Field('created_on', 'datetime', default=request.now),
    format='%(created_on)s')

db.car.name.readable = db.car.name.writable = False
db.car.created_by.readable = db.car.created_by.writable = False
db.car.created_on.readable = db.car.created_on.writable = False



db.define_table('cmnt',
    Field('post_id', 'reference car'),
    Field('body', 'text'),
    Field('created_on', 'datetime', default=request.now),
    Field('created_by', 'reference auth_user', default=auth.user_id))

db.cmnt.body.readable = db.cmnt.body.writable = False    


db.define_table('test',
    Field('test_id', 'reference car'),
    Field('body', 'text'),
    Field('created_on', 'datetime', default=request.now),
    Field('created_by', 'reference auth_user', default=auth.user_id))
                

db.test.test_id.readable = db.test.test_id.writable = False    
db.test.created_on.writable = False    
db.test.created_on.readable = False
db.test.created_by.readable = db.test.created_by.writable = False   
db.test.body.readable = db.test.body.writable = False    



db.define_table('report',
    Field("your_email"),
    Field("offender_name"),
    Field("describe_complaint",'text'),
    Field('created_on', 'datetime', default=request.now))

db.report.offender_name.requires = IS_NOT_EMPTY()
db.report.your_email.requires = IS_EMAIL()
db.report.describe_complaint.requires = IS_NOT_EMPTY()
db.report.created_on.readable = db.report.created_on.writable = False    
    
    
    
                
db.cmnt.body.requires = IS_NOT_EMPTY()
db.cmnt.post_id.readable = db.cmnt.post_id.writable = False
db.cmnt.created_by.readable = db.cmnt.created_by.writable = False
db.cmnt.created_on.readable = db.cmnt.created_on.writable = False






auth.enable_record_versioning(db)
