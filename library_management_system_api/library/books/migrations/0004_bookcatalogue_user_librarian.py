# Generated by Django 4.0.4 on 2022-06-02 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('books', '0003_language_alter_book_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookCatalogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_books', models.IntegerField(max_length=1000)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('book_catalogue',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.bookcatalogue')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.user')),
            ],
        ),
    ]
