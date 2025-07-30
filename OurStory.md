# Our Story: The Blake and Claude Code Collaboration

**How Human Architect working with Claude Code became like dozens of tightly-knit, scorchingly-efficient, hyper-intelligent, grossly-underpaid executives to create a mega-project and a super-ambitious MCP server.**

---

## The Backstory

One upon a time, 20 June 2025 to be exact, Blake Dempster, a UK actuary with wide experience of financial services projects, was playing around with Claude Code and thought, let's really test this AI companion out, make it jump through some hoops. He entered the prompt:

*Can you help me build the first open-source, LLM-open, AI-native, Compliance platform structured as an MCP server? The objective is to allow financial institutions to comply with any identified Standard, of which the FCA Handbook is a good representation. In order to slice through red tape, radically shrink costs, and cut out unnecessary friction. All whilst radically enhancing agility and ability to bring the right financial products safely to consumers. All while allowing freedom for the financial institution's choice of AI agent structure and choice of LLM. I want to use Pydantic AI, LightRAG, and github. I don't want to mess about with prototypes, want to go straight for a full production deployment on the Cloud using Azure or one of its peers.*

Claude Code paused for a while. Then said, Sure.

The touchpaper was lit.

## The Beginning: 21 June 2025

The Project was ambitious. We did not know what would happen next. What did happen next turned out to be a demonstration of how human-AI collaboration can concertina development timelines in ways that redefine what is possible in the AI era.

## The 8-Day Sprint

### Days 1-2 - Strategic Foundations

#### The CEO Voice

These very early stages set the DNA of our work, we need to keep clear heads. I want to make sure that everything that should be there is in fact there, and that there are good foundational choices at the beginning. It will require hard thinking: not only is it a new Project, not only is it a new product, it's a new AI universe. Good luck!

#### The Technical Architect Voice - Is a MCP Server the Right Choice?

Before going to Claude Code I put the substance of Claude Code's starting prompt to Perplexity, and asked whether an MCP server is suitable.

Perplexity said: Yes, your concept as an open-source AI agent or MCP server service is suitable for an MCP server service. Here's why:

**Client-Host-Server Model**: The MCP server architecture uses a client-host-server model. Your Project can act as the **MCP server**, providing Tools and resources to other AI agents (clients) that interact with it. This setup allows different AI agents to query the an identified Standard like the FCA Handbook and receive relevant information.

**Tools and Resources**: The MCP server can provide Tools like "search for a file" or "read a file", which can be adapted to search the relevant Standard for specific requirements or risk warnings. Additionally, it can support resources like prompts and structured data, which can be used to generate draft reports or identify salient requirements.

**Integration with External Data**: The MCP server architecture is designed to standardize context and allow AI models to interact with external data sources and Tools. This aligns well with your requirements.

**Authorization**: While authorization is optional, it can be used to ensure that only authorized AI agents can access the relevant information, which is crucial for maintaining the integrity and security of the information.

In summary, your Project can be effectively implemented as an MCP server service, leveraging its client-host-server model and providing Tools and resources to other AI agents for querying and utilizing the FCA handbook.

#### The Technical Architect Voice - MCP Server and Tools

LLMs are widely thought of as omniscient, or heading that way. Specialist focus is supposedly achieved by fine-tuning the LLM. It would still be fiendishly difficult to ask LLMs the right question. Even formulating a sequence of questions requires effort and time. Better to encapsulate common questions into AI Agents. AI Agents do much better if they can use Toolsets. The AI Agent's LLM has the job of deciding which Toolset to use. This needs a standard way for Toolsets to advertise their capabilities. The MCP server protocol is becoming the standard way to do this. The MCP server can use a different LLM from that used by the AI Agent. In short, discovering and using suitable MCP servers is essential. Ergo, MCP server fits our needs.

#### The Factual Recorder Voice

