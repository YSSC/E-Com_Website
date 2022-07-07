import shelve, User, Customer, Card, courseType, Inventorys, Supplier, Product, Detail, Voucher, Point
from flask import Flask, render_template, request, redirect, url_for, session, flash, Response
from Forms import CreateUserForm, CreateCustomerForm, ChangeEmail, LoginForm, Cardpayment, ChangePassword, ChangePhoneNumber, Forgetpassword, EditProfile, CreateOnCourseForm, CreateOffCourseForm, CreateSupplierForm, CreateOrderForm, CreateWarehouseForm, CreateProductForm, CreateDetailForm
from Forms_rewards import CreateVoucherForm, CreatePointForm
from PIL import Image
import os
import os.path

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

basedir = os.getcwd()
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def home():
    if os.path.isfile('offcourse.db.dat') is False:
        db = shelve.open('offcourse.db', 'c')
        db['OffCourses'] = {}
        db.close()
    if os.path.isfile('oncourse.db.dat') is False:
        db = shelve.open('oncourse.db', 'c')
        db['OnCourses'] = {}
        db.close()
    return render_template('home.html')


@app.route('/home2')
def home2():
    return render_template('home2.html')


@app.route('/home3')
def home3():
    session['admin'] = '3'
    return render_template('home3.html')


@app.route('/AdminHome')
def AdminHome():
    return render_template('AdminHome.html')


@app.route('/staffdashboard')
def staffdashboard():
    return render_template('staffdashboardtry.html')


@app.route('/staffdashboardmonth')
def staffdashboardmonth():
    return render_template('staffdashboardmonth.html')


@app.route('/custdashboard')
def custdashboard():
    return render_template('custdashboardtry.html')


@app.route('/custdashboardmonth')
def custdashboardmonth():
    return render_template('custdashboardmonth.html')


@app.route('/signupsuccessC')
def signupsuccessC():
    return render_template('signupsuccess4c.html')


@app.route('/signupsuccessS')
def signupsuccessS():
    return render_template('signupsuccess4s.html')


@app.route('/signout')
def signout():
    session.pop('email', None)
    return render_template('signout.html')


@app.route('/custprofile')
def custprofile(card=None, customer=None):
    customers_dict = {}
    db = shelve.open('customer.db', 'r')
    customers_dict = db['Customers']
    db.close()
    customers_list = []

    for key in customers_dict:
        if 'email' in session:
            if session['email'] == customers_dict.get(key).get_email():
                customer = customers_dict.get(key)
                print(customers_dict.get(key).get_email())

    card_dict = {}
    db = shelve.open('card.db', 'c')
    card_list = []

    if 'Cards' in db:
        try:
            card_dict = db['Cards']
        except:
            print('Error in opening card.db')
    else:
        db['Cards'] = card_dict

    for key in card_dict:
        if 'card' in session:
            if session['card'] == card_dict.get(key).get_cnum():
                card = card_dict.get(key)
                print(card_dict.get(key).get_cnum())

    return render_template('custprofile.html', count=len(customers_list), customers_list=customers_list, customer=customer, card=card, card_list=card_list)


@app.route('/adminprofile')
def adminprofile(user=None):
    users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()
    users_list = []

    for key in users_dict:
        if session['email'] == users_dict.get(key).get_email():
            user = users_dict.get(key)
            print(users_dict.get(key).get_email())

    return render_template('adminprofile.html', count=len(users_list), users_list=users_list, user=user)


@app.route('/editadmprofile/<int:id>/', methods=['GET', 'POST'])
def editadmprofile(id):
    editprofile = EditProfile(request.form)
    if request.method == 'POST' and editprofile.validate():
        users_dict = {}
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']
        session['email'] = editprofile.email.data
        user = users_dict.get(id)
        user.set_first_name(editprofile.first_name.data)
        user.set_last_name(editprofile.last_name.data)
        user.set_gender(editprofile.gender.data)
        user.set_email(editprofile.email.data)
        user.set_phonenumber(editprofile.phonenumber.data)

        db['Users'] = users_dict
        db.close()
        session['adminprofile_updated'] = 'Your profile has been updated successfully!'
        return redirect(url_for('adminprofile'))
    else:
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(id)
        editprofile.first_name.data = user.get_first_name()
        editprofile.last_name.data = user.get_last_name()
        editprofile.gender.data = user.get_gender()
        editprofile.email.data = user.get_email()
        editprofile.phonenumber.data = user.get_phonenumber()
    return render_template('editadmprofile.html', form=editprofile)


@app.route('/change_email/<int:id>/', methods=['GET', 'POST'])
def change_email(id):
    change_email = ChangeEmail(request.form)
    if request.method == 'POST' and change_email.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'w')
        customers_dict = db['Customers']
        customer = customers_dict.get(id)
        customer.set_email(change_email.confirmnewemail.data)
        session['email'] = change_email.newemail.data
        db['Customers'] = customers_dict
        db.close()
        session['email_updated'] = 'Your email has been updated successfully!'
        return redirect(url_for('custprofile'))
    else:
        customers_dict = {}
        db = shelve.open('customer.db', 'r')
        customers_dict = db['Customers']
        db.close()

        customer = customers_dict.get(id)
        change_email.currentemail.data = customer.get_email()
    return render_template('change_email.html', form=change_email)


@app.route('/change_phonenumber/<int:id>/', methods=['GET', 'POST'])
def change_phonenumber(id):
    change_phonenumber = ChangePhoneNumber(request.form)
    if request.method == 'POST' and change_phonenumber.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'w')
        customers_dict = db['Customers']
        customer = customers_dict.get(id)
        customer.set_phonenumber(change_phonenumber.confirmnewphone.data)
        db['Customers'] = customers_dict

        db.close()
        session['phonenumber_updated'] = 'Your phone number has been updated successfully!'
        return redirect(url_for('custprofile'))
    else:
        customers_dict = {}
        db = shelve.open('customer.db', 'r')
        customers_dict = db['Customers']
        db.close()

        customer = customers_dict.get(id)
        change_phonenumber.currentphone.data = customer.get_phonenumber()
    return render_template('change_phonenumber.html', form=change_phonenumber)


@app.route('/change_password/<int:id>/', methods=['GET', 'POST'])
def change_password(id):
    change_password = ChangePassword(request.form)
    if request.method == 'POST' and change_password.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'w')
        customers_dict = db['Customers']
        customer = customers_dict.get(id)
        customer.set_password(change_password.confirmnewpassword.data)

        db['Customers'] = customers_dict
        db.close()
        session['password_updated'] = 'Your password has been updated successfully!'
        return redirect(url_for('custprofile'))
    else:
        customers_dict = {}
        db = shelve.open('customer.db', 'r')
        customers_dict = db['Customers']
        db.close()

        customer = customers_dict.get(id)
        change_password.currentpassword.data = customer.get_password()
    return render_template('change_password.html', form=change_password)


@app.route('/cardpayment', methods=['Get', 'Post'])
def cardpayment(error=None):
    cardpayment = Cardpayment(request.form)
    if request.method == 'POST' and cardpayment.validate():
        card_dict = {}
        db = shelve.open('card.db', 'c')
        try:
            card_dict = db['Cards']
        except:
            print("Error in retrieving Cards from card.db.")

        card = Card.Card(cardpayment.cname.data, cardpayment.cnum.data, cardpayment.expiry.data, cardpayment.cvv.data,
                         cardpayment.address.data, cardpayment.city.data, cardpayment.state.data, cardpayment.postalcode.data)

        for key in card_dict:
            card = card_dict.get(key)
            session['card'] = card_dict.get(key).get_cnum()

        card_dict[card.get_card_id()] = card
        db['Cards'] = card_dict
        db.close()
        session['c_d_card_added'] = 'Your card has been added!'
        return redirect(url_for('custprofile'))

    return render_template('cardpayment.html', form=cardpayment, error=error)


