# Technical Architecture

## Executive Summary

For comprehensive project planning and resource allocation, see Planning.md. For LLM selection strategy and technical rationale, see LLMChoice.md.

**Technology Stack**: Python 3.11+, FastAPI, MCP Protocol, LightRAG, Supabase PostgreSQL
**Architecture Type**: Layered microservices with MCP integration
**Key Differentiator**: MCP-integrated Compliance platform enabling AI-agent native access

## System Architecture

### High-Level Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   AI Agents     │    │   FSCompliance   │    │   Knowledge     │
│  (MCP Clients)  │◄──►│   MCP Server     │◄──►│     Store       │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │                        │
                              ▼                        ▼
                       ┌──────────────┐         ┌─────────────┐
                       │ LLM Gateway  │         │  LightRAG   │
                       │(Claude 3.5)  │         │  Engine     │
                       └──────────────┘         └─────────────┘
```

### Architecture Layers

1. **MCP Server Layer**: Protocol-compliant JSON-RPC 2.0 server
2. **Knowledge Management Layer**: LightRAG-powered regulatory document processing
3. **Compliance Intelligence Layer**: see ComplianceTools.md
4. **Memory and Learning Layer**: Long-term memory with privacy controls
5. **LLM Abstraction Layer**: Multi-model support with Claude 3.5 Sonnet default

### Strategic Architecture Decisions

For comprehensive LLM selection rationale and multi-model strategy, see LLMChoice.md.

**Key Principles:**
- **Architectural Independence**: MCP server LLM operates independently from enterprise AI agent LLM choices
- **No Fine-Tuning**: Standard LLMs with advanced RAG architecture per LLMChoice.md decision
- **MCP-Native Design**: Built specifically for AI-agent interaction through Model Context Protocol
- **Self-Hostable**: Complete on-premises deployment capability

## Technology Stack

### Core Technologies

**Backend Framework:**
- **Python 3.11+**: Primary development language
- **FastAPI**: Web framework and API development
- **Pydantic v2**: Data validation and serialization
- **Poetry**: Dependency management and packaging

**AI/ML Stack:**
- **LightRAG**: Knowledge graph and retrieval system
- **Multiple LLM Support**: Claude 3.5 Sonnet (default), LLaMA 3, Mistral Medium
- **Vector Processing**: Advanced semantic search and similarity

**Database and Storage:**
- **Supabase**: PostgreSQL with PGVector extension (migration planned Q3 2025)
- **Real-time Capabilities**: Live updates and synchronized data
- **Vector Storage**: Optimized for regulatory document embeddings

**Protocol and Integration:**
- **MCP (Model Context Protocol)**: Primary integration protocol
- **JSON-RPC 2.0**: Standard communication protocol
- **OAuth 2.1**: Authentication and authorization
- **WebSocket/HTTP SSE**: Real-time communication support

### Development Tools

For detailed development guidelines and coding standards, see Rules.md.

**Quality Assurance:**
- **pytest**: Comprehensive testing framework
- **Black**: Code formatting
- **Ruff**: Fast Python linting
- **Pre-commit hooks**: Automated quality checks

## Infrastructure Requirements

### Development Environment

**Minimum Requirements:**
- **CPU**: 4+ cores for development, 8+ cores recommended
- **Memory**: 16GB RAM minimum, 32GB recommended
- **Storage**: 50GB+ for development environment
- **Network**: Stable internet for LLM API access

**Cloud Development:**
- **GitHub Codespaces**: Pre-configured development environment
- **Docker**: Containerized development and deployment
- **CI/CD**: GitHub Actions for automated testing and deployment

### Production Infrastructure

**Server Specifications:**
- **CPU**: 8+ cores for production workloads
- **Memory**: 32GB+ RAM for concurrent processing
- **Storage**: 200GB+ with backup capabilities
- **Network**: High-bandwidth for API communications

**Scalability Considerations:**
- **Horizontal Scaling**: Load balancing across multiple instances
- **Database Scaling**: PostgreSQL read replicas and connection pooling
- **Caching**: Redis for performance optimization
- **Monitoring**: Comprehensive logging and performance metrics

## Security Architecture

### Enterprise Security Features

**Authentication and Authorization:**
- **OAuth 2.1**: Industry-standard authentication
- **Role-Based Access Control**: Granular permission management
- **API Key Management**: Secure service-to-service authentication
- **Session Management**: Secure token handling and refresh

**Data Protection:**
- **TLS Encryption**: All communications encrypted in transit
- **Data Anonymization**: Automatic PII detection and masking
- **Audit Logging**: Complete compliance decision tracking
- **Privacy Controls**: User-configurable memory and data retention

**Security Compliance:**
- **OWASP Standards**: Security best practices implementation
- **Input Validation**: Comprehensive data validation using Pydantic
- **Penetration Testing**: Regular security assessments
- **Vulnerability Management**: Automated security scanning

### Privacy and Compliance

**Data Governance:**
- **Local Processing**: On-premises deployment options
- **Data Residency**: Configurable data storage locations
- **GDPR Compliance**: Privacy-by-design architecture
- **Financial Services Standards**: Enterprise-grade security controls

## Deployment Architecture

### Deployment Options

**Self-Hosted Deployment:**
- **Docker Containers**: Portable deployment packages
- **Kubernetes**: Orchestrated production deployment
- **Helm Charts**: Simplified Kubernetes deployment
- **Infrastructure as Code**: Automated provisioning

**Cloud Deployment:**
- **Multi-Cloud Support**: Azure, AWS, GCP compatibility
- **Managed Services**: Database and infrastructure automation
- **Auto-Scaling**: Dynamic resource allocation
- **Disaster Recovery**: Multi-region backup and failover

### Configuration Management

**Environment Configuration:**
```bash
# LLM Configuration
FSCOMPLIANCE_DEFAULT_LLM=claude-3.5-sonnet
FSCOMPLIANCE_ENABLE_MULTI_MODEL=true