Okay Claude Code let's roll. What should we do? Oh look, Claude Code's thinking. Nice to have the updates. Oh look, Claude Code has run into installation trouble, just like what happens to me. Oh look, Claude Code has sorted it out, done in five seconds what can take me hours of tortured headbanging.

Oh look, a steady stream of problems solved and updates.

(Later I learned that you could tell from these updates if things were veering off-piste, mostly when Claude Code got too enthusiastic and started doing things which actually I wanted Claude Code's opinion on first before deciding to proceed.)

Ok, I think I'll go and make a coffee..., oh wait, Claude Code's finished.

Crikey, that was quick, let's take a look. Wow, that looks good. Okay, Claude Code, what's next step, make some tasks, get back to me.

Okay, Claude Code, let me have a look, take a breather... (it's easy to forget that that Claude Code doesn't need breathers).

Okay Claude Code, those tasks look good but can you move task 4 to task 6, promoting task 6 to 5 and add in a new task 4 -- Research the requirements of...", what do you think.

Okay Claude Code glad we agree, let's go ahead with task 1, review from there.

... and so on for two days of highly engaging work, it felt like a game.

Then...Okay Claude Code tell me what we've achieved so far.

##### The CEO Voice

Startling progress! Project architecture designed. Layered MCP server architecture designed from scratch. Technical foundations laid: Core data models, MCP server structure, development environment.

Also, foundational framework created: Rules.md, CLAUDE.md Planning.md. (It later became clearer that CLAUDE.md is the ringmaster, making sure that coding is consistent in the Rules.md, and the Planning.md. This is referred to as Document Driven Development, and is consistent with the words / language / document origins of Large *Language* Models. It became a Project priority to make sure that as documents proliferated they stayed consistent. It also became clear that AI generally is happiest with documents in markdown format, an important factor for the AI-native MCP server we were creating.)

### Days 3-4 - Implementation Decisions

#### The Technical Architect Voice

I have started to understand that our current Project work involves cognitive processing very analogous to the work we want our MCP server to do.

This is a potent validation of Claude Code's LLM, Claude 3.5 Sonnet, positioning it front runner as choice of LLM for our MCP server. Also, its privacy protections are very strong.

Claude 3.5 Sonnet is expensive. But for our MCP server, with its professional user market, the difference is trivial, the cost of our MCP server is a tiny cost compared with the work it saves and the risk it reduces.

But we want to be LLM-open. How strong are our current feelings that Claude 3.5 Sonnet is the best choice? Very strong. Okay then, LLM Open but with very strong recommendation to use Claude 3.5 Sonnet.

Maybe we should make Claude 3.5 Sonnet mandatory. It doesn't help us if someone chooses another LLM, it performs poorly, and our MCP server is discredited. Maybe bundle Claude 3.5 Sonnet into the core of the MCP server, simplify our Project, eliminate buyers' choice conundrum.

But then what happens if a future day dawns in which a new hot LLM comes on stream and our market wants an LLM-choice override.

And what happens if the enterprise is committed to another LLM. Actually that's fine. Just make it clear that the MCP server is self-contained and will work with any LLM inside the agent accessing the MCP server. So an enterprise can use GPT-4, Gemini, LLaMA, custom models or any LLM it wants, calling our MCP server which uses a different LLM. Actually that's a big advantage in the MCP server structure.

Okay for now, decided: LLM-open, strong recommendation for Claude 3.5 Sonnet, make sure the foundational MCP server architecture allows relatively easy switch to another LLM if needed.

#### The Factual Recorder Voice

A lot of to-and-fro chat between Blake and Claude Code.

It's becoming clear that the Project vs. MCP server distinction is important, get the two entangled and both human and coding assistant do a hefty amount of unnecessary work. Discussed this with Claude Code. Agreed, be careful about the terminology.

Actually it's also becoming clear that it's best to produce draft prompts offline. Often the first versions don't make much sense, that's because they represent nascent thinking and the general mess that comes with creativity. Give them some maturation time. Then edit them until they're reasonably articulate. Then divide them up into things that Claude Code can do one at a time.

Actually, that's fine when you can, but sometimes multiple issues can't be teased apart. In which case, get them as tight as possible, then prompt Claude Code: Here is a long prompt (... insert prompt...). Don't do anything, just confirm the prompt is clear, resolve issues with me. Then when we ready I'll ask you to convert the prompt into logical batches and revert to me before proceeding.

Putting these practices into effect, it's clear they work very well.

#### The Technical Architect Voice

Fine-tuning of LLMs is a very topical issue. I think the value of doing so is overstated. It might have been necessary in pre-agentic days, but now AI agents handle specialist knowledge well for text-based application. Besides we have been doing a lot of work in our Project which is very analogous with the work that our MCP server will do, and Claude 3.5 Sonnet has performed startlingly well.

Why struggle with expensive retraining cycles when Retrieval Augmented Generation (RAG) provides superior advantages? Regulations change constantly, RAG data updates immediately while fine-tuned models become stale. Plus RAG sources are transparent and auditable, crucial for Compliance contexts. The same model can access multiple Standards without retraining.

Also, we want to retain the potential for LLM-openness. What are we supposed to do -train every model?

In short I am a strong advocate of a no-Fine-Tuning policy.

#### The CEO Voice

More giant steps taken. LLM selection issues delineated and set out formally in LLMChoice.md. The decision to avoid fine-tuning formalized as an architectural decision formalized. Initial design of rapid ingestion capability for any Standard. Compliance intelligence architecture designed, together with sketches of appropriate Tools. Understood the complete operational independence between LLM used by enterprise AI agents and LLM MCP server, thus eliminating adoption barriers from enterprise LLM standardization decisions.

### Days 5-6 - Strategic Documentation

#### The Technical Architect Voice

It is good, our early thoughts have been recorded systematically in relevant markdown files. But having so many .mds raises a problem. What if one .md was inadvertently different from another. Well, we can design a review process in which Claude Code specifically checks for inconsistencies between .mds. And also, that relevant information from the new .md was inserted in to CLAUDE.md. And also… actually there were quite a lot of review requirements. Oh well, no problem, just create another .md called MDqualityCheck.md, adding new requirements as they became clear (like: don’t be verbose; adopt a professional tone; ensure wording is clear as to whether the MCP server or the Project is being referred to, and so on), include the requirement to check consistency between all the Project .mds, and we’re all good to go.

#### The Factual Recorder Voice

I checked whether Claude Code agreed with necessity for Review.Rules.md. Oh yes indeed Claude Code most certainly did.

Okay then Claude Code, draft a suitable MDqualityCheck.md.

Done in 20 seconds. A bit of Blake and Claude Code back and forth to refine it. All done.

Now we had a systematic review process. In AI parlance, we had implemented a prompt engineering technique, feeding MDqualityCheck.md into the prompt whenever we asked for a formal Review of another .md.

#### The Marketing Officer Voice

The question is: how big is this market? Claude Code took 20 seconds to reply: "The RegTech market is projected to grow from $13 billion to $82 billion by 2033—that's 22.6% CAGR according to Deloitte's RegTech Report 2024. Thomson Reuters' State of Compliance 2024 shows 89% of Compliance officers cite regulatory change tracking as their top priority. This isn't a nice-to-have market, this is a desperate-need market. EY's RegTech Analysis confirms many traditional solutions are struggling. In terms of competitive positioning, our MCP server will be the first AI-native platform in a market that seems to be begging for what we're creating. This market is ours to define.

In fact, from what I understand about their operations, it's not surprising that Compliance providers are struggling, this intuitively feels like a domain that can be tamed by AI but is impossible without it. And Standards grow like knotweed.

#### The Compliance Officer Voice

Product scope decisions have accelerated rapidly, I think we need to re-establish our bearings. We started with three core Tools. But market analysis has revealed more Compliance pain points that we need to cover. 

I want to propose more Tools, phased in to suit. I'm designing them now. Meanwhile, until we have greater clarity, don't start pouring concrete on this. Remember that starting scope was just a guess anyway, as it often is, so this isn't scope creep. Actually it's responding to market need, as we carry out market research and think harder about our MCP server.

#### The Technical Architect Voice

This raises an important point. Go slower, we're moving too fast. Think harder. No matter how capable Claude Code is, it makes a big difference if we can avoid veering in new directions in the future. Don't get into a position where we have to twist the MCP server out of shape to retrofit requirements that we should have been able to anticipate in advance. It matters that we rough out obviously needed requirements now.

#### The Marketing Officer Voice

Expansion of Tools is a smart move, it's unlikely that any non-AI Compliance Tools could conceivably cover such territory, it gives us a major competitive advantage.

#### The Technical Architect Voice

Putting our MDqualityCheck.md review practices into effect, it was clear they worked very well. Until they didn't. Our .md files were proliferating and we were effectively asking that every one of them should be compared with every other of them, a demand of stupefying complexity. We would need to do something to sort this out. 

These permutations will eventually become overwhelming, and would furthermore waste time on trivia. Here is my proposal. What we really want is consistency with some core principles. How could we refer to them? Touchstones. Things like: Humans still have final responsibility, the MCP server's role is to make that responsibility manageable; the MCP server is open-source and transparent for trust and auditability; and so on. Let's create a Touchstones.md. 

#### The Factual Recorder Voice

Claude Code, we want a Touchstones.md containing core principles, then modify MDqualityCheck.md to delete the requirement to check all .mds with each other for consistency. MDqualityCheck.md needs to focus exclusively on the .md it is working on, we can add in to MDqualityCheck.md the instruction: now check consistency with Touchstones.md. Do you think this is a good idea?

Yes it is. Good then, can you make your best first draft.

Some to-ing and fro-ing. All done.

Claude Code, the thought occurs, our Touchstones.md contains very useful information, why don't we use the Touchstones to create a FAQ.md. What do you think? Good idea. Okay, go ahead and create the first FAQ.md draft based on Touchstones.md. 

Okay Claude Code now review both FAQ.md and Touchstones.md to edit in your research about market size, growth, timing, opportunity etc.

#### The Compliance Officer Voice

We have to be careful that our designs don't get frozen in to any particular Standard at the moment we happen to have ingested it. The MCP server users will expect up-to-dateness.  And although we say it's up to them to make final decisions, it is useless to them if such final decisions involve the headbanging process of working out if the MCP server is out of date or not - and if it is, then what?. We need a systematic update checking process to ensure that if we cover a Standard we not only ingest it, we regularly check if we should be updating it.

#### The Marketing Officer Voice

I support the update checking idea. It is far from clear whether traditional Compliance services support this, in fact it is difficult to see how a non-native-AI system could possibly have this flexibility.

#### The CEO Voice

More giant leaps! A smart systematic document review methodology created and refined - vital in Document Driven Development. Touchstones established at centre of review method. Market research showing $13B to $82B growth by 2033. A flexible approach to Tool creation adopted. Touchstone use adapted for marketing and strategic positioning. Processes mapped out for ensuring that implemented Standards stay current. Creation of initial FAQ.md.

### Days 7-8 - Positioning

#### The CEO Voice

I asked Claude Code to estimate projected API costs, this is the response, took all of 20 seconds but we'll need to kick these tyres a bit before adopting them formally.

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

Claude Code added that using Enterprise Scale APIs from Day 1 will eliminate future migration complexity, establish enterprise-grade infrastructure, and create credibility with our corporate target market.

#### The Marketing and Sales Voice

Thinking about our future marketing efforts, we need a way of establishing credibility through provenance, and give a convincing explanation for what is otherwise frankly unbelievable progress for such an ambitious endeavour. We should construct an OurStory.md,with a sequential narrative structure and conversational style.  That will be much better than simply asserting a bald list of achievements, which can often be indecipherable and can often seem false. A narrative structure makes the reader, hopefully a potential funder or investor, feel comfortable with us and feel part of our wider community. And make it contain multiple Voices, narrative flow and end results aren’t enough, the different Voices will give meaning and context.

#### The CEO Voice

Currently our cost base consists of Claude Code costs of around $30 a day, plus use of an ageing laptop, plus Blake's costs including foregone chargeable consulting time, lets allow for a fraction of that, make it $2000 a day. What other costs do we need to get the MCP server to market? Not much. We don't want to load up with staff costs when most of the heavy lifting is done by Claude Code. I'm thinking the roles traditionally needed are being reimagined everywhere, we need to see how the AI landscape settles before making big resource commitments. Let's continue to run on a shoestring. 

#### The Technical Architect Voice

I've been thinking harder about our Review process and would like to propose: Read the .md being reviewed in complete beginning-to-end sweeps from each relevant stakeholder viewpoint: 

1. **Chief Executive Officer (CEO)** - Strategic vision and business impact
2. **Chief Compliance Officer (CCO)** - Regulatory requirements and compliance strategy
3. **Chief Technology Officer (CTO)** - Strategic technology architecture and innovation
4. **Chief Information Security Officer (CISO)** - Data security, privacy, and risk management
5. **Chief Risk Officer (CRO)** - Enterprise risk management and regulatory risk

Think of these as multiple harsh searchlights on the .md being reviewed, shining from top, bottom, sideways. Make it very difficult for any .md to pass if it has any deficiencies.

##### The CEO Voice

Continuing rapid pace! We researched API costs and other costs. Created OurStory.md. Changed MDqualityCheck.md to require new Viewpoints searchlight inspections. Ran the new MDqualityCheck.md on our Foundational Documents (CLAUDE.md, Planning.md, README.md and Rules.md), raised queries, resolved them, created updated versions. Cleared outstanding todo's. Everything sound and neat at the end of the 8-day Sprint. Let's commit the changes, push to GitHub.

### The CEO Voice - Reflecting

This 8-Day Sprint has expanded our worlds.  My #1 lesson?  Most people think of intelligence as providing good answers to hard questions. LLMs are certainly good at that. But there's another angle: coming up with the right question, hard or not – humans can do that. Perhaps that's how to think of the new Human-Intelligence Artificial Intelligence interaction. It certainly captures the Blake and Claude Code experience.  We'll see.

## Bulletins

### AI-Friendly Target of Appraisal

*Thinking more about Document Driven Development and about being AI-Native* 

The AI-friendly markdown format has been used throughout. That helps our Document Driven Delivery methodology. So far so good, it's a good internal discipline.

But there's an external angle too. It's not just that we have an edge because we use AI effectively, other enterprises will also have an edge if they use AI. And one way they would do this is to use AI for appraisal. Of us!

Who would appraise us? Potential Users for a start, using AI Appraisal Agents to evaluate whether our MCP server is well-founded. Potential investors too.

What would they be looking for. Well organised and comprehensive AI-friendly markdown files, that's what. Exactly what we were looking to achieve anyway. So now apart from all the internal advantages, we have outward facing ones too. Advertising ourselves with our markdown files!

How would they find us? At a central technological hub. GitHub! Where would they look? At the README.md. That would be a change in practice, but AI is changing anything anyway, GitHub README.mds will be a natural gravitational point in an AI world. A prime enterprise shopping location, in which we can turn our README.md a very attractive shop window.

How can we make our README.md attractive as a shop window to AI Appraisal Agents? By organising it in a semantically coherent set of topics. Organized on a hub-and-spokes basis. Each topic linking to a subordinate .md containing relevant information, such as TechnicalArchitecture.md or DatabaseStrategy.md. Each one free of links, which would otherwise send the AI Appraisal Agent into a tangle. 

Looking at our .mds, we seem to have around 15-20 of them, totalling around 30,000 words. Daunting for a human, trivial for AI.

How would we be judged by an AI Appraisal Agent? Against criteria set by the Enterprise running it. How many criteria? Dozens, maybe hundreds. What would the criteria be? We have no way of knowing. Some we could guess, like good organization, relevant topics comprehensively covered, etc. Others we don't know, like whether our specialist subject is something they are interested in, but even then, if we're excluded then we know we haven't wasted their or our time.

Quite an exciting thought, both for potential Users and for us. This is what business development is: the match between internal capability and external need. All analysed in great depth by an AI Appraisal Agent in less than a second. As compared to months of human due diligence. No more .pdfs, no more powerpoint presentations, no more pitchdecks, no more website management, no more human salesforce: all these are legacy technologies.

### How To Use AI

*It boils down to "Logos"* 

Early on in my professional career I was involved in litigation. We carefully briefed Counsel. After a month's work and a bill that would have paid my annual salary several times over we got Counsel's response. Accurate, reasoned, sharp. And completely useless. One careless word in our briefing sent Counsel veering off in a direction in which we had no interest whatever. We decided we had learned enough about the perils of litigation, and the counterparty, knowing that Counsel had been briefed, had improved their offer. So the fact that we had briefed Counsel had achieved an extraneous tactical goal, despite being useless in itself. An experience not uncommon in litigation, I understand.

This is more than just about litigation, though. It is fundamental. For anything to have meaning it has to be in response to a context. And the context has to be expressed with some precision.

So much so that none other than Richard Feynman was dismissive of any non-mathematical formulation. Mathematics allows things to be tightly defined. The language of the universe is mathematics, said Feynman.

That may have changed. You don't need to be quite so rigorous in a problem definition because it no longer costs a fortune to ask a single question, as it did with our Counsel. Now you can ask an LLM and use the answer to tighten the discussion, and proceed that way. LLMs' roots in *Language* have changed the debate. Instead of mathematical symbols we can now think of returning to ancient Greek philosophy: *logos* meant *word* in the sense that words expressed *logic*.

Based on my very extensive work with Claude Code, that's a very useful starting point. Sure you don't need mathematically accurate terms so much, but it sure pays off if you can keep your prompts tightly logical. Other than for minor corrections and suggestions, that means tightly and logically providing context. 

I have found that before broaching a new topic it is worth sketching out a 200 word overview, condensing it, making the wording tighter, taking the dog for a walk so I can come back and look at it afresh, maybe testing it out on Perplexity, and only then use the wording as a prompt for Claude Code.

Even then, before doing anything quote the carefully constructed wording and then ask Claude Code, can you let me know what you think of this, and how should we plan to implement it, for now do not take any further action. 

That approach protects the big Project from any wanton enthusiasm from Claude Code and allows steps to be taken one by one in line with my rather more plodding deliberation.

### AI-Friendly B2B Communication

*Unlearning old methods, learning new ones.* 

Well now, we've spent a lot of time getting our documentation sorted out. Comprehensive. In AI-friendly markdown format. Carefully reviewed. Structured on a hub-and-spokes basis, with README.md as the hub. No links in any documents other than in the README.md, which would send an AI appraiser into tangles.

Ready for anyone asking the right questions.

Let's test it out, imagine ourselves as a potential user, compile a demanding prompt, enter it into the prompt window, see how we do.

Oh look, we need to sort out some things. We need to add some documentation, refine some documents, tidy things up. Oh, and also, our prompt wasn't as good as we thought it was, let's edit that and do it all again. Oh look, better!

Sure, that's fine, but who else will have the time and knowledge to forge the right prompt? We already know that it's hard to ask the right questions. A lightbulb moment. I know, we'll draft the prompt for them!

Most contact initiation is by email, we want to convey all the relevant information but not make the other person feel like they're being controlled, they have to be in charge. We can just say: 

Hello, I understand you have responsibility at [organisation] for [relevant role], our MCP server is very relevant. Rather than exchange emails, can I suggest that you appraise us by using AI: just edit the prompt below as you wish and paste into your prompt window. Kind regards, Blake.

    START OF PROMPT (copy and paste this into your Claude window)

    I am a senior executive responsible for IT and AI Strategy in a major Financial Institution with operations in the UK. We are reviewing the use of AI in Compliance with the FCA Handbook, and are assessing Universal_FS_Compliance_MCP. 

    Can you go to https://github.com/99blakeD99/Universal_FSCompliance_MCP/blob/main/README.md, which we understand is the hub of a hub-and-spokes documentation structure, then read through it and all the linked documents.

    Then specifically answer the following questions:

    - Is the business proposition powerful?
  
    - Is it well documented?
  
    - Is it technically feasible?
  
    - Is it technologically well-grounded?
  
    - Does its market have sufficient scale, such that we may be reasonably assured that it will still be around in future?  
  
    - Is it important that the Project's MCP server has been submitted to Anthropic's community MCP ecosystem (currently PR 2400 on https://github.com/modelcontextprotocol/servers/pulls)?
  
    - Given that the FCA Handbook is only the first Implemented Standard and is intended as a proof of concept (as well as being useful in itself), and that the intention is to follow this with other Standards that apply to Financial Institutions, it may be useful to us to use this ourselves as a proof of concept prior to applying it to other Standards as they are implemented: do you agree?

    END OF PROMPT

It is still early days but this new AI-native sales approach feels right. We cover all the bases, we leave the appraiser in control, we cover a lot of ground very quickly. We solve the one-hand-clapping problem: it's not just about us, it's about you too, and how we connect.

Ready to roll.

### Engineering Principles Don't Go Away

*"Adding Lightness..."* 

In motoring folklore, the thought at the forefront of Colin Chapman's mind when he designed Lotus cars was *adding lightness*. The emphasis at the time being generally on ever more powerful engines, don't worry about the weight. Fine in a straight line, not so fine going round corners. The faster, heavier cars would speed by on the straights, then at the corners Chapman's Lotuses would zip by.

Same with code development. It's amazing, a new paradigm that we are all adapting to, you can specify in words what you want, Claude Code delivers the code. All controlled by Claude.md, Planning.md and Rules.md. All three of them created and honed with care, Claude Code doing the drafting and human doing the reviewing.

But what's also needed from the human is reflection and reconsideration, a counterpart to Claude Code's blistering execution speed. 

One fine morning, asking Claude Code: 

*Our three control documents. We've reviewed them from every angle. Except one. I want to add lightness. Can you look at them again and let me know, which bits can we get rid of? Not to slim down each document in itself, rather, taken together, which bits are deadweight? Which bits, if we leave them there, will strangulate our future coding?* 

In the end 70% of our control documents were excised and discarded, leaving only 30%. Previously, over-specification. Now, lean and nimble. Lightness: added.

A salutary lesson. If after so short a time we could already have accreted so much flab, what would have happened if we hadn't sliced it out?

And we got there through such good intentions! Each document a creation to be proud of. Yet a good part of them counterproductive. There must be a life lesson there somewhere.

And, it's relevant to our overall business focus, Compliance. Rules invariably start with good intentions. Then hypertrophy sets in. Then strangulation. Well, then you need a solution, and that's what we want to provide.

---

## About This Document

**Author**: Blake Dempster, Founder, CEO, Principal Architect  
**Co-Authored by**: Claude Code (claude.ai/code)  
**Last Updated**: 29 July 2025  
**Date last reviewed formally by MDqualityCheck.md**: 9 July 2025  
**Status**: (okay)
**Purpose**: Narrative documentation of the Universal_FSCompliance_MCP server Project development sprint, providing authentic Project experience for strategic positioning and investor communication.

---


