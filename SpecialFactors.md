# Special Factors

## AI Optimization.

### Prompts

For the UniversalFSCompliance Project, the AI Agent will be responding directly or indirectly to a prompt about Compliance. This implies a structure. The prompt cannot meaningfully just say "Does [situation] comply?". Comply with what? The prompt only becomes meaningful if it says "Does [situation] comply with the requirements of [Standard]?". In this situation the [Standard] assumes maximum semantic significance for AI: it becomes a semantic "anchor".

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

Beneath the Naming framework, Tool coding is simple, especially with the aid of AI coding assistants. The process consists of providing a Tool description and examples, and prompting the AI coding assistant to produce the code. Then walking through and testing the results. In fact the amount of code required for each Tool is modest, as would be expected from the modular nature of each Tool. The value of the overall toolbox resides not in the advanced coding, more in the maintenance of good documentation and organization.

## Standards

### Structure of Standards

Standards are extremely organised under nested headings which have all been clearly given careful consideration. This level of organization is a prerequisite for Implementing any Standard.

Each of the headings can thus be viewed as a Semantic Anchor in its own right. 

### Layering

The question arises as to whether only Heading1s should be the significant Semantic Anchors, or Heading1s and Heading2s, or Heading1s and Heanding2s and Heading3s. After research and inspection of the FCA Handbook text, it was decided that using only Heading1s left too broad a scope underneath, Heading2s provided convenient scope sizes, but Heading3s had an excessively narrowing effect. 

Thus a 2-layer Semantic Matching pointed at Heading1s and Heading2s was adopted.

### Pareto Issues.

A Standard is generally large. Moreover a lot of the size consists of detail which may not suit vectorising, being abstruse in nature and footnote-like in character. 

It is likely that most of it will never be needed by the User of the AI Agent. Including it will be cumbersome to implement and slow down performance of the Tool. This resembles a Pareto distribution challenge: approximately 90% of the regulatory value is concentrated in 30% of the content. 

Our vector database has therefore been designed to hold all headings, to include all content beneath Heading1 and Heading2 other than what appear semantically to be less important content under Heading3s, Heading4s and lower. In other words, all headings are retained, most of the content, but not the content that seems semantically to be too abstruse.

Where the Tool's semantic search leads to a Heading where content has been omitted, it will respond along the lines of (depending on context): "It looks like a relevant point is covered under [x.x.x HeadingN] - I do not have its contents but can get more information. Would you like me to do that?"

As part of routine dashboard management, our database will collect user statistics for which Tools are used, and which parts of the Implemented Standard are used in the Prompt response. Where the semantic search leads to a Heading where content has been omitted, and where there is significant traffic to this Heading, the content can be restored. 

### No Need for Graph Database

The highly structured nature of Standards is such that vectorization is a sufficiently powerful technology. Graph databases appear currently to be more suited to environments where discovery of new relationships, rather than application of existing structured text. Graph databases have thus not been implemented. 

The benefits of this are: avoids over-engineering; maintains simplicity; avoids unnecessary overhead and complexity; focuses resources on core 2-layer semantic matching; easier maintenance and scaling.

This approach will be reviewed periodically.

### Implementation of Standards

The UniversalFSCompliance Project's first Implemented Standard is the FCA Handbook, from which methods have been developed. It is expected that these will continue to evolve over time.

The next Standard will be determined by market demand, driven by User feedback. It will be used to test and expand the UniversalFSCompliance Project's methods.

In this way feedback loops will be put in place which continuously enhance capability.

## Ground Truth

### Extending beyond the Standard Wording

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

In AI, the term "Ground Truth" is often used to describe how the parameters in LLMs are refined such as to improve the LLM's answers to the Qs in the Ground Truth data, scored against the As in the Ground Truth data. This is not how Ground Truth data is used in the Universal_FSComplianceMCP Project, where Ground Truth data is used not for LLM parameter refinement, but rather is used as described above.

---

## About This Document

**Author**: Blake Dempster, Founder, CEO, Principal Architect  
**Last Updated**: 11 August 2025  
**Date last reviewed formally by MDqualityCheck.md**: 11 August 2025  
