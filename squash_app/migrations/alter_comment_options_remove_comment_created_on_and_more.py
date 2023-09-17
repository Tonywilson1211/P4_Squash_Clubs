import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("squash_app", "comment_approved_alter_club_skill_level_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={
                "ordering": ["created_at"],
                "verbose_name_plural": "List of Comments",
            },
        ),
        migrations.RemoveField(model_name="comment", name="created_on",),
        migrations.AddField(
            model_name="comment",
            name="created_at",
            field=models.DateTimeField(
                auto_created=True,
                default=datetime.datetime(2023, 9, 15, 7, 16, 55, 639524),
            ),
            preserve_default=False,
        ),
    ]
