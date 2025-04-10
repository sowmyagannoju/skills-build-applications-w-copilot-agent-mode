from django.core.management.base import BaseCommand
from tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Add test users
        user1 = User.objects.create(email='john.doe@example.com', name='John Doe', password='password123')
        user2 = User.objects.create(email='jane.smith@example.com', name='Jane Smith', password='password123')

        # Add test teams
        team1 = Team.objects.create(name='Team Alpha', members=[user1.id, user2.id])

        # Add test activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30)
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45)

        # Add test leaderboard
        Leaderboard.objects.create(team=team1, score=100)

        # Add test workouts
        Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session to start the day.')
        Workout.objects.create(name='HIIT', description='High-Intensity Interval Training for fat burning.')

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
