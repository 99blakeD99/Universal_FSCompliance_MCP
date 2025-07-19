# Technical Architecture

## Executive Summary

For comprehensive project planning and resource allocation, see Planning.md. For LLM selection strategy and technical rationale, see LLMChoice.md. For database architecture details, see DatabaseStrategy.md.

**Technology Stack**: Python 3.11+, FastAPI, MCP Protocol, Supabase PostgreSQL with PGVector, OpenAI Embeddings
**Architecture Type**: AI Agent Oriented multi-server architecture with standard-specific MCP servers  
**Key Differentiator**: First MCP-integrated compliance platform with semantic anchoring for AI agent discovery

## System Architecture

### AI Agent Oriented Multi-Server Architecture

The Universal Standards Engine implements multiple standard-specific MCP servers to optimize AI agent tool discovery and semantic matching:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────────┐
│   AI Agents     │    │ FCA_Compliance   │    │    Database         │
│  (MCP Clients)  │◄──►│   MCP Server     │◄──►│  (fca_ tables)      │
└─────────────────┘    └──────────────────┘    └─────────────────────┘
                              │                        │
                       ┌──────────────────┐            │
                       │ MiFID_Compliance │            │
                       │   MCP Server     │◄───────────┤
                       └──────────────────┘            │
                              │                        │
                       ┌──────────────────┐            │
                       │  SEC_Compliance  │            │
                       │   MCP Server     │◄───────────┤
                       └──────────────────┘            │
                              │                        │
                              ▼                        ▼
                       ┌──────────────┐         ┌─────────────┐
                       │ LLM Gateway  │         │  Two-Layer  │
                       │(Claude 3.5)  │         │  Semantic   │
                       └──────────────┘         │  Matching   │
                                               └─────────────┘
```

### Architecture Principles

**AI Agent Oriented Design**: Each regulatory standard receives a dedicated MCP server with semantic anchors that match AI agent query patterns (e.g., "Does this comply with **FCA** requirements?" → `FCA_Compliance_MCP`)

**Standard-by-Standard Expansion**: Universal in potential, implemented standard-by-standard following systematic methodology outlined in StandardImplementMCP.md

**Semantic Clarity**: Tool names include regulatory context (`FCA_quickly_check_compliance`) to optimize AI agent tool selection algorithms

**Database Isolation with Infrastructure Unity**: Single database with standard-specific table prefixes maintains data boundaries while simplifying infrastructure management

### Architecture Layers

1. **MCP Server Layer**: Standard-specific protocol-compliant JSON-RPC 2.0 servers
2. **Two-Layer Semantic Matching**: Semantic anchors + vector similarity search optimized for structured regulatory content
3. **Compliance Intelligence Layer**: 7 focused tools for daily compliance officer work
4. **Database Abstraction Layer**: Standard-specific data access with unified infrastructure
5. **LLM Integration Layer**: Multi-model support with Claude 3.5 Sonnet default (see LLMChoice.md)

### Strategic Architecture Decisions

**AI Agent Focused**: Architecture optimized for AI agent discovery and interaction rather than human-friendly interfaces

**Multiple MCP Servers**: Separate servers per standard provide semantic clarity and prevent "straitjacket" constraints while maintaining systematic implementation methodology

**No Graph Database**: Structured regulatory standards are sufficiently served by vectorization and two-layer semantic matching

**Database Table Prefixes**: Single database with `fca_`, `mifid_`, `sec_` table prefixes balances isolation with operational efficiency (see DatabaseStrategy.md)

**Azure-First Deployment**: Prioritized cloud deployment on Azure with containerized architecture for enterprise adoption

## Technology Stack

### Core Technologies

**Backend Framework:**
- **Python 3.11+**: Primary development language with modern async capabilities
- **FastAPI**: Web framework optimized for API development and MCP protocol implementation
- **Pydantic v2**: Data validation and serialization for regulatory content
- **Poetry**: Dependency management and packaging for multi-server architecture

**AI/ML Stack:**
- **Two-Layer Semantic Matching**: Semantic anchors + vector similarity search
- **OpenAI Embeddings**: text-embedding-3-small for vector generation
- **Multiple LLM Support**: Claude 3.5 Sonnet (default), configurable alternatives
- **Semantic Anchoring**: Regulatory context optimization for AI agents

**Database and Storage:**
- **Supabase**: PostgreSQL with PGVector extension for unified vector and relational data
- **Table Prefix Architecture**: Standard-specific tables (`fca_documents`, `mifid_documents`) with shared infrastructure
- **Ground Truth Integration**: Designed for future regulatory Q&A datasets
- **Real-time Capabilities**: Live updates for regulatory change monitoring

**Protocol and Integration:**
- **MCP (Model Context Protocol)**: Primary integration protocol for AI agent communication
- **JSON-RPC 2.0**: Standard communication protocol with WebSocket support
- **OAuth 2.1**: Authentication and authorization for enterprise deployments
- **Container Orchestration**: Docker/Kubernetes for multi-server deployment

### MCP Tool Architecture

**Core Compliance Tools (7 Tools per Standard):**

Each standard-specific MCP server implements these tools with appropriate prefixing:

1. **`[STANDARD]_quickly_check_compliance`**: Rapid policy assessment for concept validation
2. **`[STANDARD]_identify_compliance_requirements_in_specific_case`**: Context-specific regulatory requirement extraction
3. **`[STANDARD]_systematically_analyse_compliance_implications`**: Comprehensive strategic compliance analysis
4. **`[STANDARD]_suggest_remediation`**: Gap-specific remediation recommendations
5. **`[STANDARD]_prepare_draft_compliance_audit_report`**: Professional audit documentation preparation
6. **`[STANDARD]_validate_ground_truth`**: Enterprise-grade validation and benchmarking
7. **`[STANDARD]_status_of_standard_ingestion`**: System status and coverage visibility

**Example: FCA_Compliance_MCP Tools:**
- `FCA_quickly_check_compliance`
- `FCA_identify_compliance_requirements_in_specific_case`
- `FCA_systematically_analyse_compliance_implications`
- etc.

## Database Architecture

### Single Database with Standard-Specific Tables

For comprehensive database architecture details, see DatabaseStrategy.md.

**Table Structure:**
```sql
-- FCA Tables
fca_documents (id, section_reference, content, embedding, ingestion_level)
fca_ground_truth (id, question, answer, owner_organization)
fca_ingestion_status (section_reference, status, coverage_level)

