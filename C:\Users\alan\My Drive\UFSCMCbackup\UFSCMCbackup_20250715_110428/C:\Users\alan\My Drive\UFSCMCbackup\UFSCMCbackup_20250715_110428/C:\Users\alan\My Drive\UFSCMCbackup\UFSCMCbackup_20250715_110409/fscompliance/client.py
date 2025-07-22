"""Client interface for FSCompliance."""

import asyncio
import json
import logging
from typing import Any, Dict, List, Optional

from .compliance import ComplianceAnalyzer
from .config import settings


class FSComplianceClient:
    """Client interface for FSCompliance MCP service."""
    
    def __init__(self):
        self.compliance_analyzer = ComplianceAnalyzer()
        self.logger = logging.getLogger(__name__)
    
    async def analyze_policy(self, policy_text: str, query_type: str = "gap_analysis") -> Dict[str, Any]:
        """Analyze policy for compliance gaps."""
        return await self.compliance_analyzer.analyze_policy(policy_text, query_type)
    
    async def assess_customer_scenario(self, scenario: str, requirements: List[str]) -> Dict[str, Any]:
        """Assess customer scenario for compliance."""
        return await self.compliance_analyzer.assess_customer_scenario(scenario, requirements)
    
    async def search_regulations(self, query: str, context: str = "") -> Dict[str, Any]:
        """Search FCA Handbook for regulations."""
        return await self.compliance_analyzer.search_regulations(query, context)
    
    # Synchronous wrappers for backward compatibility
    def analyze_policy_sync(self, policy_text: str, query_type: str = "gap_analysis") -> Dict[str, Any]:
        """Synchronous version of analyze_policy."""
        return asyncio.run(self.analyze_policy(policy_text, query_type))
    
    def assess_customer_scenario_sync(self, scenario: str, requirements: List[str]) -> Dict[str, Any]:
        """Synchronous version of assess_customer_scenario."""
        return asyncio.run(self.assess_customer_scenario(scenario, requirements))
    
    def search_regulations_sync(self, query: str, context: str = "") -> Dict[str, Any]:
        """Synchronous version of search_regulations."""
        return asyncio.run(self.search_regulations(query, context))