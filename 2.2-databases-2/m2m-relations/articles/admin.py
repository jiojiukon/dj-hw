from django.contrib import admin

from django.core.exceptions import ValidationError
from .models import Article, Tag, Scope
from django.forms import BaseInlineFormSet


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            for x, y in form.cleaned_data.items():
                if x == 'is_main' and y is True:
                    counter += 1 
            if counter > 1:
                raise ValidationError('Основной тэг может быть только один!')
            if counter == 0:
                raise ValidationError('Обязательно должен быть основной тэг!')
        return super().clean() 
    

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

