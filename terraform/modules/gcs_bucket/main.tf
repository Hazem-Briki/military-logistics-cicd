resource "google_storage_bucket" "raw" {
  name     = var.bucket_name
  location = var.location

  uniform_bucket_level_access = true

  labels = {
    environment = var.environment
    purpose     = "raw-data"
    project     = "military-logistics"
  }
}