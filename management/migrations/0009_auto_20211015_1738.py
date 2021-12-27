# Generated by Django 3.1.7 on 2021-10-15 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_auto_20210604_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='name',
            field=models.TextField(max_length=256),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=256)),
                ('avatar', models.TextField(max_length=256)),
                ('Role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.roles')),
            ],
        ),
        migrations.CreateModel(
            name='GameChosenRoles',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]