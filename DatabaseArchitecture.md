# Database Architecture

## Executive Summary

A database is required to hold Standards, and for usage statistics. 

Database architecture is designed to optimize AI Agent discovery and interaction. Foundationally, it achieves this with Standard-specific semantic boundaries.

A single database with Standard-specific table prefixes has been adopted, facilitating:

- Simplified infrastructure management

- Semantic clarity

- Tool isolation (each Standard-specific MCP server queries only its relevant data sets)

- Discoverability (database structure that reinforces the semantic anchoring principle)

- Efficient querying, with two-layer semantic matching

## Core Structure

Rather than creating separate databases for each Standard, a unified database has been set up with Standard-specific table prefixes:

### Standard-Specific Tables, Examples

- FCA Tables: `fca_documents`, `fca_ground_truth`, `fca_ingestion_status`

- SEC Tables: `sec_documents`, `sec_ground_truth`, `sec_ingestion_status`

### Shared Infrastructure Tables, Examples

- `Standards_registry`: Catalog of implemented Standards and their status

- `system_config`: Global configuration parameters

- `user_access_control`: Cross-Standard user permissions and access policies

## Allowances for Special Factors of Standards

Each Standard-specific document table supports 2-layer semantic matching architecture with fields for Heading ID, Title, vector embedding, and ingestion level, and the Pareto issues set out in [SpecialFactors.md](SpecialFactors.md). 

Ground truth tables capture enterprise validation data with questions, answers, regulatory references, confidence levels, and organization ownership controls. 

For each Standard, ingestion status tables capture word counts, chunk counts, and coverage levels.

### Ground Truth Integration

A natural pattern is thus implemented for Standard-specific ground truth tables, with appropriate access controls per User requirements. Supports both public ground truth (industry consensus) and private ground truth (organization-specific Q&A).

## Implementation Considerations

### Query Isolation Strategy

Each MCP server connects to the same database but queries only its prefixed tables, maintaining logical separation.

### Standards_registry Table

The standards_registry table maintains metadata about each implemented Standard including Standard tag, name, MCP server name, associated database tables, ingestion status, and last updated timestamps.

### Access Control and Security

User permissions can be managed at the table level, enabling fine-grained access to specific Standards or ground truth datasets. Row-level security policies can be applied per Standard.

## Future Standards Integration

### Template Approach for New Standards

When implementing new regulatory Standards, the database structure follows a consistent pattern:

1. Create Standard-specific tables following naming convention
2. Update Standards_registry with new Standard metadata
3. Implement Standard-specific ground truth tables if available
4. Configure access controls appropriate to regulatory requirements

### Cross-Standard Analysis Capabilities

While AI agents operate within Standard-specific boundaries, the unified database enables cross-Standard analysis for advanced use cases:

Cross-Standard analysis capabilities enable regulatory overlap analysis by comparing embeddings between different Standards, identifying high similarity regulatory concepts across frameworks like FCA and SEC.

## Operational Analytics and Management Information

### Interaction Analytics 

Interaction analytics tables capture interaction data per Standard including user and organizational context, tool usage patterns, billing alignment fields, regulatory navigation patterns, response characteristics, and temporal context. 

Cross-Standard analytics views provide strategic insights by aggregating usage patterns, confidence metrics, processing times, and boundary message frequencies across regulatory Standards.

### Dashboard Integration

Interaction analytics enables multiple visualization and analytics platforms:

- Native Dashboard: Built-in analytics with real-time capabilities

- Enterprise BI Integration: Power BI, Tableau, Grafana connectivity


- Custom Analytics Applications: Direct database access for specialized insights

- API-Driven Dashboards: RESTful analytics endpoints for third-party integration


### Multi-Stakeholder Value Generation

Interaction Analytics are useful for multiple purposes:

#### Operational Management Intelligence

- Individual user compliance query patterns and professional development needs

- Department-level tool usage for resource allocation and training priorities

#### Strategic Marketing and Thought Leadership

- Regulatory complexity insights for thought leadership content

- Compliance pain point identification for solution development

- RegTech effectiveness measurement for industry presentations

#### Regulatory Intelligence for Standards Bodies

- Real-world compliance query patterns revealing regulatory interpretation challenges

- Identification of most-consulted regulations for policy effectiveness assessment

- Emerging compliance themes for proactive guidance development

- Regulatory complexity measurement through boundary message frequency

#### Academic Research Dataset

- Anonymized compliance interaction patterns across financial services sectors

- AI adoption patterns in regulated industries with performance benchmarking

## Data Privacy and Access Control

### Multi-Tenant Security Architecture

Row-level security policies ensure user-specific and organization-specific data access controls for usage analytics, preventing unauthorized access to interaction data while maintaining appropriate visibility for organizational analytics.

### Data Retention and Compliance Framework

- Data Minimization: Collect only necessary analytics data with clear business justification

- Retention Periods: 7 years for compliance audit trails (Standard financial services requirement), 3 years for operational analytics, 1 year for research datasets

- Right to Erasure: Automated deletion capabilities for user data upon request

- Data Subject Rights: Export, rectification, and deletion processes for individual users

- Lawful Basis: Legitimate interest for compliance analytics, consent for research participation

Enterprise Data Governance:

- Data Classification: Personal data (GDPR), business confidential, aggregated analytics, public research

- Geographic Restrictions: EU data residency compliance through regional deployment

- Cross-Border Transfers: Standard Contractual Clauses (SCCs) for international analytics sharing
  
- Regulatory Reporting: Automated compliance reporting for data processing activities

#### Anonymization for Research and Public Insights

- Personal Identifiers: Removed for academic and regulatory analysis

- Organizational Context: Categorized (size, business model) without identification

- Query Content: Aggregated patterns without specific text for public insights

- Geographic Clustering: Regional patterns without institution-specific data

- k-Anonymity: Minimum group sizes (k≥5) for all published research datasets

## Further Details

The following information is available but out of scope of this document:

### Technology Stack & Dependencies

  - Database Platform
  - Vector Database embeddings
  - Backup & Recovery
  - Third-party Dependencies

### Operational Requirements

  - Performance Specifications, SLA metrics, concurrent user limits, query response times
  - Scalability Planning for growth in Standards and users
  - Disaster Recovery, business continuity and failover procedures
  - Monitoring & Alerting, database health, performance metrics, capacity planning

### Security & Compliance

  - Encryption: Data at rest and in transit protection
  - Access Controls, Authentication methods, SSO integration
  - Network Security, VPC, firewall requirements, API security

### Cost & Resource Management

  - Infrastructure Costs, database hosting, storage, compute estimates
  - Maintenance Windows, planned downtime for updates/patches
  - Resource Requirements, GPU, CPU, memory, storage 

### Integration & Migration

  - Data Migration Strategy: How to onboard existing compliance data
  - Integration Points: APIs, ETL processes, enterprise system connectivity
  - Deployment Architecture: Production, staging, development environments

## About This Document

Author: Blake Dempster, Founder, CEO, Principal Architect  
Last Updated: 12 August 2025  
Date last reviewed formally by MDqualityCheck.md: 12 August 2025  
