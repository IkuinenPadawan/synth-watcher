from apscheduler.schedulers.blocking import BlockingScheduler
from run import fetch_and_send

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=8)
def scheduled_job():
    fetch_and_send()
sched.start()