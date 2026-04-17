// Update an existing subject owned by the authenticated user.
query "subjects" verb=PATCH {
  api_group = "Subjects"
  auth = "user"

  input {
    int id
    text name
    text description
    text teacher
    int hours
    bool active
  }

  stack {
    db.get subject {
      field_name = "id"
      field_value = $input.id
      output = ["id", "account_id"]
    } as $subject

    precondition ($subject != null && $subject.account_id == $auth.account_id) {
      error_type = "accessdenied"
      error = "Not authorized to update this subject."
    }

    db.update subject {
      field_name = "id"
      field_value = $input.id
      values = {
        name        : $input.name || null
        description : $input.description || null
        teacher     : $input.teacher || null
        hours       : $input.hours || null
        active      : $input.active
      }
      output = ["id", "name", "description", "teacher", "hours", "active", "created_at"]
    } as $updated
  }

  response = $updated
  tags = ["xano:quick-start"]
}
