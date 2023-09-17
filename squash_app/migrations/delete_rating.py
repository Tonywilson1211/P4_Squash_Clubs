from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("squash_app", "alter_comment_created_at_rating"),
    ]

    operations = [
        migrations.DeleteModel(name="Rating",),
    ]
