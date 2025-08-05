# The Tools In the MCP Toolset

## Purpose of this Document

As an AI Agent Oriented MCP platform, the Universal Standards Engine makes available curated sets of specialist Tools through Standard-specific MCP servers. 

This document sets out Tools currently being worked on. Future Tools will be developed as the need arises.

## AI Agent Oriented Naming

- Tools are designed to optimize AI agent discovery and semantic matching

- Each Standard is housed in a separate semantically anchored MCP server containing semantically anchored Tool names

- Tool names include reference to the Implemented Standard as context to match AI agent query patterns (e.g., "Does this comply with **FCA** requirements?" → `FCA_quickly_check_compliance`)
  
- The structured and codified nature of Standards makes them ideal for AI-powered analysis through two-layer semantic matching

- Following MCP best practice, tools use lowercase with underscores

## Core Tools

Each standard-specific MCP server implements these tools with appropriate prefixing:

### **1. [standard]_quickly_check_compliance**

- **Purpose**: Rapid compliance assessment for policy conceptualization and quick validation
  
- **Example FCA**: "Here is proposed wording for a new investment policy. What FCA compliance issues arise?"
- 
- **Example MiFID**: "Does this client categorization process comply with MiFID II requirements?"
- **Usage**: Quick, accessible compliance assistance.

### **2. [standard]_identify_compliance_requirements_in_specific_case**

- **Purpose**: Context-specific regulatory requirement extraction for particular scenarios

- **Example FCA**: "What are the 10 most significant FCA requirements for advising a 65-year-old single woman on pension transfers?"

- **Example SEC**: "What SEC requirements apply when launching a new mutual fund for retail investors?"

- **Usage**: Research and requirement identification with context-aware extraction from Standards.

### **3. [standard]_systematically_analyse_compliance_implications**

- **Purpose**: Comprehensive strategic compliance analysis with risk scoring and business impact assessment

- **Example FCA**: "We are thinking about a marketing relationship with a provider of complementary financial services, details attached. Analyse this against FCA requirements. Provide risk scores and implementation timeline."

- **Example MiFID**: "What issues arise from our cross-border investment services, details attached, against MiFID II provisions."

- **Usage**: Wider and deeper strategic policy review than quick compliance check, with systematic risk assessment.

### **4. [standard]_suggest_remediation**

- **Purpose**: AI-powered gap-specific remediation recommendations with implementation guidance

- **Example FCA**: "We have an FCA suitability assessment gap in our advisory process. Suggest remediation actions with costs and timelines."

- **Example Basel**: "Our capital adequacy reporting shows Basel III shortfalls. Recommend remediation approach."

- **Usage**: Convert compliance gaps into actionable solutions with practical implementation guidance

### **5. [standard]_prepare_draft_compliance_audit_report**

- **Purpose**: Professional audit documentation preparation with evidence collection and compliance scoring

- **Example FCA**: "Prepare draft FCA compliance audit report for our wealth management division covering Q1-Q3 2025."

- **Example MiFID**: "Generate MiFID II compliance audit documentation for our investment research operations."

- **Usage**: Reduce audit preparation burden with systematic evidence collection and professional report formatting

### **6. [standard]_validate_ground_truth**

- **Purpose**: Enterprise-grade validation and benchmarking against known compliance scenarios

- **Example FCA**: "Validate our FCA compliance tools against these ground truth scenarios and provide accuracy assessment."

- **Usage**: Quality assurance and continuous improvement with accuracy benchmarking for enterprise deployment

### **7. [standard]_status_of_standard_ingestion**

- **Purpose**: System status and coverage

- **Example FCA**: "Show current status of FCA Handbook ingestion and coverage statistics."

- **Example MiFID**: "What MiFID II sections are available for compliance analysis?"

- **Usage**: Reassurance through transparency into system capabilities and boundaries

### **Future Tools**

Future Tools will be developed as the need arises.

## Background Tools.

### **A. [standard]_update_standard**

- **Purpose**: Ensure Implemented Standard is up to date

- **Usage**: Internal hygiene measure run regularly.

### **B. [standard]_ingest_new_standard**

- **Purpose**: Ingest new Standard to make it an Implemented Standard.

- **Usage**: Internal for now. May make available to Users eg for ingesting Users' internal management codes.

---

## About This Document

**Author**: Blake Dempster, Founder, CEO, Principal Architect  
**Co-Authored by**: Claude Code (claude.ai/code)  
**Last Updated**: 29 July 2025  
**Date last reviewed formally by MDqualityCheck.md**: 1 August 2025  
