# Quality Check Rules for MCP Project Documentation

This document establishes a systematic methodology for quality checking .md files to ensure consistency, formatting standards, and strategic alignment across the Universal_FSCompliance_MCP Project documentation.

## Review Sequence

When reviewing any .md file, follow this systematic approach:

### 1. Content Quality Check
- **Avoid repetition** - Don't repeat what has substantially been said before
- **Professional tone** - Avoid colloquialisms, avoid being bombastic, be succinct, adopt a tone suited to the corporate world, stay constructive and positive, don't be scary, don't be hyperbolic
- **No links** - Avoid links, either to our .mds or web links, except in README.md
- **Check README.md links** - ensure that all the links in README.md work.
- **Internal consistency** - Check the document's internal logic and consistency
- **Special for OurStory.md** - If reviewing OurStory.md, allow warmer narrative tone that
  may differ from standard corporate style. Also pay special attention to whether any "Voice" part substantively repeats a previous "Voice" part, this document is being drafted on the fly and repetition is difficult for the author to monitor.
- **Special for "Outline of Management Impacts"** - If reviewing content relating to "Outline of Management Impacts" emailshots, use internal/MgmtImpactRules.md methodology instead of this MDqualityCheck.md process. 
- **Special for reviewing Touchstones.md** - To avoid circular reasoning, omit the Touchstones alignment requirements when reviewing Touchstones.md.

### 2. Touchstones Alignment
- **Check against Touchstones.md** - verify no inconsistencies with Touchstones.md
- **Resolve inconsistencies** - If conflicts exist, resolve them or seek direction
- **Identify new touchstones** - If you identify potential new touchstones, raise them and seek direction on whether to add them
- **Explicit touchstone assessment** - Always conclude this step with either:
  - "No new touchstones proposed" (if document aligns with existing touchstones)
  - "New touchstone proposed: [description]" (if new fundamental principle identified)

### 3. Inter-Document Consistency
- **Use Touchstones method** - Don't try to check against every other .md file individually
- **Avoid complexity overload** - The Touchstones approach prevents overwhelming complexity from holding multiple documents in attention simultaneously

### 4. CLAUDE.md Impact Assessment
Determine if changes require updates to CLAUDE.md implementation guidance:
- **Technical architecture or configuration changes** - Does this affect system design, LLM selection, or deployment architecture?
- **Development practices or coding standards** - Does this impact how code should be written or structured?
- **Implementation tasks or requirements** - Does this require new development work or modify existing tasks?
- **User-facing elements** - Does this affect UI copy, messaging, or user workflows that need implementation?
- **If yes to any**, update CLAUDE.md with specific implementation guidance linking strategic decisions to code requirements

### 5. Multi-Perspective Review
Read the .md being reviewed in complete sweeps beginning-to-end sweeps from each relevant stakeholder viewpoint:

**Financial Institution Perspectives:**
1. **Chief Executive Officer (CEO)** - Strategic vision and business impact
2. **Chief Compliance Officer (CCO)** - Regulatory requirements and compliance strategy
3. **Chief Technology Officer (CTO)** - Strategic technology architecture and innovation
4. **Chief Information Security Officer (CISO)** - Data security, privacy, and risk management
5. **Chief Risk Officer (CRO)** - Enterprise risk management and regulatory risk

**Note:** Some documents may not be relevant to all perspectives - simply note this and move on to applicable viewpoints.

## Naming Conventions

**Reserved Usage of "MCP":**
- **The Universal_FSCompliance_MCP Project** - refers to the comprehensive development initiative creating a suite of specialist Compliance MCP servers for enterprise deployment and use
- **Any other use of "MCP"** - is fine, for example when referring to the Model Context Protocol itself
- Maintain this consistent Project terminology across all documentation.

## Governance Support

- **Track review completion** - Mark documents as reviewed in todo systems
- **About section requirement** - Check if the .md has an About section at the end, if not add it
- **Formal review tracking** - Add "Date last reviewed formally by MDqualityCheck.md: [date]" to the About section
- **Document changes** - Significant changes should be noted and justified
- **Date handling** - Follow Date Handling Protocol in CLAUDE.md: never add "Created" fields, use current date for "Last Updated", preserve external research citations
- **Date format standard** - Use UK date format "DD Month YYYY" (e.g., "9 July 2025") for Last Updated dates

---

## About This Document

**Author**: Blake Dempster, Founder, CEO, Principal Architect  
**Co-Authored by**: Claude Code (claude.ai/code)  
**Last Updated**: 29 July 2025  
**Date last reviewed formally by MDqualityCheck.md**: 8 July 2025  
**Purpose**: Systematic methodology for reviewing MCP Project documentation to ensure consistency, quality, and strategic alignment.

---