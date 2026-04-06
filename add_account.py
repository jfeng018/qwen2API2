with open("backend/api/admin.py", "r") as f:
    content = f.read()

new_route = """
@router.post("/accounts", dependencies=[Depends(verify_admin)])
async def add_account(request: Request):
    import time
    from backend.core.account_pool import Account, AccountPool
    from backend.services.qwen_client import QwenClient
    
    pool: AccountPool = request.app.state.account_pool
    client: QwenClient = request.app.state.qwen_client
    
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(400, detail="Invalid JSON body")
        
    token = data.get("token", "")
    if not token:
        raise HTTPException(400, detail="token is required")
        
    acc = Account(
        email=data.get("email", f"manual_{int(time.time())}@qwen"),
        password=data.get("password", ""),
        token=token,
        cookies=data.get("cookies", ""),
        username=data.get("username", "")
    )
    
    is_valid = await client.verify_token(token)
    if not is_valid:
        return {"ok": False, "error": "Invalid token (验证失败，请确认Token有效)"}
        
    await pool.add(acc)
    return {"ok": True, "email": acc.email}

"""

if "@router.post(\"/accounts\"" not in content:
    content = content.replace(
        "async def list_accounts(request: Request):",
        new_route + "\n@router.get(\"/accounts\", dependencies=[Depends(verify_admin)])\nasync def list_accounts(request: Request):"
    )

    with open("backend/api/admin.py", "w") as f:
        f.write(content)
