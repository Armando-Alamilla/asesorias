# Generated by Django 2.2.10 on 2020-04-20 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('is_admin', models.BooleanField(default=False, help_text="School admins can update the school's data and change its members.", verbose_name='school admin')),
                ('is_teacher', models.BooleanField(default=False, help_text='Teachers can upload content such as videos or articles on school subjects.', verbose_name='school teacher')),
                ('used_invitations', models.PositiveSmallIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True, help_text='Only active users are allowed to interact in the school.', verbose_name='active status')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='school name')),
                ('slug_name', models.SlugField(max_length=40, unique=True)),
                ('about', models.CharField(max_length=255, verbose_name='school description')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='schools/pictures')),
                ('subjects_offered', models.PositiveIntegerField(default=0)),
                ('verified', models.BooleanField(default=False, help_text='verified schools are also recognized as an official school.', verbose_name='verified school')),
                ('is_public', models.BooleanField(default=True, help_text='Visible schools are listed in the main page so everyone know about their existence.')),
            ],
            options={
                'ordering': ['-subjects_offered'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
