from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



def get_path_upload_image(file):
    time = timezone.now().strftime("%Y-%m-%d")
    end_extention = file.split('.')[1]
    head = file.split('.')[0]
    if len(head) > 10:
        head = head[:10]
    file_name = head + '_' + timezone.now().strftime("%h-%m-%s") + '.' + end_extention
    return os.path.join('{}', '{}').format(time, file_name)



class Profile(models.Model):
    """Профиль"""
    user = models.OneToOneField(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE
    )

    avatar = models.ImageField("Аватар", upload_to="avatars/", blank=True, null=True)
    phone = models.TextField("Номер телефона", max_length=15,blank=True, null=True)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    slug = models.SlugField(
        "url",
        max_length=200,
        unique=True,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        self.slug = ("profile-" + str(self.user.id))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("profile", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()