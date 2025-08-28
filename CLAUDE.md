# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

The project Overview is as per the "Vision, Mission, Identity" section at the top of README.md.

## Target Users

Primary users: Compliance Officers in financial institutions requiring AI-native regulatory intelligence for daily compliance tasks.

## Core Tool Implementation

Initially 7 core tools are to be implemented with standard-specific prefixing, as set out in ComplianceTools.md.

## Universal Standards - Definitions

The Universal_FSCompliance_MCP Project uses "Standard" widely to include:

- **Regulatory frameworks** (FCA Handbook, SEC rules, MiFID II, Basel III)
- **Industry codes** (conduct codes, best practice guidelines)  
- **Statutory requirements** (legislation, acts, laws)
- **International standards** (IFRS, SOX, ISO standards)
- **Jurisdictional regulations** (state, provincial, national requirements)
- **Consultation documents** (regulatory proposals, policy consultations, draft guidance)

"Implemented Standards" refers to Standards which have been implemented. The Project is universal in the sense of being capable of being applied to any codified Standard.

## Strategic & Planning Document Hierarchy

1. CLAUDE.md - primary
2. Rules.md - coding
3. Planning.md - constraints
4. LLMChoice.md, Touchstones.md, ComplianceTools.md - lynchpins
5. SpecialFactors.md - 2-layer sematic matching and use of Ground Truth, no graph databases for now.
6. DatabaseArchitecture.md - organisation of knowledge base and records
7. TechnologyStack.md - technologies adopted, enterprise self hosting.
8. LegalLiability.md - liability framework, audit trails, user responsibility.
9. Charging.md - billing architecture, usage metering, pricing models.

## Architecture

### Principles:

1. **Multi-Server MCP Layer**: Standard-specific protocol-compliant JSON-RPC 2.0 servers (mcp-server-fca-compliance, mcp-server-mifid-compliance, etc.)
2. **Two-Layer Semantic Matching**: Semantic anchors + vector similarity search optimized for structured regulatory content
3. **Compliance Intelligence Tools**: Initially, 7 Tools for daily compliance officer work with Standard-specific prefixing
4. **Database Abstraction Layer**: Standard-specific data access with unified infrastructure (table prefix approach)
5. **LLM Integration Layer**: Multi-LLM support with configurable default LLM. 

### Usage

- **LLM Strategy**: Users can specify LLM to be used by the Tool.
- **LLM Independence**: Our MCP servers run their own LLM separately from enterprise AI agent LLM choices.
- **LLM-Open Architecture**: Abstract interfaces maintained for LLM-open support.
- **Database Architecture**: Currently, unified Supabase (PostgreSQL + PGVector) with standard-specific table prefixes per `DatabaseArchitecture.md`.

### BYOLLM Architecture (Mandatory)

**SECURITY-FIRST CREDENTIAL HANDLING**: All Universal_FSCompliance_MCP components implement zero-trust credential architecture:

- **Zero Server-Side Storage**: No LLM credentials stored in server memory, environment variables, or persistent storage
- **Radical Anti-Harvesting Design**: Architecture fundamentally excludes any possibility of credential harvesting
- **Per-Request Authentication**: User credentials provided with each request via user_context or API payload
- **No Fallback Analysis**: Systems only work with securely provided user LLM credentials - no server defaults or fallback modes
- **Professional IT Standards**: Architecture designed to pass enterprise security audit requirements
- **Consistent Implementation**: Identical credential handling across all MCP servers and interfaces
- **Immediate Credential Discard**: Credentials used for analysis and immediately discarded - never persisted

### Key Technologies
- **Python 3.11+** with Poetry for dependency management
- **Pydantic v2** for data validation and serialization
- **LightRAG** for knowledge retrieval and if graph processing implemented
- **FastAPI** for web framework and MCP server implementation
- **Supabase** for unified database with real-time capabilities and comprehensive interaction analytics
- **OAuth 2.1** for authentication and security

## Development Principles

- Follow AI Agent Oriented multi-server architecture with Standard-specific MCP servers.
- Use database table prefix approach per `DatabaseArchitecture.md`
- Maintain Anthropic's MCP protocol compliance across all servers.
- Create comprehensive Pytest unit tests (90%+ coverage for core compliance logic)
- Iterative Development: Implement minimum reasonable functionality first, ready for staged improvements.
- Follow file size guidelines per Rules.md (500 lines preferred, 1000 lines maximum for complex tools)
- Include Standard citations in compliance logic
- Implement privacy controls for all memory features
- Validate all inputs, especially financial/customer data

## Strategy-to-Implementation Translation

