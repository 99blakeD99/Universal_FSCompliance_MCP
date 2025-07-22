# Folder Organization - Universal_FSCompliance_MCP Project

## Overview

This document provides a comprehensive guide to the Universal_FSCompliance_MCP Project folder structure, explaining the AI Agent Oriented multi-server architecture and systematic organization approach that enables rapid expansion to new regulatory standards.

## Repository Structure

### **📁 Main Repository**
```
/home/blaked/Universal_FSCompliance_MCP/
```

**Purpose**: Central repository for the Universal_FSCompliance_MCP Project containing strategic documentation, multi-server MCP architecture, and ecosystem integration components.

## **Strategic Documentation (Root Level)**

### **Core Strategic Files**
```
├── CLAUDE.md                    # Primary development guidance for Claude Code
├── README.md                    # Project overview and getting started
├── Planning.md                  # Technical constraints and project scope
├── Touchstones.md              # Core project principles and consistency framework
├── Rules.md                    # Development guidelines and coding standards
├── Tasks.md                    # Development tasks organized by phases
```

### **Architecture and Technical Strategy**
```
├── TechnicalArchitecture.md     # Enterprise technical architecture guide
├── StandardImplementMCP.md      # Methodology for implementing new standards
├── ComplianceTools.md          # Tool architecture and roadmap
├── DatabaseStrategy.md         # Database architecture and migration planning
├── LLMChoice.md               # LLM selection strategy and rationale
```

### **Business and Market Strategy**
```
├── MinimumViableProposition.md # Staged deployment strategy framework
├── FAQ.md                     # User-facing project information
├── ChargingModels.md          # Usage metering and billing architecture
├── LegalLiability.md          # Legal framework and user responsibilities
├── BusinessDevelopment.md     # Market positioning and growth strategy
├── OutlineOfManagementImpacts.md # Executive decision framework
├── OurMCPdifferentiators.md   # Competitive differentiation analysis
├── OurStory.md               # Project narrative and development journey
```

## **Multi-Server MCP Architecture**

### **🏗️ MCP Servers Directory**
```
mcp-servers/
├── fca-compliance/           # FCA Handbook compliance server (PRODUCTION)
└── [future standards]/      # MiFID, SEC, Basel servers (PLANNED)
```

**Purpose**: AI Agent Oriented multi-server architecture where each regulatory standard receives its own dedicated MCP server for optimal semantic matching and tool discovery.

### **📋 FCA Compliance Server Structure**
```
mcp-servers/fca-compliance/
├── Dockerfile                # Container deployment configuration
├── LICENSE                   # Open source license
├── README.md                 # MCP server documentation
├── index.py                  # MCP server entry point
├── package.json              # Node.js compatibility metadata
├── poetry.lock               # Locked Python dependencies
├── pyproject.toml            # Python project configuration
│
├── src/mcp_server_fca_compliance/
│   ├── __init__.py           # Python package initialization
│   ├── server.py             # Main MCP server implementation (202KB)
│   ├── llm_provider.py       # LLM abstraction layer
│   └── config.py             # Configuration management system
│
├── docs/
│   └── std_FCAHandbook_Status.md  # FCA Handbook ingestion status
│
├── tests/                    # Comprehensive test suite (90%+ coverage goal)
│   ├── test_analyzer_only.py        # ComplianceAnalyzer unit tests
│   ├── test_audit_report.py         # Audit report generation tests
│   ├── test_database_validation.py  # Database connection tests
│   ├── test_full_tool.py            # End-to-end tool tests
│   ├── test_map_relationships.py    # Relationship mapping tests
│   ├── test_requirements_tool.py    # Requirements extraction tests
│   ├── test_similarity_function.py  # Vector similarity tests
│   ├── test_status_ingestion.py     # Ingestion status tests
│   ├── test_suggest_remediation.py  # Remediation suggestion tests
│   ├── test_systematic_analysis.py  # Systematic analysis tests
│   └── test_validate_ground_truth.py # Ground truth validation tests
│
└── tools/                    # Development and maintenance tools
    ├── check_database.py              # Database connectivity checker
    ├── create_similarity_function.sql # PGVector similarity function
    ├── fca_ingestion.py               # FCA Handbook data ingestion
    └── fca_structure_tracker.py       # Document structure analysis
```

## **MCP Ecosystem Integration**

### **🌐 Ecosystem Submission Directory**
```
mcp-ecosystem-submission/     # Fork of modelcontextprotocol/servers
├── README.md                 # MCP ecosystem documentation (includes our FCA entry)
├── src/                      # Official MCP servers collection
│   ├── everything/          # Standard MCP servers
│   ├── fetch/               # Standard MCP servers
│   ├── filesystem/          # Standard MCP servers
│   ├── git/                 # Standard MCP servers
│   ├── memory/              # Standard MCP servers
│   ├── sequentialthinking/  # Standard MCP servers
│   └── time/                # Standard MCP servers
└── [ecosystem files]        # PR submission components
```

