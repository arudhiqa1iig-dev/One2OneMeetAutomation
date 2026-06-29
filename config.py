import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    base_url: str = "https://one2onemeet.com/"
    login_url: str = "https://app.one2onemeet.com/auth/login"
    timeout: int = 10
    headless: bool = os.getenv("CI") is not None


settings = Settings()
