# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install system dependencies (kubectl, terraform, ansible, docker-cli optional)
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    && chmod +x kubectl \
    && mv kubectl /usr/local/bin/

# Optional: Install Terraform CLI
RUN curl -LO https://releases.hashicorp.com/terraform/1.6.7/terraform_1.6.7_linux_amd64.zip \
    && unzip terraform_1.6.7_linux_amd64.zip \
    && mv terraform /usr/local/bin/ \
    && rm terraform_1.6.7_linux_amd64.zip

# Optional: Install Ansible
RUN pip install ansible

# Default command
CMD ["python3"]
