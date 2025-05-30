from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible
from django.core import validators


@deconstructible
class UnicodePhoneValidator(validators.RegexValidator):
    regex = r"^\+998\d{9}$"
    message = _(
        "Yaroqli telefon raqamini kiriting. Format: +998XXXXXXXXX (aniq 13 ta belgi)."
    )
    flags = 0

phone_validator = UnicodePhoneValidator()


class CustomUserManager(BaseUserManager):
    def create_user(self, telefon, password=None, **extra_fields):
        if not telefon:
            raise ValueError(_('Telefon raqami kiritilishi shart'))
        telefon = self.normalize_phone(telefon)
        user = self.model(telefon=telefon, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, telefon, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(telefon, password, **extra_fields)

    def normalize_phone(self, telefon):
        return telefon


class UserModel(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('rahbar', 'Rahbar'),
        ('xodim', 'Xodim'),
    )

    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50)
    telefon = models.CharField(
        _("telefon"),
        max_length=13,
        unique=True,
        help_text=_("Majburiy. Format: +998XXXXXXXXX."),
        validators=[phone_validator],
        error_messages={
            "unique": _("Bu telefon raqamiga ega foydalanuvchi allaqachon mavjud."),
        },
    )
    password = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='avatars/', null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    code = models.CharField(max_length=6, null=True)
    expire_date = models.DateTimeField(null=True)

    USERNAME_FIELD = 'telefon'

    objects = CustomUserManager()

    def generate_verification_code(self):
        from datetime import datetime, timedelta
        import random
        self.code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        self.expire_date = datetime.now() + timedelta(minutes=1)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_by_natural_key(cls, telefon):
        return cls.objects.get(telefon=telefon)