def login():
    return dict()

def loginProcess():
     email = request.vars.email
     password = request.vars.password
     if not auth.login_bare(email, password):
         redirect(URL('login'))
     redirect(URL('index'))

# def signup():
#     submittted_firstname = request.vars.firstName
#     submittted_lastname = request.vars.lastName
#     submittted_email = request.vars.email
#     submittted_password = request.vars.password
#
#     result = db.auth_user.insert(
#             firstName = submittted_firstname,
#             lastName = submittted_lastname,
#             email = submittted_email,
#             password = submittted_password
#     )
#
#     if result:
#         return "Account Created Succesfully"
#     else:
#         return "Error"
#
#     return dict()

@auth.requires_login()
def addLoanee():
    form = crud.create(db.loans, next=URL('index') , message = T("New Loanee Added"))
    return dict(form=form)

def user():
    return dict(form=auth())

@auth.requires_login()
def index():
    loans = db(db.loans.created_by==auth.user).select()
    return dict(loans=loans)

def viewLoanee():
    return dict(form = crud.read(db.loans,request.args(0)) )

def editLoan():
    return dict(form = crud.update(db.loans, request.args(0), next=URL('index'), message = T("Loan Details Editted")))

def deleteLoan():
    crud.delete(db.loans, request.args(0),next=URL('index'),message = T("Loan Deleted"))

def userProfile():
    return dict(form=auth.profile())

def change_password():
    return dict(form=auth.change_password())

def register():
    return dict()

def registerProcess():
     firstName = request.vars.firstName
     lastName = request.vars.lastName
     email = request.vars.email
     password = request.vars.password
     if not auth.register_bare(first_name=firstName,last_name=lastName,email=email, password=password):
         redirect(URL('register'))
     redirect(URL('login'))