@app.route('/deleteCard/<int:id>', methods=['POST', 'GET'])
def delete_card(id):
    card_dict = {}
    db = shelve.open('card.db', 'w')
    card_dict = db['Cards']

    card_dict.pop(id)

    db['Cards'] = card_dict
    db.close()

    return redirect(url_for('custprofile'))


@app.route('/forgetpassword', methods=['Get', 'Post'])
def forgetpassword(error=None):
    forgetpassword = Forgetpassword(request.form)
    if request.method == 'POST' and forgetpassword.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'w')
        customers_dict = db['Customers']
        for key in customers_dict:
            if forgetpassword.email.data == customers_dict.get(key).get_email():
                error=None
                session['email_sent'] = 'Please check your email to reset your password!'
                return redirect(url_for('home'))
            else:
                error = 'wrongemail'
                break

        db['Customers'] = customers_dict
        db.close()

    elif request.method == 'POST' and forgetpassword.validate():
        users_dict = {}
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']
        for key in users_dict:
            if forgetpassword.email.data == users_dict.get(key).get_email():
                error=None
                session['email_sent'] = 'Please check your email to reset your password!'
                return redirect(url_for('home'))
            else:
                error = 'wrongemail'
                break

        db['Users'] = users_dict
        db.close()

    return render_template('forgetpassword.html', form=forgetpassword, error=error)


@app.route('/LoginS', methods=['GET', 'POST'])
def Staff(error=None):
    Login_user_form = LoginForm(request.form)
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'c')

        try:
            users_dict = db['Users']
            users_list = []
            for key in users_dict:
                users = users_dict.get(key)
                users_list.append(users)
            for users in users_list:
                User.User.count_id = users.get_user_id()
        except:
            print("Error in retrieving Users from user.db.")

        for key in users_dict:
            if create_user_form.email.data == users_dict.get(key).get_email():
                error = 'account_created_alr'
                break
        else:
            user = User.User(create_user_form.first_name.data, create_user_form.last_name.data,
                             create_user_form.gender.data, create_user_form.email.data,
                             create_user_form.phonenumber.data, create_user_form.dateofbirth.data,
                             create_user_form.jobscope.data, create_user_form.password.data,
                             create_user_form.confirmpassword.data, create_user_form.status.data)

            users_dict[user.get_user_id()] = user
            db['Users'] = users_dict
            db.close()
            return redirect(url_for('signupsuccessS'))

    elif request.method == 'POST' and Login_user_form.validate():
        db = shelve.open('user.db', 'r')
        session_dict = shelve.open('session.db', 'c')
        user_id_dict = {}
        try:
            if 'loginUser' in session_dict:
                user_id_dict = session_dict['loginUser']
            else:
                session_dict['loginUser'] = user_id_dict
        except:
            print("Error in loginUser session")

        try:
            users_dict = db['Users']
            for key in users_dict:
                user = users_dict.get(key)
                userid = user.get_user_id()

                if Login_user_form.email.data == users_dict.get(key).get_email():
                    if Login_user_form.password.data == users_dict.get(key).get_password():
                        error=None
                        user_id_dict['user_id'] = userid
                        session_dict['loginUser'] = user_id_dict
                        session['email'] = users_dict.get(key).get_email()
                        db.close()
                        session['user_created'] = 'Hi, ' + user.get_first_name() + ' ' + user.get_last_name() + '!'
                        return redirect(url_for('AdminHome'))
                    else:
                        error = 'wrongpassword'
                        break
            else:
                flash("No Account Made! Please proceed to sign up!")
        except:
            print('Error in retrieving Users from user.db.')

    return render_template('Login(S).html', form=create_user_form, form2=Login_user_form, error=error)


@app.route('/LoginC', methods=['GET', 'POST'])
def Customers(error=None):
    Login_customer_form = LoginForm(request.form)
    create_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and create_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'c')
        try:
            customers_dict = db['Customers']
            customers_list = []
            for key in customers_dict:
                customers = customers_dict.get(key)
                customers_list.append(customers)
            for customers in customers_list:
                Customer.Customer.count_id = customers.get_customer_id()
        except:
            print("Error in retrieving Customers from customer.db.")

        for key in customers_dict:
            if create_customer_form.email.data == customers_dict.get(key).get_email():
                error = 'account_created_alr'
                break
        else:
            customer = Customer.Customer(create_customer_form.first_name.data, create_customer_form.last_name.data,
                         create_customer_form.gender.data, create_customer_form.email.data,
                         create_customer_form.phonenumber.data, create_customer_form.dateofbirth.data,
                         create_customer_form.date_joined.data, create_customer_form.membership.data,
                         create_customer_form.address.data, create_customer_form.password.data,
                         create_customer_form.confirmpassword.data, create_customer_form.status.data)

            customers_dict[customer.get_customer_id()] = customer
            db['Customers'] = customers_dict
            db.close()
            return redirect(url_for('signupsuccessC'))

    elif request.method == 'POST' and Login_customer_form.validate():
        db = shelve.open('customer.db', 'r')
        try:
            customers_dict = db['Customers']
            for key in customers_dict:
                customer = customers_dict.get(key)

                if Login_customer_form.email.data == customers_dict.get(key).get_email():
                    if Login_customer_form.password.data == customers_dict.get(key).get_password():
                        error=None
                        session['email'] = customers_dict.get(key).get_email()
                        session['customer_created'] = 'Hi, ' + customer.get_first_name() + ' ' + customer.get_last_name() + '!'
                        return redirect(url_for('home2'))
                    else:
                        error = 'wrongpassword'
                        break
            else:
                flash("Account Not Made! Please proceed to Sign Up!")
        except:
            print("Error in retrieving Customers from customer.db.")

    return render_template('Login(C).html', form=create_customer_form, form2=Login_customer_form, error=error)


@app.route('/retrieveUsers')
def retrieve_users():
    users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()
    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

    return render_template('retrieveUsers.html', count=len(users_list), users_list=users_list)


@app.route('/retrieveCustomers')
def retrieve_customers():
    customers_dict = {}
    db = shelve.open('customer.db', 'r')
    customers_dict = db['Customers']
    db.close()

    customers_list = []
    for key in customers_dict:
        customer = customers_dict.get(key)
        customers_list.append(customer)

    return render_template('retrieveCustomers.html', count=len(customers_list), customers_list=customers_list)


@app.route('/updateUser/<int:id>/', methods=['GET', 'POST'])
def update_user(id):
    update_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']

        user = users_dict.get(id)
        user.set_first_name(update_user_form.first_name.data)
        user.set_last_name(update_user_form.last_name.data)
        user.set_gender(update_user_form.gender.data)
        user.set_email(update_user_form.email.data)
        user.set_phonenumber(update_user_form.phonenumber.data)
        user.set_dateofbirth(update_user_form.dateofbirth.data)
        user.set_jobscope(update_user_form.jobscope.data)
        user.set_password(update_user_form.password.data)
        user.set_confirmpassword(update_user_form.confirmpassword.data)
        user.set_status(update_user_form.status.data)

        db['Users'] = users_dict
        db.close()
        session['user_updated'] = user.get_first_name() + ' ' + user.get_last_name()
        return redirect(url_for('retrieve_users'))

    else:
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(id)
        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.gender.data = user.get_gender()
        update_user_form.email.data = user.get_email()
        update_user_form.phonenumber.data = user.get_phonenumber()
        update_user_form.dateofbirth.data = user.get_dateofbirth()
        update_user_form.jobscope.data = user.get_jobscope()
        update_user_form.password.data = user.get_password()
        update_user_form.confirmpassword.data = user.get_confirmpassword()
        update_user_form.status.data = user.get_status()

        return render_template('updateUser.html', form=update_user_form)


