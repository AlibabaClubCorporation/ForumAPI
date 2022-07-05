from rest_framework import serializers
from .models import * 


class _FilterAnswerSerializer( serializers.ListSerializer ):
    """ Класс сериализатора, который убирает из общего списка Answers записей записи с parent_answer != None """

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
        fields = ( 'creator', 'date_of_creation', 'is_correct', 'content', 'child_answers' )



class PhorSerializer( serializers.ModelSerializer ):
    """ Сериализатор для экземпляра Phors модели """

    answers = _AnswerSerializer( many = True )

    theme = serializers.SlugRelatedField( slug_field = 'slug', read_only = True )
    creator = serializers.SlugRelatedField( slug_field = 'username', read_only = True )

    class Meta:
        model = Phors
        fields = ( 'title', 'creator', 'theme', 'date_of_creation', 'slug', 'description', 'answers' )


class PhorsSerializer( serializers.ModelSerializer ):
    """ Сериализатор для экземпляров Phors модели """

    theme = serializers.SlugRelatedField( slug_field = 'slug', read_only = True )
    creator = serializers.SlugRelatedField( slug_field = 'username', read_only = True )

    class Meta:
        model = Phors 
        fields = ( 'title', 'slug', 'theme', 'creator', )



class ThemesSerializer( serializers.ModelSerializer ):
    """ Сериализатор для экземпляров Themes модели """

    class Meta:
        model = Themes 
        fields = ( 'title', 'slug', )

class ThemeSerializer( serializers.ModelSerializer ):
    """ Сериализатор для экземпляра Themes модели """

    phors = PhorsSerializer( many = True )

    class Meta:
        model = Themes 
        fields = ( 'title', 'slug', 'phors', )




