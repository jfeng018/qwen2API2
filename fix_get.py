with open("backend/api/admin.py", "r") as f:
    content = f.read()

content = content.replace(
    "@router.get(\"/accounts\", dependencies=[Depends(verify_admin)])\n\n@router.post(\"/accounts\", dependencies=[Depends(verify_admin)])",
    "@router.post(\"/accounts\", dependencies=[Depends(verify_admin)])"
)

with open("backend/api/admin.py", "w") as f:
    f.write(content)
