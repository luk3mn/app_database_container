output "public_ip" {
  value = aws_instance.server.public_ip
}

output "status" {
  value = aws_instance.server.instance_state
}