@app.route('/updateCustomer/<int:id>/', methods=['GET', 'POST'])
def update_customer(id):
    update_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and update_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'w')
        customers_dict = db['Customers']

        customer = customers_dict.get(id)
        customer.set_first_name(update_customer_form.first_name.data)
        customer.set_last_name(update_customer_form.last_name.data)
        customer.set_gender(update_customer_form.gender.data)
        customer.set_email(update_customer_form.email.data)
        customer.set_phonenumber(update_customer_form.phonenumber.data)
        customer.set_dateofbirth(update_customer_form.dateofbirth.data)
        customer.set_date_joined(update_customer_form.date_joined.data)
        customer.set_membership(update_customer_form.membership.data)
        customer.set_address(update_customer_form.address.data)
        customer.set_password(update_customer_form.password.data)
        customer.set_confirmpassword(update_customer_form.confirmpassword.data)
        customer.set_status(update_customer_form.status.data)

        db['Customers'] = customers_dict
        db.close()
        session['customer_updated'] = customer.get_first_name() + ' ' + customer.get_last_name()
        return redirect(url_for('retrieve_customers'))
    else:
        customers_dict = {}
        db = shelve.open('customer.db', 'r')
        customers_dict = db['Customers']
        db.close()

        customer = customers_dict.get(id)
        update_customer_form.first_name.data = customer.get_first_name()
        update_customer_form.last_name.data = customer.get_last_name()
        update_customer_form.gender.data = customer.get_gender()
        update_customer_form.email.data = customer.get_email()
        update_customer_form.phonenumber.data = customer.get_phonenumber()
        update_customer_form.dateofbirth.data = customer.get_dateofbirth()
        update_customer_form.date_joined.data = customer.get_date_joined()
        update_customer_form.membership.data = customer.get_membership()
        update_customer_form.address.data = customer.get_address()
        update_customer_form.password.data = customer.get_password()
        update_customer_form.confirmpassword.data = customer.get_confirmpassword()
        update_customer_form.status.data = customer.get_status()

        return render_template('updateCustomer.html', form=update_customer_form)


#RACHEL'S PART----------------------------------------------------------------------------------------------------


@app.route('/createOffCourse', methods=['GET', 'POST'])  # create offline course
def create_off_course():
    create_off_course_form = CreateOffCourseForm(request.form)
    if request.method == 'POST' and create_off_course_form.validate():

        off_courses_dict = {}
        db = shelve.open('offcourse.db', 'c')

        try:
            off_courses_dict = db['OffCourses']
            off_courses_list = []
            for key in off_courses_dict:
                off_courses = off_courses_dict.get(key)
                off_courses_list.append(off_courses)
            for Offline in off_courses_list:
                courseType.Offline.count_id = Offline.get_course_id()
        except:
            print("Error in retrieving Courses from course.db.")

        offcourse = courseType.Offline(create_off_course_form.course_name.data, create_off_course_form.course_description.data,create_off_course_form.course_instructor.data, create_off_course_form.course_date.data, create_off_course_form.course_time.data, create_off_course_form.course_duration.data, create_off_course_form.course_location.data, create_off_course_form.course_status.data)

        img = Image.open(request.files["image"])
        img.load()
        img.resize((1200, 600))
        img.convert("RGB")
        img.save(f"{basedir}/static/images/offcourse/{offcourse.get_course_id()}.png")

        off_courses_dict[offcourse.get_course_id()] = offcourse
        db['OffCourses'] = off_courses_dict

        db.close()
        return redirect(url_for('retrieve_off_courses'))
    return render_template('createOffCourse.html', form=create_off_course_form)


@app.route('/createOnCourse', methods=['GET', 'POST'])  # create online course
def create_on_course():
    create_on_course_form = CreateOnCourseForm(request.form)
    if request.method == 'POST' and create_on_course_form.validate():

        on_courses_dict = {}
        db = shelve.open('oncourse.db', 'c')

        try:
            on_courses_dict = db['OnCourses']
            on_courses_list = []
            for key in on_courses_dict:
                on_courses = on_courses_dict.get(key)
                on_courses_list.append(on_courses)
            for Online in on_courses_list:
                courseType.Online.count_id = Online.get_course_id()
        except:
            print("Error in retrieving Courses from course.db.")

        oncourse = courseType.Online(create_on_course_form.course_name.data, create_on_course_form.course_description.data, create_on_course_form.course_instructor.data, create_on_course_form.course_date.data, create_on_course_form.course_time.data, create_on_course_form.course_duration.data, create_on_course_form.course_link.data, create_on_course_form.course_status.data)
        img = Image.open(request.files["image"])
        img.load()
        img.resize((1200, 600))
        img.convert("RGB")
        img.save(f"{basedir}/static/images/oncourse/{oncourse.get_course_id()}.png")

        on_courses_dict[oncourse.get_course_id()] = oncourse
        db['OnCourses'] = on_courses_dict

        db.close()
        return redirect(url_for('retrieve_on_courses'))
    return render_template('createOnCourse.html', form=create_on_course_form)


@app.route('/retrieveOnCourses')  # retrieve online course
def retrieve_on_courses():
    on_courses_dict = {}
    db = shelve.open('oncourse.db', 'r')
    on_courses_dict = db['OnCourses']
    db.close()

    on_courses_list = []
    for key in on_courses_dict:
        oncourse = on_courses_dict.get(key)
        on_courses_list.append(oncourse)

    return render_template('retrieveOnCourses.html', count=len(on_courses_list), on_courses_list=on_courses_list)


@app.route('/retrieveOffCourses')  # retrieve offline course
def retrieve_off_courses():
    off_courses_dict = {}
    db = shelve.open('offcourse.db', 'r')
    off_courses_dict = db['OffCourses']
    db.close()

    off_courses_list = []
    for key in off_courses_dict:
        offcourse = off_courses_dict.get(key)
        off_courses_list.append(offcourse)

    return render_template('retrieveOffCourses.html', count=len(off_courses_list), off_courses_list=off_courses_list)


