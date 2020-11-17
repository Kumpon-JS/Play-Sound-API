FROM ubuntu:18.04
SHELL [ "/bin/bash", "-c" ]
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
# RUN apt install python3-gi
RUN python --version
RUN pip list
COPY . .
RUN python -m pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]