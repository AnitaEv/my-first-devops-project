resource "local_file" "devops_report" {
  filename = "inventory.txt"
  content  = "My DevOps Project is growing! App version: 1.0"
}
