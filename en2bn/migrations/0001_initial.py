# Generated by Django 3.1.6 on 2021-02-27 05:32

from django.db import migrations, models
import en2bn.comma_separated_strings_field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ABValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_hash_indx', models.BigIntegerField()),
                ('a', models.IntegerField()),
                ('b', models.IntegerField()),
                ('m', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='WordList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_hash_indx', models.BigIntegerField()),
                ('s_hash_indx', models.BigIntegerField()),
                ('bn', models.CharField(max_length=100)),
                ('en', models.CharField(max_length=100)),
                ('bn_syns', en2bn.comma_separated_strings_field.CommaSeparatedStringsField(blank=True, max_length=1000)),
                ('en_syns', en2bn.comma_separated_strings_field.CommaSeparatedStringsField(blank=True, max_length=1000)),
                ('sents', en2bn.comma_separated_strings_field.QuoteSeparatedStringsField(blank=True, max_length=5000)),
            ],
        ),
    ]
