# AI for Financial Institutions - Outline of Management Impacts

**Updated**: 3 July 2025

## LLMs, AI Agents, MCPs

- **LLMs are widely thought of as omniscient, or heading that way**
- **Specialist focus is supposedly achieved by fine-tuning the LLM**
- **It would still be fiendishly difficult to ask LLMs the right question**
- **Even formulating a sequence of questions requires effort and time**
- **Better to encapsulate common questions into AI Agents**
- **AI Agents do much better if they can use toolsets**
- **The AI Agent's LLM has the job of deciding which toolset to use**
- **This needs a standard way for toolsets to advertise their capabilities**
- **The MCP protocol is becoming the standard way to do this**
- **The MCP can use a different LLM from that used by the AI Agent**
- **In short, discovering and using suitable MCPs is essential.**

*BD 3 July 2025*

## Is it Safe to Pass Private Data to LLMs?

- **Any private data passed to a proprietary LLM enters into an impenetrable tangle**
- **Proprietary LLMs have a voracious appetite for such data**
- **Public data has already been ingested, private data is a major LLM prize**
- **Experience with social media has shown that use of private data is hard to control**
- **The risks are compounded when AI agents are involved - the agent is in charge**
- **This is problematic for financial institutions - agents are the most powerful use for AI**
- **The solution is to run an opensource LLM *inside* the financial institution's IT stack**
- **This is very manageable given the availability of powerful proven AI software**
- **One consequence is that expensive GPUs will be required in the internal stack**
- **Not all LLMs will be available, but opensource LLMs normally have adequate power**
- **If a particular proprietary LLM is required, separate special measures will be required**

*BD 25 June 2025*

## Software Packages or AI Architecture?

- **Pre-AI, software packages were useful**
- **They were a way of dealing with development risks and costs**
- **They were the cement, bonding innumerable sub-applications**
- **AI architectures are a stronger and more pliable cement**
- **AI coding assistants can replicate software packages cheaply and quickly**
- **AI can quickly eliminate faults, and accommodate new requirements**
- **Powerful new AI platforms are available**
- **Software packages with AI add-ons are arguably an obsolete paradigm**
- **In AI architecture a low level of abstraction is desirable**
- **Low abstraction enables fast, accurate analytics and modification**
- **This architecture transfers power from suppliers to users**
- **These dynamics foundationally affect IT projects**

*BD 18 June 2025*

## Monetisation Potential of Proprietary Data

- **Context: 90% of the world's data is thought to be private**
- **Context: 99.9% of public data has already been ingested by LLMs**
- **Financial institutions' proprietary data is a rich mine of information**
- **Covering behaviour, risk, longevity, health, choices, lifestyle and other factors**
- **Valuable for compliance, risk, market analysis, and many other uses**
- **Layers of legacy systems have previously made such information inaccessible**
- **AI can deal with unstructured data in new and powerful ways**
- **AI can view data semantically rather than structurally**
- **Semantic data by definition allows the *meaning* of data to be accessible**
- **Thus providing more useful insights**
- **The semantic data structure enables unbreachable anonymity**
- **Increasingly, semantic data can be made available commercially**

*BD 11 June 2025*

## AI - Driver of Enterprise Value

- **Successful AI implementation substantially reduces operating costs**
- **These cost reductions can reach 80% in many operational areas**
- **AI radically reduces the spend on associated IT**
- **Gearing effects mean that the cost reductions drive large earnings increases**
- **With an unchanged PE ratio, this translates directly to Enterprise Value**
- **The PE ratio will sharply increase in recognition of effective use of AI**
- **Near-doubling of Enterprise Value is readily achievable, for example:**

| *Item* | *Limited AI* | *AI Inroads* |
|--------|--------------|--------------|
| **Operating Revenue** | 1000m | 1000m |
| **Operating Costs** | -800m | -700m |
| **Earnings** | =200m | =300m |
| **PE Ratio** | x14 | x16 |
| **Enterprise Value** | =2800m | =4800m |

*BD 4 June 2025*

## Why is AI Different for Financial Institutions?

