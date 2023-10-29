Сущности:

1. Преподаватель (админ)

2. Предмет

3. Класс

4. Ученик (пользователь). При регистрации обязательно должен указать класс.

5. Домашнее задание. Выдается преподавателем по определенному предмету для определеннного класса.

6. Ответ на домашнее задание. Создается учеником класса, которому было задано д\з и содержит информацию о том, какой ученик его отправил.

```python
# models.py

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=100)
    date_from = models.DateField()
    date_to = models.DateField()

    def __str__(self):
        return self.name  # TODO: добавить информацию про учебный год в отображаемое название


class Student(AbstractUser):
    # username, email, password, password_confirmation
    fio = models.CharField(max_length=250)
    student_class = models.ForeignKey('Class', on_delete=models.CASCADE, null=True, default=None)
    submitted_homeworks = models.ManyToManyField('Homework', through='HomeworkSubmission')
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.fio


class Homework(models.Model):
    name = models.CharField(max_length=250)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    class_it_is_assigned_to = models.ForeignKey('Class', on_delete=models.CASCADE)
    date_of_issue = models.DateField(default=datetime.datetime.today())
    deadline_date = models.DateField()
    assignment_text = models.TextField()
    fines_information = models.TextField(blank=True, null=True)
    students_who_submitted_it = models.ManyToManyField('Student', through='HomeworkSubmission')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('homework_detail', args=[str(self.id)])

    def get_absolute_url_teacher(self):
        return reverse('teacher_homework_detail', args=[str(self.id)])

    def get_dates(self):
        return f"Выдано: {self.date_of_issue}, дедлайн: {self.deadline_date}"

    def snippet(self):
        return self.assignment_text[:250]


class HomeworkSubmission(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    homework = models.ForeignKey('Homework', on_delete=models.CASCADE)
    submission_date = models.DateField(auto_now_add=True)
    submission_text = models.TextField()
    grade = models.PositiveIntegerField(null=True, default=None)

    def get_absolute_url(self):
        return reverse('submitted_homework_detail', args=[str(self.id)])

    def snippet(self):
        return self.submission_text[:250]


class HomeworkDisplay:
    def __init__(self, homework, submission):
        self.homework = homework
        self.submission = submission

    def get_absolute_url(self):
        return self.homework.get_absolute_url()

    def snippet(self):
        return self.homework.snippet()

    def __str__(self):
        return self.homework.name

    def get_grade(self):
        return self.submission.grade if self.submission else None

```
Клиентская часть (ученик):

Ученики могут регистрироваться в системе. Обязательно при регистрации указывать класс.
Ученик может просматривать домашние задания, выданные его классу, и отправлять ответы на них. Ответ можно редактировать вплоть до проверки преподавателем. После проверки и выставления отметки возможность редактирования закрывается. 
Также ученик может частично изменять данные своего профиля (ФИО, дату рождения и адрес).

Клиентская часть (преподаватель):

Преподаватель может добавлять новые классы и предметы только через панель администратора. В созданной системе сущность преподавателя уникальна. 
Преподаватель не может редактировать данные своего профиля.
Преподаватель может создавать, редактировать и удалять домашние задания, а также выставлять отметки сданным домашним заданиям. Отметка должна лежать в диапазоне от 1 до 5.


Что ещё можно сделать:
 1. Добавить поддержку markdown-форматирования вводимых текстовых полей

 2. Добавить возможность прикреплять файлы

 3. Дать пользователю возможность изменять логин и пароль

 4. Восстановление пароля по электронной почте. Также добавить поле с почтой при регистрации

 5. Обязательное одобрение админом присоединяющихся в качестве пользователей учеников/доступ к регистрации на платформе по специальному коду 

 6. Более проработанные ссылки «назад» (сейчас большая часть ведет на основную страницу, а не на фактически предыдущую)

 7. Поддержка нескольких преподавательских профилей (требует переработки концепции всего приложения) 

 8. Разобраться, как работает голубой background div и сделать его по ширине браузерного окна, а не по ширине контента 

Демонстрация работоспособности сайта:
![type:video](./static/v.mp4?noautoplay=1)
