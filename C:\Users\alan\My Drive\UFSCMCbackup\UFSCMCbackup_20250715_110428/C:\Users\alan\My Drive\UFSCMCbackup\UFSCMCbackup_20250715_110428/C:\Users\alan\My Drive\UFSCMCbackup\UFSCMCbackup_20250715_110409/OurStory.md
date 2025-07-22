# Our Story: The BD-CC Collaboration

**How Human Architect working with Claude Code became like dozens of tightly-knit, scorchingly-efficient, hyper-intelligent, grossly-underpaid executives to create a mega-project and a super-ambitious product.**

---

## The Backstory

One upon a time, 25 June 2025 to be exact, Blake Dempster (BD), a UK actuary with wide experience of financial services projects, was playing around with Claude Code (CC) and thought, let's really test this AI companion out, make it jump through some hoops. He entered the prompt:

Can you help me build the first open-source, LLM-open, AI-native, Compliance platform structured as an MCP? The objective is to allow financial institutions to comply with any identified Standard, of which the FCA Handbook is a good representation. In order to slice through red tape, radically shrink costs, and cut out unnecessary friction. All whilst radically enhancing agility and ability to bring the right financial products safely to consumers. And whilst allowing complete freedom for the financial institution's choice of IT architectures and choice of LLM. I want to use Pydantic AI, LightRAG, and github. I want to go straight for a full production deployment on the Cloud using Azure or one of its peers, no messing about with prototypes.

CC paused for a while. Then said, Sure.

The touchpaper was lit.

## The Beginning: 25 June 2025

The project was ambitious. We did not know what would happen next. What did happen next turned out to be a demonstration of how human-AI collaboration can concertina development timelines in ways that redefine what is possible in the AI era.

## The 8-Day Sprint

### Days 1-2 - Strategic Foundations

#### CEO Voice

Listen everyone these very early stages set the DNA of our work, we need to keep our heads clear. We need to ensure that everything that should be there is in fact there, and that we make the right foundational choices at the beginning. It will require hard thinking: not only is it a new project, not only is it a new product, it's a new AI universe. Good luck!

#### The Technical Architect Voice

Before going to CC BD had put the substance of CC's starting prompt to Perplexity, and asked whether an MCP is suitable.

Perplexity said: Yes, your concept as an open-source AI agent or MCP service is suitable for an MCP service. Here's why:

**Client-Host-Server Model**: The MCP architecture uses a client-host-server model. Your project can act as the **MCP server**, providing tools and resources to other AI agents (clients) that interact with it. This setup allows different AI agents to query the an identified Standard like the FCA Handbook and receive relevant information.

**Tools and Resources**: The MCP server can provide tools like "search for a file" or "read a file", which can be adapted to search the relevant Standard for specific requirements or risk warnings. Additionally, it can support resources like prompts and structured data, which can be used to generate draft reports or identify salient requirements.

**Integration with External Data**: The MCP architecture is designed to standardize context and allow AI models to interact with external data sources and tools. This aligns well with your requirements.

**Authorization**: While authorization is optional, it can be used to ensure that only authorized AI agents can access the relevant information, which is crucial for maintaining the integrity and security of the information.

In summary, your project can be effectively implemented as an MCP service, leveraging its client-host-server model and providing tools and resources to other AI agents for querying and utilizing the FCA handbook.

#### The Technical Architect Voice

LLMs are widely thought of as omniscient, or heading that way. Specialist focus is supposedly achieved by fine-tuning the LLM. It would still be fiendishly difficult to ask LLMs the right question. Even formulating a sequence of questions requires effort and time. Better to encapsulate common questions into AI Agents. AI Agents do much better if they can use toolsets. The AI Agent's LLM has the job of deciding which toolset to use. This needs a standard way for toolsets to advertise their capabilities. The MCP protocol is becoming the standard way to do this. The MCP can use a different LLM from that used by the AI Agent. In short, discovering and using suitable MCPs is essential.. Ergo, MCP fits our needs.

#### The Factual Recorder Voice

Okay CC let's roll. What should we do? Oh look, CC's thinking. Nice to have the updates. Oh look, CC has run into installation trouble, just like what happens to me. Oh look, CC has sorted it out, done in five seconds what can take me hours of tortured headbanging.

