with open("backend/api/admin.py", "r") as f:
    content = f.read()

content = content.replace(
    "is_valid = await client.verify_account(acc)",
    "is_valid = await client.verify_token(acc.token)"
)

content = content.replace(
    "is_valid = await client.verify_token(acc.token)\n    if not is_valid:\n        return {\"ok\": False, \"error\": \"Invalid token (验证失败，请确认Token有效)\"}",
    "is_valid = await client.verify_token(token)\n    if not is_valid:\n        return {\"ok\": False, \"error\": \"Invalid token (验证失败，请确认Token有效)\"}"
)

with open("backend/api/admin.py", "w") as f:
    f.write(content)
