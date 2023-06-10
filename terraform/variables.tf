variable "region" {
  description = "Set a regian"
  default = "us-east-1"
}

variable "instance_type" {
  description = "Define instance type"
  default = "t2.micro"
}

variable "name" {
  description = "Instance name"
  default = "server01"
}

variable "key_name" {
  description = "Key pair name for connection ssh"
  default = "ec2_access"
}