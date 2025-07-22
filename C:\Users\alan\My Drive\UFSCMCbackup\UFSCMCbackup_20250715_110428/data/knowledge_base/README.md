# Knowledge Base Directory

This directory contains the knowledge base data for the Universal_FSCompliance_MCP.

## Structure

- `fca_handbook/` - FCA Handbook regulatory documents
- `regulations/` - Other regulatory documents
- `indices/` - Vector indices and search data
- `cache/` - Cached analysis results

## Initial Setup

To initialize the knowledge base with FCA Handbook data:

1. Run the knowledge base initialization script:
   ```bash
   python3 -m fscompliance.scripts.init_knowledge_base
   ```

2. Or use the CLI:
   ```bash
   python3 -m fscompliance cli init-kb
   ```

## Data Sources

The knowledge base is designed to ingest:
- FCA Handbook sections
- Regulatory guidance documents
- Consultation papers
- Policy statements
- Rules and technical standards

## Privacy & Security

All data is processed locally and can be anonymized according to privacy settings in your `.env` file.