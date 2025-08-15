# Technology Stack

## Core Technologies

## Backend Framework

- Python 3.11+: Primary development language with modern async capabilities
- FastAPI: Web framework optimized for API development and MCP protocol implementation
- Pydantic v2: Data validation and serialization for regulatory content
- Poetry: Dependency management and packaging for multi-server architecture

## AI/ML Stack

- Two-Layer Semantic Matching: Semantic anchors + vector similarity search
- OpenAI Embeddings: text-embedding-3-small for vector generation
- Multiple LLM Support: Configurable default provider, enterprise-flexible alternatives
- Semantic Anchoring: Context optimization for AI agents in analysing Standards

## Database and Storage

- Supabase: PostgreSQL with PGVector extension for unified vector and relational data
- Table Prefix Architecture: Standard-specific tables (`fca_documents`, `mifid_documents`) with shared infrastructure
- Ground Truth Integration: Designed for future regulatory Q&A datasets
- Real-time Capabilities: Live updates for regulatory change monitoring

## Protocol and Integration

- MCP (Model Context Protocol): Primary integration protocol for AI agent communication
- JSON-RPC 2.0: Standard communication protocol with WebSocket support
- OAuth 2.1: Authentication and authorization for enterprise deployments
- Container Orchestration: Docker/Kubernetes for multi-server deployment

## Enterprise Self-Hosting

The MCP servers are designed for enterprise self-hosting, and accommodate:

**On-Premise Deployment**:
- Deploy within your secure enterprise perimeter
- Complete data sovereignty and regulatory compliance control
- No external dependencies or third-party cloud risks
- Full integration with existing enterprise security policies
- Regulatory data never leaves your infrastructure

**Container-Based Architecture**:
Docker/Kubernetes deployment provides:
- Standardized deployment across enterprise environments
- Seamless scaling within existing infrastructure
- Integration with enterprise container orchestration platforms
- Consistent, repeatable deployment process

**Enterprise IT Requirements**:
- Standard enterprise containerization capabilities
- Kubernetes or Docker Swarm orchestration
- Enterprise-grade networking and security controls
- Integration with existing authentication systems (OAuth 2.1, LDAP, Active Directory)

## Infrastructure Requirements

Development Environment:
- CPU: 4+ cores (8+ recommended for multi-server testing)
- Memory: 16GB RAM minimum, 32GB recommended
- Storage: 50GB+ for development environment with multiple standards
- Network: Stable internet for OpenAI API and Supabase connections

Production Infrastructure (Azure):
- Compute: Azure Container Instances or AKS with auto-scaling
- Database: Managed PostgreSQL with PGVector extension support
- Storage: Azure Blob Storage for regulatory document staging
- Networking: Azure Load Balancer with SSL termination
- Monitoring: Azure Monitor + Application Insights integration

## Enterprise Security Features

Multi-Tenant Security:
- Standard-Specific Access Control: Users can be granted access to specific regulatory standards
- Row-Level Security: Ground truth data filtered by organization ownership
- API Key Management: Separate keys per MCP server with scope limitations
- Audit Trails: Complete compliance decision tracking per standard

Data Protection:
- TLS Encryption: All API communications encrypted in transit
- Database Encryption: Supabase encryption at rest and in transit
- Vector Data Security: Embeddings treated as sensitive regulatory intelligence
- Privacy Controls: Configurable data retention per standard and organization

General Compliance Framework Integration:
- SOC 2 Infrastructure: Supabase provides enterprise-grade security compliance
- GDPR Support: Data anonymization and right-to-be-forgotten capabilities
- Financial Services Standards: Enterprise security controls suitable for regulated industries
- Penetration Testing: Regular security assessments across all MCP servers

## Performance Specifications

### Performance Targets by Standard

Response Time Goals:
- Quick Compliance Check: <5 seconds response time
- Complex Analysis: <30 seconds for comprehensive compliance analysis  
- Document Analysis: <60 seconds for full document compliance assessment
- Ground Truth Validation: <10 seconds for accuracy benchmarking

Scalability Targets:
- Concurrent Users: 50+ simultaneous connections per MCP server
- Query Throughput: 1000+ queries per hour across all standards
- Multi-Standard Support: Independent scaling per regulatory framework
- Database Performance: Sub-second vector similarity searches

Accuracy and Quality Goals:
- Initial Accuracy: 75%+ for new Standard implementations
- Production Accuracy: 85%+ target for production deployment
- Long-term Accuracy: 95%+ goal validated through Ground Truth benchmarking

### Monitoring and Observability

Multi-Server Monitoring:
- Per-Standard Metrics: Query volume, accuracy, response time by regulatory framework
- Cross-Standard Analysis: Usage patterns and performance comparison
- Database Performance: Vector search performance and query optimization
- AI Agent Behavior: Tool selection patterns and semantic matching effectiveness

## MCP Protocol Implementation per Standard

Standard-Specific MCP Servers:
- Transport Methods: WebSocket, HTTP SSE, stdio, HTTP per server
- Tool Registration: Dynamic tool discovery with standard-specific naming
- Session Management: Stateful connections with compliance context preservation
- Error Handling: Graceful degradation with fallback to demonstration mode

## API Architecture

###  Management APIs (FastAPI-based):
- LLM Configuration: Runtime switching between LLM providers (Claude, OpenAI, etc.) per MCP server via REST endpoints
- Usage Analytics: Custom dashboards with Supabase analytics integration for real-time query volumes, response times, and accuracy metrics
- Billing Management: FastAPI-based cost tracking with configurable pricing models, usage allowances, and overage monitoring
- Access Control: User permissions, standard-specific access rights, and organization boundaries via OAuth 2.1
- System Administration: Health monitoring, server status, and configuration management through unified REST interface

### Cross-Standard Coordination:
- Standards Registry API: Discover available regulatory frameworks and implementation status
- User Access Management: Cross-standard permission verification and role assignments
- Unified Dashboard: Aggregated metrics and management across all MCP servers

## Migration and Upgrade Strategy

Migration Safety:
- Zero-Downtime Database Migration: Live table renaming with connection pooling
- Rollback Procedures: Complete rollback capability for each migration phase
- Data Validation: Integrity verification after each phase
- Performance Monitoring: Response time and accuracy validation post-migration

## About This Document

Author: Blake Dempster, Founder, CEO, Principal Architect  
15 August 2025  
