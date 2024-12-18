from main_app.models import User, Note, StudyGroup
def run():
    user = User.objects.create_user(username='testuser', email='test@example.com', password='password123', role='student')
    group = StudyGroup.objects.create(name='Math Study Group')
    group.members.add(user)