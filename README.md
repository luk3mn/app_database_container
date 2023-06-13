# Container Application: PostgreSQL Database Creation on AWS EC2 Instance

## 1. Infrastructure Setup with Terraform

In this step, we use Terraform to provision the necessary infrastructure on AWS, specifically an EC2 instance for hosting the container.

## 2. Docker Configuration: PostgreSQL Database

We configure a PostgreSQL database using the Docker container with the Postgres version 15.0 image.

## 3. Python Automation: Control of Terraform and Docker

We use Python to automate the execution of Terraform and Docker commands for seamless provisioning of the infrastructure and deployment of the PostgreSQL container.

### Function 1: Terraform Execution

- This function executes the main Terraform commands, enabling the automatic creation of an EC2 instance.
- It ensures that the infrastructure is provisioned with the required specifications.

### Function 2: Get EC2 Instance Public IP

- This function retrieves the public IP address of the running EC2 instance.
- The public IP is a necessary parameter for the subsequent functions.

### Function 3: Copy Files and Perform Linux Tasks

- This function copies the `docker-compose.yaml` and `docker.py` files to the EC2 instance.
- It also performs necessary Linux tasks such as package updates and installation of Docker.

### Function 4: Execute Docker Commands

- This function remotely executes the `docker.py` file on the EC2 instance.
- It automatically installs Docker Compose and builds the PostgreSQL container using the `docker-compose.yaml` file.
- Once the database container is running, the function returns the authentication details.

**Note:** Please ensure that you handle authentication information securely and avoid exposing sensitive data in the application. This application serves as a simple test and should be enhanced with appropriate security measures before production use.

Feel free to enhance this documentation further, adding any additional details, security considerations, or other improvements as required.