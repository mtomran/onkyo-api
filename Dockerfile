FROM python:2.7
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN easy_install onkyo-eiscp
COPY . .
CMD [ "python", "-u", "./main.py" ]