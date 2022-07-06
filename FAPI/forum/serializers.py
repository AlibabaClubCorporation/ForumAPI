from rest_framework import serializers
from django.utils.text import slugify

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
        fields = ( 'creator', 'date_of_creation', 'is_correct', 'content', 'child_answers' )



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
        fields = ( 'title', 'creator', 'theme', 'date_of_creation', 'slug', 'description', 'answers' )

class CreatePhorSerializer( serializers.ModelSerializer ):
    """ Сериализатор для создания экземпляра Phors модели """

    class Meta:
        model = Phors 
        fields = ( 'title', 'description' )

    def create(self, validated_data):
        title = validated_data.get( 'title', None )
        description = validated_data.get( 'description', None )
        slug_of_phor = slugify( title )
        creator = self.context['request'].user
        
        slug_of_theme = self.context['request'].path.split('/')[2]

        theme = Themes.objects.get( slug = slug_of_theme )
        
        phor = Phors.objects.create( title = title, slug = slug_of_phor, description = description, theme = theme, creator = creator )

        return phor




class ThemeSerializer( serializers.ModelSerializer ):
    """ Сериализатор для экземпляра Themes модели """

    phors = _ListPhorSerializer( many = True )

    class Meta:
        model = Themes 
        fields = ( 'title', 'slug', 'phors', )

class ListThemeSerializer( serializers.ModelSerializer ):
    """ Сериализатор для экземпляров Themes модели """

    class Meta:
        model = Themes 
        fields = ( 'title', 'slug', )

class CreateThemeSerializer( serializers.ModelSerializer ):
    """ Сериализатор для создания экземпляра Themes модели """

    
    class Meta:
        model = Themes
        fields = ( 'title', )

    def create(self, validated_data):
        title = validated_data.get( 'title', None )
        slug_of_theme = slugify( title )
        
        theme = Themes.objects.create( title = title, slug = slug_of_theme )

        return theme
