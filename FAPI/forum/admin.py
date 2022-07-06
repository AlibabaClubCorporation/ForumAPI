from django.contrib import admin
from .models import *


class PhorInline( admin.StackedInline ):
    """ StackedInline класс фора """

    model = Phors 
    extra = 0

    readonly_fields = ( 'date_of_creation', )
    fieldsets = (
        ( None, {
            'fields' : ( ( 'creator', 'theme' ), 'title', 'date_of_creation', ),
        }),

        ( 'Содержимое', {
            'classes' : ( 'collapse', ),
            'fields' : ( 'description', )
        }),

        ( 'Дополнительно', {
            'classes' : ( 'collapse', ),
            'fields' : ( 'slug', )
        })
    )

class AnswerInline( admin.StackedInline ):
    """ StackedInline класс ответа """

    model = Answers
    extra = 0

    readonly_fields = ( 'date_of_creation', 'parent_answer')
    fieldsets = (
        ( None, {
            'fields' : ( ( 'phor', 'creator' ), ('date_of_creation', 'is_correct'), 'parent_answer'  )
        }),

        ( 'Содержимое', {
            'classes' : ( 'collapse', ),
            'fields' : ( 'content', )
        })
    )

class ParentAnswerInline( admin.StackedInline ):
    """ StackedInline класс ответа при редактировании другого ответа """

    model = Answers
    extra = 0

    verbose_name = 'Дочерний омментарий'
    verbose_name_plural = 'Дочернии комментарии'

    readonly_fields = ( 'date_of_creation', )
    fieldsets = (
        ( None, {
            'fields' : ( ( 'phor', 'creator' ), ('date_of_creation', 'is_correct')  )
        }),

        ( 'Содержимое', {
            'classes' : ( 'collapse', ),
            'fields' : ( 'content', )
        })
    )


@admin.register( Themes )
class ThemesAdmin( admin.ModelAdmin ):
    """ Регистрация модели темы """

    search_fields = ( 'title', )
    list_filter = ( 'title', )
    list_display = ( 'title', )
    list_display_links = ( 'title', )

    prepopulated_fields = { 'slug' : ( 'title', ) }

    inlines = [PhorInline, ]

    save_on_top = True

@admin.register( Phors )
class PhorsAdmin( admin.ModelAdmin ):
    """ Регистрация модели фора """

    list_display = ( 'title', 'date_of_creation', 'theme', 'creator' )
    list_display_links = ( 'title', )
    list_editable = ( 'theme', )
    list_filter = ( 'title', 'date_of_creation', )
    search_fields = ( 'title', )
    readonly_fields = ( 'date_of_creation', )
    
    fieldsets = (
        ( None, {
            'fields' : ( ( 'creator', 'theme' ), 'title', 'date_of_creation', ),
        }),

        ( 'Описание проблемы', {
            'classes' : ( 'collapse', ),
            'fields' : ( 'description', )
        }),

        ( 'Дополнительно', {
            'classes' : ( 'collapse', ),
            'fields' : ( 'slug', )
        })
    )

    prepopulated_fields = { 'slug' : ( 'title', ) }

    inlines = [AnswerInline, ]

    save_on_top = True
    save_as = True


@admin.register( Answers )
class AnswersAdmin( admin.ModelAdmin ):
    """ Регистрация модели ответа """

    list_display = ( 'creator', 'phor', 'date_of_creation', 'is_correct', 'parent_answer')
    list_filter = ( 'date_of_creation', )
    readonly_fields = ( 'date_of_creation', 'parent_answer' )
    
    fieldsets = (
        ( None, {
            'fields' : ( ( 'phor', 'creator' ), ('date_of_creation', 'is_correct'), 'parent_answer'  )
        }),

        ( 'Содержимое', {
            'classes' : ( 'collapse', ),
            'fields' : ( 'content', )
        })
    )

    inlines = [ParentAnswerInline, ]

    save_on_top = True
    save_as = True


