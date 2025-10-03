# FROM python:3.11-slim

# # Create user 'user' with UID 1000 and HOME
# RUN useradd -m -u 1000 user

# WORKDIR /home/user/app

# # Copy requirements.txt as the non-root user
# COPY --chown=user requirements.txt .
# RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# # Copy the rest of your app as the non-root user
# COPY --chown=user . .

# # Switch to non-root user UID 1000
# USER user

# ENV HOME=/home/user
# ENV APP_PORT=7251
# EXPOSE 7251

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7251"]

FROM python:3.11-slim
WORKDIR /app
RUN echo 'print("Hello, world!")' > app.py
CMD ["python", "app.py"]
