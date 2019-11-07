# Generated by Django 2.2.5 on 2019-10-30 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("trans", "0042_original_state")]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="instructions",
            field=models.TextField(
                blank=True,
                help_text="You can use Markdown and mention users by @username.",
                verbose_name="Translation instructions",
            ),
        )
    ]