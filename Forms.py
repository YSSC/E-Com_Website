from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, PasswordField, BooleanField, TimeField, FloatField, IntegerField
from wtforms.fields import EmailField, DateField
from wtforms.validators import ValidationError
from flask_wtf.file import FileAllowed, FileField
import datetime


class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male'), ('O', 'Others')], default='')
    email = EmailField('Email', [validators.Length(min=6), validators.Email(message='Invalid email!'), validators.DataRequired()])
    phonenumber = StringField('Phone Number', [validators.Length(min=8, max=8), validators.DataRequired()])
    dateofbirth = DateField('Date Of Birth', [validators.DataRequired()])
    jobscope = RadioField('Job Scope', choices=['Sales', 'Marketing', 'Finance', 'Others'], default='Sales')
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=8)])
    confirmpassword = PasswordField('Confirm Password', [validators.EqualTo('password', message='Password must match!')])
    status = SelectField('Status', [validators.DataRequired()], choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active')

    def validate_password(form, field):
        if field.data == '123456':
            raise ValidationError('Password Not Strong! Try Again.')

    def validate_dateofbirth(form, field):
        if (datetime.date.today() - field.data) < datetime.timedelta(days=18*365):
            raise ValidationError('Required Minimum Age is 18 years old!')


class CreateCustomerForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male'), ('O', 'Others')], default='')
    email = EmailField('Email', [validators.Length(min=6), validators.Email(message='Invalid email!'), validators.DataRequired()])
    phonenumber = StringField('Phone Number', [validators.Length(min=8, max=8), validators.DataRequired()])
    dateofbirth = DateField('Date Of Birth', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=8, message='Select a stronger password!')])
    confirmpassword = PasswordField('Confirm Password', [validators.EqualTo('password', message='Password must match!')])
    date_joined = DateField('Date Joined')
    membership = RadioField('Membership', choices=[('I', 'INSIDER'), ('V', 'VIB'), ('R', 'ROGUE')], default='I')
    address = TextAreaField('Mailing Address', [validators.Length(max=200), validators.DataRequired()])
    status = SelectField('Status', [validators.DataRequired()], choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active')

    def validate_dateofbirth(form, field):
        if (datetime.date.today() - field.data) < datetime.timedelta(days=18*365):
            raise ValidationError('Required Minimum Age is 18 years old!')

    def validate_date_joined(form, field):
        if field.data != datetime.date.today():
            raise ValidationError('Date cannot be in the past!')

    def validate_password(form, field):
        if field.data == '123456':
            raise ValidationError('Password Not Strong! Try Again.')

    def validate_phonenumber(form, field):
        if field.data.isdigit():
            pass
        else:
            raise ValidationError('Non-digits are not allowed!')


class LoginForm(Form):
    email = EmailField('Email', [validators.Length(min=6), validators.Email(message='Enter a valid email!'), validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=8, message='Select a stronger password!')])
    remember = BooleanField('Remember Me')


class Cardpayment(Form):
    cname = StringField('Full Name (as per on the card):', [validators.Length(min=1, max=150), validators.DataRequired()])
    cnum = StringField('Card Number', [validators.DataRequired(), validators.Length(min=16, max=16)])
    expiry = DateField('Expiry Date', [validators.DataRequired()])
    cvv = StringField('CVV', [validators.DataRequired(), validators.Length(min=3, max=3)])
    address = StringField('Address', [validators.DataRequired()])
    city = StringField('City', [validators.DataRequired()])
    state = StringField('State', [validators.DataRequired()])
    postalcode = StringField('Postal Code / Zip', [validators.DataRequired()])

    def validate_expiry(form, field):
        if field.data < datetime.date.today():
            raise ValidationError('Date cannot be in the past!')


class ChangeEmail(Form):
    currentemail = EmailField('Enter Current Email Address:', [validators.Length(min=6), validators.Email(message='Enter a valid email!'), validators.DataRequired()])
    newemail = EmailField('Enter New Email:', [validators.DataRequired(), validators.Length(min=6), validators.Email(message='Enter a valid email!')])
    confirmnewemail = EmailField('Confirm New Email:', [validators.EqualTo('newemail', message='Email must match!')])


