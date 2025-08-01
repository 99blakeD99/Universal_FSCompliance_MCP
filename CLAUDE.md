# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**The Universal_FSCompliance_MCP Project** is the open-source compliance intelligence platform built exclusively for financial services. We make regulatory intelligence accessible to any AI agent through innovative MCP integration while increasing the effectiveness of compliance professionals. Built as a universal Standards engine with the FCA Handbook as our first ingested Standard, the Universal_FSCompliance_MCP Project rapidly ingests any well-articulated Standard, broadly defined to include regulatory frameworks, industry codes, statutory requirements, international standards, jurisdictional regulations, and consultation documents. The Universal_FSCompliance_MCP Project is positioned as the first MCP-integrated compliance platform, **with MCP tools that turbocharge AI effectiveness by transforming general AI agents into compliance experts**, ultimately serving the goal of **making it easier to bring the right financial products safely to consumers**.

## Key Project Files

### Strategic & Planning Documents
- **`Planning.md`**: Complete project architecture, goals, technical specifications, and development roadmap
- **`Rules.md`**: Development guidelines, coding standards, and project-specific conventions
- **`Tasks.md`**: Current and completed development tasks organized by development phases
- **`ComplianceTools.md`**: Strategic market analysis and comprehensive MCP tool roadmap
- **`LLMChoice.md`**: LLM selection strategy and multi-provider architecture rationale
- **`MDqualityCheck.md`**: Systematic methodology for document reviews with multi-stakeholder perspectives
- **`Touchstones.md`**: Core project principles and strategic consistency framework

### Documentation & Brand Materials
- **`FAQ.md`**: User-facing project information and comprehensive capability descriptions
- **`DatabaseStrategy.md`**: Database architecture evaluation and migration planning
- **`StandardImplementMCP.md`**: Systematic methodology for implementing new regulatory standards

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

## Architecture

The Universal_FSCompliance_MCP Project follows an AI Agent Oriented multi-server architecture as the first MCP-integrated compliance platform:

1. **Multi-Server MCP Layer**: Standard-specific protocol-compliant JSON-RPC 2.0 servers (mcp-server-fca-compliance, mcp-server-mifid-compliance, etc.)
2. **Two-Layer Semantic Matching**: Semantic anchors + vector similarity search optimized for structured regulatory content
3. **Compliance Intelligence Layer**: 7 focused tools for daily compliance officer work with standard-specific prefixing
4. **Database Abstraction Layer**: Standard-specific data access with unified infrastructure (table prefix approach)
5. **LLM Integration Layer**: Multi-model support with configurable default LLM. **Architectural Independence**: Our MCP servers operate independently from enterprise AI agent LLM choices

### Strategic Architecture Decisions
- **LLM Strategy**: Default LLM configurable based on enterprise requirements and real-world validation through the Universal_FSCompliance_MCP Project development; no fine-tuning architectural decision per `LLMChoice.md`
- **LLM Independence**: Our MCP server runs its own LLM completely separately from enterprise AI agent LLM choices, eliminating adoption barriers from corporate LLM standardization decisions  
- **LLM-Open Architecture**: Phased implementation with enterprise-preferred LLM optimization while maintaining abstract interfaces for multi-LLM expansion per `LLMChoice.md`
- **Database Architecture**: Unified Supabase (PostgreSQL + PGVector) with standard-specific table prefixes per `DatabaseStrategy.md` for simplified architecture and real-time capabilities
- **MCP Tool Priority**: 7 core tools identified in `ComplianceTools.md` with standard-specific prefixing (removed map_relationships as not aligned with daily compliance work)
- **Brand Positioning**: Positioned as first MCP-integrated compliance platform per `Brand.md` competitive analysis
- **UI/UX Design**: Professional financial services interface specifications detailed in `UserInterface.md`

### Key Technologies
- **Python 3.11+** with Poetry for dependency management
- **Pydantic v2** for data validation and serialization
- **LightRAG** for knowledge retrieval and graph processing
- **FastAPI** for web framework and MCP server implementation
- **Supabase** for unified database with real-time capabilities and comprehensive interaction analytics
- **OAuth 2.1** for authentication and security

## Universal Standards Definition

The Universal_FSCompliance_MCP Project uses "Standard" widely to include:
- **Regulatory frameworks** (FCA Handbook, SEC rules, MiFID II, Basel III)
- **Industry codes** (conduct codes, best practice guidelines)  
- **Statutory requirements** (legislation, acts, laws)
- **International standards** (IFRS, SOX, ISO standards)
- **Jurisdictional regulations** (state, provincial, national requirements)
- **Consultation documents** (regulatory proposals, policy consultations, draft guidance)

This universal approach enables the Universal_FSCompliance_MCP Project to serve as a comprehensive compliance intelligence platform across multiple regulatory contexts.

