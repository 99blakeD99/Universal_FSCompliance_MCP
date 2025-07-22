# The Universal_FSCompliance_MCP Project Overview

## Project Overview

### Project and Product Terminology

The Universal_FSCompliance_MCP **Project** is the project to build The Universal_FSCompliance_MCP **Product**.

### The Universal_FSCompliance_MCP Product - Summary

The Product is an open-source MCP (Model Context Protocol) service designed for financial institutions and other financial enterprises ("Users") to enable them to manage Compliance with Identified Standards. 

### "Standard"

"Standard" is a reserved term for the Project. It refers to:

- **Regulatory frameworks** 
- **Industry codes**   
- **Statutory requirements** 
- **International standards** 
- **Jurisdictional regulations** 
- **Consultation documents**

### "Identified Standard"

The expression "Identified Standard" is also a reserved term. It is needed to protect Users from the impression that The Universal_FSCompliance_MCP Product can be used indiscriminately for Compliance with the requirements of a nebulous collection of poorly defined Standards. Only Identified Standards are covered.

### First Identified Standard

The FCA Handbook is planned to be our first Identified Standard, to provide useful functionality and also to serve as a proof of concept. 

### Subsequent Identified Standards

#### Architecture.

Using the AI techniques and architectures established and validated for our First Standard, other Standards will be addressed methodically, with momentum expected to be quickly established. Without AI, such momentum would have been unrealistic. With AI the momentum is expected.

#### List of Prospective Standards

First:

- FCA Handbook

Next (not in priority order, priorities will be set in order of User Demand):

- SEC rules
- MiFID II
- Basel III
- industry codes (conduct codes, best practice guidelines)
- statutory requirements (legislation, acts, laws)
- identified international standards (IFRS, SOX, ISO standards)
- jurisdictional regulations (state, provincial, national requirements)
- consultation documents (regulatory proposals, policy consultations, draft guidance).

### Strategic Context

Compliance with legal, regulatory, and industry requirements has become particularly challenging for Users. The environment is driven by the worldwide compulsive urge to regulate, combined with the real-life knotweed nature of resulting regulations. Arguably, Compliance is simply impossible without an AI-native application like The Universal_FSCompliance_MCP Product. 

The consequences of non-compliance can be severe - both in public reputation and legal liability. Prior to AI, this regulatory burden was becoming unmanageable, creating mounting friction, costs, and reduced agility for Users.

This is central to The Universal_FSCompliance_MCP Product's mission to **slice through red tape** and **make it easier to bring the right financial products safely to consumers**.

### Technical Overview

The Universal_FSCompliance_MCP Project has adopted the following principal technical underpinnings:

- Open-Source. To expose the insides of the coding to millions of pairs of eyeballs, including those of our Users, thus building trust.

- Publicly Available on GitHub. To maximise exposure. To provide full documentation in AI-friendly markdown format, with accessibility facilitated through signposting in README.md. The effect is to maximise ease of access for the AI-enabled discovery and appraisal tools used by Users and potential investors.

- AI-Native. Using AI from the ground up, not merely adding AI features. Includes the use of databases and RAG (Retrieval Augmented Generation) components designed for the AI context.

- MCP Protocol. Taking advantage of the MCP protocol, thus: Reducing User integration barriers; Implementing standardized AI tool interfaces that work with any User AI agent architecture; Facilitating the optimization of LLM for the MCP's specialist purpose (separately from the LLM chosen for other User purposes such as AI agents).


## Broad Project Scope

### Primary Objectives

- Create an "MCP" (formally a "Model Context Protocol (MCP) Server")  containing Tools to enable Users to Comply with Identified Standards.
  
- Create the flexibility to add more Tools as the need arises.
  
- Achieve full production deployment on the Cloud using Azure or one of its peers, ie no prior prototype versions.
- Maintain long-term memory for improved responses over time.
- Ensure LLM-open architecture to allow for User choice of LLM within the MCP.
- Choose a default LLM to be used by the MCP, and publish a clear explanation for the choice of default LLM.


### "Identified Standards" Focus

- So that Users can comply with requirements. 
  
### Target Users

- Executives working within enterprises, including:
- Compliance Officers
- Risk Officers
- Regulatory Auditors
- Professional Advisers 

#### Core Technology Stack

- Python
- Pydantic AI
- LightRAG
- GitHub
- LLM: Claude 3.5 Sonnet as default, with architecture supporting LLaMA 3, Falcon, Mistral Medium, and user-defined LLMs
- MCP Architecture: as set out by Anthropic
  
## Use Cases

Use Cases correspond to an initial set of Tools made available through the MCP. These Tools are set out in ComplianceTools.md.

