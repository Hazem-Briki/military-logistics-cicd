output "raw_bucket_name" {
  description = "Name of the DEV RAW GCS bucket"
  value       = module.raw_bucket.bucket_name
}