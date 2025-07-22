"""Tests for compliance analysis functionality."""

import pytest
from unittest.mock import Mock, patch

from fscompliance.compliance import ComplianceAnalyzer, ComplianceGap


@pytest.fixture
def analyzer():
    """Create test compliance analyzer."""
    return ComplianceAnalyzer()


@pytest.mark.asyncio
async def test_analyze_policy_gap_analysis(analyzer):
    """Test policy analysis for gap analysis."""
    policy_text = "Our firm provides investment advice to retail customers."
    
    result = await analyzer.analyze_policy(policy_text, "gap_analysis")
    
    assert "compliance_status" in result
    assert "confidence_score" in result
    assert "gaps_identified" in result
    assert "recommendations" in result
    assert isinstance(result["confidence_score"], float)
    assert 0 <= result["confidence_score"] <= 1


@pytest.mark.asyncio
async def test_analyze_policy_requirement_check(analyzer):
    """Test policy analysis for requirement check."""
    policy_text = "We conduct suitability assessments for all customers."
    
    result = await analyzer.analyze_policy(policy_text, "requirement_check")
    
    assert result["compliance_status"] in ["compliant", "non-compliant", "partial"]
    assert isinstance(result["gaps_identified"], list)
    assert isinstance(result["recommendations"], list)


@pytest.mark.asyncio
async def test_assess_customer_scenario(analyzer):
    """Test customer scenario assessment."""
    scenario = "60+ year old customer investing in high-risk products"
    requirements = ["risk_warnings", "suitability_assessment"]
    
    result = await analyzer.assess_customer_scenario(scenario, requirements)
    
    assert "compliance_status" in result
    assert "confidence_score" in result
    assert "requirements_met" in result
    assert "requirements_failed" in result
    assert isinstance(result["requirements_met"], list)
    assert isinstance(result["requirements_failed"], list)


@pytest.mark.asyncio
async def test_search_regulations(analyzer):
    """Test regulation search functionality."""
    query = "risk disclosure requirements"
    
    result = await analyzer.search_regulations(query)
    
    assert "results" in result
    assert "total_results" in result
    assert "query" in result
    assert isinstance(result["results"], list)
    assert isinstance(result["total_results"], int)


@pytest.mark.asyncio
async def test_analyze_policy_error_handling(analyzer):
    """Test error handling in policy analysis."""
    # Mock the LLM gateway to raise an exception
    with patch.object(analyzer.llm_gateway, 'analyze_compliance') as mock_llm:
        mock_llm.side_effect = Exception("LLM service unavailable")
        
        result = await analyzer.analyze_policy("test policy", "gap_analysis")
        
        assert result["compliance_status"] == "error"
        assert result["confidence_score"] == 0.0
        assert "Analysis failed" in result["recommendations"][0]


def test_compliance_gap_model():
    """Test ComplianceGap model validation."""
    gap = ComplianceGap(
        description="Missing risk disclosure",
        regulation_reference="FCA COBS 4.5",
        severity="high",
        recommendation="Add comprehensive risk warnings"
    )
    
    assert gap.description == "Missing risk disclosure"
    assert gap.regulation_reference == "FCA COBS 4.5"
    assert gap.severity == "high"
    assert gap.recommendation == "Add comprehensive risk warnings"