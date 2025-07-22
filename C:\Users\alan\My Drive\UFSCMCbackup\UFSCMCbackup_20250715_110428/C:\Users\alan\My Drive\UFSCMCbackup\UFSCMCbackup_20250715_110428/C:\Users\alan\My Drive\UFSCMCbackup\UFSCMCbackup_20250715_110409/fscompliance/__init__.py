"""
FSCompliance - Universal Financial Services Compliance Platform

An open-source MCP (Model Context Protocol) service for financial regulatory compliance.
Provides AI-powered compliance analysis tools for financial services professionals.
"""

__version__ = "0.1.0"
__author__ = "FSCompliance Project"
__email__ = "dev@fscompliance.org"

from .client import FSComplianceClient
from .config import Settings

__all__ = ["FSComplianceClient", "Settings"]