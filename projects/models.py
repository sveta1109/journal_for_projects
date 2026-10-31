from django.db import models


# Create your models here.
class Project(models.Model):
    TYPES = [('termpaper',"Курсовая"), ('article',"Статья"),('diploma', "Диплом"),('other', "Другое")]
    title = models.CharField("Название", max_length=200)
    project_type = models.CharField("Тип", max_length=20, choices=TYPES)
    subject = models.CharField("Дисциплина", max_length=100, blank=True)
    supervisor = models.CharField("Научрук", max_length=100, blank=True)
    deadline = models.DateTimeField("Дедлайн", null=True, blank=True)
    date_of_start = models.DateTimeField(auto_now_add=True)
    date_of_finish = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_of_start"]
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.title

    def progress(self):
        tasks = Task.objects.filter(chapter__projects=self)
        total = tasks.count()
        done = tasks.filter(is_done=True).count()
        return done, total


class Chapter(models.Model):
    STATUSES = [('todo', "Не начата"), ("in process","В процессе"), ('review', "На проверке"),('done', "Завершена!"), ('fail',"Заброшена")]
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='chapters')
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    title = models.CharField("Название", max_length=200, )
    status = models.CharField("Статус", max_length=20, choices=STATUSES, default='Не начата')
    order = models.PositiveIntegerField("Порядок", default=0 )

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Глава'
        verbose_name_plural = "Главы"

    def __str__(self):
        return self.title

    def depth(self):
        d, node = 0, self
        while node.parent_id:
            d += 1
            node = node.parent
        return d


class Task(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='tasks')
    text = models.CharField("Задача", max_length=300)
    is_done = models.BooleanField("Сделано", default=False)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering= ['order', 'id']
        verbose_name = 'Задача'
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.text