class ChangePhoneNumber(Form):
    currentphone = StringField('Enter current Phone Number:', [validators.Length(min=8, max=8), validators.DataRequired()])
    newphone = StringField('Enter New Phone Number:', [validators.Length(min=8, max=8), validators.DataRequired()])
    confirmnewphone = StringField('Confirm New Phone Number:', [validators.Length(min=8, max=8), validators.EqualTo('newphone', message='Phone Number must match!')])


class ChangePassword(Form):
    currentpassword = PasswordField('Enter Current Password:', [validators.DataRequired()])
    newpassword = PasswordField('Enter New Password:', [validators.DataRequired(), validators.Length(min=8, message='Select a stronger password!')])
    confirmnewpassword = PasswordField('Confirm New Password:', [validators.Length(min=8), validators.EqualTo('newpassword', message='Password must match!')])


class Forgetpassword(Form):
    email = EmailField('Email', [validators.Length(min=6), validators.Email(message='Enter a valid email!'), validators.DataRequired()])


class EditProfile(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male'), ('O', 'Others')])
    email = EmailField('Email', [validators.Length(min=6), validators.Email(message='Invalid email!'), validators.DataRequired()])
    phonenumber = StringField('Phone Number', [validators.Length(min=8, max=8), validators.DataRequired()])


class CreateOnCourseForm(Form):
    course_name = StringField('Course Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    course_description = StringField('Course Description', [validators.Length(min=1, max=999), validators.DataRequired()])
    course_instructor = StringField('Course Instructor', [validators.Length(min=1, max=150), validators.DataRequired()])
    course_date = DateField('Date', [validators.DataRequired()])
    course_time = TimeField('Time', [validators.DataRequired()])
    course_duration = FloatField('Duration (Hr)', [validators.DataRequired()])
    course_link = StringField('Link for Zoom', [validators.Length(min=1, max=150), validators.DataRequired()])
    course_status = SelectField('Status', [validators.DataRequired()], choices=[('', 'Select'), ('Upcoming', 'Upcoming'), ('Available', 'Available'), ('Closed', 'Closed')], default='')
    image = FileField(
        "Image",
        validators=[
            FileAllowed(["jpg", "png", "gif", "jpeg"], "Images only please"),
        ],
    )

    def validate_course_date(form, field):
        if field.data < datetime.date.today():
            raise ValidationError('Date cannot be in the past.')


class CreateOffCourseForm(Form):
    course_name = StringField('Course Name', [validators.Length(min=1, max=50), validators.DataRequired()])
    course_description = StringField('Course Description', [validators.Length(min=1), validators.DataRequired()])
    course_instructor = StringField('Course Instructor', [validators.Length(min=1), validators.DataRequired()])
    course_date = DateField('Date', [validators.DataRequired()])
    course_time = TimeField('Time', [validators.DataRequired()])
    course_duration = FloatField('Duration (Hr)', [validators.DataRequired()])
    course_location = StringField('Location', [validators.Length(min=1, max=150), validators.DataRequired()])
    course_status = SelectField('Status', [validators.DataRequired()], choices=[('', 'Select'), ('Upcoming', 'Upcoming'), ('Available', 'Available'), ('Closed', 'Closed')], default='')
    image = FileField(
        "Image",
        validators=[
            FileAllowed(["jpg", "png", "gif", "jpeg"], "Images only please"),
        ],
    )

    def validate_course_date(form, field):
        if field.data < datetime.date.today():
            raise ValidationError('Date cannot be in the past.')


class CreateSupplierForm(Form):
    supplier = StringField('Supplier', [validators.Length(min=1, max=150), validators.DataRequired()])
    name = TextAreaField('Name', [validators.length(max=200), validators.DataRequired()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    contact_no = StringField('Contact Number', [validators.Length(min=1, max=150), validators.DataRequired()])
    address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])
    country = StringField('Country/State', [validators.Length(min=1, max=150), validators.DataRequired()])
    postal_code = StringField('Postal Code', [validators.Length(min=1, max=150), validators.DataRequired()])
    bank = SelectField('Bank', [validators.DataRequired()], choices=[('American Express', 'American Express'), ('OCBC', 'OCBC'), ('POSB', 'POSB'), ('UOB', 'UOB'), ('Bank of India', 'Bank of India'), ('Bank of China', 'Bank of China')], default='F')
    bank_acc = StringField('Bank Account', [validators.Length(min=1, max=150), validators.DataRequired()])
    status = SelectField('Status', [validators.DataRequired()], choices=[('Active', 'Active'), ('Non-Active', 'Non-Active')], default='F')


class CreateOrderForm(Form):
    def validate_order_date(form, field):
        if field.data < datetime.date.today():
            raise ValidationError('Date cannot be in the past.')

    def validate_delivery_date(form, field):
        if field.data < form.order_date.data:
            raise ValidationError('Date cannot be past Order Date.')

    order_date = DateField('Order Date', format='%Y-%m-%d',validators=[validate_order_date])
    quantity = IntegerField('Quantity', [validators.NumberRange(min=1, max=10000), validators.DataRequired()])
    product_number = StringField('Product Number', [validators.Length(min=1, max=150), validators.DataRequired()])
    product = TextAreaField('Product', [validators.length(max=200), validators.DataRequired()])
    category = SelectField('Category', [validators.DataRequired()], choices=[('Makeup', 'Makeup'), ('Facial Care', 'Facial Care')], default='F')
    sub_category = SelectField('Sub-Category', [validators.DataRequired()], choices=[('Face', 'Face'), ('Lips', 'Lips'), ('Eyes', 'Eyes')], default='F')
    supplier = StringField('Supplier', [validators.Length(min=1, max=150), validators.Optional()])
    amount = StringField('Amount', [validators.Length(min=1, max=150), validators.DataRequired()])
    delivery_date = DateField('Delivery Date', format='%Y-%m-%d',validators=[validate_delivery_date])


class CreateWarehouseForm(Form):
    product_number = StringField('Product Number', [validators.Length(min=1, max=150), validators.DataRequired()])
    product = TextAreaField('Product', [validators.length(max=200), validators.DataRequired()])
    quantity = IntegerField('Quantity', [validators.NumberRange(min=1, max=10000), validators.DataRequired()])
    supplier = StringField('Supplier', [validators.Length(min=0, max=150), validators.Optional()])
    threshold = IntegerField('Threshold', [validators.NumberRange(min=1, max=4000), validators.Optional()])
    category = SelectField('Category', [validators.DataRequired()], choices=[('Makeup', 'Makeup'), ('Facial Care', 'Facial Care')], default='F')
    sub_category = SelectField('Sub-Category', [validators.DataRequired()], choices=[('Face', 'Face'), ('Lips', 'Lips'), ('Eyes', 'Eyes')], default='F')


class CreateProductForm(Form):
    brand = StringField('Brand Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    name = StringField('Product Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    shade = StringField('Shade Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    number = IntegerField('Product Number', [validators.NumberRange(min=1, max=30), validators.DataRequired()])
    price = IntegerField('Price $', [validators.NumberRange(min=1, max=80), validators.DataRequired()])
    description = TextAreaField('Description', [validators.Length(min=1, max=150), validators.DataRequired()])
    category = SelectField(u'Category', choices=[('makeup', 'makeup')])
    sub = SelectField('Availability', choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')])
    quantity = IntegerField('Quantity', [validators.NumberRange(min=1, max=80), validators.DataRequired()])
    image = FileField(
        "Image",
        validators=[
            FileAllowed(["jpg", "png", "gif", "jpeg"], "Images only please"),
        ],
    )


class CreateDetailForm(Form):

    brand = StringField('Brand Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    name = StringField('Product Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    shade = StringField('Shade Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    number = IntegerField('Product Number', [validators.NumberRange(min=1, max=30), validators.DataRequired()])
    price = IntegerField('Price $', [validators.NumberRange(min=1, max=80), validators.DataRequired()])
    description = TextAreaField('Description', [validators.Length(min=1, max=150), validators.DataRequired()])
    category = SelectField(u'Category', choices=[('makeup', 'makeup')])
    sub = SelectField('Availability', choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')])
    quantity = IntegerField('Quantity', [validators.NumberRange(min=1, max=80), validators.DataRequired()])
    image = FileField(
        "Image",
        validators=[
            FileAllowed(["jpg", "png", "gif", "jpeg"], "Images only please"),
        ],
    )
