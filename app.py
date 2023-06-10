'''Application for executing ec2 and container'''
import subprocess

def execute_instance() -> None:
    ''' executing the ec2 instance
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
    output_command = "terraform -chdir=terraform output public_ip"
    return subprocess.run(output_command, check=True, shell=True, capture_output=True, text=True).stdout

if __name__ == "__main__":
    execute_instance()

    public_ip = get_ip()
    print(f"This is my public ip: {public_ip}")
