from rest_framework import serializers

from .models import * 


class _FilterAnswerSerializer( serializers.ListSerializer ):
    """ Класс сериализатора, который убирает из общего списка Answers записи c parent_answer != None """

    def to_representation(self, data):
        data = data.filter( parent_answer = None )

        return super().to_representation(data)

class _ChildAnswerSerializer( serializers.Serializer ):
    """ Сериализатор для рекурсии и отображения дочерних Answers """

    def to_representation(self, value):
        serializer = _AnswerSerializer( value, context = self.context )

        return serializer.data

class _AnswerSerializer( serializers.ModelSerializer ):
    """ Сериализатор для Answers """

    child_answers = _ChildAnswerSerializer( many = True )
    creator = serializers.SlugRelatedField( slug_field = 'username', read_only = True ) 

    class Meta:
        list_serializer_class = _FilterAnswerSerializer
        model = Answers
        fields = ( 'creator', 'date_of_creation', 'is_correct', 'content', 'child_answers', 'pk' )

class CreateAnswerSerializer( serializers.ModelSerializer ):
    """ Сериализатор для создания экземпляров Answers модели """

    creator = serializers.HiddenField( default = serializers.CurrentUserDefault() )

    class Meta:
        model = Answers 
        fields = ( 'content', 'phor', 'parent_answer', 'creator' )



class _ListPhorSerializer( serializers.ModelSerializer ):
    """ Сериализатор для экземпляров Phors модели """

    theme = serializers.SlugRelatedField( slug_field = 'slug', read_only = True )
    creator = serializers.SlugRelatedField( slug_field = 'username', read_only = True )

    class Meta:
        model = Phors 
        fields = ( 'title', 'slug', 'theme', 'creator', )

class PhorSerializer( serializers.ModelSerializer ):
    """ Сериализатор для экземпляра Phors модели """

    answers = _AnswerSerializer( many = True )

    theme = serializers.SlugRelatedField( slug_field = 'slug', read_only = True )
    creator = serializers.SlugRelatedField( slug_field = 'username', read_only = True )

    class Meta:
        model = Phors
        fields = ( 'title', 'creator', 'theme', 'date_of_creation', 'slug', 'description', 'answers', 'pk' )

class CreatePhorSerializer( serializers.ModelSerializer ):
    """ Сериализатор для создания экземпляра Phors модели """

    creator = serializers.HiddenField( default = serializers.CurrentUserDefault() )

    class Meta:
        model = Phors 
        fields = ( 'title', 'slug', 'description', 'theme', 'creator' )



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

    
    class Meta:
        model = Themes
        fields = ( 'title', 'slug' )
