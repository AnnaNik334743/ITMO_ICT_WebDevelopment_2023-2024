# Generated by Django 4.2.5 on 2023-10-01 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("homework_board_app", "0002_alter_student_fio_alter_student_group"),
    ]

    operations = [
        migrations.RenameModel(old_name="Group", new_name="Class",),
        migrations.RenameField(
            model_name="student", old_name="group", new_name="students_class",
        ),
        migrations.RemoveField(model_name="student", name="fio",),
    ]