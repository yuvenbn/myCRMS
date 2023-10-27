# Generated by Django 4.2.6 on 2023-10-27 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_police_policeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.customuser'),
        ),
        migrations.AlterField(
            model_name='police',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin', to='authentication.customuser'),
        ),
        migrations.AlterField(
            model_name='police',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.customuser'),
        ),
        migrations.AlterField(
            model_name='regularuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.customuser'),
        ),
    ]