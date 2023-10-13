# Select Python version
FROM python:3.11

# Define working directory
WORKDIR /app

# Copy requirments text file into container
COPY requirements.txt .

#Install dependencies based on requirements.txt
RUN pip install -r requirements.txt

# Copy Python script into container
Copy semantics.py .

# Run container
CMD ["python", "semantics.py"]