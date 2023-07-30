FROM python:3.9-alpine

# Add your application
COPY ./run.py /app/run.py
COPY ./config.ini /app/config.ini
RUN chmod +r /app/config.ini
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy and enable your CRON task
COPY ./crontab /app/crontab
RUN crontab /app/crontab

# Create empty log (TAIL needs this)
RUN touch /tmp/out.log

# Start TAIL - as your always-on process (otherwise - container exits right after start)
CMD crond && tail -f /tmp/out.log