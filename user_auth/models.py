from django.db import models

# Create your models here.


# class accounts(models.Model):
#     screen_name = models.CharField(max_length=140)
#     user_name = models.CharField(max_length=140)
#     user_id = models.CharField(max_length=140)
#     user_img = models.CharField(max_length=140)
#     user_created_at = models.CharField(max_length=140)
#     followers = models.IntegerField()
#     follow = models.IntegerField()
    

#     def __str__(self):
#         return self.user_name
# class User(AbstractUser):

class client(models.Model):
    
    GENDER_CHOICES = (
        (1, '男性'),
        (2, '女性'),
        (3, 'その他'),
    )
    
    Name = models.CharField(max_length=100)
    age = models.IntegerField()
    contactdate = models.DateField()
    gender = models.IntegerField(verbose_name='性別', choices=GENDER_CHOICES, blank=True, null=True)
    
class OAuthTokenTemp(models.Model):
    user_id = models.BigIntegerField(primary_key=True, unique=True)
    oauth_token = models.CharField(max_length=255, db_index=True, unique=True)
    oauth_token_secret = models.CharField(max_length=255, db_index=True, unique=True)
    name = models.CharField(max_length=255, null=False)
    # description = models.CharField(max_length=1000)
    friends_count = models.IntegerField()
    followers_count = models.IntegerField()
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user_id", "oauth_token", "oauth_token_secret"],
                name="oauth_unique"
            ),
        ]