# Database Configuration
FSCOMPLIANCE_DB_URL=postgresql://user:pass@localhost/fscompliance
FSCOMPLIANCE_VECTOR_STORE=pgvector

# Privacy Settings
FSCOMPLIANCE_MEMORY_ENABLED=true
FSCOMPLIANCE_ANONYMIZE_DATA=true
FSCOMPLIANCE_AUDIT_LOGGING=true

# MCP Server Settings
FSCOMPLIANCE_MCP_PORT=8000
FSCOMPLIANCE_MCP_HOST=localhost
```

## Integration Specifications

### MCP Protocol Implementation

**Supported Transport Methods:**
- **WebSocket**: Real-time bidirectional communication
- **HTTP SSE**: Server-sent events for streaming
- **stdio**: Direct process communication
- **HTTP**: Standard REST API compatibility

**Tool Integration:**
For comprehensive MCP tool specifications and implementation roadmap, see ComplianceTools.md.

**Core MCP Tools (Phase 2 Complete):**
- `analyze_compliance`: Policy analysis and gap detection
- `extract_requirements`: Regulatory requirement extraction
- `detect_gaps`: Compliance gap identification

### API Specifications

**RESTful API:**
- **OpenAPI 3.0**: Comprehensive API documentation
- **JSON Schema**: Structured data validation
- **Rate Limiting**: API usage controls
- **Versioning**: Backward compatibility management

**Integration Patterns:**
- **AI Agent Integration**: Direct MCP protocol communication
- **Enterprise System Integration**: Standard API and webhook support
- **Third-Party Integrations**: Configurable connector framework

## Performance Specifications

### Performance Targets

**Response Time:**
- **Standard Queries**: <2 seconds response time
- **Complex Analysis**: <10 seconds for comprehensive reports
- **Concurrent Users**: 50+ simultaneous connections
- **Throughput**: 1000+ queries per hour

**Reliability:**
- **Uptime Target**: 99.9% availability
- **Error Rate**: <0.1% system errors
- **Recovery Time**: <5 minutes for system restart
- **Data Integrity**: 100% compliance decision accuracy

### Monitoring and Observability

**System Monitoring:**
- **Performance Metrics**: Response time, throughput, error rates
- **Resource Monitoring**: CPU, memory, storage utilization
- **Application Metrics**: Business logic performance tracking
- **User Experience**: End-to-end transaction monitoring

**Logging and Audit:**
- **Structured Logging**: JSON-formatted log entries
- **Audit Trails**: Complete compliance decision tracking
- **Security Logs**: Authentication and authorization events
- **Performance Logs**: System performance and optimization data

## Data Architecture

### Data Models

**Core Data Structures:**

```python
class ConductRequirement(BaseModel):
    id: str
    source: str  # e.g., "FCA_HANDBOOK"
    section: str  # e.g., "SYSC.4.1.1"
    title: str
    content: str
    requirement_type: RequirementType
    applicability: List[str]
    severity: SeverityLevel
    last_updated: datetime
    related_requirements: List[str]