@app.route('/updateOnCourse/<int:id>/', methods=['GET', 'POST'])  # update online course
def update_on_course(id):
    update_on_course_form = CreateOnCourseForm(request.form)
    if request.method == 'POST' and update_on_course_form.validate():
        on_courses_dict = {}
        db = shelve.open('oncourse.db', 'w')
        on_courses_dict = db['OnCourses']

        oncourse = on_courses_dict.get(id)
        oncourse.set_course_name(update_on_course_form.course_name.data)
        oncourse.set_course_description(update_on_course_form.course_description.data)
        oncourse.set_course_instructor(update_on_course_form.course_instructor.data)
        oncourse.set_course_date(update_on_course_form.course_date.data)
        oncourse.set_course_time(update_on_course_form.course_time.data)
        oncourse.set_course_duration(update_on_course_form.course_duration.data)
        oncourse.set_course_link(update_on_course_form.course_link.data)
        oncourse.set_course_status(update_on_course_form.course_status.data)

        db['OnCourses'] = on_courses_dict
        db.close()

        return redirect(url_for('retrieve_on_courses'))
    else:
        on_courses_dict = {}
        db = shelve.open('oncourse.db', 'r')
        on_courses_dict= db['OnCourses']
        db.close()

        oncourse = on_courses_dict.get(id)
        update_on_course_form.course_name.data = oncourse.get_course_name()
        update_on_course_form.course_description.data = oncourse.get_course_description()
        update_on_course_form.course_instructor.data = oncourse.get_course_instructor()
        update_on_course_form.course_date.data = oncourse.get_course_date()
        update_on_course_form.course_time.data = oncourse.get_course_time()
        update_on_course_form.course_duration.data = oncourse.get_course_duration()
        update_on_course_form.course_link.data = oncourse.get_course_link()
        update_on_course_form.course_status.data = oncourse.get_course_status()

        return render_template('updateOnCourse.html', form=update_on_course_form)


@app.route('/updateOffCourse/<int:id>/', methods=['GET', 'POST'])  # update offline course
def update_off_course(id):
    update_off_course_form = CreateOffCourseForm(request.form)
    if request.method == 'POST' and update_off_course_form.validate():
        off_courses_dict = {}
        db = shelve.open('offcourse.db', 'w')
        off_courses_dict = db['OffCourses']

        offcourse = off_courses_dict.get(id)
        offcourse.set_course_name(update_off_course_form.course_name.data)
        offcourse.set_course_description(update_off_course_form.course_description.data)
        offcourse.set_course_instructor(update_off_course_form.course_instructor.data)
        offcourse.set_course_date(update_off_course_form.course_date.data)
        offcourse.set_course_time(update_off_course_form.course_time.data)
        offcourse.set_course_duration(update_off_course_form.course_duration.data)
        offcourse.set_course_location(update_off_course_form.course_location.data)
        offcourse.set_course_status(update_off_course_form.course_status.data)

        db['OffCourses'] = off_courses_dict
        db.close()

        return redirect(url_for('retrieve_off_courses'))
    else:
        off_courses_dict = {}
        db = shelve.open('offcourse.db', 'r')
        off_courses_dict= db['OffCourses']
        db.close()

        offcourse = off_courses_dict.get(id)
        update_off_course_form.course_name.data = offcourse.get_course_name()
        update_off_course_form.course_description.data = offcourse.get_course_description()
        update_off_course_form.course_instructor.data = offcourse.get_course_instructor()
        update_off_course_form.course_date.data = offcourse.get_course_date()
        update_off_course_form.course_time.data = offcourse.get_course_time()
        update_off_course_form.course_duration.data = offcourse.get_course_duration()
        update_off_course_form.course_location.data = offcourse.get_course_location()
        update_off_course_form.course_status.data = offcourse.get_course_status()

        return render_template('updateOffCourse.html', form=update_off_course_form)


@app.route('/retrieveOnCoursesCust')  # retrieve online course - customer side
def retrieve_on_courses_cust():
    oncoursescust_dict = {}
    db = shelve.open('oncourse.db', 'r')
    oncoursescust_dict = db['OnCourses']
    db.close()

    oncoursescust_list = []
    for key in oncoursescust_dict:
        oncoursecust = oncoursescust_dict.get(key)
        if oncoursecust.get_course_status() != 'Closed':
            oncoursescust_list.append(oncoursecust)

    return render_template('retrieveOnCoursesCust.html', count=len(oncoursescust_list), oncoursescust_list=oncoursescust_list)


@app.route('/retrieveOffCoursesCust')  # retrieve offline course - customer side
def retrieve_off_courses_cust():
    offcoursescust_dict = {}
    db = shelve.open('offcourse.db', 'r')
    offcoursescust_dict = db['OffCourses']
    db.close()

    offcoursescust_list = []
    for key in offcoursescust_dict:
        offcoursecust = offcoursescust_dict.get(key)
        if offcoursecust.get_course_status() != 'Closed':
            offcoursescust_list.append(offcoursecust)

    return render_template('retrieveOffCoursesCust.html', count=len(offcoursescust_list), offcoursescust_list=offcoursescust_list)


@app.route('/retrieveOffCoursesDetails/<int:id>/')  # retrieve offline course details - customer side
def retrieve_off_courses_details(id):
    offcoursescust_dict = {}
    db = shelve.open('offcourse.db', 'r')
    off_courses_dict = db['OffCourses']
    db.close()

    offcoursescust_list = []
    offcoursecust = off_courses_dict.get(id)
    if offcoursecust.get_course_status() != 'Closed':
        offcoursescust_list.append(offcoursecust)

    return render_template('retrieveOffCourseDetails.html', count=len(offcoursescust_list), offcoursescust_list=offcoursescust_list)


@app.route('/retrieveOnCoursesDetails/<int:id>/')  # retrieve online course details - customer side
def retrieve_on_courses_details(id):
    oncoursescust_dict = {}
    db = shelve.open('oncourse.db', 'r')
    on_courses_dict = db['OnCourses']
    db.close()

    oncoursescust_list = []
    oncoursecust = on_courses_dict.get(id)
    if oncoursecust.get_course_status() != 'Closed':
        oncoursescust_list.append(oncoursecust)

    return render_template('retrieveOnCourseDetails.html', count=len(oncoursescust_list), oncoursescust_list=oncoursescust_list)


@app.route('/retrieveOffCoursesDetailsOut/<int:id>/')  # retrieve offline course details - customer side
def retrieve_off_courses_details_out(id):
    offcoursescust_dict = {}
    db = shelve.open('offcourse.db', 'r')
    off_courses_dict = db['OffCourses']
    db.close()

    offcoursescust_list = []
    offcoursecust = off_courses_dict.get(id)
    if offcoursecust.get_course_status() != 'Closed':
        offcoursescust_list.append(offcoursecust)

    return render_template('retrieveOffCourseDetailsOut.html', count=len(offcoursescust_list), offcoursescust_list=offcoursescust_list)


@app.route('/retrieveOnCoursesDetailsOut/<int:id>/')  # retrieve online course details - customer side
def retrieve_on_courses_details_out(id):
    oncoursescust_dict = {}
    db = shelve.open('oncourse.db', 'r')
    on_courses_dict = db['OnCourses']
    db.close()

    oncoursescust_list = []
    oncoursecust = on_courses_dict.get(id)
    if oncoursecust.get_course_status() != 'Closed':
        oncoursescust_list.append(oncoursecust)

    return render_template('retrieveOnCourseDetailsOut.html', count=len(oncoursescust_list), oncoursescust_list=oncoursescust_list)


#CINDY'S PART-----------------------------------------------------------------------------------------------------


