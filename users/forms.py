from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, ValidationError
from wtforms.validators import DataRequired, Length


class UserRegistrationForm(FlaskForm):
   email = EmailField("Email", validators=[])
   full_name = StringField('Full Name', validators=[DataRequired(), Length(0, 40)])
   password = PasswordField("Password")
   password2 = PasswordField("Confirm Password")

   def validate_password(self, field):
        password2 = self.data["password2"]
        if password2 != field.data:
            raise ValidationError("Both passwords are not matched !!!")
