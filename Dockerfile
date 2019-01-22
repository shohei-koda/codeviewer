FROM python:3.7

ARG project_dir=/gooya_cycleci/

ADD src/requirements.txt $project_dir

WORKDIR $project_dir

RUN pip install -r requirements.txt