@app.route('/createWarehouse', methods=['GET', 'POST'])
def create_warehouse():
    create_warehouse_form = CreateWarehouseForm(request.form)
    if request.method == 'POST' and create_warehouse_form.validate():
        warehouses_dict = {}
        db = shelve.open('warehouse.db', 'c')
        try:
            warehouses_dict = db['Warehouses']
            warehouse_list = []
            for key in warehouses_dict:
                warehouses = warehouses_dict.get(key)
                warehouse_list.append(warehouses)
            for warehouse in warehouse_list:
                Inventorys.Warehouse.count_id = warehouse.get_warehouse_id()
        except:
            print('Error in retrieving Warehouse from warehouse.db')

        if len(create_warehouse_form.supplier.data) == 0:
            create_warehouse_form.supplier.data = 'NIL'

        warehouse = Inventorys.Warehouse(
            product_number = create_warehouse_form.product_number.data,
            product = create_warehouse_form.product.data,
            quantity = create_warehouse_form.quantity.data,
            supplier = create_warehouse_form.supplier.data,
            threshold = create_warehouse_form.threshold.data,
            category = create_warehouse_form.category.data,
            sub_category = create_warehouse_form.sub_category.data,)
        warehouses_dict[warehouse.get_warehouse_id()] = warehouse
        db['Warehouses'] = warehouses_dict

        # Test codes
        warehouses_dict = db['Warehouses']
        warehouse = warehouses_dict[warehouse.get_warehouse_id()]
        print(warehouse.product, warehouse.category, warehouse.sub_category,
              "was stored in warehouse.db successfully with warehouse_id ==",
              warehouse.get_warehouse_id())

        db.close()

        return redirect(url_for('retrieve_warehouse'))
    return render_template('createWarehouse.html', form=create_warehouse_form)


@app.route('/createSupplier', methods=['GET', 'POST'])
def create_supplier():
    create_supplier_form = CreateSupplierForm(request.form)
    if request.method == 'POST' and create_supplier_form.validate():
        suppliers_dict = {}
        db = shelve.open('supplier.db', 'c')
        try:
            suppliers_dict = db['Suppliers']
            supplier_list = []
            for key in suppliers_dict:
                suppliers = suppliers_dict.get(key)
                supplier_list.append(suppliers)
            for supplier in supplier_list:
                Supplier.Supplier.count_id = supplier.get_supplier_id()
        except:
            print('Error in retrieving db')

        supplier = Supplier.Supplier(create_supplier_form.supplier.data,
                                     create_supplier_form.name.data,
                                      create_supplier_form.email.data,
                                      create_supplier_form.contact_no.data,
                                      create_supplier_form.address.data,
                                      create_supplier_form.country.data,
                                     create_supplier_form.postal_code.data,
                                     create_supplier_form.bank.data,
                                     create_supplier_form.bank_acc.data,
                                     create_supplier_form.status.data)
        suppliers_dict[supplier.get_supplier_id()] = supplier
        db['Suppliers'] = suppliers_dict

        # Test codes
        suppliers_dict = db['Suppliers']
        supplier = suppliers_dict[supplier.get_supplier_id()]
        print(supplier.get_supplier(), supplier.get_email(),
              "was stored in supplier.db successfully with supplier_id ==",
              supplier.get_supplier_id())

        db.close()

        return redirect(url_for('retrieve_suppliers'))
    return render_template('createSupplier.html', form=create_supplier_form)


@app.route('/createOrder', methods=['GET', 'POST'])
def create_order():
    create_order_form = CreateOrderForm(request.form)
    if request.method == 'POST' and create_order_form.validate():
        orders_dict = {}
        db = shelve.open('order.db', 'c')

        try:
            orders_dict = db['Orders']
            orders_list = []
            for key in orders_dict:
                orders = orders_dict.get(key)
                orders_list.append(orders)
            for order in orders_list:
                Inventorys.Order.count_id = order.get_order_id()
        except:
            print("Error in retrieving Orders from order.db.")

        if len(create_order_form.supplier.data) == 0:
            create_order_form.supplier.data = 'NIL'

        order = Inventorys.Order(
            order_date = create_order_form.order_date.data,
            quantity = create_order_form.quantity.data,
            product_number = create_order_form.product_number.data,
            product = create_order_form.product.data,
            category = create_order_form.category.data,
            sub_category = create_order_form.sub_category.data,
            supplier = create_order_form.supplier.data,
            amount = create_order_form.amount.data,
            delivery_date = create_order_form.delivery_date.data)
        orders_dict[order.get_order_id()] = order
        db['Orders'] = orders_dict

        # Test codes
        orders_dict = db['Orders']
        order = orders_dict[order.get_order_id()]
        print(order.get_order_date(),order.product, order.supplier,
              "was stored in order.db successfully with order_id ==",
              order.get_order_id())

        db.close()

        return redirect(url_for('retrieve_orders'))
    return render_template('createOrder.html', form=create_order_form)


@app.route('/retrieveWarehouse')
def retrieve_warehouse():
    warehouses_dict = {}
    db = shelve.open('warehouse.db', 'r')
    warehouses_dict = db['Warehouses']
    db.close()

    db = shelve.open('supplier.db', 'r')
    suppliers_dict: dict = db['Suppliers']
    db.close()

    db = shelve.open('order.db', 'r')
    orders_dict = db['Orders']
    db.close()

    warehouses_list = []
    for key in warehouses_dict:
        warehouse = warehouses_dict.get(key)
        warehouses_list.append(warehouse)

    suppliers_list = []
    for key in suppliers_dict:
        supplier = suppliers_dict.get(key)
        suppliers_list.append(supplier)

    orders_list = []
    for key in orders_dict:
        order = orders_dict.get(key)
        orders_list.append(order)

    return render_template('retrieveWarehouse.html', count=len(warehouses_list), warehouses_list=warehouses_list, suppliers_list=suppliers_list,orders_list=orders_list)


@app.route('/retrieveSuppliers')
def retrieve_suppliers():
    suppliers_dict = {}
    db = shelve.open('supplier.db', 'r')
    suppliers_dict = db['Suppliers']
    db.close()

    suppliers_list = []
    for key in suppliers_dict:
        supplier = suppliers_dict.get(key)
        suppliers_list.append(supplier)

    return render_template('retrieveSuppliers.html', count=len(suppliers_list), suppliers_list=suppliers_list)


@app.route('/retrieveOrders')
def retrieve_orders():
    orders_dict = {}
    db = shelve.open('order.db', 'r')
    orders_dict = db['Orders']
    db.close()

    orders_list = []
    for key in orders_dict:
        order = orders_dict.get(key)
        orders_list.append(order)

    return render_template('retrieveOrders.html', count=len(orders_list), orders_list=orders_list)


@app.route("/status_order/<int:id>", methods=["POST"])
def status_order(id):
    db = shelve.open('order.db', "w")
    orders_dict: dict = db["Orders"]
    warehouse_db = shelve.open('warehouse.db', 'w')
    warehouses_dict: dict = warehouse_db['Warehouses']
    orders_id = orders_dict.get(id)
    if orders_id.get_order_status() == "Delivering":
        print(f"Order Key {orders_id.get_order_id()} has been Delivered!")
        orders_id.set_order_status("Delivered")
        for key in warehouses_dict:
            warehouse = warehouses_dict.get(key)
            if orders_id.product_number == warehouse.product_number:
                warehouse.quantity += orders_id.quantity

    db["Orders"] = orders_dict
    warehouse_db['Warehouses'] = warehouses_dict
    db.close()
    warehouse_db.close()
    return redirect(url_for("retrieve_orders"))