class ComplianceQuery(BaseModel):
    query_id: str
    user_role: UserRole
    query_type: QueryType
    content: str
    context: Optional[Dict[str, Any]]
    privacy_mode: bool
    timestamp: datetime

class ComplianceResponse(BaseModel):
    query_id: str
    requirements: List[ConductRequirement]
    compliance_status: ComplianceStatus
    gaps_identified: List[ComplianceGap]
    recommendations: List[str]
    confidence_score: float
    sources: List[str]
```

### Knowledge Management

**Document Processing:**
- **FCA Handbook Ingestion**: Automated regulatory document processing
- **Entity Extraction**: Regulatory relationship identification
- **Graph Construction**: Knowledge relationship mapping
- **Vector Embeddings**: Semantic search optimization

**Knowledge Updates:**
For systematic regulatory update processes, see UpdateCheck.md.

**Update Management:**
- **Real-time Updates**: Live regulatory change detection
- **Version Control**: Document change tracking
- **Impact Analysis**: Change impact assessment
- **Automated Testing**: Update validation and verification

## Development and Testing

### Development Environment Setup

**Quick Start:**
```bash
# Clone repository
git clone https://github.com/99blakeD99/fscompliance.git
cd fscompliance

# Install dependencies
poetry install

# Start development server
poetry run python -m fscompliance.server
```

**Development Tools:**
```bash
# Run tests
poetry run pytest

# Format code
poetry run black .

# Lint code
poetry run ruff check .

# Type checking
poetry run mypy .
```

### Testing Strategy

For detailed testing plans and quality standards, see Planning.md Quality Management section.

**Testing Levels:**
- **Unit Tests**: Individual component testing
- **Integration Tests**: System component interaction testing
- **End-to-End Tests**: Complete workflow validation
- **Performance Tests**: Load and stress testing
- **Security Tests**: Vulnerability and penetration testing
- **Ground Truth Validation**: Enterprise-provided real compliance scenarios for accuracy benchmarking

**Quality Targets:**
- **Test Coverage**: 90%+ code coverage
- **Response Time**: <2 second standard query response
- **Accuracy**: 95%+ compliance analysis accuracy (validated through Ground Truth benchmarking)
- **Uptime**: 99.9% system availability

## Migration and Upgrade Strategy

### Database Migration Strategy

For comprehensive database architecture and migration planning, see DatabaseStrategy.md.

**Migration Phases:**
- **Phase 1**: Current development database
- **Phase 2**: Supabase PostgreSQL migration (Q3 2025)
- **Phase 3**: Production optimization and scaling

**Data Migration:**
- **Zero-Downtime Migration**: Live data transfer
- **Rollback Procedures**: Safe migration rollback
- **Data Validation**: Integrity verification
- **Performance Testing**: Post-migration optimization

---

## About This Document

**Author**: Blake Dempster, Founder, CEO, Principal Architect  
**Co-Authored by**: Claude Code (claude.ai/code)  
**Created**: 9 July 2025  
**Last Updated**: 14 July 2025  
**Date last reviewed formally by MDqualityCheck.md**: 14 July 2025  
**Status**: (okay)  
**Purpose**: Comprehensive technical architecture guide for enterprise evaluation, deployment planning, and development implementation of the Universal_FSCompliance_MCP Project.

*This document serves as the authoritative technical reference for IT departments, purchasing teams, and development organizations evaluating or implementing the Universal_FSCompliance_MCP Project.*

---