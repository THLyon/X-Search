from typing import Dict, Any, Iterable, Optional
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential
import os

API_BASE = os.getenv("X_API_BASE_URL")

class XClient: 
    def __init__(self, bearer_token: str, timeout: float = 20.0): 
        self._headers = {
            "Authorization": f"Bearer {bearer_token}", 
            "User-Agent": "xsearch-cli/0.1", 
        }
        self._client = httpx.Client(headers=self._headers, timeout=timeout, http2=True)

    def close(self):
        self._client.close()

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=8))
    def get_user_by_username(self, username: str) -> Dict[str, Any]:
        r = self._client.get(
            f"{API_BASE}/users/by/username/{username}", 
            params={"user.fields": "is,name,username"}, 
        )
        r.raise_for_status()
        return r.json()
    
    
