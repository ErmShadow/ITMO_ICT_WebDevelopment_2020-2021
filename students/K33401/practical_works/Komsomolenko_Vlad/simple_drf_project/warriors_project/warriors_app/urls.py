from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
   path('warriors/', WarriorAPIView.as_view()),
   path('profession/create/', ProfessionCreateView.as_view()),
   path('skills/', SkillAPIView.as_view()),
   path('skills/create/', SkillCreateView.as_view()),
   path('warriors/skills/create/', SkillOfWarriorAPIView.as_view()),
   path('warriors/list/', WarriorListAPIView.as_view()),
   path('profession/generic_create/', ProfessionCreateAPIView.as_view()),
   path('warriors/create/', WarriorsCreateView.as_view()),
   path('warriors/updel/<int:pk>', WarriorsUpdateDeleteView.as_view()),
   path('warriors/profession/', WarriorsProfessionSkillView.as_view()),
   path('warriors/professionskill/', WarriorsProfessionView.as_view()),
   path('warriors/skill/', WarriorsSkillView.as_view()),
]
