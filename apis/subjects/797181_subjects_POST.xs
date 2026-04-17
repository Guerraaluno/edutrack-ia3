// Create a new subject for the authenticated user's account.
query "subjects" verb=POST {
  api_group = "Subjects"
  auth = "user"

  input {
    text name filters=trim
    text description
    text teacher
    int hours
    bool active
  }

  stack {
    db.insert subject {
      values = {
        name        : $input.name
        description : $input.description || null
        teacher     : $input.teacher || null
        hours       : $input.hours || null
        active      : $input.active
        account_id  : $auth.account_id
        user_id     : $auth.id
      }
      output = ["id", "name", "description", "teacher", "hours", "active", "created_at"]
    } as $subject
  }

  response = $subject
  tags = ["xano:quick-start"]
}
