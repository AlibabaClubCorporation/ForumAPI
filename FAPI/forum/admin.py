from django.contrib import admin
from .models import *


class PhorInline( admin.StackedInline ):
    model = Phors 
    extra = 0

    readonly_fields = ( 'date_of_creation', )
    fieldsets = (
        ( None, {
            'fields' : ( ( 'creator', 'theme' ), 'title', 'date_of_creation', ),
        }),

        ( 'Description', {
            'classes' : ( 'collapse', ),
            'fields' : ( 'description', )
        }),

        ( 'Options', {
            'classes' : ( 'collapse', ),
            'fields' : ( 'slug', )
        })
    )

class AnswerInline( admin.StackedInline ):
    model = Answers
    extra = 0

    readonly_fields = ( 'date_of_creation', )
    fieldsets = (
        ( None, {
            'fields' : ( ( 'phor', 'creator' ), ('date_of_creation', 'is_correct')  )
        }),

        ( 'Content', {
            'classes' : ( 'collapse', ),
            'fields' : ( 'content', )
        })
    )


@admin.register( Themes )
class ThemesAdmin( admin.ModelAdmin ):
    search_fields = ( 'title', )
    list_filter = ( 'title', )
    list_display = ( 'title', )
    list_display_links = ( 'title', )

    prepopulated_fields = { 'slug' : ( 'title', ) }

    inlines = [PhorInline, ]

    save_on_top = True

@admin.register( Phors )
class PhorsAdmin( admin.ModelAdmin ):
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

        ( 'Description', {
            'classes' : ( 'collapse', ),
            'fields' : ( 'description', )
        }),

        ( 'Options', {
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
    list_display = ( 'creator', 'phor', 'date_of_creation', 'is_correct', )
    list_filter = ( 'date_of_creation', )
    readonly_fields = ( 'date_of_creation', )
    
    fieldsets = (
        ( None, {
            'fields' : ( ( 'phor', 'creator' ), ('date_of_creation', 'is_correct')  )
        }),

        ( 'Content', {
            'classes' : ( 'collapse', ),
            'fields' : ( 'content', )
        })
    )

    save_on_top = True
    save_as = True


