# Method for implenting an MCP Server covering a new Standard

## AI Agent Orientation

### Primary Use.

Our MCP Server is designed for use as an MCP server available to AI Agents. Direct human interaction is facilitated by a user front end but this is mostly for demonstration purposes.

### The AI Agent's Needs.

In our context, The AI Agent will be responding directly or indirectly to a prompt about Compliance for a Financial Institution. But this implies a structure. The prompt cannot meaningfully just say "Does [situation] comply?". Comply with what? The prompt only becomes meaningful if it says "Does [situation] comply with the requirements of [Standard]?". In this situation the [Standard] assumes maximum semantic significance for the AI Agent.

### Example: the FCA Handbook, our first Identified Standard.

Consider the prompt: "Does [situation] comply with the requirements of the FCA?". It can be assumed that our User, a financial institution, will have constructed the AI agent in the expectation that this sort of prompt will arise, and incorporated into the AI agent access to our MCP server. The question is what would make the AI Agent use the Tools provided in our MCP server.

### As Initially Designed.

Our MCP Server is currently called universal-fscompliance-mcp, with the vague starting intention that it would contain all implemented Identified Standards. 

It contains tools called quickly_check_compliance, identify_compliance_requirements_in_specific_case, systematically_analyse_compliance_implications, suggest_remediation, prepare_draft_compliance_audit_report, map_relationships, validate_ground_truth, status_of_standard_ingestion. 

These names are good semantic anchors but it feels unlikely that the AI Agent will ever consider using them. What good will they seem if the AI Agent's primary concern is to respond to a prompt whose most important word is "FCA"?

### Proposed New Design.

It is proposed that each new Identified Standard is structured as a separate MCP server with the name [Standard_Tag]_Compliance_MCP. Our first one would thus be FCA_Compliance_MCP.

Inside it the tools need to include the [Standard_Tag] prepend, eg FCA_quickly_check_compliance, FCA_identify_compliance_requirements_in_specific_case etc.

This would then give the AI Agent a specific match on the most important word in its prompt, both for the MCP Server and for the Tools which it can use.

## Our First Standard - the FCA Handbook.

## Ingestion - Pareto Issues.

Ingestion of the FCA Handbook raised immediate and interesting issues. First, size. In total it is large. Moreover a lot of the size consists of detail which may not suit vectorising, being abstruse in nature and footnote-like in character. It is likely that most of it will never be needed by the User of the AI Agent. Including it will be cumbersome to implement and slow down performance of the Tool. This is a classic Pareto problem, but more so: 99.99% of the value is in about 30% of the content, as an intuitive guess.

## Structure

The FCA Handbook is extremely organised under nested headings. Each of the headings can be viewed as a semantic anchor. This enabled us to make a good initial ingestion, identifying the important headings and vectorising them together with the content beneath them, whilst omitting the headings and content that are footnote-like in character. 

## 2-Layer Semantic Matching

The headings in the FCA Handbook clearly set out to communicate maximum meaning in condensed wording, making them useful Semantic Anchors. Our Tool's semantic matching should clearly give them more weight. The question is how many levels of heading to apply this thinking to. After reflection and inspection of the text it was decided that Level 1 still left too broad a scope underneath it, Level 2 provided convenient scope sizes, but Level 3 had an excessively narrowing effect. Thus a 2-layer Semantic Matching was adopted.

## Unified but Efficient Approach

This suggests an optimum approach: make the same decision identifying the important headings and vectorising them together with the content beneath them, but also ingesting the less important headings *without* the content beneath them. This will mean that if it turns out that the less important heading did in the event turn out to be relevant, through use of the 2-Layer Semantic Matching, the Tool could return a message saying: "It looks like the [less important heading] may be relevant but we do not have full information of what lies beneath it." 

## Future Identified Standards Implementation Methodology

### Phase 1: Standard Assessment and Feasibility
1. **Structure Analysis**: Evaluate the regulatory standard to ensure it utilizes well-organized hierarchical headings suitable for semantic anchor extraction. Standards lacking clear structural organization should be considered for deferral as they may be unsuitable for AI-powered analysis.

2. **Regulatory Engagement**: Contact the relevant regulatory authority to assess:
   - Availability of structured digital formats
   - Potential access to ground truth validation datasets
   - Update frequency and notification procedures

### Phase 2: Technical Implementation
3. **MCP Server Creation**: Establish new MCP server following naming convention `[Standard_Tag]_Compliance_MCP` (e.g., `MiFID_Compliance_MCP`, `SEC_Compliance_MCP`).

4. **Codebase Duplication**: Create new server by copying existing `FCA_Compliance_MCP` implementation, providing proven foundation with established two-layer semantic matching architecture.

5. **Tool Customization**: Update all tool names to include standard-specific prefixes:
   - `[Standard_Tag]_quickly_check_compliance`
   - `[Standard_Tag]_identify_compliance_requirements_in_specific_case`
   - `[Standard_Tag]_systematically_analyse_compliance_implications`
   - (Complete set following established pattern)

### Phase 3: Data Infrastructure Setup
6. **Database Table Creation**: Implement standard-specific table set within unified database:
   - `[standard_tag]_documents`
   - `[standard_tag]_ground_truth` 
   - `[standard_tag]_ingestion_status`

7. **Content Ingestion**: Adapt FCA ingestion methodology for new regulatory context, applying Pareto analysis to identify high-value content areas and implementing unified-but-efficient approach for comprehensive coverage.

8. **Status Documentation**: Create `std_[Standard_Tag]_Status.md` file to provide ingestion progress visibility for AI agents and system monitoring.

### Phase 4: Validation and Deployment
9. **Ground Truth Integration**: Implement standard-specific ground truth validation capabilities when regulatory or user-contributed datasets become available.

10. **Quality Assurance**: Conduct systematic testing against known compliance scenarios before production deployment.

11. **Documentation Updates**: Update CLAUDE.md and related technical documentation to reflect new standard implementation.

This methodology ensures consistent implementation quality while maintaining the AI Agent Oriented principle of semantic clarity and discoverability.

## Ground Truth

It is possible that we will get access to Ground Truth data, from regulators and from Users, normally held in Q&A form. This will be extremely valuable. For now we have none so we don't want to become too distracted by this, but in construction of the MCP server it is important that we make it easy to accommodate Ground Truth.

Note that many Users are motivated to maintain the reputation of the industry they work in, and Regulators similarly, so may well make available Ground Truth databases.

It is envisaged that the Tool would, in addition to carrying out the 2-layer semantic matching would also go through the following Ground_Truth process:

1. Is there Ground Truth relating to this [Standard_Tag]?
2. Is it available for this User (ie is it only available for the User defined as its Owner)?
3. If it is available, do any of the Q's semantically match the prompt in the current query?
4. If there is a match, modify reply accordingly.

In addition we should give consideration to running our MCP Server against the Qs in the Ground Truth (without the Ground_Truth process), and score the results, to see what can be learned.

## Database Strategy Reference

The technical database architecture supporting this methodology is detailed in `DatabaseStrategy.md`, which specifies the single database with table prefixes approach optimized for AI Agent Oriented tool design.