@app.route('/updateWarehouse/<int:id>/', methods=['GET', 'POST'])
def update_warehouse(id):
    update_warehouse_form = CreateWarehouseForm(request.form)
    if request.method == 'POST' and update_warehouse_form.validate():
        warehouses_dict = {}
        db = shelve.open('warehouse.db', 'w')
        warehouses_dict = db['Warehouses']

        warehouse = warehouses_dict.get(id)
        warehouse.product_number = update_warehouse_form.product_number.data
        warehouse.product = update_warehouse_form.product.data
        warehouse.quantity = update_warehouse_form.quantity.data
        warehouse.supplier = update_warehouse_form.supplier.data
        warehouse.threshold = update_warehouse_form.threshold.data
        warehouse.category = update_warehouse_form.category.data
        warehouse.sub_category = update_warehouse_form.sub_category.data

        db['Warehouses'] = warehouses_dict
        db.close()

        return redirect(url_for('retrieve_warehouse'))
    else:
        warehouses_dict = {}
        db = shelve.open('warehouse.db', 'r')
        warehouses_dict = db['Warehouses']
        db.close()

        warehouse = warehouses_dict.get(id)
        update_warehouse_form.product_number.data = warehouse.product_number
        update_warehouse_form.product.data = warehouse.product
        update_warehouse_form.quantity.data = warehouse.quantity
        update_warehouse_form.supplier.data = warehouse.supplier
        update_warehouse_form.threshold.data = warehouse.threshold
        update_warehouse_form.category.data = warehouse.category
        update_warehouse_form.sub_category.data = warehouse.sub_category
        return render_template('updateWarehouse.html', form=update_warehouse_form)


@app.route('/updateSupplier/<int:id>/', methods=['GET', 'POST'])
def update_supplier(id):
    update_supplier_form = CreateSupplierForm(request.form)
    if request.method == 'POST' and update_supplier_form.validate():
        suppliers_dict = {}
        db = shelve.open('supplier.db', 'w')
        suppliers_dict = db['Suppliers']

        supplier = suppliers_dict.get(id)
        supplier.set_supplier(update_supplier_form.supplier.data)
        supplier.set_name(update_supplier_form.name.data)
        supplier.set_email(update_supplier_form.email.data)
        supplier.set_contact_no(update_supplier_form.contact_no.data)
        supplier.set_address(update_supplier_form.address.data)
        supplier.set_country(update_supplier_form.country.data)
        supplier.set_postal_code(update_supplier_form.postal_code.data)
        supplier.set_bank(update_supplier_form.bank.data)
        supplier.set_bank_acc(update_supplier_form.bank_acc.data)
        supplier.set_status(update_supplier_form.status.data)

        db['Suppliers'] = suppliers_dict
        db.close()

        return redirect(url_for('retrieve_suppliers'))
    else:
        suppliers_dict = {}
        db = shelve.open('supplier.db', 'r')
        suppliers_dict = db['Suppliers']
        db.close()

        supplier = suppliers_dict.get(id)
        update_supplier_form.supplier.data = supplier.get_supplier()
        update_supplier_form.name.data = supplier.get_name()
        update_supplier_form.email.data = supplier.get_email()
        update_supplier_form.contact_no.data = supplier.get_contact_no()
        update_supplier_form.address.data = supplier.get_address()
        update_supplier_form.country.data = supplier.get_country()
        update_supplier_form.postal_code.data = supplier.get_postal_code()
        update_supplier_form.bank.data = supplier.get_bank()
        update_supplier_form.bank_acc.data = supplier.get_bank_acc()
        update_supplier_form.status.data = supplier.get_status()

        return render_template('updateSupplier.html', form=update_supplier_form)


@app.route('/updateOrder/<int:id>/', methods=['GET', 'POST'])
def update_order(id):
    update_order_form = CreateOrderForm(request.form)
    if request.method == 'POST':
        orders_dict = {}
        db = shelve.open('order.db', 'w')
        orders_dict = db['Orders']

        order = orders_dict.get(id)
        order.set_order_date(update_order_form.order_date.data)
        order.quantity = update_order_form.quantity.data
        order.product_number = update_order_form.product_number.data
        order.product = update_order_form.product.data
        order.category = update_order_form.category.data
        order.sub_category = update_order_form.sub_category.data
        order.supplier = update_order_form.supplier.data
        order.set_amount(update_order_form.amount.data)
        order.set_delivery_date(update_order_form.delivery_date.data)

        db['Orders'] = orders_dict
        db.close()

        return redirect(url_for('retrieve_orders'))
    else:
        orders_dict = {}
        db = shelve.open('order.db', 'r')
        orders_dict = db['Orders']
        db.close()

        order = orders_dict.get(id)
        update_order_form.order_date.data = order.get_order_date()
        update_order_form.quantity.data = order.quantity
        update_order_form.product_number.data = order.product_number
        update_order_form.product.data = order.product
        update_order_form.category.data = order.category
        update_order_form.sub_category.data = order.sub_category
        update_order_form.supplier.data = order.supplier
        update_order_form.amount.data = order.get_amount()
        update_order_form.delivery_date.data = order.get_delivery_date()

        return render_template('updateOrder.html', form=update_order_form)


@app.route("/extractdata/<int:id>", methods=["POST"])
def extractdata(id):
    if request.method == "POST":
        db = shelve.open('order.db', 'r')
        orders_dict = db['Orders']
        db.close()
        order = orders_dict.get(id)
        new_line = '\n'
        lines = [f"Order ID: {order.get_order_id()}{new_line} Order Date: {order.get_order_date()}{new_line} Quantity: {order.quantity}{new_line} Product Number:{order.product_number}{new_line} Product: {order.product}{new_line} Category: {order.category}{new_line} Sub-Category: {order.sub_category}{new_line} Supplier: {order.supplier}{new_line} Amount: {order.get_amount()}{new_line} Delivery Date: {order.get_delivery_date()}{new_line} Order Status:{order.get_order_status}{new_line}"]
        return Response(
            lines,
            mimetype="text/csv",
            headers={"Content-Disposition": "attachment; filename=OrderData.csv"},
        )


@app.route('/deleteWarehouse/<int:id>', methods=['POST'])
def delete_warehouse(id):
    warehouses_dict = {}
    db = shelve.open('warehouse.db', 'w')
    warehouses_dict = db['Warehouses']

    warehouses_dict.pop(id)

    db['Warehouses'] = warehouses_dict
    db.close()

    return redirect(url_for('retrieve_warehouse'))


@app.route('/deleteSupplier/<int:id>', methods=['POST'])
def delete_supplier(id):
    suppliers_dict = {}
    db = shelve.open('supplier.db', 'w')
    suppliers_dict = db['Suppliers']

    suppliers_dict.pop(id)

    db['Suppliers'] = suppliers_dict
    db.close()

    return redirect(url_for('retrieve_suppliers'))


@app.route('/deleteOrder/<int:id>', methods=['POST'])
def delete_order(id):
    orders_dict = {}
    db = shelve.open('order.db', 'w')
    orders_dict = db['Orders']

    orders_dict.pop(id)

    db['Orders'] = orders_dict
    db.close()

    return redirect(url_for('retrieve_orders'))


#PRIYA'S PART------------------------------------------------------------------------------------------------------


@app.route('/Productpagecust')
def productpagecust():
    detail_dict = {}
    db = shelve.open('detail.db', 'r')
    detail_dict = db['Detail']
    db.close()

    detail_list = []
    for key in detail_dict:
        detail = detail_dict.get(key)
        if detail.get_sub() != 'Unavailable':
            detail_list.append(detail)
    return render_template('Productpagecust.html', count=len(detail_list), detail_list=detail_list)


