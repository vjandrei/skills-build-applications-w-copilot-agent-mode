from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc, is_superhero=True),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
        ]

        # Create Activities
        for user in users:
            Activity.objects.create(user=user, type='Running', duration=30, date=timezone.now().date())
            Activity.objects.create(user=user, type='Cycling', duration=45, date=timezone.now().date())

        # Create Workouts
        workout1 = Workout.objects.create(name='Pushups', description='Upper body workout')
        workout2 = Workout.objects.create(name='Squats', description='Lower body workout')
        workout1.suggested_for.set(users[:3])  # Marvel
        workout2.suggested_for.set(users[3:])  # DC

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
