FROM python:3.10
COPY . /flask-aws-pipeline
WORKDIR /flask-aws-pipeline
RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ "python", "excel_to_json/app.py" ]