-- MiFID Tables  
mifid_documents (id, section_reference, content, embedding, ingestion_level)
mifid_ground_truth (id, question, answer, owner_organization)
mifid_ingestion_status (section_reference, status, coverage_level)

-- Shared Infrastructure
standards_registry (standard_tag, standard_name, mcp_server_name)
user_access_control (user_id, standard_access, permissions)
```

### Two-Layer Semantic Matching Implementation

**Layer 1: Semantic Anchors**
- Map query context to regulatory sections (e.g., "client categorization" → COBS)
- Optimize query scope and improve performance

**Layer 2: Vector Similarity Search**
- Semantic search within identified regulatory sections
- OpenAI text-embedding-3-small embeddings with PGVector similarity operations

**Unified but Efficient Approach**:
- High-value content: Full ingestion (heading + content)
- Lower-value content: Heading-only ingestion with coverage boundary messaging

## Infrastructure and Deployment

### Azure-First Cloud Architecture

**Azure Container Instances (ACI) Deployment:**
```yaml
# Multi-container deployment
services:
  fca-compliance-mcp:
    image: universal-fscompliance/fca-compliance-mcp:latest
    ports: ["8001:8000"]
    environment:
      - STANDARD_TAG=FCA
      - DATABASE_URL=${SUPABASE_URL}
    
  mifid-compliance-mcp:
    image: universal-fscompliance/mifid-compliance-mcp:latest
    ports: ["8002:8000"] 
    environment:
      - STANDARD_TAG=MiFID
      - DATABASE_URL=${SUPABASE_URL}