@app.route('/AdminProduct', methods=['GET', 'POST'])
def create_product():
    create_product_form = CreateProductForm(request.form)
    if request.method == 'POST' and create_product_form.validate():
        product_dict = {}
        db = shelve.open('product.db', 'c')

        try:
            product_dict = db['Product']
            product_list = []
            for key in product_dict:
                product = product_dict.get(key)
                product_list.append(product)
        except:
            print("Error in retrieving Product from product.db.")

        product = Product.Product(create_product_form.brand.data,
                                  create_product_form.name.data, create_product_form.shade.data,
                                  create_product_form.number.data, create_product_form.price.data,
                                  create_product_form.description.data, create_product_form.category.data,
                                  create_product_form.sub.data, create_product_form.quantity.data)

        img = Image.open(request.files["image"])
        img.load()
        img.resize((100, 100))
        img.convert("RGB")
        img.save(f"{basedir}/static/images/{product.get_product_id()}.png")

        product_dict[product.get_product_id()] = product
        db['Product'] = product_dict

        db.close()

        session['product_created'] = product.get_brand() + ' ' + product.get_name()

        return redirect(url_for('retrieve_product'))
    return render_template('AdminProduct.html', form=create_product_form)


@app.route('/createDetail', methods=['GET', 'POST'])
def create_detail():
    create_detail_form = CreateDetailForm(request.form)
    if request.method == 'POST' and create_detail_form.validate():
        detail_dict = {}
        db = shelve.open('detail.db', 'c')

        try:
            detail_dict = db['Detail']
            detail_list = []
            for key in detail_dict:
                detail = detail_dict.get(key)
                detail_list.append(detail)
        except:
            print("Error in retrieving Detail from detail.db.")

        detail = Detail.Detail(create_detail_form.brand.data,
                               create_detail_form.name.data,
                               create_detail_form.shade.data,
                               create_detail_form.number.data,
                               create_detail_form.price.data,
                               create_detail_form.description.data,
                               create_detail_form.category.data,
                               create_detail_form.sub.data,
                               create_detail_form.quantity.data)

        img = Image.open(request.files["image"])
        img.load()
        img.resize((100, 100))
        img.convert("RGB")
        img.save(f"{basedir}/static/images/{detail.get_detail_id()}.png")

        detail_dict[detail.get_detail_id()] = detail
        db['Detail'] = detail_dict

        db.close()

        session['customer_created'] = detail.get_brand() + ' ' + detail.get_name()

        return redirect(url_for('retrieve_detail'))
    return render_template('createDetail.html', form=create_detail_form)


@app.route('/AdminRetrieve')
def retrieve_product():
    product_dict = {}
    db = shelve.open('product.db', 'r')
    product_dict = db['Product']
    db.close()

    product_list = []
    for key in product_dict:
        product = product_dict.get(key)
        product_list.append(product)

    return render_template('AdminRetrieve.html', count=len(product_list), product_list=product_list)


@app.route('/retrieveDetail')
def retrieve_detail():
    detail_dict =\
        {}
    db = shelve.open('detail.db', 'r')
    detail_dict = db['Detail']
    db.close()

    detail_list = []
    for key in detail_dict:
        detail = detail_dict.get(key)
        detail_list.append(detail)

    return render_template('retrieveDetail.html', count=len(detail_list), detail_list=detail_list)


@app.route('/Productpage')
def Product_page():
    detail_dict = {}
    db = shelve.open('detail.db', 'r')
    detail_dict = db['Detail']
    db.close()

    detail_list = []
    for key in detail_dict:
        detail = detail_dict.get(key)
        if detail.get_sub() != 'Unavailable':
            detail_list.append(detail)

    return render_template('Productpage.html', count=len(detail_list), detail_list=detail_list)


@app.route('/singleproduct')
def single_product():
    detail_dict = {}
    db = shelve.open('detail.db', 'r')
    detail_dict = db['Detail']
    db.close()

    detail_list = []
    for key in detail_dict:
        detail = detail_dict.get(key)
        if detail.get_sub() != 'Unavailable':
            detail_list.append(detail)

    return render_template('singleproduct.html', count=len(detail_list), detail_list=detail_list)


@app.route('/updateProduct/<int:id>/', methods=['GET', 'POST'])
def update_product(id):
    update_product_form = CreateProductForm(request.form)
    if request.method == 'POST' and update_product_form.validate():
        product_dict = {}
        db = shelve.open('product.db', 'w')
        product_dict = db['Product']

        product = product_dict.get(id)
        product.set_brand(update_product_form.brand.data)
        product.set_name(update_product_form.name.data)
        product.set_shade(update_product_form.shade.data)
        product.set_number(update_product_form.number.data)
        product.set_price(update_product_form.price.data)
        product.set_description(update_product_form.description.data)
        product.set_category(update_product_form.category.data)
        product.set_sub(update_product_form.sub.data)
        product.set_quantity(update_product_form.quantity.data)

        img = Image.open(request.files["image"])
        img.load()
        img.resize((100, 100))
        img.convert("RGB")
        img.save(f"{basedir}/static/images/{product.get_product_id()}.png")

        db['Product'] = product_dict
        db.close()

        session['product_updated'] = product.get_brand() + ' ' + product.get_name()

        return redirect(url_for('retrieve_product'))
    else:
        product_dict = {}
        db = shelve.open('product.db', 'r')
        product_dict = db['Product']
        db.close()

        product = product_dict.get(id)
        update_product_form.brand.data = product.get_brand()
        update_product_form.name.data = product.get_name()
        update_product_form.shade.data = product.get_shade()
        update_product_form.number.data = product.get_number()
        update_product_form.price.data = product.get_price()
        update_product_form.description.data = product.get_description()
        update_product_form.category.data = product.get_category()
        update_product_form.sub.data = product.get_sub()
        update_product_form.quantity.data = product.get_quantity()

        return render_template('updateProduct.html', form=update_product_form)


@app.route('/updateDetail/<int:id>/', methods=['GET', 'POST'])
def update_detail(id):
    update_detail_form = CreateDetailForm(request.form)
    if request.method == 'POST' and update_detail_form.validate():
        detail_dict = {}
        db = shelve.open('detail.db', 'w')
        detail_dict = db['Detail']

        detail = detail_dict.get(id)
        detail.set_brand(update_detail_form.brand.data)
        detail.set_name(update_detail_form.name.data)
        detail.set_shade(update_detail_form.shade.data)
        detail.set_number(update_detail_form.number.data)
        detail.set_price(update_detail_form.price.data)
        detail.set_description(update_detail_form.description.data)
        detail.set_category(update_detail_form.category.data)
        detail.set_sub(update_detail_form.sub.data)
        detail.set_quantity(update_detail_form.quantity.data)

        img = Image.open(request.files["image"])
        img.load()
        img.resize((100, 100))
        img.convert("RGB")
        img.save(f"{basedir}/static/images/{detail.get_detail_id()}.png")

        db['Detail'] = detail_dict
        db.close()

        session['customer_updated'] = detail.get_brand() + ' ' + detail.get_name()

        return redirect(url_for('retrieve_detail'))
    else:
        detail_dict = {}
        db = shelve.open('detail.db', 'r')
        detail_dict = db['Detail']
        db.close()

        detail = detail_dict.get(id)
        update_detail_form.brand.data = detail.get_brand()
        update_detail_form.name.data = detail.get_name()
        update_detail_form.shade.data = detail.get_shade()
        update_detail_form.number.data = detail.get_number()
        update_detail_form.price.data = detail.get_price()
        update_detail_form.description.data = detail.get_description()
        update_detail_form.category.data = detail.get_category()
        update_detail_form.sub.data = detail.get_sub()
        update_detail_form.quantity.data = detail.get_quantity()

        return render_template('updateDetail.html', form=update_detail_form)


