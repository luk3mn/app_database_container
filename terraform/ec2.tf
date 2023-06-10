data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "server" {
  ami = data.aws_ami.ubuntu.id 
  instance_type = var.instance_type # t2.micro 
  key_name = var.key_name # ec2_access

  tags = {
    Name = var.name # server01
  }

  vpc_security_group_ids = [aws_security_group.allow_server01.id]
}