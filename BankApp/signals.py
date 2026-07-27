from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserProfile, Transaction

User = get_user_model()


# Automatically create a profile when a new user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, balance=0)


# Track balance changes
@receiver(pre_save, sender=UserProfile)
def track_balance_changes(sender, instance, **kwargs):
    if not instance.pk:
        return

    old_instance = UserProfile.objects.filter(pk=instance.pk).first()
    if not old_instance:
        return

    old_balance = old_instance.balance
    new_balance = instance.balance

    if new_balance != old_balance:
        instance._balance_diff = new_balance - old_balance
        instance._description = "Credit" if new_balance > old_balance else "Debit"


# Create transaction after balance changes
@receiver(post_save, sender=UserProfile)
def create_transaction(sender, instance, created, **kwargs):
    if created:
        return

    if hasattr(instance, "_balance_diff") and instance._balance_diff != 0:
        amount = abs(instance._balance_diff)

        Transaction.objects.create(
            user=instance.user,
            amount=amount,
            balance_after=instance.balance,
            description=instance._description,
        )

        print(
            f"{instance._description}: {amount:,.2f} | New Balance: {instance.balance:,.2f}"
        )
