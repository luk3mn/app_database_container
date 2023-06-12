'''Application for executing ec2 and container'''
import subprocess
import re
import time
import paramiko

def execute_instance() -> None:
    ''' executing the terraform files to build the ec2 instance
    '''
    # terraform command
    terraform_commands = ['init', 'plan', 'apply']

    for command in terraform_commands:
        terraform = ['terraform','-chdir=terraform',command]
        if command == 'apply':
            terraform.append('-auto-approve')
        subprocess.run(terraform, check=True)

def get_ip() -> str:
    ''' capturing the public ip of the ec2 instance
    '''

    # get ec2 instance status
    status = "terraform -chdir=terraform output status"
    output_status = subprocess.run(status, check=True, shell=True, capture_output=True, text=True).stdout

    # get public ip
    pub_ip = "terraform -chdir=terraform output public_ip"
    output_ip = subprocess.run(pub_ip, check=True, shell=True, capture_output=True, text=True).stdout

    # Extract the public IP address from the output
    ip_address = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", output_ip).group(1)

    print(f'{output_ip} -> {output_status}')
    return ip_address, output_status

def copy_to_ec2(pub_ip: str) -> None:
    ''' Copy docker-compose to AWS instance'''

    key_file = "~/aws/ec2_access.pem"
    remote_path = "/home/ubuntu/"
    local_path = "docker-compose.yaml docker.py"

    cmd = f"scp -o StrictHostKeyChecking=no -i {key_file} {local_path} ubuntu@{pub_ip}:{remote_path}"
    subprocess.call(cmd, shell=True)
    print("Public ip: ", pub_ip, type(pub_ip))

def execute_py_ec2(host: str, username: str, key_name: str, file_name: str) -> None:
    ''' the function that executes the Python file with docker and Linux tasks
    '''
    # Create an SSH client
    ssh = paramiko.SSHClient()

    # Automatically add the host to known_hosts
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the SSH host using key pair authentication
    ssh.connect(host, username=username, key_filename=key_name)

    # Execute the Python file remotely
    stdin, stdout, stderr = ssh.exec_command(f'python3 /home/ubuntu/{file_name}')

    # Wait for the command to finish
    stdout.channel.recv_exit_status()

    # Print the output
    output = stdout.read().decode().strip()
    print(output)

    # Close the SSH connection
    ssh.close()

if __name__ == "__main__":
    # Create the ec2 instance
    execute_instance() 

    # recovering the public ip from ec2 instance
    public_ip, ec2_status = get_ip() 
    print("Status: ", ec2_status)
    time.sleep(10) # wait for 10 seconds

    # make a copy from python and docker files
    copy_to_ec2(pub_ip=public_ip)

    # execute files
    execute_py_ec2(host=public_ip, username='ubuntu', file_name='docker.py', key_name='ec2_access.pem')

    print("+=========== PostgreSQL Authentication ============+")
    print("Host: ", public_ip)
    print("Usename: postgres")
    print("Database: mydb")
    print("Password: Teste123")
    print("+ ================================================ +")
