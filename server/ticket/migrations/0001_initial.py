# Generated by Django 3.1.2 on 2021-01-10 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import ticket.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=64, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'booking',
            },
        ),
        migrations.CreateModel(
            name='UpLoad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('remark', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, upload_to=ticket.models.file_path_name)),
                ('date', models.DateField(auto_now_add=True)),
                ('object_id', models.PositiveIntegerField()),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='uploads', to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'db_table': 'upload',
            },
        ),
        migrations.CreateModel(
            name='ticket_history',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('serial_no', models.CharField(blank=True, max_length=32, null=True)),
                ('air_line', models.CharField(blank=True, max_length=16, null=True)),
                ('air_info', models.CharField(blank=True, max_length=1024, null=True)),
                ('air_class', models.CharField(blank=True, max_length=64, null=True)),
                ('fare', models.FloatField(blank=True, null=True)),
                ('tax', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('is_confirm', models.BooleanField(blank=True, default=False, null=True)),
                ('is_cancel', models.BooleanField(blank=True, default=False, null=True)),
                ('is_booking', models.BooleanField(blank=True, default=True, null=True)),
                ('is_complete', models.BooleanField(blank=True, default=False, null=True)),
                ('date', models.DateField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('author', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical ticket',
                'db_table': 'ticket_history',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(blank=True, max_length=32, null=True)),
                ('air_line', models.CharField(blank=True, max_length=16, null=True)),
                ('air_info', models.CharField(blank=True, max_length=1024, null=True)),
                ('air_class', models.CharField(blank=True, max_length=64, null=True)),
                ('fare', models.FloatField(blank=True, null=True)),
                ('tax', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('is_confirm', models.BooleanField(blank=True, default=False, null=True)),
                ('is_cancel', models.BooleanField(blank=True, default=False, null=True)),
                ('is_booking', models.BooleanField(blank=True, default=True, null=True)),
                ('is_complete', models.BooleanField(blank=True, default=False, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ticket_authors', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ticket',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json', models.JSONField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('read', models.BooleanField(blank=True, default=False, null=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'message',
            },
        ),
        migrations.CreateModel(
            name='itinerary_history',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('serial_no', models.CharField(blank=True, max_length=32, null=True)),
                ('email', models.CharField(blank=True, max_length=64, null=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('passport_no', models.CharField(blank=True, max_length=16, null=True)),
                ('entry', models.CharField(blank=True, max_length=256, null=True)),
                ('exit', models.CharField(blank=True, max_length=256, null=True)),
                ('ticket1', models.CharField(blank=True, max_length=256, null=True)),
                ('ticket2', models.CharField(blank=True, max_length=256, null=True)),
                ('hotel', models.CharField(blank=True, max_length=256, null=True)),
                ('is_lock', models.BooleanField(default=False, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('author', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('booking', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ticket.booking')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('ticket', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ticket.ticket')),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical itinerary',
                'db_table': 'itinerary_history',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(blank=True, max_length=32, null=True)),
                ('email', models.CharField(blank=True, max_length=64, null=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('passport_no', models.CharField(blank=True, max_length=16, null=True)),
                ('entry', models.CharField(blank=True, max_length=256, null=True)),
                ('exit', models.CharField(blank=True, max_length=256, null=True)),
                ('ticket1', models.CharField(blank=True, max_length=256, null=True)),
                ('ticket2', models.CharField(blank=True, max_length=256, null=True)),
                ('hotel', models.CharField(blank=True, max_length=256, null=True)),
                ('is_lock', models.BooleanField(default=False, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='itinerary_authors', to=settings.AUTH_USER_MODEL)),
                ('booking', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='itineraries', to='ticket.booking')),
                ('ticket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='itineraries', to='ticket.ticket')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='itinerary_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'itinerary',
                'permissions': (('lock_itinerary', 'Can lock itinerary'),),
            },
        ),
        migrations.CreateModel(
            name='booking_history',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=64, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('author', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical booking',
                'db_table': 'booking_history',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