- **Current AI technologies can meet most needs**
- **Nano-second responsiveness is generally not needed**
- **Multi-modal AI capability is generally not needed**
- **Lower-specced LLMs are generally more than adequate**
- **Complexity and legacy are near-unmanageable without AI**
- **Chatbot access to LLMs barely scratches the AI surface**
- **AI agents are particularly important, for handling multifaceted tasks**
- **AI coding assistants have transformed system development**
- **Market entrants can use AI as the means of disrupting incumbents**
- **Humans-in-the-loop are essential, for QM, compliance and accountability**
- **Resource requirements are radically changed, especially IT and HR**
- **Bureaucratic bloat can be slashed, efficiency increased by 5x or more**

*BD 28 May 2025*

## LLM Fine-Tuning

- **Fine-tuning first emerged as a response to unsatisfactory LLM responses**
- **The thinking is: tweak the LLM's inner parameter values to tune it to particular needs**
- **There are billions of parameters, approximation techniques are applied**
- **It is not clear whether fine-tuned LLMs show demonstrably superior results**
- **It is onerous to assemble the particular data to which the LLM is being tuned**
- **Non-tuned LLMs are improving so fast as often to outpace the effect of fine-tuning**
- **Fine-tuning multiple fast-changing LLMs is not feasible**
- **Different LLMs do different things well, better to select the right one for the specific task**
- **AI agents enable use of multiple best-for-purpose LLMs for multi-task jobs**
- **In-house data are arguably better used for injecting into prompt than for fine-tuning**

*BD 21 May 2025*

## Guard Rails

- **Guard rails make AI safe to use**
- **Guard rails formalise the boundaries that reasonable humans would observe**
- **AI agents now make guard rails manageable and adaptable**
- **AI guard rail agents operate at the input and output stages**
- **Input guard rail agents can include compliance with AI usage standards**
- **E.g. "return error if user request breaches decency standards"**
- **Output guard rail agents can include compliance with regulatory standards**
- **E.g. "return error if response breaches FCA Handbook requirements"**
- **One LLM can be used at input, another for the main query, a third at output**
- **Guard rail breaches can be handled through automatic feedback loops**
- **An audit trail can be automatically created**
- **Protection from hallucinations is enhanced**
- **Quality and compliance are engineered in, not stapled on**
- **Delivery of service is much faster and safer than is possible by humans alone**

*BD 14 May 2025*

## The Evolution of "Prompting"

1. **Prompting is what humans do to interact with LLMs**
2. **Or, a prompt is the text that is entered into a chatbot**
3. **The more skilful the prompt, the better the result**
4. **Then: Very long "context windows" for prompts became possible**
5. **But long prompts can simply introduce confusion**
6. **Then: Prompt libraries were developed to improve prompt quality**
7. **Then: External data were provided as context: RAG was born**
8. **Then: Specified apps were injected into the prompt: Tools were born**
9. **Then: A standard means of injecting tools developed: MCP was born**
10. **Then: Common data and tools were encapsulated: AI Agents were born**
11. **Then: Agent orchestration capabilities developed**
12. **Then: Agent monitoring and audit frameworks developed**
13. **LLMs: Not the source of information, more for deciding what to do**
14. **Outcome: Careful architecture, then massive productivity gains**

*BD 8 May 2025*

## Is Action on AI Urgent?

- **The coming of massive processing power brings fundamental change**
- **The transformer architecture and LLMs also bring fundamental change**
- **Change has accelerated with the emergence of capable AI agents**
- **Enterprise valuations can be significantly raised if effective AI action can be shown**
- **Overheads and costs can be radically reduced**
- **The technology is moving so fast that a methodical, systemic response is needed**
- **A major spur to action is that all existing IT projects may themselves be obsolescent**
- **The smart way forward is to have a priority list, get results, learn, re-prioritise, apply.**

*BD 1 May 2025*

## Agentic AI Connectivity

- **AI agents have already transformed the potential of AI for enterprises, now the pace of change is accelerating thanks to emerging standard frameworks for interconnectivity**
- **MCP ("Model Context Protocol"), put forward by Anthropic, is for making data and executable functions, called "tools", available to AI agents**
- **A2A (Agent-to-Agent), put forward by Google, is for making it easy for AI agents to use other AI agents**
- **MCP and A2A are not software, they are open and public frameworks**
- **They allow AI agents to be applied in a standard way and have been widely adopted**
- **Using MCP and A2A, a chosen LLM decides how to use the tools, data, and other AI agents**
- **This is normally initiated by a prompt from a human**
- **Third-party data, tools, and AI agents are easily available, comparable with APIs**
- **However there are many security, testing and complexity issues**
- **The optimum approach is to be MCP- and A2A- ready but not yet to use third-party offerings**