**Purpose**: Fork of Anthropic's modelcontextprotocol/servers repository used for submitting FCA Compliance to the MCP ecosystem. Our FCA server entry is added to the main README.md, with the actual server code remaining in our separate repository at `mcp-servers/fca-compliance/`.

## **Development Infrastructure**

### **📊 Data and Knowledge Management**
```
data/
├── knowledge_base/
│   ├── README.md
│   └── sample_fca_data.json  # Sample regulatory data structures
```

### **🔧 Development Tools**
```
├── backup.sh                # Repository backup automation
├── check-github-log.sh      # Git log analysis tool
├── poetry.lock              # Project-wide dependency lock
├── pyproject.toml           # Project-wide Python configuration
├── index.html               # Project web interface (if applicable)
```

### **🧪 Testing Infrastructure**
```
tests/                       # Project-wide integration tests
├── __init__.py
├── test_compliance.py       # Cross-server compliance tests
└── test_server.py          # Multi-server integration tests
```

## **Internal Documentation and Management**

### **📋 Internal Strategy Documents**
```
internal/
├── Brand.md                 # Brand positioning and messaging
├── BrandEvaluationReport.md # Brand assessment and recommendations
├── Funding.md               # Investment and funding strategy
├── MDqualityCheck.md        # Document quality assurance methodology
├── MgmtImpactRules.md      # Management impact assessment rules
├── OurStoryLog.md          # Development progress log
├── esbpAnthropic.md        # Anthropic engagement strategy
├── esbpFCAsandbox.md       # FCA regulatory sandbox strategy
├── todos.md                # Internal task tracking
└── FolderOrganization.md   # This document
```

**Purpose**: Internal strategic documents, development logs, and management frameworks not included in public documentation.

## **Architectural Design Principles**

### **🎯 AI Agent Oriented Design**
- **Semantic Anchoring**: Each MCP server name includes regulatory context (`mcp-server-fca-compliance`)
- **Tool Prefixing**: All tools include standard context (`FCA_quickly_check_compliance`)
- **Multi-Server Architecture**: Separate servers optimize AI agent tool discovery

### **🔄 Systematic Expansion Pattern**
- **Template Structure**: FCA server serves as proven template for new standards
- **Consistent Naming**: `mcp-servers/[standard]-compliance/` pattern
- **Database Isolation**: Table prefixes (`fca_`, `mifid_`, `sec_`) with shared infrastructure
- **Documentation Standards**: Each server includes comprehensive docs and tests

### **📦 Package Architecture**
- **Python Packages**: Underscore naming (`mcp_server_fca_compliance`)
- **MCP Server Names**: Hyphen naming (`mcp-server-fca-compliance`)
- **Container Ready**: All servers include Dockerfile for cloud deployment
- **Dependency Management**: Poetry for reproducible Python environments

## **Development Workflow Integration**

### **🚀 Deployment Architecture**
- **Local Development**: Poetry virtual environments in each server directory
- **Container Deployment**: Dockerized servers for Azure/cloud deployment
- **Ecosystem Integration**: Automated submission to MCP official integrations
- **Quality Assurance**: Comprehensive test suites before production deployment

### **📈 Expansion Methodology**
Following `StandardImplementMCP.md` methodology:

1. **Phase 1**: Structure analysis and feasibility assessment
2. **Phase 2**: MCP server creation using FCA template
3. **Phase 3**: Database table creation with standard-specific prefixes
4. **Phase 4**: Validation and deployment with quality assurance testing

### **🔍 Monitoring and Maintenance**
- **Status Documentation**: Each server maintains ingestion status documents
- **Database Tools**: Connectivity checkers and data validation utilities
- **Performance Testing**: Load testing and accuracy benchmarking frameworks
- **Analytics Integration**: Interaction logging and usage tracking infrastructure

## **Strategic Alignment**

This folder organization directly supports:

- **Universal Standards Engine**: Rapid ingestion of new regulatory frameworks
- **AI Agent Native Design**: Semantic anchoring and tool discovery optimization  
- **Enterprise Deployment**: Professional structure suitable for corporate evaluation
- **Open Source Transparency**: Clear organization for public inspection and contribution
- **Systematic Quality**: Consistent structure enabling systematic expansion and maintenance

The architecture balances comprehensive functionality with systematic organization, enabling both current FCA Handbook operations and future expansion to MiFID II, SEC Rules, Basel III, and other regulatory frameworks.

---

## About This Document

**Author**: Blake Dempster, Founder, CEO, Principal Architect  
**Co-Authored by**: Claude Code (claude.ai/code)  
**Created**: 22 July 2025  
**Last Updated**: 22 July 2025  
**Purpose**: Comprehensive folder organization guide for Universal_FSCompliance_MCP Project development, maintenance, and strategic expansion.

---