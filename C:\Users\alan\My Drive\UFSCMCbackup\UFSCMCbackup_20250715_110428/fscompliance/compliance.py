"""Compliance analysis core functionality."""

import asyncio
import logging
from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from .config import settings
from .llm import LLMGateway
from .rag import KnowledgeStore


class ComplianceGap(BaseModel):
    """Represents a compliance gap."""
    description: str
    regulation_reference: str
    severity: str
    recommendation: str


class ComplianceAnalysisResult(BaseModel):
    """Result of compliance analysis."""
    compliance_status: str
    confidence_score: float
    gaps_identified: List[ComplianceGap]
    recommendations: List[str]
    analysis_summary: str


class CustomerScenarioResult(BaseModel):
    """Result of customer scenario assessment."""
    compliance_status: str
    confidence_score: float
    requirements_met: List[str]
    requirements_failed: List[str]
    recommendations: List[str]


class RegulationSearchResult(BaseModel):
    """Result of regulation search."""
    results: List[Dict[str, Any]]
    total_results: int
    query: str


class ComplianceAnalyzer:
    """Core compliance analysis engine."""
    
    def __init__(self):
        self.llm_gateway = LLMGateway()
        self.knowledge_store = KnowledgeStore()
        self.logger = logging.getLogger(__name__)
    
    async def analyze_policy(self, policy_text: str, analysis_type: str) -> Dict[str, Any]:
        """Analyze policy text for compliance issues."""
        self.logger.info(f"Analyzing policy with type: {analysis_type}")
        
        try:
            # Retrieve relevant regulations
            relevant_regs = await self.knowledge_store.search_regulations(
                query=policy_text[:500],  # Use first 500 chars as context
                limit=10
            )
            
            # Prepare analysis prompt
            prompt = self._build_analysis_prompt(policy_text, analysis_type, relevant_regs)
            
            # Get LLM analysis
            analysis_result = await self.llm_gateway.analyze_compliance(prompt)
            
            # Parse and structure result
            result = self._parse_analysis_result(analysis_result, analysis_type)
            
            return result.model_dump()
            
        except Exception as e:
            self.logger.error(f"Policy analysis failed: {e}")
            return {
                "compliance_status": "error",
                "confidence_score": 0.0,
                "gaps_identified": [],
                "recommendations": [f"Analysis failed: {str(e)}"],
                "analysis_summary": f"Error occurred during analysis: {str(e)}"
            }
    
    async def assess_customer_scenario(self, scenario: str, requirements: List[str]) -> Dict[str, Any]:
        """Assess customer scenario for compliance."""
        self.logger.info(f"Assessing customer scenario for {len(requirements)} requirements")
        
        try:
            # Search for relevant regulations
            relevant_regs = await self.knowledge_store.search_regulations(
                query=f"{scenario} {' '.join(requirements)}",
                limit=15
            )
            
            # Build assessment prompt
            prompt = self._build_scenario_prompt(scenario, requirements, relevant_regs)
            
            # Get LLM assessment
            assessment_result = await self.llm_gateway.assess_scenario(prompt)
            
            # Parse result
            result = self._parse_scenario_result(assessment_result, requirements)
            
            return result.model_dump()
            
        except Exception as e:
            self.logger.error(f"Scenario assessment failed: {e}")
            return {
                "compliance_status": "error",
                "confidence_score": 0.0,
                "requirements_met": [],
                "requirements_failed": requirements,
                "recommendations": [f"Assessment failed: {str(e)}"]
            }
    
    async def search_regulations(self, query: str, context: str = "") -> Dict[str, Any]:
        """Search FCA Handbook for regulations."""
        self.logger.info(f"Searching regulations for: {query}")
        
        try:
            # Combine query and context
            search_query = f"{query} {context}".strip()
            
            # Search knowledge store
            results = await self.knowledge_store.search_regulations(
                query=search_query,
                limit=20
            )
            
            return RegulationSearchResult(
                results=results,
                total_results=len(results),
                query=search_query
            ).model_dump()
            
        except Exception as e:
            self.logger.error(f"Regulation search failed: {e}")
            return {
                "results": [],
                "total_results": 0,
                "query": query,
                "error": str(e)
            }
    
    def _build_analysis_prompt(self, policy_text: str, analysis_type: str, relevant_regs: List[Dict]) -> str:
        """Build prompt for policy analysis."""
        reg_context = "\n".join([
            f"- {reg.get('title', 'Unknown')}: {reg.get('content', '')[:200]}..."
            for reg in relevant_regs[:5]
        ])
        
        return f"""
        Analyze the following policy text for compliance with FCA regulations.
        
        Analysis Type: {analysis_type}
        
        Policy Text:
        {policy_text}
        
        Relevant FCA Regulations:
        {reg_context}
        
        Please provide:
        1. Compliance status (compliant/non-compliant/partial)
        2. Confidence score (0-1)
        3. Specific gaps identified
        4. Recommendations for improvement
        5. Analysis summary
        
        Format your response as structured JSON.
        """
    
    def _build_scenario_prompt(self, scenario: str, requirements: List[str], relevant_regs: List[Dict]) -> str:
        """Build prompt for scenario assessment."""
        reg_context = "\n".join([
            f"- {reg.get('title', 'Unknown')}: {reg.get('content', '')[:200]}..."
            for reg in relevant_regs[:5]
        ])
        
        return f"""
        Assess the following customer scenario for compliance with FCA requirements.
        
        Customer Scenario:
        {scenario}
        
        Requirements to Check:
        {', '.join(requirements)}
        
        Relevant FCA Regulations:
        {reg_context}
        
        Please assess:
        1. Overall compliance status
        2. Confidence score (0-1)
        3. Which requirements are met
        4. Which requirements are failed
        5. Specific recommendations
        
        Format your response as structured JSON.
        """
    
    def _parse_analysis_result(self, llm_result: str, analysis_type: str) -> ComplianceAnalysisResult:
        """Parse LLM analysis result."""
        # This is a placeholder - in real implementation, you'd parse the LLM response
        # For now, return a mock result
        return ComplianceAnalysisResult(
            compliance_status="partial",
            confidence_score=0.75,
            gaps_identified=[
                ComplianceGap(
                    description="Risk disclosure requirements may not be fully met",
                    regulation_reference="FCA COBS 4.5",
                    severity="medium",
                    recommendation="Enhance risk disclosure language"
                )
            ],
            recommendations=[
                "Review risk disclosure procedures",
                "Ensure customer understanding verification"
            ],
            analysis_summary=f"Analysis complete for {analysis_type}. Partial compliance identified."
        )
    
    def _parse_scenario_result(self, llm_result: str, requirements: List[str]) -> CustomerScenarioResult:
        """Parse LLM scenario result."""
        # This is a placeholder - in real implementation, you'd parse the LLM response
        return CustomerScenarioResult(
            compliance_status="partial",
            confidence_score=0.8,
            requirements_met=requirements[:len(requirements)//2],
            requirements_failed=requirements[len(requirements)//2:],
            recommendations=[
                "Implement additional risk warnings",
                "Enhance suitability assessment procedures"
            ]
        )