# Generated by Django 2.1.7 on 2019-03-24 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields
import files.models.uploaded_file_permission_mixin
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('object_id', models.PositiveIntegerField()),
                ('filename', models.CharField(max_length=255)),
                ('filename_slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='filename', unique=True)),
                ('mimetype', models.CharField(max_length=255)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files_uploadedfile_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UploadedFile versioned',
                'verbose_name_plural': 'UploadedFiles versioned',
            },
            bases=(files.models.uploaded_file_permission_mixin.UploadedFilePermissionMixin, models.Model),
        ),
        migrations.CreateModel(
            name='UploadedFileVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('version', models.IntegerField(default=1)),
                ('download_hash', models.CharField(max_length=255, unique=True)),
                ('filestack_status', models.CharField(choices=[('Stored', 'Active'), ('InTransit', 'InTransit'), ('Failed', 'Failed'), ('Disabled', 'Disabled')], default='Stored', max_length=20)),
                ('filestack_url', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files_uploadedfileversion_related', to=settings.AUTH_USER_MODEL)),
                ('uploaded_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='files.UploadedFile')),
            ],
            options={
                'verbose_name': 'UploadedFile version',
                'verbose_name_plural': 'UploadedFile versions',
                'ordering': ['-version'],
            },
        ),
    ]
