from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

# class UserView(ModelView):
#     can_edit=False
#     can_delete=False
#     def is_accessible(self):
#         return current_user.is_authenticated and current_user.is_admin
