# The Tools In the MCP Toolset

## Purpose of this Document

As an AI Agent Oriented MCP platform, the Universal Standards Engine makes available curated sets of specialist Tools through standard-specific MCP servers. This document sets out the tool architecture and roadmap for regulatory compliance intelligence.

The roadmap may change in light of emerging priorities and this document will record any changes.

## Context

### AI Agent Oriented Design

- Tools are designed to optimize AI agent discovery and semantic matching
- Each regulatory standard receives its own MCP server with semantically anchored tool names
- Tool names include regulatory context to match AI agent query patterns (e.g., "Does this comply with **FCA** requirements?" → `FCA_quickly_check_compliance`)
- The structured nature of regulatory standards makes them ideal for AI-powered analysis through two-layer semantic matching

### Naming Convention

- **Standard-Specific Prefixing**: Tools are named `[STANDARD]_tool_name` format (e.g., `FCA_quickly_check_compliance`, `MiFID_identify_compliance_requirements`)
- **Semantic Anchoring**: Tool names serve as semantic anchors that AI agents can directly match to regulatory contexts
- **Lowercase Formatting**: Following MCP best practices, tools use lowercase with underscores
- **Regulatory Context**: Each tool name explicitly identifies the applicable regulatory standard

### Architecture Pattern

- **Multiple MCP Servers**: Each standard gets a dedicated server (`FCA_Compliance_MCP`, `MiFID_Compliance_MCP`, `SEC_Compliance_MCP`)
- **Universal Implementation**: Same 7 core tools implemented across all standards with appropriate prefixing
- **Database Isolation**: Standard-specific database tables with unified infrastructure
- **Systematic Expansion**: New standards follow methodology outlined in StandardImplementMCP.md

## Usage Pattern

- **AI Agent Discovery**: AI agents automatically discover appropriate MCP server based on regulatory context in queries
- **Tool Selection**: LLM intelligently selects tools based on semantic anchors and compliance context
- **Natural Interaction**: Users enter prompts naturally without memorizing tool names or syntax
- **Intelligent Routing**: Multi-server architecture routes queries to appropriate regulatory framework
- **Standard-Specific Results**: Each server provides compliance analysis specific to its regulatory context

## Core Tool Architecture (7 Tools per Standard)

Each standard-specific MCP server implements these tools with appropriate prefixing:

### **1. [STANDARD]_quickly_check_compliance**
- **Purpose**: Rapid compliance assessment for policy conceptualization and quick validation
- **Example FCA**: "Here is proposed wording for a new investment policy. What FCA compliance issues arise?"
- **Example MiFID**: "Does this client categorization process comply with MiFID II requirements?"
- **Usage**: Quick, accessible compliance assistance during policy development using two-layer semantic matching against regulatory content

### **2. [STANDARD]_identify_compliance_requirements_in_specific_case**
- **Purpose**: Context-specific regulatory requirement extraction for particular scenarios
- **Example FCA**: "What are the 10 most significant FCA requirements for advising a 65-year-old single woman on pension transfers?"
- **Example SEC**: "What SEC requirements apply when launching a new mutual fund for retail investors?"
- **Usage**: Research and requirement identification with context-aware extraction from regulatory frameworks

### **3. [STANDARD]_systematically_analyse_compliance_implications**
- **Purpose**: Comprehensive strategic compliance analysis with risk scoring and business impact assessment
- **Example FCA**: "Analyze this new digital advice platform against FCA conduct requirements. Provide risk scores and implementation timeline."
- **Example MiFID**: "Systematic analysis of our cross-border investment services against MiFID II provisions."
- **Usage**: Strategic policy review, wider and deeper than quick compliance check, with systematic risk assessment

### **4. [STANDARD]_suggest_remediation**
- **Purpose**: AI-powered gap-specific remediation recommendations with implementation guidance
- **Example FCA**: "We have an FCA suitability assessment gap in our advisory process. Suggest remediation actions with costs and timelines."
- **Example Basel**: "Our capital adequacy reporting shows Basel III shortfalls. Recommend remediation approach."
- **Usage**: Convert compliance gaps into actionable solutions with practical implementation guidance

