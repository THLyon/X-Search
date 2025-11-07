from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings: 
    bearer_token=str

def get_settings() -> Settings: 
    token = os.getenv("TWITTER_BEARER_TOKEN") or os.getenv("TWITTER_BEARER_TOKEN".upper())
    if not token: 
        raise RuntimeError(
            "Missing TWITTER_BEARER_TOKEN in environment."
            "Create a developer token at development.twitter.com and set it in .env."
        )
    return Settings(bearer_token=token)