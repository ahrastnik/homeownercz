FROM python:3.8.17-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install all required Python packages
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN playwright install --with-deps chromium

# Setup Django Environment
COPY ./backend /project
WORKDIR /project

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
