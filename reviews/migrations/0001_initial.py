# Generated by Django 3.0.6 on 2022-06-16 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField(max_length=200)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='contents.Content')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
