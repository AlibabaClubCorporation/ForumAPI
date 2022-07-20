from email.policy import default
from rest_framework import serializers

from .models import * 
from .services.service_of_slug import text_to_slug
from .services.service_of_data_base import get_answer_by_pk, get_theme_by_slug, get_phor_by_slug, get_user_of_client_by_pk

# Рекурсия дочерних ответов вызывает проблемы с оптимизацией sql запросов. по этому отложена до поиска решений

# class _FilterAnswerSerializer( serializers.ListSerializer ):
#     """ Класс сериализатора, который убирает из общего списка Answers записи c parent_answer != None """

#     def to_representation(self, data):
#         data = data.filter( parent_answer = None )

#         return super().to_representation(data)

# class _ChildAnswerSerializer( serializers.Serializer ):
#     """ Сериализатор для рекурсии и отображения дочерних Answers """

#     def to_representation(self, value):
#         serializer = _AnswerSerializer( value, context = self.context )

#         return serializer.data

class _AnswerSerializer( serializers.ModelSerializer ):
    """ Сериализатор для Answers """

    creator = serializers.SlugRelatedField( slug_field = 'username', read_only = True)
    parent_answer = serializers.PrimaryKeyRelatedField( queryset = Phors.objects.all() )
    # child_answers = _ChildAnswerSerializer

    class Meta:
        # list_serializer_class = _FilterAnswerSerializer
        model = Answers
        fields = ( 'creator', 'date_of_creation', 'is_correct', 'content', 'parent_answer', 'pk' )

class CreateAnswerSerializer( serializers.ModelSerializer ):
    """ Сериализатор для создания экземпляров Answers модели """

    class Meta:
        model = Answers 
        fields = ( 'content', 'parent_answer',)

    def create(self, validated_data):
        slug_of_phor = self.context['view'].kwargs.get( 'slug_of_phor' )

        validated_data['creator'] = self.context['view'].kwargs.get( 'user_of_client' )

        validated_data['phor'] = get_phor_by_slug( slug_of_phor )

        return super().create(validated_data)

class ChangeContentOfAnswerSerializer( serializers.ModelSerializer ):
    """ Сериализатор для изменения содержимого ответа """

    class Meta:
        model = Answers
        fields = ( 'content', )

    def save(self, **kwargs):
        answer = get_answer_by_pk( kwargs.get( 'pk_of_answer' ) )
        answer.content = self.validated_data[ 'content' ]
        answer.save()



class _ListPhorSerializer( serializers.ModelSerializer ):
    """ Сериализатор для экземпляров Phors модели """

    creator = serializers.SlugRelatedField( slug_field = 'username', read_only = True)

    class Meta:
        model = Phors 
        fields = ( 'title', 'slug', 'creator', )

class PhorSerializer( serializers.ModelSerializer ):
    """ Сериализатор для экземпляра Phors модели """

    answers = _AnswerSerializer( many = True )

    theme = serializers.SlugRelatedField( slug_field = 'slug', read_only = True )
    creator = serializers.SlugRelatedField( slug_field = 'username', read_only = True)

    class Meta:
        model = Phors
        fields = ( 'title', 'creator', 'theme', 'date_of_creation', 'slug', 'description', 'answers', 'pk' )

class CreatePhorSerializer( serializers.ModelSerializer ):
    """ Сериализатор для создания экземпляра Phors модели """

    class Meta:
        model = Phors 
        fields = ( 'title', 'description', )

    def create(self, validated_data):
        slug_of_theme = self.context['view'].kwargs.get( 'slug_of_theme' )

        validated_data['creator'] = self.context['view'].kwargs.get( 'user_of_client' )

        validated_data['slug'] = text_to_slug( validated_data['title'] )
        validated_data['theme'] = get_theme_by_slug( slug_of_theme )

        return super().create(validated_data)

class ChangeDescriptionOfPhorSerializer( serializers.ModelSerializer ):
    """ Сериализатор для изменения содержимого фора """

    class Meta:
        model = Phors
        fields = ( 'description', )

    def save(self, **kwargs):
        phor = get_phor_by_slug( kwargs.get( 'slug_of_phor' ) )
        phor.description = self.validated_data[ 'description' ]
        phor.save()



class ThemeSerializer( serializers.ModelSerializer ):
    """ Сериализатор для экземпляра Themes модели """

    phors = _ListPhorSerializer( many = True )

    class Meta:
        model = Themes 
        fields = ( 'title', 'slug', 'phors', 'pk' )

class ListThemeSerializer( serializers.ModelSerializer ):
    """ Сериализатор для экземпляров Themes модели """

    class Meta:
        model = Themes 
        fields = ( 'title', 'slug', )

class CreateThemeSerializer( serializers.ModelSerializer ):
    """ Сериализатор для создания экземпляра Themes модели """

    creator = serializers.HiddenField( default = serializers.CurrentUserDefault() )

    class Meta:
        model = Themes
        fields = ( 'title', 'creator' )

    def create(self, validated_data):
        validated_data['slug'] = text_to_slug( validated_data['title'] )

        return super().create(validated_data)



class LogOfClientSerializer( serializers.ModelSerializer ):
    """ Сериализатор для экземпляра ( -ов ) LogOfClient модели """

    class Meta:
        model = LogOfClient
        fields = '__all__'


class LogOfUserOfClientSerializer( serializers.ModelSerializer ):
    """ Сериализатор для экземпляра ( -ов ) LogOfUserOfClient модели """

    class Meta:
        model = LogOfUserOfClient
        fields = '__all__'



class UserOfClientSerializer( serializers.ModelSerializer ):
    """ Сериализатор для экземпляров UserOfClient модели """

    class Meta:
        model = UsersOfClient
        fields = '__all__'

class DetailUserOfClientSerializer( UserOfClientSerializer ):
    """ Сериализатор для экземпляра UserOfClient модели """

    logs = LogOfUserOfClientSerializer( many = True )

class CreateUserOfClientSerializer( UserOfClientSerializer ):
    """ Сериализатор для создания экземпляра UserOfClient модели """

    client = serializers.HiddenField( default = serializers.CurrentUserDefault() )