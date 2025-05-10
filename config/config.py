from dataclasses import dataclass
import os
from dotenv import load_dotenv

@dataclass
class Config:
    """Конфигурация бота"""
    token: str = "7949770451:AAGcWxCGApTKBX939JuMRV8bDyjF70gqWoI"
    admin_ids: list[int] = None
    log_level: str = "INFO"
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    log_file: str = "bot.log"

    def __post_init__(self):
        if self.admin_ids is None:
            self.admin_ids = []

def load_config() -> Config:
    """Загрузка конфигурации"""
    return Config() 