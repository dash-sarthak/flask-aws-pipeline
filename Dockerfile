FROM python:3.10
COPY . /flask-aws-pipeline
WORKDIR /flask-aws-pipeline
RUN pip install -r requirements.txt
#RUN export FLASK_APP=app.py
EXPOSE 5000
WORKDIR /flask-aws-pipeline/excel_to_json
CMD [ "python3", "-u", "app.py" ]
