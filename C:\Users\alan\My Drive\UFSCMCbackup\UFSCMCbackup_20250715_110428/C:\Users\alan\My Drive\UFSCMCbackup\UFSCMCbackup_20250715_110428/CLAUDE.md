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
- **`LLMChoice.md`**: LLM selection strategy and Claude 3.5 Sonnet decision rationale
- **`MDqualityCheck.md`**: Systematic methodology for document reviews with multi-stakeholder perspectives
- **`Touchstones.md`**: Core project principles and strategic consistency framework

### Documentation & Brand Materials
- **`FAQ.md`**: User-facing project information and comprehensive capability descriptions
- **`internal/Brand.md`**: Brand positioning, competitive differentiation, and market strategy
- **`internal/DatabaseStrategy.md`**: Database architecture evaluation and migration planning
- **`internal/FCAsandbox.md`**: FCA Sandbox application strategy and regulatory validation timeline
- **`internal/UserInterface.md`**: UI/UX design specifications and presentation prototypes

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
poetry run pytest --cov=fscompliance
```

### MCP Server
```bash
# Start MCP server
poetry run python -m fscompliance.server

# Test MCP server
poetry run python -m fscompliance.test_client
```

## Architecture

The Universal_FSCompliance_MCP Project follows a layered architecture as the first MCP-integrated compliance platform:

1. **MCP Server Layer**: Protocol-compliant JSON-RPC 2.0 server
2. **Knowledge Management Layer**: LightRAG-powered FCA Handbook processing
3. **Compliance Intelligence Layer**: AI-powered requirement analysis and gap detection
4. **Memory and Learning Layer**: Long-term memory with privacy controls
5. **LLM Abstraction Layer**: Multi-model support with Claude 3.5 Sonnet default (LLaMA 3, Falcon, Mistral Medium alternatives). **Architectural Independence**: Our MCP server operates independently from enterprise AI agent LLM choices

### Strategic Architecture Decisions
- **LLM Strategy**: Claude 3.5 Sonnet selected as default based on extensive real-world validation through the Universal_FSCompliance_MCP Project development; no fine-tuning architectural decision per `LLMChoice.md`
- **LLM Independence**: Our MCP server runs its own LLM completely separately from enterprise AI agent LLM choices, eliminating adoption barriers from corporate LLM standardization decisions
- **Database Evolution**: Migrating to Supabase (PostgreSQL + PGVector) per `DatabaseStrategy.md` for simplified architecture and real-time capabilities
- **MCP Tool Priority**: 7 priority tools identified in `ComplianceTools.md` for Phase 3 implementation
- **Brand Positioning**: Positioned as first MCP-integrated compliance platform per `Brand.md` competitive analysis
- **UI/UX Design**: Professional financial services interface specifications detailed in `UserInterface.md`

### Key Technologies
- **Python 3.11+** with Poetry for dependency management
- **Pydantic v2** for data validation and serialization
- **LightRAG** for knowledge retrieval and graph processing
- **FastAPI** for web framework and MCP server implementation
- **Supabase** for unified database with real-time capabilities (migration planned Q3 2025)
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

## Development Guidelines

**Always consult `Rules.md` before starting development work.** Key principles:

- Follow layered architecture from `Planning.md`
- Maintain MCP protocol compliance
- Create comprehensive Pytest unit tests
- Never exceed 500 lines per file
- Include regulatory source citations in compliance logic
- Implement privacy controls for all memory features
- Validate all inputs, especially financial/customer data

## Quality Standards (from TechnicalArchitecture.md)

**Performance Targets:**
- **Test Coverage**: 90%+ code coverage requirement
- **Response Time**: <2 seconds for standard queries, <10 seconds for complex analysis
- **Accuracy**: 95%+ compliance analysis accuracy (validated through Ground Truth benchmarking)
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
- **Default LLM Configuration**: Claude 3.5 Sonnet must be default in config files/environment variables
- **Multi-Model Architecture**: Code must support configurable LLM providers (Claude, LLaMA 3, Mistral, user-defined)
- **Architectural Independence**: The MCP server LLM choice operates completely independently from AI agent LLM choices

### From Touchstones.md:
- **Universal Standards Engine**: Code must support rapid ingestion of new regulatory frameworks beyond FCA Handbook
- **Self-Hostable Architecture**: All components must be deployable on enterprise infrastructure
- **Standard Models + RAG**: No fine-tuning infrastructure - use standard LLMs with advanced retrieval

### From ComplianceTools.md:
- **MCP Tool Priority**: Implement 9 tools (quickly_check_compliance, systematically_analyse_compliance_implications, identify_compliance_requirements_in_specific_case, prepare_draft_compliance_audit_report, map_relationships, validate_ground_truth, ingest_new_identified_standard, update_identified_standard, suggest_remediation)
- **Tool Specifications**: Each tool requires specific schemas, validation, and response formats
- **Tool Naming Convention**: Use lowercase format for tool names (e.g., `quickly_check_compliance`, not `quickly_check_Compliance`)
- **Ground Truth Validation**: Implement `validate_ground_truth` tool for enterprise accuracy benchmarking with confidential testing environment

### From LegalLiability.md:
- **Liability Framework Integration**: Implement user interface components that integrate liability reminders and warnings
- **Initial Liability Acceptance**: Code must require acceptance of liability terms before system access
- **Periodic Liability Reinforcement**: Implement notifications during extended user sessions to reinforce liability framework
- **Tool-Specific Warnings**: Implement warnings for high-risk activities, particularly Standard ingestion using `ingest_new_identified_standard` tool
- **Audit Trail Requirements**: Implement comprehensive logging and documentation systems for compliance audit purposes
- **Permanent Record Systems**: Code must support user IT systems maintaining permanent records of tool usage, outputs, and professional review processes
- **Emergency Procedures**: Implement system limitation warnings and alternative compliance verification prompts during errors/outages
- **User Responsibility Reinforcement**: All tool outputs must include disclaimers that AI-generated content requires human review and validation

### Project vs Product Naming:
- **The Universal_FSCompliance_MCP Project**: Refers to project, codebase, development initiative - use in technical documentation, git commits, code comments
- **The Universal_FSCompliance_MCP Product**: Refers to deployed product - use in user-facing interfaces, API responses, configuration

### Documentation Standards:
- **UK Date Format**: Use "DD Month YYYY" format (e.g., "25 December 2024") in all documentation
- **Professional Tone**: Corporate financial services audience - avoid colloquialisms, be succinct
- **Touchstones Consistency**: Check strategic decisions against Touchstones.md principles
- **Document Quality**: Follow MDqualityCheck.md methodology for systematic document reviews with multi-stakeholder perspectives

## Target Users

- Compliance Officers
- Risk Managers  
- Regulatory Inspectors
- Professional Advisers

## Use Cases

Based on ComplianceTools.md analysis and current MCP tool roadmap:

### Primary Use Cases (Phase 2 Complete)
1. **Compliance Gap Analysis**: AI agents analyze policies to identify the ten most salient requirements and flag compliance gaps using `analyze_compliance` and `detect_gaps` tools
2. **Regulatory Intelligence**: AI agents extract relevant requirements from FCA Handbook using `extract_requirements` for specific policy or scenario analysis
3. **Compliance Assessment**: AI agents provide comprehensive policy analysis against regulatory requirements with confidence scoring

### Advanced Use Cases (Core Tool Implementation)
4. **Quick Compliance Assessment**: AI agents perform rapid compliance checking using `quickly_check_compliance` for policy conceptualization assistance
5. **Systematic Compliance Analysis**: AI agents conduct detailed strategic analysis using `systematically_analyse_compliance_implications` with risk scoring and remediation guidance
6. **Requirement Identification**: AI agents extract context-specific regulatory requirements using `identify_compliance_requirements_in_specific_case`
7. **Audit Preparation**: AI agents compile compliance evidence and prepare draft audit reports using `prepare_draft_compliance_audit_report`
8. **Relationship Mapping**: AI agents visualize regulatory connections and business impact using `map_relationships`
9. **Ground Truth Validation**: AI agents enable enterprise accuracy benchmarking using `validate_ground_truth` for confidential testing of system performance on real compliance data
10. **Standard Ingestion**: AI agents enable user-driven expansion using `ingest_new_identified_standard` for platform growth (requires liability framework integration)
11. **Standard Updates**: AI agents maintain system currency using `update_identified_standard` for automatic regulatory change monitoring
12. **Gap Remediation**: AI agents provide actionable compliance solutions using `suggest_remediation` for gap resolution

### Future Use Cases (Phase 4+)
13. **Automated Regulatory Reporting**: AI agents generate draft regulatory reports and submissions using `generate_compliance_reports`
14. **Additional Capabilities**: Future tools based on user feedback and market validation

## Strategic Document Review Process

When reviewing any .md file, follow the systematic methodology in MDqualityCheck.md:
1. **Content Quality**: Check professional tone, avoid repetition, ensure internal consistency
2. **Touchstones Alignment**: Verify consistency with Touchstones.md principles
3. **CLAUDE.md Impact**: Assess whether changes require updates to implementation guidance
4. **Multi-Perspective Review**: Evaluate from stakeholder viewpoints (CEO, CCO, CTO, CISO, CRO, IT Director, Purchasing Director, Head of AI, Operational Director, Regulatory Affairs Director)

**Coding-Relevant Documents** that may require CLAUDE.md updates:
- Planning.md, LLMChoice.md, Rules.md, ComplianceTools.md, Tasks.md (direct coding impact)
- FAQ.md, Brand.md, UserInterface.md, LegalLiability.md (UI/UX and user-facing elements)

**Strategic-Only Documents** (no CLAUDE.md impact):
- FCAsandbox.md, TakeToMarket.md, DatabaseStrategy.md, MgmtImpactRules.md, UpdateCheck.md, Touchstones.md, MDqualityCheck.md

---

## About This Document

**Author**: Blake Dempster, Founder, CEO, Principal Architect  
**Co-Authored by**: Claude Code (claude.ai/code)  
**Created**: 25 December 2024  
**Last Updated**: 15 July 2025  
**Date last reviewed formally by MDqualityCheck.md**: 9 July 2025  
**Status**: (needs eyeball)
**Purpose**: Guidance for Claude Code when working with the Universal_FSCompliance_MCP Project code, including strategic-to-implementation translation and systematic review processes.

---