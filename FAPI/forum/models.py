from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from . import abstract_models 



class UsersOfClient( models.Model ):
    """
        Модель пользователя клиентского форума
    """

    client_admin = models.BooleanField( verbose_name = 'Наличие статуса админа у пользователя клиентского форума', default = False )

    username = models.CharField( verbose_name = 'Имя пользователя клиентского форума', max_length = 255)
    email = models.EmailField( verbose_name = 'Почта пользователя клиентского форума', blank = True, null = True, )
    
    date_of_creation = models.DateTimeField( verbose_name = 'Дата создания пользователя клиента', auto_now_add = True )

    client = models.ForeignKey( verbose_name = 'Клиент пользователя', to = User, on_delete = models.CASCADE, related_name = 'accounts', )

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = [ '-date_of_creation', 'client', 'username', ]
        verbose_name = 'Пользователь клиента'
        verbose_name_plural = 'Пользователи клиентов'



class Themes(models.Model):
    """
        Класс модели темы
    """

    title = models.CharField( verbose_name = "Название темы", max_length = 128, unique = True, )

    slug = models.SlugField( verbose_name = "Слаг темы", max_length = 256, unique = True, db_index = True, )

    creator = models.ForeignKey( verbose_name = 'Создатель темы', to = User, on_delete = models.SET_NULL, null = True, related_name = 'themes')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse( 'theme', kwargs = { 'slug_of_theme' : self.slug } )

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'



class Phors(models.Model):
    """
        Класс модели фора
    """

    title = models.CharField( verbose_name = "Заголовок фора", max_length = 128, unique = True )
    description = models.TextField( verbose_name = "Описание проблемы в форе", max_length = 4096, )

    date_of_creation = models.DateTimeField( verbose_name = "Дата создания фора", auto_now_add = True, )

    theme = models.ForeignKey( verbose_name = "Ссылка на тему фора", to = Themes, on_delete = models.CASCADE, related_name = 'phors' )
    creator = models.ForeignKey( verbose_name = "Ссылка на создателя фора", to = UsersOfClient, on_delete = models.SET_NULL, null = True, related_name = 'phors' )

    slug = models.SlugField( verbose_name = "Слаг фора", max_length = 256, unique = True, db_index = True, )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse( 'phor', kwargs = { 'slug_of_phor' : self.slug, 'slug_of_theme' : self.theme.slug } )

    class Meta:
        ordering = [ '-date_of_creation', 'title' ]
        verbose_name = 'Фор'
        verbose_name_plural = 'Форы'



class Answers(models.Model):
    """
        Класс модели ответа
    """

    content = models.TextField( verbose_name = "Содержимое ответа", max_length = 4096, )

    date_of_creation = models.DateTimeField( verbose_name = "Дата создания ответа", auto_now_add = True, )

    is_correct = models.BooleanField( verbose_name = "Наличие статуса 'правильный ответ' у ответа", default = False, )

    phor = models.ForeignKey( verbose_name = "Ссылка на фор ответа", to = Phors, on_delete = models.CASCADE, related_name = 'answers' )
    creator = models.ForeignKey( verbose_name = "Ссылка на создателя ответа", to = UsersOfClient, on_delete = models.CASCADE, related_name = 'answers' )
    parent_answer = models.ForeignKey( verbose_name = "Ссылка на родительский ответ ответа", to = 'self', on_delete = models.CASCADE, blank = True, null = True, related_name = 'child_answers' )

    def __str__(self) -> str:
        return f'Ответ от {self.creator.username} для фора {self.phor.title} | PK : {self.pk}'

    class Meta:
        ordering = [ '-date_of_creation', ]
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'



class LogOfClient( abstract_models.Log ):
    """
        Класс модели лога клиента ( Записи событий связанных непосредственно с клиентом )
    """

    client = models.ForeignKey( verbose_name = 'Клиент', to = User, on_delete = models.CASCADE, related_name = 'logs' )

    def __str__(self) -> str:
        return f'Запись лога клиента {self.client.username}'

    class Meta:
        ordering = [ '-date_of_creation', 'client__username', ]
        verbose_name = 'Лог клиента'
        verbose_name_plural = 'Логи клиентов'



class LogOfUserOfClient( abstract_models.Log ):
    """
        Класс модели лога пользователя клиента ( Записи событий связанных непосредственно с пользователем клиента )
    """

    user_of_client = models.ForeignKey( verbose_name = 'Пользователь клиента', to = UsersOfClient, on_delete = models.CASCADE, related_name = 'logs' )

    def __str__(self) -> str:
        return f'Запись лога пользователя клиента {self.user_of_client.username}'

    class Meta:
        ordering = [ '-date_of_creation', 'user_of_client__client__username', 'user_of_client__username', ]
        verbose_name = 'Лог пользователя клиента'
        verbose_name_plural = 'Логи пользователей клиентов'
