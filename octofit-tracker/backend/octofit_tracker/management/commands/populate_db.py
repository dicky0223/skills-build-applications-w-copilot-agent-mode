from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models


from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # 清空舊資料
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # 建立隊伍
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # 建立使用者
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel),
            User.objects.create_user(username='captain', email='captain@marvel.com', password='password', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc),
            User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc),
        ]

        # 建立活動
        activities = [
            Activity.objects.create(user=users[0], type='run', duration=30, calories=200),
            Activity.objects.create(user=users[1], type='cycle', duration=45, calories=350),
            Activity.objects.create(user=users[2], type='swim', duration=60, calories=400),
            Activity.objects.create(user=users[3], type='yoga', duration=50, calories=150),
        ]

        # 建立排行榜
        Leaderboard.objects.create(user=users[0], score=500)
        Leaderboard.objects.create(user=users[1], score=400)
        Leaderboard.objects.create(user=users[2], score=600)
        Leaderboard.objects.create(user=users[3], score=550)

        # 建立訓練
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        Workout.objects.create(name='Strength Training', description='Strength for all heroes', duration=60)

        self.stdout.write(self.style.SUCCESS('octofit_db 已成功建立測試資料'))

# 你需要在 octofit_tracker/models.py 中定義 Team, Activity, Leaderboard, Workout 等模型。
