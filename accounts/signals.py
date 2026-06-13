from .utils import (
    generate_student_credentials,
    generate_lecturer_credentials,
)


def post_save_account_receiver(instance=None, created=False, *args, **kwargs):
    if created:
        if instance.is_student:
            username, password = generate_student_credentials()
            instance.username = username
            instance.set_password(password)
            instance.save()

        if instance.is_lecturer:
            username, password = generate_lecturer_credentials()
            instance.username = username
            instance.set_password(password)
            instance.save()
