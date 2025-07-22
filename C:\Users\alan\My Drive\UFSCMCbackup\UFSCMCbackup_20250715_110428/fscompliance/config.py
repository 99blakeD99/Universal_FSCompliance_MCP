"""Configuration management for FSCompliance MCP server."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """FSCompliance application settings."""
    
    model_config = SettingsConfigDict(
        env_prefix="FSCOMPLIANCE_",
        env_file=".env",
        case_sensitive=False,
    )
    
    # LLM Configuration
    default_llm: str = Field(default="claude-3.5-sonnet", description="Default LLM model")
    claude_api_key: str = Field(default="", description="Anthropic API key")
    enable_multi_model: bool = Field(default=True, description="Enable multi-model support")
    
    # Database Configuration
    db_url: str = Field(default="sqlite:///fscompliance.db", description="Database URL")
    vector_store: str = Field(default="pgvector", description="Vector store type")
    
    # Privacy Settings
    memory_enabled: bool = Field(default=True, description="Enable long-term memory")
    anonymize_data: bool = Field(default=True, description="Anonymize sensitive data")
    audit_logging: bool = Field(default=True, description="Enable audit logging")
    
    # MCP Server Settings
    mcp_port: int = Field(default=8000, description="MCP server port")
    mcp_host: str = Field(default="localhost", description="MCP server host")
    
    # Development Settings
    debug: bool = Field(default=False, description="Debug mode")
    log_level: str = Field(default="INFO", description="Log level")


# Global settings instance
settings = Settings()