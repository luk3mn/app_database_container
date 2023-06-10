terraform {
  required_providers {
    aws = {
      version = "5.2.0"
    }
  }
}

provider "aws" {
  # Configuration options
  region = var.region
}