Implementation should be guided by the documents set out in ## Strategic & Planning Document Hierarchy.

## Quality Standards

**Performance Targets:**
- **Test Coverage**: 90%+ for core compliance logic, 75%+ for integration components, 60%+ for UI/UX components
- **Response Time**: <5 seconds for standard queries, <30 seconds for complex analysis, <60 seconds for comprehensive document analysis
- **Accuracy**: Phased targets - 75% initial accuracy, 85% by production, 95% long-term goal (validated through Ground Truth benchmarking)
- **Uptime**: 99.9% system availability target
- **Concurrent Users**: Support 50+ simultaneous connections
- **Throughput**: 1000+ queries per hour capacity

**Testing Requirements:**
- **Unit Tests**: Individual component testing
- **Integration Tests**: System component interaction testing
- **End-to-End Tests**: Complete workflow validation
- **Performance Tests**: Load and stress testing
- **Security Tests**: Vulnerability and penetration testing
- **Ground Truth Validation**: Enterprise-provided real compliance scenarios for accuracy benchmarking

## Interaction Analytics

All MCP tools must implement automatic interaction logging per `DatabaseArchitecture.md`:

- **Mandatory Logging**: Every tool includes `await self._log_interaction(data)` 
- **Performance**: Asynchronous, <5ms overhead, never blocks tool execution
- **Data Capture**: User context, tool usage, regulatory navigation, response metrics
- **Privacy**: Row-level security, anonymization support, configurable participation
- **Dashboard Support**: Multi-platform integration (Supabase, Grafana, Power BI, custom)
- **Data Retention**: Automated deletion (7yr compliance audit, 3yr operational, 1yr research)
- **GDPR Compliance**: Data subject rights API endpoints (export, rectify, erase)

## Usage Metering and Billing Architecture

All MCP tools must include usage tracking infrastructure aligned with `Charging.md` specifications:

- **Billing Tool Categories**: Map tools to categories ('basic_query', 'analysis', 'report', 'validation')
- **Complexity Tiers**: Classify queries ('simple', 'medium', 'complex') for tiered pricing
- **Pricing Alignment**: Record applicable rates (currently 0.00) and subscription tiers
- **Allowance Tracking**: Monitor usage against subscription allowances and overages
- **Rate Limiting**: Configurable quotas per organization with hourly rate limits
- **Configuration-Driven**: External pricing config without code deployment (pricing_config.yaml)

## DirectAccessAgent (Web Interface)

**PURPOSE**: The DirectAccessAgent provides web-based access to MCP server functionality, allowing users to experience Universal_FSCompliance_MCP capabilities before integrating MCP servers into their enterprise AI agents.

**ARCHITECTURAL REQUIREMENTS**:
- **Perfect MCP Mirroring**: Web interface must faithfully replicate main MCP server functionality via Docker configuration
- **Identical Tool Behavior**: Same 7 core FCA tools with identical responses and error handling
- **BYOLLM Consistency**: Web interface uses same zero-trust credential architecture as main MCP servers
- **Docker Configuration**: Single source of truth maintained through containerized MCP server replication
- **User Experience**: Seamless transition from web testing to MCP server integration
- **Security Parity**: Web interface meets same professional IT security standards as MCP servers

**DEPLOYMENT**: Docker-based deployment ensures DirectAccessAgent exactly replicates MCP server behavior without code duplication.

## Date Handling Protocol

**CRITICAL DATE RULE**: Before using any date, check if the current date is being referred to: if it is, check the actual date and use that (beware of December 2024); if not, do not correct it.

- **For current dates**: Always check system reminder for today's date
- **For project timeline**: Project began 20 June 2025, never December 2024
- **For review dates**: Use actual current date, not historical placeholders
- **For external references**: Do not modify (e.g., "Deloitte's RegTech Report 2024" stays as 2024)
- **When updating documents**: Check "Last Updated" fields and use current date
- **Default assumption**: December 2024 is always wrong for this project

## Development Commands

### Setup

```bash
# Install Poetry (dependency management)
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install

# Activate virtual environment
poetry shell
```

### Development
```bash
# Format code
poetry run black .

# Lint code
poetry run ruff check .

# Run tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=fca_compliance
```

### MCP Server
```bash
# Start FCA Compliance MCP server
cd mcp-server-fca-compliance
poetry run python -m mcp_server_fca_compliance.server

# Test FCA Compliance MCP server
poetry run python -m mcp_server_fca_compliance.test_client
```

## About This Document

**Author**: Blake Dempster, Founder, CEO, Principal Architect  
**Last Updated**: 28 August 2025  