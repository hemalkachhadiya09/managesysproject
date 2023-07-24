# Generated by Django 2.0 on 2021-04-22 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addevent',
            fields=[
                ('NEvent', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('DEvent', models.CharField(max_length=70)),
                ('DateE', models.CharField(max_length=10)),
                ('TEvent', models.CharField(max_length=10)),
                ('Fund', models.CharField(max_length=10)),
                ('Venue', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='complain',
            fields=[
                ('Name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ctitle', models.CharField(max_length=20)),
                ('comp', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='guard_reg',
            fields=[
                ('uname', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VName', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='maintain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Month', models.CharField(max_length=10)),
                ('Amount', models.CharField(max_length=10)),
                ('pmethod', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('timestamp',),
            },
        ),
        migrations.CreateModel(
            name='rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Month', models.CharField(max_length=10)),
                ('Amount', models.CharField(max_length=10)),
                ('pmethod', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SendRecieve',
            fields=[
                ('sr', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='user_reg',
            fields=[
                ('uname', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=20)),
                ('mname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=10)),
                ('house', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Option', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='rent',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageapp.user_reg'),
        ),
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='manageapp.SendRecieve'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='manageapp.SendRecieve'),
        ),
        migrations.AddField(
            model_name='maintain',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageapp.user_reg'),
        ),
        migrations.AddField(
            model_name='guest',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageapp.user_reg'),
        ),
    ]