```

**Azure Kubernetes Service (AKS) for Production:**
- **Multi-server orchestration** with service mesh for load balancing
- **Horizontal pod autoscaling** based on compliance query volume
- **Azure Database for PostgreSQL** with managed Supabase integration
- **Azure Key Vault** integration for secrets management

### Infrastructure Requirements

**Development Environment:**
- **CPU**: 4+ cores (8+ recommended for multi-server testing)
- **Memory**: 16GB RAM minimum, 32GB recommended
- **Storage**: 50GB+ for development environment with multiple standards
- **Network**: Stable internet for OpenAI API and Supabase connections

**Production Infrastructure (Azure):**
- **Compute**: Azure Container Instances or AKS with auto-scaling
- **Database**: Managed PostgreSQL with PGVector extension support
- **Storage**: Azure Blob Storage for regulatory document staging
- **Networking**: Azure Load Balancer with SSL termination
- **Monitoring**: Azure Monitor + Application Insights integration

## Security Architecture

### Enterprise Security Features

**Multi-Tenant Security:**
- **Standard-Specific Access Control**: Users can be granted access to specific regulatory standards
- **Row-Level Security**: Ground truth data filtered by organization ownership
- **API Key Management**: Separate keys per MCP server with scope limitations
- **Audit Trails**: Complete compliance decision tracking per standard

**Data Protection:**
- **TLS Encryption**: All API communications encrypted in transit
- **Database Encryption**: Supabase encryption at rest and in transit
- **Vector Data Security**: Embeddings treated as sensitive regulatory intelligence
- **Privacy Controls**: Configurable data retention per standard and organization

**Compliance Framework Integration:**
- **SOC 2 Infrastructure**: Supabase provides enterprise-grade security compliance
- **GDPR Support**: Data anonymization and right-to-be-forgotten capabilities
- **Financial Services Standards**: Enterprise security controls suitable for regulated industries
- **Penetration Testing**: Regular security assessments across all MCP servers

## Performance Specifications

### Performance Targets by Standard

**Response Time Goals:**
- **Quick Compliance Check**: <5 seconds response time
- **Complex Analysis**: <30 seconds for comprehensive compliance analysis  
- **Document Analysis**: <60 seconds for full document compliance assessment
- **Ground Truth Validation**: <10 seconds for accuracy benchmarking

**Scalability Targets:**
- **Concurrent Users**: 50+ simultaneous connections per MCP server
- **Query Throughput**: 1000+ queries per hour across all standards
- **Multi-Standard Support**: Independent scaling per regulatory framework
- **Database Performance**: Sub-second vector similarity searches

**Accuracy and Quality Goals:**
- **Initial Accuracy**: 75% for new standard implementations
- **Production Accuracy**: 85% target for production deployment
- **Long-term Accuracy**: 95% goal validated through Ground Truth benchmarking
- **Coverage Completeness**: Systematic ingestion tracking with status visibility

### Monitoring and Observability

**Multi-Server Monitoring:**
- **Per-Standard Metrics**: Query volume, accuracy, response time by regulatory framework
- **Cross-Standard Analysis**: Usage patterns and performance comparison
- **Database Performance**: Vector search performance and query optimization
- **AI Agent Behavior**: Tool selection patterns and semantic matching effectiveness

## Integration Specifications

### MCP Protocol Implementation per Standard

**Standard-Specific MCP Servers:**
- **Transport Methods**: WebSocket, HTTP SSE, stdio, HTTP per server
- **Tool Registration**: Dynamic tool discovery with standard-specific naming
- **Session Management**: Stateful connections with compliance context preservation
- **Error Handling**: Graceful degradation with fallback to demonstration mode

**AI Agent Integration Pattern:**
```python
# AI Agent discovers and connects to appropriate MCP server
if "FCA" in compliance_query:
    mcp_server = connect_to_mcp("FCA_Compliance_MCP")
    tools = ["FCA_quickly_check_compliance", "FCA_analyse_implications"]
elif "MiFID" in compliance_query:
    mcp_server = connect_to_mcp("MiFID_Compliance_MCP") 
    tools = ["MiFID_quickly_check_compliance", "MiFID_analyse_implications"]
```

### API Architecture

**RESTful API per Standard:**
```
# Standard-specific endpoints
GET  /fca/health              # FCA server health check
POST /fca/tools/quick-check   # FCA quick compliance check
POST /fca/tools/analyse       # FCA systematic analysis

GET  /mifid/health            # MiFID server health check  
POST /mifid/tools/quick-check # MiFID quick compliance check
```

**Cross-Standard Coordination:**
- **Standards Registry API**: Discover available regulatory frameworks
- **User Access Management**: Cross-standard permission verification
- **System Status API**: Health monitoring across all MCP servers

## Data Architecture

### Standard-Specific Data Models

**Core Data Structures per Standard:**

```python
class StandardDocument(BaseModel):
    id: str
    standard_tag: str  # "fca", "mifid", "sec"
    section_reference: str
    title: str
    content: str
    embedding: List[float]
    ingestion_level: Literal["full", "heading_only"]
    metadata: Dict[str, Any]
    created_at: datetime

class GroundTruthEntry(BaseModel):
    id: str
    standard_tag: str
    question: str
    answer: str
    regulatory_reference: str
    confidence_level: str
    owner_organization: Optional[str]
    public_access: bool
    created_at: datetime