@app.route('/deleteProduct/<int:id>', methods=['POST'])
def delete_product(id):
    product_dict = {}
    db = shelve.open('product.db', 'w')
    product_dict = db['Product']

    product = product_dict.pop(id)

    db['Product'] = product_dict
    db.close()

    session['product_deleted'] = product.get_brand() + ' ' + product.get_name()

    return redirect(url_for('retrieve_product'))


@app.route('/deleteDetail/<int:id>', methods=['POST'])
def delete_detail(id):
    detail_dict = {}
    db = shelve.open('detail.db', 'w')
    detail_dict = db['Detail']

    detail = detail_dict.pop(id)

    db['Detail'] = detail_dict
    db.close()

    session['customer_deleted'] = detail.get_brand() + ' ' + detail.get_name()

    return redirect(url_for('retrieve_detail'))


#SHAHANA'S PART-------------------------------------------------------------------------------------------------


@app.route('/rewards_customer')
def rewards_customer():
    vouchers_dict = {}
    db = shelve.open('voucher.db', 'r')
    vouchers_dict = db['Vouchers']
    db.close()

    vouchers_list = []
    for key in vouchers_dict:
        voucher = vouchers_dict.get(key)
        vouchers_list.append(voucher)
    points_dict = {}
    db = shelve.open('point.db', 'r')
    points_dict = db['Points']
    db.close()

    points_list = []
    for key in points_dict:
        point = points_dict.get(key)
        points_list.append(point)
    return render_template('rewards_customer.html', vouchers_list=vouchers_list, points_list = points_list)


@app.route('/createVoucher', methods=['GET', 'POST'])
def create_voucher():
    create_voucher_form = CreateVoucherForm(request.form)
    if request.method == 'POST' and create_voucher_form.validate():
        vouchers_dict = {}
        db = shelve.open('voucher.db', 'c')

        try:
            vouchers_dict = db['Vouchers']
        except:
            print("Error in retrieving Vouchers from voucher.db.")

        voucher = Voucher.Voucher(create_voucher_form.product_name.data, create_voucher_form.claimed.data, create_voucher_form.expiry.data, create_voucher_form.status.data, create_voucher_form.code.data)
        vouchers_dict[voucher.get_voucher_id()] = voucher
        db['Vouchers'] = vouchers_dict
        db.close()

        return redirect(url_for('retrieve_vouchers'))
    return render_template('createVoucher.html', form=create_voucher_form)


@app.route('/createPoint', methods=['GET', 'POST'])
def create_point():
    create_point_form = CreatePointForm(request.form)
    if request.method == 'POST' and create_point_form.validate():
        points_dict = {}
        db = shelve.open('point.db', 'c')

        try:
            points_dict = db['Points']
        except:
            print("Error in retrieving Points from point.db.")

        point = Point.Point(create_point_form.product_name.data, create_point_form.claimed.data, create_point_form.expiry.data, create_point_form.status.data, create_point_form.code.data, create_point_form.points_needed.data)
        points_dict[point.get_point_id()] = point
        db['Points'] = points_dict

        db.close()

        return redirect(url_for('retrieve_points'))
    return render_template('createPoint.html', form=create_point_form)


@app.route('/retrieveVouchers')
def retrieve_vouchers():
    vouchers_dict = {}
    db = shelve.open('voucher.db', 'r')
    vouchers_dict = db['Vouchers']
    db.close()

    vouchers_list = []
    for key in vouchers_dict:
        voucher = vouchers_dict.get(key)
        vouchers_list.append(voucher)

    return render_template('retrieveVouchers.html', count=len(vouchers_list), vouchers_list=vouchers_list)


@app.route('/retrievePoints')
def retrieve_points():
    points_dict = {}
    db = shelve.open('point.db', 'r')
    points_dict = db['Points']
    db.close()

    points_list = []
    for key in points_dict:
        point = points_dict.get(key)
        points_list.append(point)

    return render_template('retrievePoints.html', count=len(points_list), points_list=points_list)


@app.route('/updateVoucher/<int:id>/', methods=['GET', 'POST'])
def update_voucher(id):
    update_voucher_form = CreateVoucherForm(request.form)
    if request.method == 'POST' and update_voucher_form.validate():
        vouchers_dict = {}
        db = shelve.open('voucher.db', 'w')
        vouchers_dict = db['Vouchers']

        voucher = vouchers_dict.get(id)
        voucher.set_product_name(update_voucher_form.product_name.data)
        voucher.set_claimed(update_voucher_form.claimed.data)
        voucher.set_expiry(update_voucher_form.expiry.data)
        voucher.set_status(update_voucher_form.status.data)
        voucher.set_code(update_voucher_form.code.data)

        db['Vouchers'] = vouchers_dict
        db.close()

        return redirect(url_for('retrieve_vouchers'))
    else:
        vouchers_dict = {}
        db = shelve.open('voucher.db', 'r')
        vouchers_dict = db['Vouchers']
        db.close()

        voucher = vouchers_dict.get(id)
        update_voucher_form.product_name.data = voucher.get_product_name()
        update_voucher_form.claimed.data = voucher.get_claimed()
        update_voucher_form.expiry.data = voucher.get_expiry()
        update_voucher_form.status.data = voucher.get_status()
        update_voucher_form.code.data = voucher.get_code()

        return render_template('updateVoucher.html', form=update_voucher_form)


@app.route('/updatePoint/<int:id>/', methods=['GET', 'POST'])
def update_point(id):
    update_point_form = CreatePointForm(request.form)
    if request.method == 'POST' and update_point_form.validate():
        points_dict = {}
        db = shelve.open('point.db', 'w')
        points_dict = db['Points']

        point = points_dict.get(id)
        point.set_product_name(update_point_form.product_name.data)
        point.set_claimed(update_point_form.claimed.data)
        point.set_expiry(update_point_form.expiry.data)
        point.set_status(update_point_form.status.data)
        point.set_code(update_point_form.code.data)
        point.set_points_needed(update_point_form.points_needed.data)

        db['Points'] = points_dict
        db.close()

        return redirect(url_for('retrieve_points'))
    else:
        points_dict = {}
        db = shelve.open('point.db', 'r')
        points_dict = db['Points']
        db.close()

        point = points_dict.get(id)
        update_point_form.product_name.data = point.get_product_name()
        update_point_form.claimed.data = point.get_claimed()
        update_point_form.expiry.data = point.get_expiry()
        update_point_form.status.data = point.get_status()
        update_point_form.code.data = point.get_code()
        update_point_form.points_needed.data = point.get_points_needed()

        return render_template('updatePoint.html', form=update_point_form)


@app.route('/deleteVoucher/<int:id>', methods=['POST'])
def delete_voucher(id):
    vouchers_dict = {}
    db = shelve.open('voucher.db', 'w')
    vouchers_dict = db['Vouchers']

    vouchers_dict.pop(id)

    db['Vouchers'] = vouchers_dict
    db.close()

    return redirect(url_for('retrieve_vouchers'))


@app.route('/deletePoint/<int:id>', methods=['POST'])
def delete_point(id):
    points_dict = {}
    db = shelve.open('point.db', 'w')
    points_dict = db['Points']
    points_dict.pop(id)
    db['Points'] = points_dict
    db.close()
    return redirect(url_for('retrieve_points'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
