from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionForm(FlaskForm):
    query = StringField("query", validators=[DataRequired(message="会话不能为空"),
                                             Length(max=2000, message="会话最多支持2000字")])
