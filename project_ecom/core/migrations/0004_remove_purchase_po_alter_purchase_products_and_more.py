# Generated by Django 5.1.4 on 2024-12-09 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_product_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='po',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='products',
            field=models.ManyToManyField(blank=True, to='core.items'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='status',
            field=models.CharField(choices=[('Vacio', 'Vacio'), ('Pendiente de aprobacion', 'Pendiente de aprobacion'), ('Pagado', 'Pagado'), ('En preparacion', 'En preparacion'), ('Listo para retirar', 'Listo para retirar'), ('Finalizado', 'Finalizado'), ('Cancelado', 'Cancelado')], default='Vacio', max_length=30),
        ),
    ]
