from apscheduler.schedulers.blocking import BlockingScheduler
from service.update_contacts_bd import update_contacts


def run_update_contacts():
    update_contacts()


scheduler = BlockingScheduler()
scheduler.add_job(run_update_contacts, "cron", hour=12, minute=00)
scheduler.start()
