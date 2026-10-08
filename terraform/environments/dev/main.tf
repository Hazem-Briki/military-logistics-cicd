terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 7.0"
    }
  }

  required_version = ">= 1.5.0"
}

provider "google" {
  project = "it-hazem-briki-playground0"
  region  = "us-east1"
}

module "raw_bucket" {
  source = "../../modules/gcs_bucket"

  bucket_name = "military-logistics-dev-raw"
  location    = "us-east1"
  environment = "dev"
}