## Date Handling Protocol

**CRITICAL DATE RULE**: Before using any date, check if the current date is being referred to: if it is, check the actual date and use that (beware of December 2024); if not, do not correct it.

- **For current dates**: Always check system reminder for today's date
- **For project timeline**: Project began 20 June 2025, never December 2024
- **For review dates**: Use actual current date, not historical placeholders
- **For external references**: Do not modify (e.g., "Deloitte's RegTech Report 2024" stays as 2024)
- **When updating documents**: Check "Last Updated" fields and use current date
- **Default assumption**: December 2024 is always wrong for this project

## Development Guidelines

**This document provides comprehensive implementation guidance. Also consult `Rules.md` for granular coding conventions, `Planning.md` for essential constraints, and `StandardImplementMCP.md` for new standard methodology.** Document hierarchy: 1) CLAUDE.md (primary), 2) Rules.md (coding), 3) Planning.md (constraints), 4) StandardImplementMCP.md (expansion), 5) Other strategic documents.

**Key principles:**

- Follow AI Agent Oriented multi-server architecture from `TechnicalArchitecture.md`
- Implement standard-specific MCP servers following methodology in `StandardImplementMCP.md`
- Use database table prefix approach per `DatabaseStrategy.md`
- Maintain MCP protocol compliance across all servers
- Create comprehensive Pytest unit tests (90%+ coverage for core compliance logic)
- **AI Agent Oriented Principle**: Optimize tool names and server architecture for AI agent semantic matching
- **Pragmatic Excellence**: Balance quality with practical implementation - focus on core compliance functionality first, then optimize
- **Iterative Development**: Implement minimum viable functionality first, then enhance based on validation results
- Follow file size guidelines per Rules.md (500 lines preferred, 1000 lines maximum for complex tools)
- Include regulatory source citations in compliance logic
- Implement privacy controls for all memory features
- Validate all inputs, especially financial/customer data
- **Universal Standards Engine**: Design for systematic expansion to new regulatory frameworks

## Quality Standards (from TechnicalArchitecture.md)

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

## Strategic-to-Implementation Translation

**Key Implementation Requirements from Strategic Documents:**

### From LLMChoice.md:
- **Default LLM Configuration**: Enterprise-preferred LLM configurable in config files/environment variables
- **Multi-Model Architecture**: Code must support configurable LLM providers (Claude, OpenAI, LLaMA, Mistral, user-defined)
- **Architectural Independence**: The MCP server LLM choice operates completely independently from AI agent LLM choices
- **Abstract Interface Design**: Implement LLMProvider class with provider-agnostic interface
- **Configuration-Driven LLM Selection**: Environment variables `LLM_PROVIDER` with provider-specific API keys
- **Flexible Implementation**: Enterprise-configurable implementation with abstract architecture for multi-LLM support

### From Touchstones.md:
- **Universal Standards Engine**: Code must support rapid ingestion of new regulatory frameworks beyond FCA Handbook
- **Self-Hostable Architecture**: All components must be deployable on enterprise infrastructure
- **Standard Models + RAG**: No fine-tuning infrastructure - use standard LLMs with advanced retrieval

### From ComplianceTools.md:
- **MCP Tool Priority**: Implement 7 core tools with standard-specific prefixing (FCA_quickly_check_compliance, FCA_systematically_analyse_compliance_implications, FCA_identify_compliance_requirements_in_specific_case, FCA_prepare_draft_compliance_audit_report, FCA_validate_ground_truth, FCA_suggest_remediation, FCA_status_of_standard_ingestion). Removed map_relationships as not aligned with daily compliance officer work.
- **AI Agent Oriented Design**: Tool names include regulatory context to optimize AI agent semantic matching (e.g., "Does this comply with FCA requirements?" → `FCA_quickly_check_compliance`)
- **Multi-Server Architecture**: Each regulatory standard receives dedicated MCP server following methodology in `StandardImplementMCP.md`
- **Database Table Prefixes**: Single database with standard-specific table prefixes (fca_, mifid_, sec_) per `DatabaseStrategy.md`
- **Tool Specifications**: Each tool requires specific schemas, validation, and response formats
- **Tool Naming Convention**: Use standard-specific lowercase format (e.g., `FCA_quickly_check_compliance`, not `quickly_check_Compliance`)
- **Ground Truth Validation**: Implement standard-specific `validate_ground_truth` tools for enterprise accuracy benchmarking

