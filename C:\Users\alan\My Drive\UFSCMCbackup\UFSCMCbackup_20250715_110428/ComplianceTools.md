# The Tools In the MCP Toolset

## Purpose of this Document

As an MCP-structured product, as implied by its name, the Universal_FSCompliance_MCP Product essentially makes available a curated set of specialist Tools. This document sets out a roadmap of what Tools are planned and which are available now.

The roadmap may change in light of emerging priorities and this document will record any changes. 

## Context 

- Many of the Tools are inconceivable without AI.
- Following developing MCP best practice, Tools are named in lowercase, as a composite of words joined by underscores.
- The MCP's LLM will be particularly attuned to the Tool name and it is therefore important that the Tool name is accurate and unambiguous. The Tool name can be viewed as a semantic anchor.
- The Tool names adopted for the Universal_FSCompliance_MCP Product have been parsed carefully for accuracy and unambiguousness.
- Implementation of the Planned Tools is the next overall priority.

## Usage

- The User can, but would not normally, specify the Tool: the LLM inside the MCP normally chooses what tool to use.
- The usage pattern is: User enters prompt naturally, LLM intelligently selects appropriate tools based on context, User receives results without memorizing tool names or syntax.
- The MCP serves as intelligent middleware, providing AI-assisted tool selection rather than requiring manual tool invocation.
- This eliminates the significant cognitive effort required for manual tool selection - a key competitive differentiator. 

## Planned Tools 

**1. quickly_check_compliance**
- **Purpose**: Analyses Compliance of Wording in Prompt or attached Document against requirements of the Identified Standard.
- **Example**: "Here is proposed wording for a new policy. What Compliance issues arise in relation to [Identified Standard]?"
- **Usage**: Quick, easy, and useful Compliance Assistance to provide assistance when conceptualising. Easy on the Surface, underneath the Tool uses AI to carry out complex analysis of the Identified Standard and match against Prompt or Document.

**2. systematically_analyse_compliance_implications**
- **Purpose**: Detailed analysis for policies, procedures, and business activities
- **Example**: "Here is proposed wording for a new policy. Please carry out a disciplined analysis, produce scores against standard risk criteria relevant to [Identified Standard], set out what we need to attend to."
- **Usage**: Strategic analysis, wider and deeper than quickly_check_compliance tool. Wider ranging, more systematic and thoughtful than quickly_check_compliance tool.

**3. identify_compliance_requirements_in_specific_case**
- **Purpose**: Identify relevant requirements in a particular case from the Identified Standard. 
- **Example**: "What are the 10 most significant requirements of the [Identified Standard] in relation to the investment needs of a 65 year-old single woman?"
- **Usage**: Research and requirement identification with context-aware requirement extraction

**4. prepare_draft_compliance_audit_report**
- **Purpose**: Collection and organization of Compliance evidence grounded in actual Compliance work.
- **Example**: "Please provide a trail of our Compliance activities in respect of [Identified Standard] since [date, normally of the previous Compliance Audit]. Please use this to prepare draft Compliance Audit Reports in format acceptable to Compliance Auditors."
- **Usage**: To lighten load and remove trauma of Compliance Audits. Monthly or quarterly.

**5. map_relationships**
- **Purpose**: Visualize and analyze relationships between regulations, requirements, and business activities. Especially, in relation to Consultation Documents, where the Consultation Document is included in [Identified Standard]
- **Example**: "How do the requirements of [Identified Standard] impact our processes in relation to if we are involved in transferring an investment portfolio from a corporate client to an insurer?". Or: "How would X product be affected by proposed changes?". Or: "What costs arise from these proposals?". Or: "Should we respond to this consultation?". Or: "What's our Compliance timeline if adopted?"
- **Usage**: When one-off exercises are being planned, or when processes are being designed. This will involve graph analysis of connections between Standards using LightRAG
  
**6. validate_ground_truth**
- **Purpose**: Validate quality of Tool responses. Optionally, allow the tool to anonymously learn from the exercise, as a service to the industry. Optionally, allow the tool to keep a record of the ground truths, suitably anonymised, as a service to the industry.
- **Example**: "Here is a list of ground truth problems. Apply the Tool (eg quickly_check_compliance) to each ground truth problem; record the Tool's response; and compare the Tool's response with the corresponding model answer in the list; calculate the correctness score. Do same again over the list; calculate overall score. Provide a schedule containing a list of: ground truth problem supplied; Tool response; Model Answer; correctness score. Also provide overall score."
- **Usage**: Hygiene work viewed as routine maintenance and learning for Users as well as Tool.

**7. ingest_new_identified_standard**
- **Purpose**: Enable users to add new Standards to the Product. Check whether any special considerations arise by reference to LegalLiability.md
- **Example**: "Please ingest [Standard Name] from [Source]. Parse structure, identify requirements, create knowledge graph, validate against existing standards for conflicts."
- **Usage**: Expand Product coverage to user-specific needs for coverage of Standards. Guided wizard with quality validation and review process

**8. update_identified_standard**
- **Purpose**: Monitor and apply changes to Identified Standards to maintain system currency
- **Example**: "Check for updates to [Identified Standard] since [date of last check], analyze changes, and apply updates to knowledge base; also provide impact assessment"
- **Usage**: Automatic invisible background maintenance and user-triggered updates to Identified Standards - key competitive differentiator. Initially invoked by specific request; as User base and number of Identified Standards grow, the tool will be invoked according to schedule.

**9. suggest_remediation**
- **Purpose**: AI-powered suggestions for addressing a Compliance gap, possibly identified by other Tools, or by Compliance auditor.
- **Example**: "We have identified this Compliance gap: [description of gap]. Please suggest remediation actions, including to our processes. Please indicate costs and timelines."
- **Usage**: Convert Compliance problems into actionable solutions. Allows decisive action 


---

## About This Document

**Author**: Blake Dempster, Founder, CEO, Principal Architect  
**Co-Authored by**: Claude Code (claude.ai/code)  
**Created**: 25 December 2024  
**Last Updated**: 14 July 2025  
**Date last reviewed formally by MDqualityCheck.md**: 14 July 2025  
**Status**: (okay)
**Purpose**: Tool roadmap for the Universal_FSCompliance_MCP Product - sets out what Tools are planned and which are available now.

---