// Delete a subject owned by the authenticated user.
query "subjects" verb=DELETE {
  api_group = "Subjects"
  auth = "user"

  input {
    int id
  }

  stack {
    db.get subject {
      field_name = "id"
      field_value = $input.id
      output = ["id", "account_id"]
    } as $subject

    db.delete subject {
      field_name = "id"
      field_value = $input.id
    }
  }

  response = {deleted_id: $input.id}
  tags = ["xano:quick-start"]
}
