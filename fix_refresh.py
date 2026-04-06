with open("backend/services/auth_resolver.py", "r") as f:
    content = f.read()

content = content.replace(
    'log.warning(f"[Auth] 账号 {acc.email} 缺少密码，无法自愈。")',
    'log.warning(f"[Refresh] 账号 {acc.email} 无密码，无法刷新")'
)
content = content.replace(
    'log.info(f"[Auth] 正在启动独立浏览器为 {acc.email} 自动刷新 Token...")',
    'log.info(f"[Refresh] 正在为 {acc.email} 刷新 token...")'
)
content = content.replace(
    'log.info(f"[Auth] 自愈成功，{acc.email} 获得全新 Token。")',
    'old_prefix = acc.token[:20] if acc.token else "空"\n                    log.info(f"[Refresh] {acc.email} token 已更新 ({old_prefix}... → {new_token[:20]}...)")'
)
content = content.replace(
    'log.info(f"[Auth] {acc.email} 重新校验成功。")',
    'log.info(f"[Refresh] {acc.email} token 未变化，重新标记有效")'
)
content = content.replace(
    'log.error(f"[Auth] {acc.email} 登录失败或遭遇滑块验证拦截。")',
    'log.warning(f"[Refresh] {acc.email} 登录后未获取到token，URL={page.url}")'
)
content = content.replace(
    'log.error(f"[Register] 浏览器引擎崩溃或被拦截: {str(e)}")',
    'log.error(f"[Refresh] {acc.email} 刷新异常: {e}")'
)
with open("backend/services/auth_resolver.py", "w") as f:
    f.write(content)
