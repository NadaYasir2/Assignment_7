# Generated by Django 5.0.4 on 2024-05-10 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_rename_clienttypes_clienttype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cid',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='orderdate',
            new_name='order_date',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='pid',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='shippingdate',
            new_name='shipping_date',
        ),
        migrations.RemoveField(
            model_name='clienttype',
            name='type',
        ),
        migrations.AddField(
            model_name='clienttype',
            name='type_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='cid',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='oid',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='pid',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
