output "vpc_id" {
  value = aws_vpc.kerol.id
}

output "vpc_cidr" {
  value = aws_vpc.kerol.cidr_block
}

output "public_subnet_ids" {
  value = aws_subnet.public_subnets[*].id
}

output "private_subnet_ids" {
  value = aws_subnet.private_subnets[*].id
}


output "server_public_ips" {
  value = [for instance in aws_instance.nginx : instance.public_ip]
}


