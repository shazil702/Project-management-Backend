from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Team
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(m2m_changed, sender=Team.teamMembers.through)
def check_user_team(sender, instance, action, reverse, pk_set, **kwargs):
    if action == 'pre_add':
        for pk in pk_set:
            user = User.objects.get(pk=pk)
            if user.teamMember.exists():
                raise ValidationError(f'{user.username} is member of another team')