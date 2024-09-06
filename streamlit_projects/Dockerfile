# Use Python 3.10.12 as the base image
FROM python:3.10.12-slim

# Create a working directory
WORKDIR /app

# Update the system and install necessary packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    iproute2 \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port
EXPOSE 8501

# Health check (Optional)
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Define the command to run the Streamlit application
ENTRYPOINT ["streamlit", "run", "Anasayfa.py", "--server.port=8501", "--server.address=0.0.0.0"]

# Debugging: Show environment variables and check if the port is open
RUN env
RUN ss -tuln



#docker build -t langchainmystic .
#docker run -p 8501:8501 langchainmystic
