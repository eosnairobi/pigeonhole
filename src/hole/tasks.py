from celery import shared_task


@shared_task
def get_user_account(account_name):
    pass


@shared_task
def process_message():
    pass
