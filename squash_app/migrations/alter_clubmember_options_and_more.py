from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("squash_app", "delete_rating"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="clubmember", options={"ordering": ("status", "-joined_at")},
        ),
        migrations.AlterUniqueTogether(
            name="clubmember", unique_together={("club", "user")},
        ),
    ]
