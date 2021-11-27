# Generated by Django 3.2.8 on 2021-11-27 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artigos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField()),
                ('resumo', models.TextField()),
                ('capa', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Capitulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('imagem1', models.ImageField(upload_to='')),
                ('imagem2', models.ImageField(upload_to='')),
                ('imagem3', models.ImageField(upload_to='')),
                ('artigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Artigos.artigos')),
            ],
        ),
    ]