Oh look, a steady stream of problems solved and updates.

(Later I learned that you could tell from these updates if things were veering off-piste, mostly when CC got too enthusiastic and started doing things which actually I wanted CC's opinion on first before deciding to proceed.)

Ok, I think I'll go and make a coffee..., oh wait, CC's finished.

Crikey, that was quick, let's take a look. Darn, that looks good. Okay, CC, what's next, make some tasks, get back to me.

Okay, CC, let me have a look, take a breather... (it's easy to forget that that CC doesn't need breathers).

Okay CC, those tasks look good but can you move task 4 to task 6, promoting task 6 to 5 and add in a new task 4 -- Research the requirements of...", what do you think.

Okay CC glad we agree, let's go ahead with task 1, review from there.

... and so on for two days of highly engaging work, it felt like a game.

Then...Okay CC tell me what we've achieved so far.

##### What BD-CC had done together:

Project architecture designed

Complete layered MCP architecture designed from scratch

Technical foundations laid: Core data models, MCP server structure, development environment

Foundational framework created: Rules.md, CLAUDE.md Planning.md (these would constantly be updated in line with discoveries emerging during development)

### Days 3-4 - Core Intelligence

#### The Technical Architect Voice

The understanding dawned that our current project work involves cognitive processing very analogous to the work we want our product to do.

This is a potent validation of CC's LLM, Claude 3.5 Sonnet, positioning it front runner as choice of LLM. Also, its privacy protections are very strong.

Claude 3.5 Sonnet is expensive. But for our MCP, with its professional user market, the difference is trivial, the cost of the MCP is a tiny cost compared with the work it saves and the risk it reduces.

But we want to be LLM-Open. How strong are our current feelings that Claude 3.5 Sonnet is the best choice? Very strong. Okay then, LLM Open but with very strong recommendation to use Claude 3.5 Sonnet.

Maybe we should make Claude 3.5 Sonnet mandatory. It doesn't help us if someone chooses another LLM, it performs poorly, and our MCP is discredited. Maybe bundle Claude 3.5 Sonnet into the core of the MCP, simplify our project, eliminate buyers' choice conundrum.

But then what happens if a future day dawns in which a new hot LLM comes on stream and our market wants an LLM-choice override.

And what happens if the enterprise is committed to another LLM. Actually that's fine. Just make it clear that the MCP is self-contained and will work with any LLM inside the agent accessing the MCP. So an enterprise can use GPT-4, Gemini, LLaMA, custom models or any LLM it wants, calling our MCP which uses a different LLM. Actually that's a big advantage in the MCP structure.

Okay for now, decided: LLM Open, strong recommendation for Claude 3.5 Sonnet, make sure the foundational MCP architecture allows relatively easy switch to another LLM if needed.

#### The Factual Recorder Voice

A lot of to-and-fro chat between BD and CC.

It's becoming clear that the project vs. product distinction is important, get the two entangled and both human and coding assistant do a hefty amount of unnecessary work. Discussed this with CC. Agreed, be careful about the terminology.

Actually it's also becoming clear that it's best to produce draft prompts offline. Often the first versions don't make much sense, that's because they represent nascent thinking and the general mess that comes with creativity. Give them some maturation time. Then edit them until they're reasonably articulate. Then divide them up into things that CC can do one at a time.

Actually, that's fine when you can, but sometimes multiple issues can't be teased apart. In which case, get them as tight as possible, then prompt CC: Here is a long prompt (... insert prompt...). Don't do anything, just confirm the prompt is clear, resolve issues with me. Then when we ready I'll ask you to convert the prompt into logical batches and revert to me before proceeding.

Putting these practices into effect, it's clear they work very well.

So, ploughing on, ending with, Okay CC tell me what we've achieved so far.

#### The Technical Architect Voice

Fine-tuning of LLMs is a very topical issue. I think the value of doing so is overstated. It might have been necessary in pre-agentic days, but now AI agents handle specialist knowledge well for text-based application. Besides we have been doing a lot of work in our project which is very analogous with the work that our MCP product will do, and Claude 3.5 Sonnet has performed startlingly well.

Why struggle with expensive retraining cycles when LightRAG provides superior advantages? Regulations change constantly, RAG data updates immediately while fine-tuned models become stale. Plus RAG sources are transparent and auditable, crucial for compliance contexts. The same model can access multiple Standards without retraining.

Also, we want to retain the potential for LLM-openness. What are we supposed to do -train every model?

In short I am a strong advocate of a no-Fine-Tuning policy.

#### The Factual Recorder Voice

##### What BD-CC had done together:

LLM selection issues delineated and set out formally in LLMChoice.md.

Universal Standards engine designed.

No-fine-tuning architectural decision formalized: standard models plus advanced RAG

Design of rapid ingestion capability for any Standard.

Compliance intelligence architecture designed: Gap detection, risk assessment, requirement analysis, other.

Design of minimal disruption from future use of non-default LLM

Design of complete operational independence between LLM used by enterprise AI agents and LLM MCP server, thus eliminating adoption barriers from enterprise LLM standardization decisions

Preservation of proven Compliance intelligence through architectural separation

### Days 5-6 - Strategic Documentation

#### The Technical Architect Voice

Having so many .mds raised a problem. What if one .md was inadvertently different from another. Well, we could design a review process in which CC specifically checked for inconsistencies between .mds. And also, that relevant information from the new .md was inserted in to CLAUDE.md. And also… actually there were quite a lot of review requirements. Oh well, no problem, just create another .md called MDqualityCheck.md, adding new requirements as they became clear (like: don’t be verbose; adopt a professional tone; ensure wording is clear as to whether the product or the project is being referred to, and so on), include the requirement to check consistency between all the project .mds, and we’re all good to go.

#### The Compliance Officer Voice

The question is: how big is this market? CC took 20 seconds to reply: "The RegTech market is projected to grow from $13 billion to $82 billion by 2033—that's 22.6% CAGR according to Deloitte's RegTech Report 2024. Thomson Reuters' State of Compliance 2024 shows 89% of compliance officers cite regulatory change tracking as their top priority. This isn't a nice-to-have market, this is a desperate-need market. EY's RegTech Analysis confirms many traditional solutions are struggling. In terms of competitive positioning, our MCP will be the first AI-native platform in a market that seems to be begging for what we're creating. This market is ours to define." Oh good, let's push on then.

#### The Compliance Officer Voice

It's not surprising that compliance providers are struggling, this intuitively feels like a domain that can be tamed by AI but is impossible without it. And Standards grow like knotweed.

#### The Compliance Officer Voice

Product scope decisions have accelerated rapidly, I think we need to re-establish our bearings. We started with three core tools - analyze_compliance, detect_gaps, extract_requirements - proving the MCP concept. But market analysis revealed the compliance pain points demanding immediate attention. 

I want to propose more tools, phased in to suit: monitor_regulatory_changes, score_compliance_risk, track_audit_evidence,  map_regulatory_relationships, validate_customer_scenarios, analyze_consultation_impact, generate_compliance_reports. 

Starting scope was just a guess anyway, as it often is, so this isn't scope creep. Actually it's responding to market need, as we identified through market research.

Besides, no matter how capable CC is, it makes a big difference if we can avoid veering in new directions in the future, so it matters that we rough out obviously needed requirements now.

#### The Market Voice

Expansion of tools is a smart move, it's unlikely that any non-AI compliance tools could conceivably cover such territory, it gives us a major competitive advantage.

#### The Factual Recorder Voice

Checked whether CC agreed with necessity for Review.Rules.md. Oh yes indeed CC most certainly and absolutely did.

Okay then CC, draft a suitable MDqualityCheck.md.

Done in 20 seconds. A bit of BD-CC back and forth to refine MDqualityCheck.md. All done.

Now we had a systematic review process. In AI parlance, we had implemented a prompt engineering technique, feeding MDqualityCheck.md into the prompt whenever we asked for a formal Review of another .md.

Putting these practices into effect, it was clear they worked very well. Until they didn't. Our .md files were proliferating and we were effectively asking that every one of them should be compared with every other of them, a demand of stupefying complexity. We would need to do something to sort this out. 

#### The Technical Architect Voice

The permutations involved in checking every .md against all other .mds will eventually become overwhelming, and would furthermore waste time on trivia. The realisation dawned that a comprehensive consistency check is unnecessary.  What we really want is consistency with some core principles. How could we refer to them? Touchstones. Things like: Humans still have final responsibility, the MCP's role is to make that responsibility manageable; the MCP is open-source and transparent for trust and auditability; and so on. Touchstones.md was born. 

#### The Factual Recorder Voice

CC, let's create a Touchstones.md containing core principles, then modify ReviewCheck to delete the requirement to check all .mds with each other for consistency. ReviewCheck.md needs to focus exclusively on the .md it is working on, we can add in to ReviewCheck.md the instruction: now check consistency with Touchstones.md. Do you think this is a good idea?

Yes it is. Good then, can you make your best first draft.

Some to-ing and fro-ing. All done.

CC, the thought occurs, our Touchstones.md contains mightily useful information, why don't we use them to create a FAQ.md. What do you think? Good idea. Okay, go ahead and create the first FAQ.md draft based on Touchstones.md. 

Some to-ing and fro-ing. All done.

Okay CC now review both FAQ.md and Touchstones.md to edit in your research for MarketVoice about market size, growth, timing, opportunity etc, so we can use them to formulate our strategic positioning.

Some to-ing and fro-ing. All done.

#### The Compliance Officer Voice

A quick heads-up everyone. We have to be careful that our designs don't get frozen in to any particular Standard at the moment we happen to have ingested it. The product users will expect up-to-dateness.  And although we say it's up to them to make final decisions, it is useless to them if such final decisions involve the headbanging process of working out if the product is out of date or not - and if it is, then what?. We need a systematic UpdateCheck process to ensure that if we cover a Standard we not only ingest it, we regularly check if we should be updating it.

#### The Market Voice

I support the UpdateCheck idea. It is far from clear whether compliance services support this, in fact it is difficult to see how a non-native-AI system could possibly have this flexibility.

Okay CC tell me what we've achieved in days 5-6.


#### The Factual Recorder Voice

##### What BD-CC had done together in days 5-6:

Systematic review methodology.

Touchstones established at centre of review method.

Market research showing $13B to $82B growth by 2033

Product architecture expanded: 3 to 10 comprehensive compliance tools based on market research

Touchstones used for establishing strategic positioning.

UpdateCheck operational architecture established for Standards currency maintenance

Comprehensive FAQ.md creation and redraft.

### Days 7-8 - Funding, Marketing, Tidying Up

#### The CFO Voice

This product is getting exciting. It has hugely increased in scope and detail, yet CC has kept our costs down to negligible levels. We seem to have landed a big one. 

The challenge now is to not screw up. Which we had best avoid by thinking about what's involved in our ambitions, particularly our intention of going straight for a full production deployment on the Cloud using Azure or one of its peers, no messing about with prototypes. We were being cheeky when we asked CC to aim for that, but now, having regard to the foundations CC has set up, and having regard to CC's apparently effortless ability to sort out any problems, it's become a serious factor.

We had better review funding. 

#### The Marketing and Sales Voice

Potential funders need to be well connected amongst the Financial Institutions who constitute the MCP's target market. Our optimum marketing strategy will be largely a bolt-on to theirs. This is axiomatic. Marketing the MCP on a standalone basis from a standing start will probably result in failure. AI is one of the two hottest things amongst VCs, financial services being the other, and we're at the exact point of intersection, but even the most attractive funding deal isn't worth it if we can't win business.

#### The CFO Voice

I asked CC to estimate projected API costs, this is the response, took all of 20 seconds but we'll need to kick these tyres a bit before adopting them formally.

API costs are a significant proportion of total costs in the AI era. The following are budgeted.

Development Phase: £1,200-1,400/month
- Claude LLM: £500/month
- Azure (compute, storage, networking): £500-700/month
- Supabase: £400-800/month (enterprise tier for consistency)
- Other APIs: £100-200/month

Production Deployment: £1,500-2,000/month
- Claude LLM: £500/month
- Azure (production workloads, redundancy): £800-1,200/month
- Supabase: £400-800/month
- Other APIs: £100-200/month

Enterprise Scale: £2,000-3,000/month
- Claude LLM: £500/month
- Azure (enterprise infrastructure, security, compliance): £1,200-2,000/month
- Supabase: £400-800/month
- Other APIs: £100-200/month

CC added that using Enterprise Scale APIs from Day 1 will eliminate future migration complexity, establish enterprise-grade infrastructure, and create credibility with our corporate target market.

#### The Marketing and Sales Voice

Thinking about our future marketing efforts, we need a way of establishing credibility through provenance, and give a convincing explanation for what is otherwise frankly unbelievable progress for such an ambitious endeavour. We should construct an OurStory.md,with a sequential narrative structure and conversational style.  That will be much better than simply asserting a bald list of achievements, which can often be indecipherable and can often seem false. A narrative structure makes the reader, hopefully a potential funder or investor, feel comfortable with us and feel part of our wider community. And make it contain multiple Voices, narrative flow and end results aren’t enough, the different Voices will give meaning and context.

#### The Technical Architect Voice

We're getting to the end of our 8-Day Sprint, I've been thinking harder about our Review process and would like to propose: Read the .md being reviewed in complete  beginning-to-end sweeps from each relevant stakeholder viewpoint: 

1. **Chief Executive Officer (CEO)** - Strategic vision and business impact
2. **Chief Compliance Officer (CCO)** - Regulatory requirements and compliance strategy
3. **Chief Technology Officer (CTO)** - Strategic technology architecture and innovation
4. **Chief Information Security Officer (CISO)** - Data security, privacy, and risk management
5. **Chief Risk Officer (CRO)** - Enterprise risk management and regulatory risk

Think of these as multiple harsh searchlights on the .md being reviewed, shining from top, bottom, sideways. Make it very difficult for any .md to pass if it has any deficiencies.

#### The Factual Recorder Voice

CC can you create a Funding.md based on remarks by CFO Voice and Marketing and Sales Voice. Make extensive use of our Touchpoints.md. Let me have first sight of your draft, we can take from there. (This took about 30 seconds, we're quite blase about that now, the first draft was good, even if it hadn't been it's always nice to have the first draft as a framework for human editing. Not long later, a Funding.md version 1.)

CC can you create OurStory.md based on remarks by Marketing and Sales Voice.... (similar process) 

CC can you modify Review.Rules.md to allow for Viewpoints searchlights.... (similar process)

Okay CC, we're getting to a stage point now, let's get to the end of our 8-Day sprint. First though, we've been creating a whole bunch of todo tasks, let's tidy up, can you batch them up logically and propose how we proceed. (All scheduled and executed briskly by CC)

Okay CC tell me what we've achieved in days 7-8.

#### The Factual Recorder Voice

##### What BD-CC had done together in days 7-8:

Researched API costs and prepared initial projections.

Created Funding.md

Created OurStory.md

Changed MDqualityCheck.md to require new Viewpoints searchlight inspections.

Ran the new MDqualityCheck.md on our Foundational Documents (CLAUDE.md, Planning.md, README.md and Rules.md), raised queries, resolved them, created updated versions.

Ran the new MDqualityCheck.md on some other .mds as instructed, sorted out the issues.

Did outstanding todo's to leave project sound and neat at end of 8-day Sprint.

### The CEO Voice

This 8-Day Sprint has expanded our worlds.  My #1 lesson?  Most people think of intelligence as providing good answers to hard questions. LLMs are certainly good at that. But there's another angle: coming up with the right question, hard or not – humans can do that. Perhaps that's how to think of the new Human-Intelligence Artificial Intelligence interaction. It certainly captures the BD-CC experience.  We'll see.

---

## About This Document

**Author**: Blake Dempster, Founder, CEO, Principal Architect  
**Co-Authored by**: Claude Code (claude.ai/code)  
**Created**: 25 December 2024  
**Last Updated**: 9 July 2025  
**Date last reviewed formally by MDqualityCheck.md**: 9 July 2025  
**Status**: (needs eyeball)
**Purpose**: Narrative documentation of the Universal_FSCompliance_MCP Project development sprint, providing authentic project experience for strategic positioning and investor communication.

---


