FROM public.ecr.aws/lambda/python:3.10


RUN pip install pipenv 


COPY ["Pipfile", "Pipfile.lock","./"]

RUN pipenv install --system --deploy

COPY ["lambda_function.py","gb_model.bin", "knn_model.bin","./"]


CMD ["lambda_function.lambda_handler"]