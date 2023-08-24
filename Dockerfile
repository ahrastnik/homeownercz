FROM python:3.8.17-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

# Install all required Python packages
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Setup Django Environment
COPY ./backend /project
WORKDIR /project

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
