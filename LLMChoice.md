# LLM Choice

## Executive Summary

This document defines how LLM-openness is managed in the Universal_FSCompliance_MCP Project ("UFSCMCP"). 

The LLM used by Tools is ultimately responsible for how to apply them. This will be fundamental in achieving the overarching objective of making it easier for Financial Institutions to bring the right product safely to consumers.

The LLM in the Agent using the MCP server is responsible for whether or not to use it and its component Tools. This LLM may be different from the LLM used by the Tools, or it may be the same.

Regardless of which LLMs are used, results are still subject to human review and validation, supervised by appropriately qualified professionals.

## Emerging Factors

The following factors have emerged as important during the course of UFSCMCP work:

- The LLM powering our MCP needs only to deal with text or text equivalents such as voice recordings. Thus multi-modal capability, a main focus of frontier LLMs, is unneeded. 

- Our MCP is designed to support human professionals, who make final decisions, so instantaneity would arguably be an over-engineered objective. A few seconds delay is acceptable. 
  
- New LLMs are emerging with such frequency as to make it unwise to commit to any one LLM.

- Enterprises have their own preferences, based on experience and relationships, and our stance is that we will fit in with their priorities.

- MCP servers run their own LLMs completely independently from whatever LLM the enterprise chooses for their AI agents. This is a fundamental architectural separation. Our MCP enables Users to experiment with whichever LLM suits their needs for specialist Compliance purposes.
   
- We have therefore engineered in an LLM-open approach, thus preserving enterprise flexibility both when the Tools are initially adopted and as experience develops. 

## Wider Context

#### Compliance Executives' Time Scarcity

Given compliance executives' time scarcity it may not be an efficient use of resources to use an inferior LLM and then possibly run into quality issues, or expend much time experimenting with alternative LLMs that have not proven themselves in such a well-suited compliance context. 

#### Compliance Is Expensive and Critically Important

In financial services, compliance errors can result in:

- Regulatory fines
- Reputation damage and customer loss
- Legal liability and professional indemnity claims
- Operational disruption and remediation costs

The burden of Compliance is substantial. Compliance Officers need the most effective AI support they can get.

The cost differential between LLMs is insignificant compared to these compliance failure risks.

## Separate Architectures

A major advantage of the MCP protocol is that general enterprise LLM use is separated from the use of LLMs inside the MCP, which can therefore use the optimum LLM for its special purpose. For example:

Enterprise AI Agents can use:

- GPT-4, GPT-4o, or other OpenAI LLMs
- Gemini Pro or other Google LLMs  
- LLaMA 3, Mistral, or other open-source LLMs
- Any proprietary or fine-tuned enterprise LLMs

FSCompliance MCP Server can independently run:

- Configurable default LLM provider 
- Alternative LLMs if Enterprise chooses
- Completely separate infrastructure and API calls

## Data Security

Financial Institutions and Financial Services Companies are particularly worried about data security and privacy, and some gravitate towards local LLM deployment. However, powerful non-local LLMs with data protection capabilities are emerging.

The UFSCMCP supports enterprise self-hosting and other deployment methods to ensure data security and privacy. See TechnologyStack.md.

## In-Use Criteria

Based on our experience it is suggested that Users choose an LLM taking into account the following criteria:

1. Compliance Reasoning Quality

- Complex regulatory interpretation capabilities
- Multi-document analysis and synthesis
- Contextual understanding of financial services regulations
- Nuanced risk assessment and gap detection
- Professional-grade output suitable for regulatory scrutiny

1. Business Considerations

- Integration with existing enterprise workflows
- Cost implications 
- Competitive differentiation in RegTech
- Competitive differentiation in Financial Services
- Brand alignment with "expert-backed" positioning
- Customer liability and risk management

1. Technical Architecture

- Scalability and performance characteristics
- Multi-LLM support and flexibility
- Integration simplicity and maintenance

## About This Document

Author: Blake Dempster, Principal Architect  
Last Updated: 11 September 2025  
