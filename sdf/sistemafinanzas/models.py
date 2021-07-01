from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

# Create your models here.


# Clase encargada de crear los distintos tipos de usuarios del sistema
class AccountManager(BaseUserManager):


    def create_user(self, email, first_name, password, **other_fields):
        user = self.model(email=email, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_cliente(self, email, first_name, last_name, dni, fecha_nacimiento, sbs, riesgo_sentinel,
                        algoritmo_IA , password):


        cliente = self.model(email=email, first_name=first_name, last_name=last_name, dni=dni, fecha_nacimiento=fecha_nacimiento,
                             sbs=sbs, riesgo_sentinel=riesgo_sentinel, algoritmo_IA=algoritmo_IA)
        cliente.set_password(password)
        cliente.save()
        return cliente

    def create_empleado(self, email, first_name, last_name, tipo_empleado, puede_aprobar,password):

        empleado = self.model(email=email, first_name=first_name,
                            last_name=last_name, tipo_empleado=tipo_empleado, puede_aprobar=puede_aprobar)
        empleado.set_password(password)
        empleado.save()
        return empleado


class User(AbstractBaseUser):


    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name  = models.CharField(max_length=150, blank=True)
    address = models.CharField(max_length=150, blank=True)
    dni = models.IntegerField()
    fecha_nacimiento = models.DateTimeField()
    is_staff   = models.BooleanField(default=False)
    is_active  = models.BooleanField(default=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email + self.first_name + self.last_name


class Cliente(User):
    """ Creación de un modelo Usuario tipo Cliente """

    sbs = models.FloatField()
    riesgo_sentinel = models.CharField
    algoritmo_IA = models.IntegerField()


class Empleado(User):
    """ Creación de un modelo Usuario tipo Cliente """

    tipo_empleado = models.CharField(max_length=100)
    puede_aprobar = models.BooleanField(default=False)
    User.is_staff = True

class Credito():


    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    monto = models.FloatField()
    descripcion = models.CharField(max_length=300)
    estado = models.CharField(max_length=100, default="Pendiente")


    # Este metodo permite conocer todos los creditos de un cliente especifico
    @classmethod
    def get_creditos_de_cliente(cls, username):
        creditos = Credito.objects.all()
        creditos_del_cliente = []

        for credito in creditos:
            if credito.cliente and credito.cliente.get_username() == username:
                creditos_del_cliente.append(credito)

        return creditos_del_cliente

    def get_estado(self, estado):
        self.estado = estado
        self.save()