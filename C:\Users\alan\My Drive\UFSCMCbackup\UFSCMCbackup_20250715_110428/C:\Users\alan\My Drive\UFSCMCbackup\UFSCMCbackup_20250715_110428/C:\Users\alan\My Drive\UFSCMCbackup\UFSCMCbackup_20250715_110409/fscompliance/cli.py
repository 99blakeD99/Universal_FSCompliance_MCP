"""Command line interface for FSCompliance."""

import asyncio
import typer
from rich.console import Console
from rich.table import Table

from .client import FSComplianceClient
from .config import settings
from .logging_config import setup_logging
from .server import main as server_main

app = typer.Typer(help="FSCompliance - Universal Financial Services Compliance Platform")
console = Console()


@app.command()
def server():
    """Start the MCP server."""
    console.print("🚀 Starting FSCompliance MCP Server...", style="green")
    asyncio.run(server_main())


@app.command()
def analyze(
    policy_file: str = typer.Option(help="Path to policy file"),
    analysis_type: str = typer.Option(default="gap_analysis", help="Type of analysis")
):
    """Analyze a policy file for compliance."""
    console.print(f"📊 Analyzing policy: {policy_file}", style="blue")
    
    try:
        with open(policy_file, 'r') as f:
            policy_text = f.read()
        
        client = FSComplianceClient()
        result = client.analyze_policy_sync(policy_text, analysis_type)
        
        # Display results
        table = Table(title="Compliance Analysis Results")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        
        table.add_row("Status", result.get("compliance_status", "unknown"))
        table.add_row("Confidence", f"{result.get('confidence_score', 0):.2f}")
        table.add_row("Gaps Found", str(len(result.get("gaps_identified", []))))
        
        console.print(table)
        
        if result.get("gaps_identified"):
            console.print("\n📋 Identified Gaps:", style="yellow")
            for gap in result["gaps_identified"]:
                console.print(f"• {gap.get('description', 'Unknown')}")
        
    except Exception as e:
        console.print(f"❌ Error: {e}", style="red")


@app.command()
def search(
    query: str = typer.Argument(help="Search query"),
    context: str = typer.Option(default="", help="Additional context")
):
    """Search FCA Handbook for regulations."""
    console.print(f"🔍 Searching regulations: {query}", style="blue")
    
    try:
        client = FSComplianceClient()
        result = client.search_regulations_sync(query, context)
        
        console.print(f"📚 Found {result.get('total_results', 0)} results")
        
        for i, reg in enumerate(result.get("results", [])[:5], 1):
            console.print(f"\n{i}. {reg.get('title', 'Unknown')}")
            console.print(f"   Section: {reg.get('section', 'N/A')}")
            console.print(f"   Relevance: {reg.get('relevance_score', 0):.2f}")
            
    except Exception as e:
        console.print(f"❌ Error: {e}", style="red")


@app.command()
def config():
    """Show current configuration."""
    table = Table(title="FSCompliance Configuration")
    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Default LLM", settings.default_llm)
    table.add_row("MCP Port", str(settings.mcp_port))
    table.add_row("MCP Host", settings.mcp_host)
    table.add_row("Debug Mode", str(settings.debug))
    table.add_row("Log Level", settings.log_level)
    
    console.print(table)


def main():
    """Main CLI entry point."""
    setup_logging()
    app()


if __name__ == "__main__":
    main()