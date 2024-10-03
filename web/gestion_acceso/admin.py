# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from gestion_acceso.models import User

# Register your models here.

# @admin.register(User)
# class UserAdmin(UserAdmin):
#     # Define una clase personalizada para la administración del modelo 'User', heredando de UserAdmin
#     fieldsets = (  # Define los grupos de campos que se mostrarán en el formulario de edición del usuario
#         (None, {"fields": ('username', 'password'),}),  # Grupo sin título con campos 'username' y 'password'
#         ('Personal Information', {"fields": ('first_name', 'last_name', 'email', 'rh'),}),  # Grupo con información personal 
#     #     ('Permissions', {"fields": ('is_active', 'is_staff','is_superuser','groups','user_permissions'),}),
#     )
#     list_display = [  # Define los campos que se mostrarán en la lista de usuarios en el panel de administración
#                     'id',  # Muestra el ID del usuario
#                     'first_name',  # Muestra el nombre del usuario
#                     'last_name',  # Muestra el apellido del usuario
#                     'email',  # Muestra el correo electrónico del usuario
#                     ]
    # pass
