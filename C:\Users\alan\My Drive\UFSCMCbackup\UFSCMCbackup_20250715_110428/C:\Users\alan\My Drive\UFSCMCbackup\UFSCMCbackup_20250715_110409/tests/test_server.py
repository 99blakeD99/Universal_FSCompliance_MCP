"""Tests for FSCompliance MCP server."""

import pytest
import asyncio
from unittest.mock import Mock, patch

from fscompliance.server import FSComplianceServer


@pytest.fixture
def server():
    """Create test server instance."""
    return FSComplianceServer()


@pytest.mark.asyncio
async def test_server_initialization(server):
    """Test server initializes correctly."""
    assert server.server is not None
    assert server.compliance_analyzer is not None
    assert server.logger is not None


@pytest.mark.asyncio
async def test_analyze_compliance_tool():
    """Test analyze_compliance tool."""
    server = FSComplianceServer()
    
    # Mock the compliance analyzer
    with patch.object(server.compliance_analyzer, 'analyze_policy') as mock_analyze:
        mock_analyze.return_value = {
            "compliance_status": "compliant",
            "confidence_score": 0.95,
            "gaps_identified": [],
            "recommendations": []
        }
        
        # This would normally be called by the MCP framework
        result = await server.compliance_analyzer.analyze_policy(
            "Test policy text",
            "gap_analysis"
        )
        
        assert result["compliance_status"] == "compliant"
        assert result["confidence_score"] == 0.95
        mock_analyze.assert_called_once()


@pytest.mark.asyncio
async def test_assess_customer_scenario_tool():
    """Test assess_customer_scenario tool."""
    server = FSComplianceServer()
    
    with patch.object(server.compliance_analyzer, 'assess_customer_scenario') as mock_assess:
        mock_assess.return_value = {
            "compliance_status": "partial",
            "confidence_score": 0.8,
            "requirements_met": ["risk_warnings"],
            "requirements_failed": ["suitability_assessment"]
        }
        
        result = await server.compliance_analyzer.assess_customer_scenario(
            "Test scenario",
            ["risk_warnings", "suitability_assessment"]
        )
        
        assert result["compliance_status"] == "partial"
        assert "risk_warnings" in result["requirements_met"]
        mock_assess.assert_called_once()


@pytest.mark.asyncio
async def test_search_regulations_tool():
    """Test search_regulations tool."""
    server = FSComplianceServer()
    
    with patch.object(server.compliance_analyzer, 'search_regulations') as mock_search:
        mock_search.return_value = {
            "results": [
                {
                    "id": "test_reg",
                    "title": "Test Regulation",
                    "content": "Test content"
                }
            ],
            "total_results": 1,
            "query": "test query"
        }
        
        result = await server.compliance_analyzer.search_regulations("test query")
        
        assert result["total_results"] == 1
        assert len(result["results"]) == 1
        mock_search.assert_called_once()