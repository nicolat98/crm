# Generated by Django 4.2.1 on 2023-06-04 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255)),
                ('contact_person', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=255)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('confidence', models.IntegerField(blank=True, null=True)),
                ('estimated_value', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('won', 'won'), ('contacted', 'contacted'), ('inprogress', 'inprogress'), ('new', 'New'), ('lost', 'lost')], default='new', max_length=25)),
                ('priority', models.CharField(choices=[('low', 'low'), ('high', 'high'), ('medium', 'medium')], default='medium', max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leads', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]