from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("squash_club", "initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="approved",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="club",
            name="skill_level",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("all", "All Welcome"),
                    ("beginner", "Beginner"),
                    ("junior", "Junior (16 and under)"),
                    ("intermediate", "Intermediate"),
                    ("senior", "Senior (55 and over)"),
                ],
                default="all",
                max_length=100,
                verbose_name="Skill Level",
            ),
        ),
        migrations.AlterField(
            model_name="clubmember",
            name="status",
            field=models.IntegerField(
                choices=[(1, "Join Requested"), (2, "Approved")]),
        ),
    ]
