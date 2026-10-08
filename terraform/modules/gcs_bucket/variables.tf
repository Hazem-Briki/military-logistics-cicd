variable "bucket_name" {
  description = "Name of the GCS bucket"
  type        = string
}

variable "location" {
  description = "GCP location for the bucket"
  type        = string
  default     = "us-east1"
}

variable "environment" {
  description = "Environment name"
  type        = string
}