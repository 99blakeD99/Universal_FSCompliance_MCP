"""Logging configuration for FSCompliance."""

import logging
import sys
from loguru import logger

from .config import settings


def setup_logging():
    """Setup logging configuration."""
    
    # Remove default loguru handler
    logger.remove()
    
    # Add loguru handler with custom format
    logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level=settings.log_level,
        backtrace=True,
        diagnose=True
    )
    
    # Setup standard logging to work with loguru
    class InterceptHandler(logging.Handler):
        def emit(self, record):
            # Get corresponding Loguru level if it exists
            try:
                level = logger.level(record.levelname).name
            except ValueError:
                level = record.levelno
            
            # Find caller from where originated the logged message
            frame, depth = sys._getframe(6), 6
            while frame and frame.f_code.co_filename == logging.__file__:
                frame = frame.f_back
                depth += 1
            
            logger.opt(depth=depth, exception=record.exc_info).log(
                level, record.getMessage()
            )
    
    # Replace standard logging handlers
    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)
    
    # Set specific loggers
    for logger_name in ["uvicorn", "fastapi", "sqlalchemy", "httpx"]:
        logging.getLogger(logger_name).handlers = [InterceptHandler()]
    
    logger.info("Logging configuration initialized")