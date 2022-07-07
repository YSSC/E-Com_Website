from wtforms import Form, StringField, DateField, SelectField, validators, IntegerField
from wtforms.validators import ValidationError
import datetime


class CreateVoucherForm(Form):
    product_name = StringField('Product Name', [validators.Length(min=1, max=50), validators.DataRequired()])
    claimed = IntegerField('Claimed', [validators.NumberRange(min=1, max=500), validators.DataRequired()])
    expiry = DateField('Expiry', format='%Y-%m-%d')
    status = SelectField('Status', [validators.DataRequired()], choices=[('Fully Redeemed', 'Fully Redeemed'), ('Available', 'Available')], default='F')
    code = StringField('Code', [validators.Length(min=1, max=10), validators.DataRequired()])

    def validate_expiry(form, field):
        if field.data < datetime.date.today():
            raise ValidationError('Date cannot be in the past.')


class CreatePointForm(Form):
    product_name = StringField('Product Name', [validators.Length(min=1, max=50), validators.DataRequired()])
    claimed = IntegerField('Claimed', [validators.NumberRange(min=1, max=500), validators.DataRequired()])
    expiry = DateField('Expiry', format='%Y-%m-%d')
    status = SelectField('Status', [validators.DataRequired()], choices=[('Fully Redeemed', 'Fully Redeemed'), ('Available', 'Available')], default='F')
    code = StringField('Code', [validators.Length(min=1, max=10), validators.DataRequired()])
    points_needed = IntegerField('Points Needed', [validators.NumberRange(min=50, max=500), validators.DataRequired()])

    def validate_expiry(form, field):
        if field.data < datetime.date.today():
            raise ValidationError('Date cannot be in the past.')