class ComplianceQuery(BaseModel):
    query_id: str
    standard_tag: str
    user_id: str
    tool_name: str  # e.g., "FCA_quickly_check_compliance"
    content: str
    context: Optional[Dict[str, Any]]
    timestamp: datetime

class ComplianceResponse(BaseModel):
    query_id: str
    standard_tag: str
    tool_used: str
    requirements: List[str]
    compliance_status: ComplianceStatus
    gaps_identified: List[Dict[str, Any]]
    recommendations: List[str]
    confidence_score: float
    database_mode: bool  # True if using real regulatory data
```

### Knowledge Management by Standard

**Document Processing per Standard:**
- **Regulatory Document Ingestion**: Standard-specific processing following StandardImplementMCP.md methodology
- **Semantic Anchor Extraction**: Standard-specific heading hierarchies and semantic patterns
- **Vector Embedding Generation**: OpenAI text-embedding-3-small optimized for regulatory content
- **Two-Layer Index Construction**: Layer 1 (semantic anchors) + Layer 2 (vector similarity)

**Standard Implementation Pattern:**
1. **Structure Analysis**: Evaluate regulatory standard for hierarchical organization
2. **Pareto Analysis**: Identify high-value vs. low-value content areas
3. **Semantic Anchor Mapping**: Create standard-specific semantic anchor dictionary
4. **Unified Ingestion**: Full content for important sections, headings-only for comprehensive coverage
5. **Validation**: Test two-layer semantic matching with known compliance scenarios

## Development and Testing

### Multi-Server Development Environment

**Development Setup:**
```bash
# Clone and setup universal standards engine
git clone https://github.com/99blakeD99/universal-fscompliance-mcp.git
cd universal-fscompliance-mcp

# Install dependencies
poetry install

# Start FCA compliance server
poetry run python -m fca_compliance.server --port 8001

# Start MiFID compliance server (when implemented)
poetry run python -m mifid_compliance.server --port 8002
```

**Testing Strategy:**
```bash
# Test individual MCP servers
poetry run pytest tests/fca_compliance/
poetry run pytest tests/mifid_compliance/

# Integration testing across standards
poetry run pytest tests/integration/

# AI Agent simulation testing
poetry run pytest tests/ai_agent_behavior/
```

### Quality Standards per Standard

**Testing Coverage Goals:**
- **Core Compliance Logic**: 90%+ coverage per standard
- **Integration Components**: 75%+ coverage for cross-standard functionality
- **MCP Protocol Implementation**: 95%+ coverage for protocol compliance
- **AI Agent Simulation**: Comprehensive tool discovery and usage pattern testing

**Performance Testing:**
- **Load Testing**: Concurrent access across multiple MCP servers
- **Stress Testing**: High-volume query processing per standard
- **Accuracy Testing**: Ground truth validation when regulatory datasets available
- **Semantic Matching Testing**: Two-layer architecture effectiveness validation

## Migration and Upgrade Strategy

### Current System Evolution

**Phase 1: Database Migration (Immediate)**
- Rename existing tables to `fca_` prefix following DatabaseStrategy.md
- Validate existing two-layer semantic matching with new schema
- Update current FCA_Compliance_MCP to query prefixed tables

**Phase 2: Multi-Server Architecture (Q4 2025)**  
- Implement FCA_Compliance_MCP as standalone server
- Template creation for new standard MCP servers
- Azure deployment pipeline for multiple containers

**Phase 3: Standards Expansion (2025-2026)**
- MiFID_Compliance_MCP implementation following StandardImplementMCP.md
- SEC_Compliance_MCP for U.S. market expansion
- Basel_Compliance_MCP for banking supervision requirements

**Migration Safety:**
- **Zero-Downtime Database Migration**: Live table renaming with connection pooling
- **Rollback Procedures**: Complete rollback capability for each migration phase
- **Data Validation**: Integrity verification after each phase
- **Performance Monitoring**: Response time and accuracy validation post-migration

---

## About This Document

**Author**: Blake Dempster, Founder, CEO, Principal Architect  
**Co-Authored by**: Claude Code (claude.ai/code)  
**Created**: 9 July 2025  
**Last Updated**: 19 July 2025  
**Status**: Active - updated for AI Agent Oriented multi-server architecture  
**Purpose**: Comprehensive technical architecture guide for enterprise evaluation, deployment planning, and development implementation of the Universal Standards Engine with AI Agent Oriented design principles.

*This document serves as the authoritative technical reference for IT departments, purchasing teams, and development organizations evaluating or implementing the Universal Standards Engine's multi-server compliance intelligence platform.*

---