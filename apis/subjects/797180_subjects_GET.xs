// Retrieve the authenticated user's subjects.
query subjects verb=GET {
  api_group = "Subjects"
  auth = "user"

  input {
  }

  stack {
    db.query subject {
      where = $db.subject.account_id == $auth.account_id
      return = {type: "list"}
      output = ["id", "name", "description", "teacher", "hours", "active", "created_at"]
    } as $subjects
  }

  response = $subjects
  tags = ["xano:quick-start"]
}