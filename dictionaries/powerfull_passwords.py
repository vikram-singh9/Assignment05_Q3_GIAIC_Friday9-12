import hashlib

stored_logins = {
    "user@example.com": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check):
    return email in stored_logins and stored_logins[email] == hash_password(password_to_check)

print(login("user@example.com", "hello"))
print(login("user@example.com", "wrong"))
print(login("unknown@example.com", "hello"))