# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################





def search():
    car = db().select(db.car.ALL, orderby=db.car.location_)

    
    formFake = FORM(INPUT(_id='fake',_name='fake', _type="checkbox",
              _onkeyup="ajax('', ['fake'], '');"), "Click here to find ALL" )
    
    formA=FORM(INPUT(_id='keyword1',_name='keyword1',
              _onkeyup="ajax('callbackOne', ['keyword1'], 'target56');"))
              
        
    formB=FORM(INPUT(_id='keyword2',_name='keyword2',
              _onkeyup="ajax('callbackTwo', ['keyword2'], 'target57');"))
        
    formC=FORM(INPUT(_id='keyword3',_name='keyword3',
              _onkeyup="ajax('callbackThree', ['keyword3'], 'target58');"))
              
    
    return dict(car=car, formFake=formFake,formA=formA, formB=formB, formC=formC, target_divA=DIV(_id='target56'),target_divB=DIV(_id='target57'),target_divC=DIV(_id='target58') 
)

def callbackOne():
    
    query = db.car.location_.contains(request.vars.keyword1)
    pages = db(query).select(orderby=db.car.location_)
    links = [A(p.location_ + " to " + p.destination, _href=URL('show',args=p.id)) for p in pages]
    return UL(*links)

def callbackTwo():
    
    query = db.car.destination.contains(request.vars.keyword2)
    pages = db(query).select(orderby=db.car.destination)
    links = [A(p.location_ + " to " + p.destination, _href=URL('show',args=p.id)) for p in pages]
    return UL(*links)

def callbackThree():
    
    query = db.car.name.contains(request.vars.keyword3)
    pages = db(query).select(orderby=db.car.name)
    links = [A(p.location_ + " to " + p.destination + ", driver: " + p.name, _href=URL('show',args=p.id)) for p in pages]
    return UL(*links)

@auth.requires_login()
def userPage():
    this_userPage = request.args(0,cast=int)
    userName = db.auth_user(this_userPage)
    name = db.car.name
    pages = db(db.car.created_by==this_userPage).select(db.car.id,db.car.location_,db.car.destination,orderby=db.car.location_)
    return locals()
	 
@auth.requires_login()
#def manage():
 #   grid = SQLFORM.grid(db.car.created_by==auth.user_id)
  #  return locals()

@auth.requires_login()
def edit():
    t=db.car
    rec = t(request.args(0))
    
    #if request.post_vars.username:
    #    db.car.username.requires = IS_IN_DB(db,auth_table.username) 
    
    
    form = SQLFORM(db.car, request.args(0), deletable=True, upload=URL(r=request, f='download'))
    if form.accepts(request.vars, session):
        if not form.record:
            response.flash = 'Your input data has been submitted.'
        else:
            if form.vars.delete_this_record:
                session.flash = 'User record successfully deleted.'
            else:
                session.flash = 'User record successfully updated.'
            redirect(URL(r=request, f='edit'))
    records = db().select(db.car.ALL)
    posts = db().select(db.car.ALL, orderby=db.car.created_on)

    return dict(form=form, records=records, posts=posts)

@auth.requires_login()
def create():
    db.car.created_on.writable=False
    db.car.created_on.readable=True
    db.car.name.default = auth.user.first_name, auth.user.last_name
    form = SQLFORM(db.car).process(next=URL('index'))
    return dict(form=form)
        
def index():
    car = db().select(db.car.ALL, orderby=db.car.location_)

    formB=FORM(INPUT(_id ='box2', _name="box2", _type="checkbox" , _onclick="ajax('tuesday', ['box2'], 'target2');" ), "Tuesday")
    formC=FORM(INPUT(_id ='box3', _name="box3", _type="checkbox" , _onclick="ajax('wednesday', ['box3'], 'target3');" ), "Wednesday")
    formD=FORM(INPUT(_id ='box4', _name="box4", _type="checkbox" , _onclick="ajax('thursday', ['box4'], 'target4');" ), "Thursday")
    formE=FORM(INPUT(_id ='box5', _name="box5", _type="checkbox" , _onclick="ajax('friday', ['box5'], 'target5');" ), "Friday")
    formF=FORM(INPUT(_id ='box6', _name="box6", _type="checkbox" , _onclick="ajax('saturday', ['box6'], 'target6');" ), "Saturday")
    formG=FORM(INPUT(_id ='box7', _name="box7", _type="checkbox" , _onclick="ajax('sunday', ['box7'], 'target7');" ), "Sunday")
    


    
    
    
    
    return dict(car=car, formB=formB, formC=formC, formD=formD, formE=formE, formF=formF, formG=formG,formA=FORM(INPUT(_id ='box', _name="box", _type="checkbox" , _onclick="ajax('monday', ['box'], 'target');" ), "Monday"),
                target_div=DIV(_id='target'), 
                target_div2=DIV(_id='target2'),
                target_div3=DIV(_id='target3'),
                target_div4=DIV(_id='target4'),
                target_div5=DIV(_id='target5'),
                target_div6=DIV(_id='target6'), 
                target_div7=DIV(_id='target7'))
               
               

