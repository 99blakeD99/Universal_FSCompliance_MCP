# The Tools In the MCP Toolset

## Executive Summary

This document defines how Tools are managed within MCP servers in the Universal_FSCompliance_MCP Project ("UFSCMCP"). 

The overarching consideration is that Tools are used to achieve the objective of making it easier for Financial Institutions to bring the right product safely to consumers.

Use of the Tools is subject to human review and validation, supervised by appropriately qualified professionals. The Tools are designed to make it easier for humans to do their Compliance job, not to supersede them.

## AI Agent Oriented Naming

- Tools are designed to optimize AI agent discovery and semantic matching

- Each Standard is housed in a separate semantically anchored MCP server containing semantically anchored Tool names

- Tool names include reference to the Implemented Standard as context to match AI agent query patterns (e.g. "Does this comply with **FCA** requirements?" → fca_check_compliance
  
- Following MCP best practice, tools use lowercase with underscores
  
- Structuring Tools in this way facilites usage that satisfies enterprise security and privacy standards.

## Core Tool Design

### Original Construction

Originally multiple Tools for the MCP server were constructed. However it became clear that there were no clear boundaries between Tools, and that the construction was based on quickly conceived theoretical use-cases. Selection of one such Tool on the basis of the User Prompt, provided via the AI Agent using the MCP server, risked sending the LLM into an arbitrary direction and impairing response quality. This risk became clearer on becoming more familiar with the structure of the Standard.

It was therefore decided to adopt a single main Tool and incorporate within it the logic for deciding how to achieve Semantic matching against the data.

### Advantages of a Single Main Tool Design

1. Sophisticated Search within the Tool Handles All Cases
   
2. Pre-categorization is Premature. Users' prompts often don't fit neatly into these categories. The AI Agent is adept at interpreting intent and framing responses appropriately. In contrast, inappropriate Tool selection leads the analysis down the wrong analytical path
   
3. Maintainability. One sophisticated tool is easier to optimize, debug, and enhance multiple interconnected tools with overlapping functionality.

### [standard]_check_compliance

- **Purpose**: Comprehensive compliance analysis using sophisticated
semantic search

- **Implementation**: Uses hybrid multi-stage search 
  
- **Example FCA**: "Does this comply with FCA requirements?" →
`fca_check_compliance`

- **Response Adaptation**: AI Agent frames results appropriately based on
query context

## About This Document

**Author**: Blake Dempster, Principal Architect  
**Last Updated**: 11 September 2025  

