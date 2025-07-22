"""MCP Server implementation for FSCompliance."""

import asyncio
import json
import logging
from typing import Any, Dict, List, Optional

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    CallToolRequest,
    CallToolResult,
    GetPromptRequest,
    GetPromptResult,
    ListPromptsRequest,
    ListPromptsResult,
    ListResourcesRequest,
    ListResourcesResult,
    ListToolsRequest,
    ListToolsResult,
    Prompt,
    Resource,
    Tool,
)
from pydantic import BaseModel

from .config import settings
from .compliance import ComplianceAnalyzer
from .logging_config import setup_logging


class FSComplianceServer:
    """FSCompliance MCP Server."""
    
    def __init__(self):
        self.server = Server("fscompliance")
        self.compliance_analyzer = ComplianceAnalyzer()
        self.logger = logging.getLogger(__name__)
        
        # Register MCP handlers
        self._register_handlers()
    
    def _register_handlers(self):
        """Register MCP protocol handlers."""
        
        @self.server.list_tools()
        async def list_tools() -> ListToolsResult:
            """List available compliance tools."""
            return ListToolsResult(
                tools=[
                    Tool(
                        name="analyze_compliance",
                        description="Analyze policy text for compliance gaps",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "policy_text": {
                                    "type": "string",
                                    "description": "Policy text to analyze"
                                },
                                "analysis_type": {
                                    "type": "string",
                                    "enum": ["gap_analysis", "requirement_check", "risk_assessment"],
                                    "description": "Type of analysis to perform"
                                }
                            },
                            "required": ["policy_text", "analysis_type"]
                        }
                    ),
                    Tool(
                        name="assess_customer_scenario",
                        description="Assess customer scenario for compliance",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "scenario": {
                                    "type": "string",
                                    "description": "Customer scenario to assess"
                                },
                                "requirements": {
                                    "type": "array",
                                    "items": {"type": "string"},
                                    "description": "Specific requirements to check"
                                }
                            },
                            "required": ["scenario", "requirements"]
                        }
                    ),
                    Tool(
                        name="search_regulations",
                        description="Search FCA Handbook for specific regulations",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "query": {
                                    "type": "string",
                                    "description": "Search query"
                                },
                                "context": {
                                    "type": "string",
                                    "description": "Additional context for search"
                                }
                            },
                            "required": ["query"]
                        }
                    )
                ]
            )
        
        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> CallToolResult:
            """Handle tool calls."""
            try:
                if name == "analyze_compliance":
                    result = await self.compliance_analyzer.analyze_policy(
                        arguments["policy_text"],
                        arguments["analysis_type"]
                    )
                elif name == "assess_customer_scenario":
                    result = await self.compliance_analyzer.assess_customer_scenario(
                        arguments["scenario"],
                        arguments["requirements"]
                    )
                elif name == "search_regulations":
                    result = await self.compliance_analyzer.search_regulations(
                        arguments["query"],
                        arguments.get("context", "")
                    )
                else:
                    raise ValueError(f"Unknown tool: {name}")
                
                return CallToolResult(
                    content=[
                        {
                            "type": "text",
                            "text": json.dumps(result, indent=2)
                        }
                    ]
                )
            except Exception as e:
                self.logger.error(f"Error calling tool {name}: {e}")
                return CallToolResult(
                    content=[
                        {
                            "type": "text",
                            "text": f"Error: {str(e)}"
                        }
                    ],
                    isError=True
                )
        
        @self.server.list_resources()
        async def list_resources() -> ListResourcesResult:
            """List available resources."""
            return ListResourcesResult(
                resources=[
                    Resource(
                        uri="fca://handbook",
                        name="FCA Handbook",
                        description="UK Financial Conduct Authority Handbook",
                        mimeType="application/json"
                    )
                ]
            )
        
        @self.server.list_prompts()
        async def list_prompts() -> ListPromptsResult:
            """List available prompts."""
            return ListPromptsResult(
                prompts=[
                    Prompt(
                        name="compliance_analysis",
                        description="Analyze policy for compliance gaps",
                        arguments=[
                            {
                                "name": "policy_text",
                                "description": "Policy text to analyze",
                                "required": True
                            }
                        ]
                    )
                ]
            )
    
    async def run(self):
        """Run the MCP server."""
        self.logger.info("Starting FSCompliance MCP Server...")
        async with stdio_server() as streams:
            await self.server.run(
                streams[0], streams[1], self.server.create_initialization_options()
            )


async def main():
    """Main entry point."""
    setup_logging()
    server = FSComplianceServer()
    await server.run()


if __name__ == "__main__":
    asyncio.run(main())