*24 April 2025*

## How to Generate ROI on AI

1. **Recognise that Enterprise AI is not like Consumer AI**
2. **Recognise that AI Agents matter more than any particular LLM**
3. **Compartmentalise enterprise operations, then use specialist AI agents for each**
4. **Use historic, often messy, data to create context for AI**
5. **Use AI query history to create new context and IP**
6. **Capture the value of experienced human-in-the-loop**
7. **Prioritise, based on cost and process pain-points**
8. **Scale early for production, no need for micro-prototypes**
9. **Incorporate into existing workflows, so the AI is actually used**
10. **Go for speed plus feedback loops - better than perfection**

*17 April 2025*

## AI-Induced Strategic Risks

1. **Strategic vision misaligned with AI potential**
2. **Disconnect between understanding of business and understanding of AI**
3. **Response inadequate to impending AI-originated obsolescence**
4. **Current AI work does not pragmatically meet actual business needs**
5. **Conceiving AI as merely a LLM chatbot, ignoring Agentic AI**

*10 April 2025*

## How Do We Gain Advantage?

**Yes, we understand...**
- **... how AI is set to change the world**
- **... how infrastructure build-out is happening fast**
- **... how LLMs are becoming ever more powerful**
- **... about fine-tuning, RAG, opensource**
- **... about AI Agents**
- **... about using multiple LLMs incl. DeepSeek**
- **... about MCP and A2A as connectivity standard frameworks**
- **... how LLM hallucinations and guardrails are managed**
- **... how long-term agentic memory builds knowledge**
- **... how AI can convert our proprietary data into IP**
- **... how major efficiencies can be achieved**
- **... how innovation is accelerating**

**Q: BUT HOW DO WE GAIN ADVANTAGE???**

**A: Through the careful, phased assembly of AI agents**

*2 April 2025*

## AI Evolution Q1 2025

- **The agentic AI ecosystem is newly mature - only since Jan 2025**
- **It is powerful for FCA and other regulatory compliance - and more widely**
- **Prior AI preoccupations are now more easily manageable, incl...**
- **...choice of LLMs eg DeepSeek, fine-tuning, prompt engineering, guard rails**
- **An emerging heuristic is: 80% cost reduction (= 5x performance) for many corporate functions**
- **Agentic AI is relevant to all current projects, incl...**
- **...IT, data, business processes, cost optimisation, skills**
- **Agentic AI requires astute management...**
- **...in projects, in strategic direction, in service provision**

*28 March 2025*

## AI Things to Watch Out For

- **Autonomy / FSD is not yet feasible, ie humans-in-the-loop are still necessary - regulators will want to see this in their domains anyway**
- **The costs of gathering client in-house data can be high - but this becomes client IP once stored in a semantic database**
- **New agentic AI systems can be incorporated into workflows using appropriate tools**
- **Employees' careers will be radically affected, appropriate policies are needed**
- **It is important for directors to have a wide understanding of what is happening with agentic AI, they still have ultimate responsibility**
- **The AI ecosystem is evolving fast, staying flexible is important**

*21 March 2025*

## AI Agents

- **AI agents are modules that do specialised, well-defined, compartmentalised jobs**
- **They have access to data and tools that are designed for the job**
- **Where LLMs tend to be amorphous and sprawling, AI agents are focused and specific**
- **Within the AI agent, the LLM's job is to make best use of specified information to generate answers to user prompts**
- **An AI agent is analogous to a human "agent", but taking seconds to do what a human would do in days - but still fallible**
- **Broadly AI agents can be viewed as doing things right, but not necessarily doing the right things: humans-in-the-loop are still needed, but their effectiveness is greatly increased**
- **AI agents provide a way around the problem that LLMs themselves are not reliable sources of truth**
- **AI agents can use tools which safely make messy private data useful, thus unlocking IP**
- **AI agents mean that private data, believed to comprise 90% of the world's information, can safely be made AI-available to the data owner**
- **Training of LLMs is expensive and its usefulness may be superseded by AI agents**
- **It is important that AI agent design retains the ability to switch between LLMs - different ones are good at different jobs**
- **Specified information eg FCA Handbook is supplied to the AI agent in a well defined RAG pipeline**
- **The specified information is usually stored in semantic vector or graph databases**
- **AI agents radically reduce hallucinations**
- **AI agents can include methods to store and learn from history of user AI interactions, and use the history to provide better responses**
- **AI agents tend to proliferate, they need to be managed through automated workflow systems**

