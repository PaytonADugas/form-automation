# Generated by Django 3.2.3 on 2021-05-27 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NCCS_Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=256)),
                ('first_name', models.CharField(max_length=256)),
                ('birth_date', models.DateTimeField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=256)),
                ('disabilities', models.BooleanField()),
                ('school_year', models.DateTimeField()),
                ('grade', models.IntegerField()),
                ('record_permission', models.BooleanField()),
                ('previous_school_year', models.CharField(max_length=256)),
                ('previous_school', models.CharField(max_length=256)),
                ('mailing_address', models.CharField(max_length=256)),
                ('previous_school_city', models.CharField(max_length=256)),
                ('previous_school_state', models.CharField(max_length=256)),
                ('previous_school_zip', models.CharField(max_length=256)),
                ('previous_school_phone', models.CharField(max_length=256)),
                ('previous_school_been_suspended', models.BooleanField()),
                ('father_name', models.CharField(max_length=256)),
                ('father_employment', models.CharField(max_length=256)),
                ('mother_name', models.CharField(max_length=256)),
                ('mother_employment', models.CharField(max_length=256)),
                ('family_address', models.CharField(max_length=256)),
                ('family_city', models.CharField(max_length=256)),
                ('family_state', models.CharField(max_length=256)),
                ('family_zip', models.CharField(max_length=256)),
                ('family_phone', models.CharField(max_length=256)),
                ('family_email', models.CharField(max_length=256)),
                ('student_living_with', models.CharField(max_length=256)),
                ('student_guardian', models.CharField(max_length=256)),
                ('family_church', models.CharField(max_length=256)),
                ('HSLDA_membership', models.BooleanField()),
                ('primary_teacher', models.CharField(max_length=256)),
                ('high_school_eduication', models.BooleanField()),
                ('college_eduication', models.BooleanField()),
                ('list_training', models.CharField(max_length=256)),
                ('membership_agreement', models.BooleanField()),
                ('curriculum_agreement', models.BooleanField()),
                ('record_keeping_agreement', models.BooleanField()),
                ('parent_participation_agreement', models.BooleanField()),
                ('parent_home_agreement', models.BooleanField()),
                ('attendance_grades_agreement', models.BooleanField()),
                ('course_of_study_course_description_agreement', models.BooleanField()),
                ('read_handbook_agreement', models.BooleanField()),
                ('change_schools_agreement', models.BooleanField()),
                ('enrolment_dismissal_agreement', models.BooleanField()),
                ('parent_direction_agreement', models.BooleanField()),
                ('read_agreement', models.BooleanField()),
                ('father_signature', models.CharField(max_length=256)),
                ('father_sign_date', models.DateTimeField()),
                ('mother_signature', models.CharField(max_length=256)),
                ('mother_sign_date', models.DateTimeField()),
            ],
        ),
    ]
