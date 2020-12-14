# Flask environment

# Use python image as base
FROM python:3

# Install requirements
COPY ./requirements.txt /home/nate.dev/requirements.txt
RUN pip install -r /home/nate.dev/requirements.txt

# Make Docker use a non-root user
RUN useradd --shell /bin/bash nate.dev
RUN chown --recursive nate.dev:nate.dev /opt /usr
ENV HOME /home/nate.dev

# Set current user to non-root user
USER nate.dev

# Set the working directory
WORKDIR /home/nate.dev

# Run uwsgi
CMD ["uwsgi", "application.ini"]
