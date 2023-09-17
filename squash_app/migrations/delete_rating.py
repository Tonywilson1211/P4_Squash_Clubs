from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("smsApp", "0004_alter_comment_created_at_rating"),
    ]

    operations = [
        migrations.DeleteModel(name="Rating",),
    ]