### From StandardImplementMCP.md:
- **Systematic Standard Implementation**: Follow 4-phase methodology (Standard Assessment → Technical Implementation → Data Infrastructure → Validation & Deployment) for all new regulatory frameworks
- **AI Agent Oriented Design**: Each standard gets dedicated MCP server with semantic anchoring (mcp-server-fca-compliance, mcp-server-mifid-compliance, etc.)
- **Template-Based Expansion**: Use mcp-server-fca-compliance as proven template for new standard implementations
- **Database Table Prefixes**: Implement standard-specific tables within unified database (fca_documents, mifid_documents, etc.)
- **Two-Layer Semantic Matching**: Apply semantic anchors + vector similarity search for structured regulatory content
- **Unified but Efficient Ingestion**: Full content for high-value sections, heading-only for comprehensive coverage with boundary messaging
- **Ground Truth Integration**: Design for future regulatory Q&A datasets with user-specific access controls
- **Quality Assurance**: Conduct systematic testing against known compliance scenarios before production deployment
- **Documentation Updates**: Update CLAUDE.md and technical documentation to reflect new standard implementations

### From LegalLiability.md:
- **Liability Framework Integration**: Implement user interface components that integrate liability reminders and warnings
- **Initial Liability Acceptance**: Code must require acceptance of liability terms before system access
- **Periodic Liability Reinforcement**: Implement notifications during extended user sessions to reinforce liability framework
- **Tool-Specific Warnings**: Implement warnings for high-risk activities, particularly Standard ingestion using `ingest_new_identified_standard` tool
- **Audit Trail Requirements**: Implement comprehensive logging and documentation systems for compliance audit purposes
- **Permanent Record Systems**: Code must support user IT systems maintaining permanent records of tool usage, outputs, and professional review processes
- **Emergency Procedures**: Implement system limitation warnings and alternative compliance verification prompts during errors/outages
- **User Responsibility Reinforcement**: All tool outputs must include disclaimers that AI-generated content requires human review and validation

### Project Terminology:
- **The Universal_FSCompliance_MCP Project**: Refers to the comprehensive development initiative creating a suite of specialist Compliance MCP servers - use consistently across all documentation, git commits, code comments, and user-facing interfaces

### Documentation Standards:
- **UK Date Format**: Use "DD Month YYYY" format (e.g., "25 December 2024") in all documentation
- **Professional Tone**: Corporate financial services audience - avoid colloquialisms, be succinct
- **Touchstones Consistency**: Check strategic decisions against Touchstones.md principles
- **Document Quality**: Follow MDqualityCheck.md methodology for systematic document reviews with multi-stakeholder perspectives

## Target Users

Primary users: Compliance Officers in financial institutions requiring AI-native regulatory intelligence for daily compliance tasks.

## Core Tool Implementation

The 7 core tools with standard-specific prefixing (e.g., `FCA_quickly_check_compliance`) cover:
1. Quick compliance assessment
2. Context-specific requirement identification  
3. Systematic compliance analysis
4. Gap remediation recommendations
5. Audit report preparation
6. Ground truth validation
7. System status and coverage visibility

## Interaction Analytics Requirements

All MCP tools must implement automatic interaction logging per `DatabaseStrategy.md`:

- **Mandatory Logging**: Every tool includes `await self._log_interaction(data)` 
- **Performance**: Asynchronous, <5ms overhead, never blocks tool execution
- **Data Capture**: User context, tool usage, regulatory navigation, response metrics
- **Privacy**: Row-level security, anonymization support, configurable participation
- **Dashboard Support**: Multi-platform integration (Supabase, Grafana, Power BI, custom)
- **Data Retention**: Automated deletion (7yr compliance audit, 3yr operational, 1yr research)
- **GDPR Compliance**: Data subject rights API endpoints (export, rectify, erase)

## Usage Metering and Billing Architecture

All MCP tools must include usage tracking infrastructure aligned with `ChargingModels.md` specifications:

- **Billing Tool Categories**: Map tools to categories ('basic_query', 'analysis', 'report', 'validation')
- **Complexity Tiers**: Classify queries ('simple', 'medium', 'complex') for tiered pricing
- **Pricing Alignment**: Record applicable rates (currently 0.00) and subscription tiers
- **Allowance Tracking**: Monitor usage against subscription allowances and overages
- **Rate Limiting**: Configurable quotas per organization with hourly rate limits
- **Configuration-Driven**: External pricing config without code deployment (pricing_config.yaml)

## Document Quality

Follow MDqualityCheck.md methodology for systematic document reviews. Update this file when strategic documents change coding requirements.

---

## About This Document

**Author**: Blake Dempster, Founder, CEO, Principal Architect  
**Co-Authored by**: Claude Code (claude.ai/code)  
**Last Updated**: 29 July 2025  
**Date last reviewed formally by MDqualityCheck.md**: 19 July 2025  
**Status**: (okay)
**Purpose**: Guidance for Claude Code when working with the Universal_FSCompliance_MCP Project code, including strategic-to-implementation translation and systematic review processes.

---