# Universal_FSCompliance_MCP Project - Frequently Asked Questions

## What is the Universal_FSCompliance_MCP Project?

The Universal_FSCompliance_MCP Project ("UFSCMCP") comprises a suite of MCP servers available to any AI agent through Model Context Protocol (MCP) integration. It starts with the FCA Handbook to create mcp-server-fca-compliance, containing Tools such as FCA_check_compliance and others. Other MCP servers will follow, using similar methods and using similar architectures. 

The Project is structured and denominated in this way because of the way that semantics underpin the operation of AI, AI Agents, and Tools. AI Agents will use MCP servers and Tools which are semantically weighted in accordance with usage and the originating prompt. 

The overall intent is to make it easier for Financial Institutions to bring the right product safely to consumers.

## What does "Universal" mean?

The UFSCMCP is universal in the sense of being capable of applying to any Standard.

Any Standard which is sufficiently structured (i.e. with coherent headings) will be able to be rapidly ingested to become an Implemented Standard, including:

- Regulatory frameworks (FCA Handbook, SEC rules, MiFID II, Basel III)
- Industry codes (conduct codes, best practice guidelines)
- Statutory requirements (legislation, acts, laws)
- International standards (IFRS, SOX, ISO standards)
- Jurisdictional regulations (state, provincial, national requirements)
- Consultation documents (regulatory proposals, policy consultations, draft guidance)

At present Implemented Standards are limited to the FCA Handbook - which is being used as a proof of concept. The architectures thus developed will then be replicated in ingesting other Standards.

## What is the market size?

The "RegTech" market in financial services is projected to grow from $11.7B to $83.8B by 2033 (21.6% CAGR) - Allied Market Research, 2025. The UFSCMCP is positioning to be essential support for this market.

## What is the current state of the Project?

This Project is in its early stages but has quickly taken well-delineated form. The current state is: 

- Preparation. Complete. Comprehensive documentation covering Business, Technical, and Technological matters in multiple discrete modules as outlined in README.md
  
- Stage 1. Complete. mcp-server-fca-compliance submitted to Anthropic's MCP ecosystem Official Integrations, awaiting review. This is a skeletal implementation designed to secure semantic positioning ready for Users' AI Agents, and provide a tested framework which we can then use to deploy full Tool functionality.
  
- Stage 2 In progress. Development of full Tool functionality. Strategic organization completed. Basic Tool coding well advanced. Dashboard statistics structure completed. LLM-open capability structure completed. Charging framework structure completed.
  
- Subsequent Stages. As per experience and client demand.

The Project is thus a test case of ultra-rapid large-scale development using new AI tools.

## How do automatic updates work?

The UFSCMCP has in place a special Tool to ensure that Implemented Standards are kept up to date. Traditional non-AI native Compliance tools typically find this very difficult, but the AI-native UFSCMCP makes it very achievable. Updates are invisible and automatic from the User's viewpoint.

### What is the LLM-Open Architecture?

The UFSCMCP uses an LLM-open architecture supporting enterprise LLM requirements with configurable provider selection. Enterprises can use any AI agents with any LLM (GPT-4, Gemini Pro, LLaMA 3, Mistral) to access the UFSCMCP's MCP servers without affecting the LLM used inside each MCP server. This is one of the strong advantages of the MCP protocol.

### How are AI-Native Development Timescales Concertina-ed?

In this Project, Human Architect doing the specifying, plus Claude Code doing the implementation, plus the collaborative exchanges between them, has achieved in days what otherwise would have taken many months. Further, it has been easy to ensure that the large number of component sub-projects stay in tune with the overall "Touchstones" that were identified.

### How do Tools work?

Using standard MCP architecture, each MCP server articulates its capabilities (using a .json file), so that outside AI Agents can choose to use the appropriate MCP server. Then the LLM inside each MCP server intelligently uses appropriate Tools based on context.

## What is the legal liability framework?

### User Responsibility

Users retain full legal and regulatory responsibility for all Compliance decisions, actions, and outcomes. The UFSCMCP's MCP servers serve as analytical tools to assist decision-making but do not replace professional judgment or legal accountability.

### Professional Requirements

- All Compliance activities must be supervised by appropriately qualified professionals
- AI-generated content may contain errors and requires human review and validation
- Users should ensure IT systems maintain permanent records of Tool usage and professional review

### General Disclaimer

The UFSCMCP's MCP servers provide information and analysis but do not constitute legal advice, regulatory guidance, or Compliance recommendations. Users must ensure Compliance with data protection regulations and obtain necessary permissions for data processing activities.

## How do AI Agents use MCP Server Tools?

The behaviour of the LLM being used by the AI Agent can be characterised as follows:

- I am being prompted: "Does the attached policy wording comply with FCA requirements?"
  
- Look, when I was constructed I was given access to an MCP server called mcp-server-fca-compliance - that looks very relevant.
  
- Look, there is a Tool called FCA_check_compliance, that looks like a semantic match, it contains "FCA", it contains "Compliance" and I think from the prompt that the User wants a check, I'll use that Tool.
  
- Here is what the Tool returned, I'll use that to frame a response to the User, take it from there.

## How does the LLM-Open Architecture work?

The UFSCMCP implements configurable LLM selection to meet diverse enterprise requirements. Each MCP server can be configured with the enterprise's preferred LLM, enabling optimal performance for specific compliance contexts.

## What is Document Parsing, Chunking and Embedding?

Document parsing, chunking, and embedding are fundamental AI technologies.

Document Parsing extracts structured information from Standards. This involves understanding document and website structure, hierarchy, and contextual meaning beyond simple text extraction.

Chunking divides long text into semantic units that preserve meaning while enabling efficient processing.

Embedding converts text chunks into high-dimensional vectors that capture semantic meaning, through multi-dimensional proximity. This is the fundamental method by which AI understands Implemented Standards and constructs responses that are relevant to prompts.

## How are security and privacy managed?

The MCP Server is designed for enterprise self hosting and thus can be managed for security and privacy without additional overhead.

The following features apply:

- Zero Data Retention: options with automatic deletion
- Encryption: TLS 1.3 for transit, AES-256 for data at rest
- Access Controls: OAuth 2.1 with role-based permissions
- Audit Logging: Complete tracking of compliance decisions
- OWASP Standards: Comprehensive security testing and vulnerability management
- Opt-in memory - Users choose information retention
- Data anonymization - Automatic PII detection and protection
- Self-hosted options - Complete data sovereignty available

## About

The UFSCMCP was founded by Blake Dempster, a UK actuary with extensive financial services experience and thought leader in AI and financial services intersection. The Project demonstrates Human-AI collaboration, showing how AI can transform Standard Compliance through extreme development speed and professional-grade output.

For complete development narrative and strategic insights, see OurStory.md.

## About This Document

Author: Blake Dempster, Founder, CEO, Principal Architect  
 Last Updated: 11 September 2025  