# Special Factors

## Executive Summary

This document sets out how the Universal_FSCompliance_MCP Project ("UFSCMCP") has special factors which differentiate it from other AI applications.

These special factors need to be taken into account:

- to optimise the MCP servers and their Tools having regard to the overarching objective of making it easier for Financial Institutions to bring the right product safely to consumers.
- to maximise usefulness to Users, who will be expecting that the Tools will be fit for purpose (having regard however to the fact that results are still subject to human review and validation, supervised by appropriately qualified professionals)

## AI Optimization

### Prompts

For the UFSCMCP, the AI Agent will be responding directly or indirectly to a prompt about Compliance. This implies a structure. The prompt cannot meaningfully just say "Does [situation] comply?". Comply with what? The prompt only becomes meaningful if it says "Does [situation] comply with the requirements of [Standard]?". In this situation the [Standard] assumes maximum semantic significance for AI: it becomes a semantic "anchor".

### AI Agents, Tools, MCP Architecture

A typical prompt would be: "Does [situation] comply with the requirements of the FCA?". 

Fed directly to a LLM, some sort of answer would be forthcoming - often reasonable but often weak. 

For Financial Institutions this type of prompt arises frequently. It is ideal for a specialist AI Agent that deals with it in a less generalist way. An LLM would still do the work, but now the LLM is pointed in a specified direction.

How should such an AI Agent be constructed? This was a problematic issue - until the Model Context Protocol (MCP) emerged. Publicly available, created by Anthropic, increasingly adopted since late 2024, this is widely seen as an AI breakthrough for enterprises. MCP is essentially a toolbox architecture for making Tools available to LLMs. The AI Agent is constructed to make use of the Tools it has available.

### LLM Used by Tool

As outlined in LLMChoice.md, the LLM used by the AI Agent to select the Tool can be different from the LLM used by the Tool. This allows greater specialisation, and is a major advantage of the MCP architecture.

## Tool Design

### Tool Design - Top Down

Tool design starts with the recognition that it is an LLM inside an AI Agent that makes the decision as to whether or not to use the Tool. 

Pre-AI, a tool would be explicitly called. This gives more apparent control, but relies on correct initial specification, and system changes are problematic. In the AI world, the LLM has freedom to decide what to do *in the specific situation*.

An AI Agent decides whether or not to use a Tool using *semantic* reasoning. Essentially the AI Agent says: I have been constructed with access to an MCP Server, whose name is such that it looks like it contains Tools relevant to the Prompt I am responding to. Inside the MCP Server are Tools whose names also look relevant to the Prompt. Let me select the most promising Tool, based on its name, and use that.

For the UniversalFSCompliance Project, this is accommodated by a framework in which each new Implemented Standard is given a separate MCP server with the name mcp-server-[standard]-compliance. Our first one would thus be mcp-server-fca-compliance.

Inside it the tools include the [standard] prefix, eg FCA_quickly_check_compliance, FCA_identify_compliance_requirements_in_specific_case etc.

This would then give the AI Agent specific matches on the weightiest Semantic Anchors in its Prompt, both for the MCP Server and for the Tools which it can use.

### Tool Design - Bottom Up

Beneath the Naming framework, Tool coding is simple, especially with the aid of AI coding assistants. The process consists of providing a Tool description and examples, and prompting the AI coding assistant to produce the code. Then walking through and testing the results. 

## Standards

### Making Use of the Structure of Standards

Standards are extremely organised under nested headings which have all been clearly given careful consideration. (This level of organization is a prerequisite for Implementing any Standard.)

Each of the headings can be viewed as a Semantic Anchor in its own right.

This has given rise to a sophisticated multi-stage semantic searching method to optimise matching of content against User prompt and provide relevant responses. 

### No Need for Graph Database

The highly structured nature of Standards is such that vectorization is a sufficiently powerful technology. Graph databases appear currently to be more suited to environments where discovery of new relationships is required, rather than application of existing structured text. Graph databases have thus not been implemented. 

The benefits of this are: avoids over-engineering; maintains simplicity; avoids unnecessary overhead and complexity; focuses resources on core 2-layer semantic matching; easier maintenance and scaling.

This approach will be reviewed periodically.

### Implementation of Standards

The UniversalFSCompliance Project's first Implemented Standard is the FCA Handbook, from which methods have been developed. It is expected that these will continue to evolve over time.

The next Standard will be determined by market demand, driven by User feedback. It will be used to test and expand the UniversalFSCompliance Project's methods.

In this way feedback loops will be put in place which continuously enhance capability.

### Ground Truth - Extending beyond the Standard Wording

At present the heart of the UniversalFSCompliance Project's tools is semantic matching between Prompt and Implemented Standard. This is powerful in itself. 

Access to Ground Truth data has the potential to enhance results through exposure to real-life experienced problems. This Ground Truth data will often be available from regulators and from Financial Institutions, normally held in Q&A form. 

Some Users may view Ground Truth as a source of competitive advantage, in which case the database will not make it available to other Users. Many Users however are motivated to maintain the reputation of the industry they work in, and Regulators similarly, so may well make public some Ground Truth databases.

### Making use of Ground Truth Data

In addition to carrying out the 2-layer semantic matching our Tools will go through the following Ground_Truth process:

1. Is there Ground Truth relating to this [Standard]?
2. Is it available for this User?
3. If it is available, do any of the Ground Truth Q's semantically match the prompt in the current query?
4. If there is a match, modify reply accordingly.

The Ground Truth can additionally be used as a test of our MCP Server, by running it against the Qs in the Ground Truth (without the Ground_Truth process), and semantically score the results against the As in the Ground Truth.

### Terminology

In AI, the term "Ground Truth" is often used to describe how the parameters in LLMs are refined such as to improve the LLM's answers to the Qs in the Ground Truth data, scored against the As in the Ground Truth data. This is not how Ground Truth data is used in this context: Ground Truth data is here used not for LLM parameter refinement, but rather is used as described above.

## About This Document

**Author**: Blake Dempster, Founder, CEO, Principal Architect  
**Last Updated**: 11 September 2025  