def monday():    

    find = db.car.monday
    found_post = db(find==True).select(orderby=db.car.created_on)
    all_post = [A(p.location_ +" to "+ p.destination, _href=URL("show",args=p.id)) for p in found_post]

    return UL(*all_post)

def tuesday():
    find = db.car.tuesday

    found_post = db(find==True).select(orderby=db.car.created_on)
    all_post = [A(p.location_ +" to "+ p.destination, _href=URL("show",args=p.id)) for p in found_post]
    return UL(*all_post)

def wednesday():    
    find = db.car.wednesday
    found_post = db(find==True).select(orderby=db.car.created_on)
    all_post = [A(p.location_ +" to "+ p.destination, _href=URL("show",args=p.id)) for p in found_post]
    return UL(*all_post)

def thursday():    
    find = db.car.thursday
    
       
    found_post = db(find==True).select(orderby=db.car.created_on)
    all_post = [A(p.location_ +" to "+ p.destination, _href=URL("show",args=p.id)) for p in found_post]
    return UL(*all_post)


def friday():    
    find = db.car.friday
    
    found_post = db(find==True).select(orderby=db.car.created_on)
    all_post = [A(p.location_ +" to "+ p.destination, _href=URL("show",args=p.id)) for p in found_post]
    return UL(*all_post)

def saturday():    
    find = db.car.saturday
   
    found_post = db(find==True).select(orderby=db.car.created_on)
    all_post = [A(p.location_ +" to "+ p.destination, _href=URL("show",args=p.id)) for p in found_post]
    return UL(*all_post)

def sunday():    
    find = db.car.sunday
    
    found_post = db(find==True).select(orderby=db.car.created_on)
    all_post = [A(p.location_ +" to "+ p.destination, _href=URL("show",args=p.id)) for p in found_post]
    return UL(*all_post)




def show():
    from gluon.tools import Mail
    mail = Mail()
    #mail.settings.server = 'smtp.gmail.com'
    mail.settings.server = 'logging'
    mail.settings.sender = 'garslough@gmail.com'
    mail.settings.login = 'garslough@gmail.com:password'
    
    
    
    
    
    this_page = db.car(request.args(0,cast=int)) or redirect(URL('index'))
    db.test.test_id.default = this_page.id
    db.test.test_id.writeable=db.test.test_id.readable=False

    
    
    db.test.body.writeable=False 
    db.test.body.readable=False
    
    
    if auth.user:
        db.test.body.default = auth.user.first_name +" "+ auth.user.last_name + " says they are coming, email: " + auth.user.email
    else:
        None

    form=None  
    if auth.user:
        form = SQLFORM(db.test)#db.cmnt) 
        if form.process().accepted:
            session.name = auth.user.first_name + auth.user.last_name
            session.email = auth.user.email
            session.subject = "Carpool Reminder"
            session.message = URL(args=request.args, vars=request.get_vars, host=True)
            if mail:
                if mail.send(to=[auth.user.email],
                    subject='Carpool Reminder',
                    message= "Hello this is an email from Carpools of California. \nName:"+ session.name+" \nEmail : " + session.email +"\nSubject : "+session.subject +"\nMessage : "+session.message+ ".\n "
                    ):
                    response.flash = 'email sent sucessfully.'
                else:
                    response.flash = 'fail to send email sorry!'
            else:
                response.flash = 'Unable to send the email : email parameters not defined'
        elif form.errors:
            response.flash='form has errors.'
    else: 
        None
    
    pagecomments = db(db.test.test_id==this_page.id).select()
    return dict(card=this_page, comments=pagecomments, form=form)



    


@auth.requires_login()
def report():
    db.report.your_email.readable = db.report.your_email.writable = False
    db.report.your_email.default = auth.user.email
    
    
    form = SQLFORM(db.report).process()
    return dict(form=form)
  
    


    


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