### **5. [STANDARD]_prepare_draft_compliance_audit_report**
- **Purpose**: Professional audit documentation preparation with evidence collection and compliance scoring
- **Example FCA**: "Prepare draft FCA compliance audit report for our wealth management division covering Q1-Q3 2025."
- **Example MiFID**: "Generate MiFID II compliance audit documentation for our investment research operations."
- **Usage**: Reduce audit preparation burden with systematic evidence collection and professional report formatting

### **6. [STANDARD]_validate_ground_truth**
- **Purpose**: Enterprise-grade validation and benchmarking against known compliance scenarios
- **Example FCA**: "Validate our FCA compliance tools against these ground truth scenarios and provide accuracy assessment."
- **Usage**: Quality assurance and continuous improvement with accuracy benchmarking for enterprise deployment

### **7. [STANDARD]_status_of_standard_ingestion**
- **Purpose**: System status and regulatory content coverage visibility for AI agents and users
- **Example FCA**: "Show current status of FCA Handbook ingestion and coverage statistics."
- **Example MiFID**: "What MiFID II sections are available for compliance analysis?"
- **Usage**: Transparency into system capabilities and regulatory content boundaries

## Tool Implementation Status

### **Current Production Status (FCA_Compliance_MCP)**
✅ **Completed with Real FCA Handbook Integration:**
1. `FCA_quickly_check_compliance` - Two-layer semantic matching operational
2. `FCA_identify_compliance_requirements_in_specific_case` - Context-specific requirement extraction
3. `FCA_systematically_analyse_compliance_implications` - Strategic compliance analysis with risk assessment
4. `FCA_suggest_remediation` - Gap-specific remediation recommendations
5. `FCA_prepare_draft_compliance_audit_report` - Professional audit documentation
6. `FCA_validate_ground_truth` - Enterprise-grade validation and benchmarking  
7. `FCA_status_of_standard_ingestion` - System status and coverage visibility

### **Future Standards Pipeline**
🔄 **Planned Implementation Following StandardImplementMCP.md:**
- **MiFID_Compliance_MCP**: EU investment services regulation (Priority 1)
- **SEC_Compliance_MCP**: US securities regulation (Priority 2)  
- **Basel_Compliance_MCP**: Banking supervision framework (Priority 3)

Each new standard follows systematic implementation methodology:
1. Structure analysis and feasibility assessment
2. Regulatory engagement for ground truth datasets
3. MCP server creation using FCA template
4. Tool customization with standard-specific prefixing
5. Database table creation with appropriate prefixes
6. Content ingestion following unified-but-efficient approach
7. Validation and quality assurance testing

## Tools Removed from Architecture

### **map_relationships** ❌ 
- **Rationale**: Not aligned with daily compliance officer work
- **Alternative**: Specialized regulatory research tools better serve relationship mapping needs
- **Focus**: Maintain focus on practical compliance tools for day-to-day regulatory work

## Strategic Differentiation

### **AI Agent Native Design**
- First MCP platform designed specifically for AI agent semantic matching
- Tool names and server architecture optimize AI discovery and selection
- Multi-server approach prevents "straitjacket" constraints while maintaining consistency

### **Regulatory Intelligence at Scale**
- Two-layer semantic matching (semantic anchors + vector similarity) optimized for structured regulatory content
- Unified-but-efficient ingestion approach balances comprehensive coverage with performance
- Ground truth integration enables enterprise-grade accuracy validation

### **Universal Standards Engine**
- Systematic methodology for rapid standard implementation
- Template-based approach ensures architectural consistency across regulatory frameworks
- Standard-by-standard expansion enables targeted market entry and client-specific deployments

---

## About This Document

**Author**: Blake Dempster, Founder, CEO, Principal Architect  
**Co-Authored by**: Claude Code (claude.ai/code)  
**Created**: 25 December 2024  
**Last Updated**: 19 July 2025  
**Date last reviewed formally by MDqualityCheck.md**: 19 July 2025  
**Status**: Active - updated for AI Agent Oriented multi-server architecture  
**Purpose**: Tool architecture and roadmap for the Universal Standards Engine - defining AI Agent Oriented compliance intelligence through standard-specific MCP servers.

---