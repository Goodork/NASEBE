# Generated by Django 4.2.2 on 2023-08-20 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=100)),
                ('Prenoms', models.CharField(max_length=100)),
                ('Telephone', models.CharField(max_length=130)),
                ('Objet', models.CharField(max_length=100)),
                ('Message', models.CharField(max_length=98999)),
            ],
        ),
        migrations.CreateModel(
            name='Extraitabobos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=100)),
                ('Prenoms', models.CharField(max_length=100)),
                ('Date_de_naissance', models.DateField()),
                ('Lieu_de_naissance', models.CharField(max_length=100)),
                ('Numero_acte_de_naissance', models.CharField(max_length=100)),
                ('Ville_de_residence', models.CharField(max_length=100)),
                ('Nom_et_prenoms_du_pere', models.CharField(max_length=100)),
                ('Nom_et_prenoms_de_la_mere', models.CharField(max_length=100)),
                ('Mairie_de_demande', models.CharField(choices=[('ABOB', 'ABOBO'), ('ADJA', 'ADJAME'), ('ODIE', 'ODIENNE')], max_length=100)),
                ('Nombre_de_copie', models.IntegerField()),
                ('Telephone', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('status', models.CharField(default='NON_TRAITE', max_length=20)),
                ('slug', models.SlugField(max_length=128)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('exemplaire', models.FileField(blank=True, null=True, upload_to='extraits')),
            ],
        ),
        migrations.CreateModel(
            name='Reclamation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=130)),
                ('Prenoms', models.CharField(max_length=130)),
                ('Telephone', models.CharField(max_length=130)),
                ('Message', models.CharField(max_length=98999)),
            ],
        ),
        migrations.CreateModel(
            name='Validation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('NON_TRAITE', 'NON_TRAITE'), ('ACCEPTE', 'ACCEPTE'), ('REFUSE', 'REFUSE'), ('DELIVRE', 'DELIVRE')], default='NON_TRAITE', max_length=20)),
            ],
        ),
    ]
