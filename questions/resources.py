from import_export import resources
from .models import Choice, ChoiceGroup, Question

class ChoiceResource(resources.ModelResource):
    class Meta:
        model = Choice

class ChoiceGroupResource(resources.ModelResource):
    class Meta:
        model = ChoiceGroup

class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question