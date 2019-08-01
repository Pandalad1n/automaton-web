# Generated by Django 2.1.2 on 2019-07-28 19:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('automaton', '0007_auto_20190726_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_ratings', to='automaton.Field')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_ratings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='fieldrating',
            unique_together={('field', 'user')},
        ),
    ]