## High-Level Technical Architecture

The high-level architecture is set out in TechnicalArchitecture.md

## Technical Implementation Plan

### Phase 1: Foundation
- MCP server framework setup
- Basic Pydantic models implementation
- FCA Handbook data ingestion pipeline
- LightRAG integration for document processing

### Phase 2: Core Intelligence
- Compliance requirement extraction and categorization
- Basic query processing and response generation
- LLM abstraction layer implementation
- Initial web interface for testing

### Phase 3: Advanced Features
- Long-term memory system with privacy controls
- Multi-user support and role-based access
- Advanced compliance analysis algorithms
- Performance optimization and caching

### Phase 4: Integration & Testing
- Microsoft Copilot Studio integration
- Comprehensive testing suite
- Documentation and deployment guides
- Community feedback integration

## Technology Stack

### Core Technologies
- **Python 3.11+**: Primary development language
- **Pydantic v2**: Data validation and serialization
- **LightRAG**: Knowledge retrieval and graph processing
- **FastAPI**: Web framework for MCP server
- **SQLite/PostgreSQL**: Data persistence
- **Docker**: Containerization and deployment

### AI/ML Components
- **Claude 3.5 Sonnet**: Default language model
- **Transformers**: Model loading and inference
- **Sentence Transformers**: Text embeddings
- **NetworkX**: Graph analysis and visualization

### Development Tools
- **GitHub**: Version control and collaboration
- **Poetry**: Dependency management
- **Pytest**: Testing framework
- **Black/Ruff**: Code formatting and linting
- **Pre-commit**: Code quality hooks

## Privacy and Security Considerations

### Privacy Controls
- **Opt-in Memory**: Users can enable/disable long-term memory
- **Data Anonymization**: Automatic PII detection and masking
- **Local Processing**: Option for on-premises deployment
- **Audit Logging**: Comprehensive access and query logging

### Security Measures
- **OAuth 2.1**: Secure authentication framework
- **TLS Encryption**: All communications encrypted
- **Role-based Access**: Granular permission system
- **Data Retention**: Configurable data retention policies

## Deployment Architecture

### Deployment Options
1. **Cloud SaaS**: Hosted service with subscription model
2. **On-Premises**: Enterprise deployment within organization
3. **Hybrid**: Sensitive data on-premises, processing in cloud
4. **Edge**: Lightweight deployment for specific use cases

### Scalability Considerations
- **Horizontal Scaling**: Load balancing across multiple instances
- **Database Sharding**: Regulatory data partitioning
- **Caching Strategy**: Redis for frequent queries
- **CDN Integration**: Static asset delivery optimization

## Success Metrics

### Technical Metrics
- **Query Response Time**: < 2 seconds for standard queries
- **Accuracy**: > 95% for compliance requirement identification
- **Availability**: 99.9% uptime for SaaS deployment
- **Scalability**: Support for 1000+ concurrent users

### Business Metrics
- **User Adoption**: to be set and monitored as experience develops
- **Query Volume**: to be set and monitored as experience develops
- **Community Engagement**: to be set and monitored as experience develops
- **Regulatory Coverage**: Expand beyond FCA Handbook to additional Identified Standards as soon as FCA Handbook settles.
  
## Risk Assessment

### Technical Risks
- **LLM Accuracy**: Risk of incorrect compliance advice
- **Performance**: Large document processing latency
- **Integration**: MCP specification compatibility challenges
- **Security**: Potential data breach or unauthorized access

### Mitigation Strategies
- **Human Review**: Automated flagging for human verification
- **Performance Testing**: Load testing and optimization
- **Standards Compliance**: Regular MCP specification updates
- **Security Audits**: Regular penetration testing and reviews

## Market Strategy & Competitive Positioning

Market Strategy will follow, based on the Vision and Mission, and the Identity, set out in README.md.

Competitive Positioning will emerge. Early research indicates that there is no AI-native competitor.

## Strategic Milestones

Strategic Milestones are represented by the Phases in Tasks.md.

---

## About This Document

**Author**: Blake Dempster, Founder, CEO, Principal Architect  
**Co-Authored by**: Claude Code (claude.ai/code)  
**Created**: 25 December 2024  
**Last Updated**: 9 July 2025  
**Date last reviewed formally by MDqualityCheck.md**: 9 July 2025  
**Status**: (do when ready, consider deleting)
**Purpose**: Strategic overview and foundational context for the Universal_FSCompliance_MCP Project platform development.

*This planning document serves as the foundation for the Universal_FSCompliance_MCP Project development. It will be updated as the project evolves and requirements are refined.*

---