*14 March 2025*

## Compliance and QA

- **Apply AI to FCA and other regulatory compliance**
- **Apply same methods to QA, standards, mandates, guardrails**
- **Manageable scale**
- **Pragmatic early AI experience**
- **Create an early AI trophy**
- **Increase compliance efficiency by 5x**
- **Reduce friction, increase agility**
- **Safely crystallise huge value of proprietary data**
- **Leverage lessons into wider AI applications.**
- **Retain adaptability for burgeoning AI ecosystem**

*7 March 2025*

## AI for FCA and Other Compliance

- **Powerful for FCA, PRA and other codes**
- **A high value, pragmatic AI use-case**
- **A method, not a software package**
- **No need to use frontier LLMs**
- **Can use opensource incl. DeepSeek**
- **Option to switch between LLMs**
- **Radically enhances human value**
- **Minimises LLM fine-tuning**
- **Embeds corporate AI guard rails**

*28 February 2025*

## DeepSeek - Ramifications

**Update.** May 2025 update of RI model delivers even better performance.

**Cost.** 95% lower cost than comparable LLMs.

**MIT License.** Free to use for commercial purposes.

**Business Landscape.** DeepSeek appears set to shift the balance of power away from LLM providers towards LLM applications, software, and users (such as financial institutions).

**Quality.** Generally, amongst the best performing LLMs.

**Architecture.** Quality is achieved through elegant use of Reinforcement Learning applied to a large number of advanced and difficult test cases, combined with sophisticated filtering techniques.

**Security.** If accessed via DeepSeek API, security is sieve-like. If run locally, security is amenable to normal disciplines.

**Opensource.** DeepSeek is opensource, giving its inner workings exposure to armies of developers and millions of pairs of eyes - arguably the most powerful quality test.

**Local Version.** Using Ollama or similar, the DeepSeek engine can be downloaded to run locally, and achieve high levels of performance and security.

**Agentic RAG.** For many purposes the most effective way to apply DeepSeek is as part of regular Agentic RAG pipelines.

**LLM Menu.** It is usually smart to enable any AI agent to access any model suitable for purpose. DeepSeek can simply be added to the menu of possible options.

**Risk Management.** The menu approach finesses the need to make once-forever commitments. If doubts emerge, eg over DeepSeek's provenance, the menu option can simply be turned off.

**Human-in-the-Loop.** Applications which retain humans-in-the-loop, such as Compliance eg with the FCA Handbook, are particularly well placed to consider DeepSeek - the human provides the commonsense test.

*21 February 2025, updated*

## About

**This Outline of Management Impacts originated in an AI project with a major firm of legal advisers.**

**The focus of the original project was on Compliance with FCA Handbook requirements for UK financial institutions.**

**This broadened into compliance with other regulatory, statutory, legal, mandate and management requirements.**

**The principles proved applicable for many other enterprise AI applications in financial institutions.**

**One of the biggest challenges is keeping senior management briefed on AI issues, at a time of explosive change in AI.**

**The author, Blake Dempster, has been tasked with creating an Outline which:**

- **concentrates on the special AI requirements of financial institutions**
- **focuses on what to do about AI, and why (not so much the how, which AI readily solves)**
- **seeks to filter out hype**
- **takes account of the many moving parts in the fast-evolving AI ecosystem**
- **is built on under-the-hood application of AI concepts, techniques, and technologies**
- **carries knowledge at a coding level**
- **gives management context in which to make AI-related strategic decisions**
- **forms a statement of principles to align AI project participants with management vision**

**This Outline is a public version of the Outline.**

---

## About This Document

**Author**: Blake Dempster, Founder, CEO, Principal Architect  
**Created**: 9 July 2025  
**Date last reviewed formally by MDqualityCheck.md**: 9 July 2025  
**Status**: (okay)
**Purpose**: Management briefing on AI issues for financial institutions, converted from HTML format for AI-friendly access and integration into the Universal_FSCompliance_MCP Project documentation.

---