# The Universal_FSCompliance_MCP Project Development Rules

This document establishes development guidelines and conventions for the Universal_FSCompliance_MCP Project to ensure consistency, quality, and regulatory compliance across all code contributions. These rules reflect enterprise-grade development practices and financial services regulatory requirements.

## 🔄 Project Awareness & Context

- **Always read `PLANNING.md`** at the start of a new conversation to understand the project's architecture, goals, style, and constraints.
- **Check `Tasks.md`** before starting a new task. If the task isn't listed, add it with a brief description and today's date.
- **When reviewing .md files**, follow the systematic methodology in `MDqualityCheck.md` with Touchstones.md consistency checks.
- **Use consistent naming conventions, file structure, and architecture patterns** as described in `PLANNING.md`.
- **Maintain MCP protocol compliance** - ensure all server implementations follow MCP specification requirements.

## 🧱 Code Structure & Modularity

- **Never create a file longer than 500 lines of code.** If a file approaches this limit, refactor by splitting it into modules or helper files.
- **Organize code into clearly separated modules**, grouped by feature or responsibility.
- **Use clear, consistent imports** (prefer relative imports within packages).
- **Follow the layered architecture** defined in Planning.md (MCP Server, Knowledge Management, Compliance Intelligence, Memory/Learning, LLM Abstraction).
- **Maintain LLM architectural independence** - Our MCP server operates independently from enterprise AI agent LLM choices per LLMChoice.md strategy.

## 🧪 Testing & Reliability

- **Always create Pytest unit tests for new features** (functions, classes, routes, etc).
- **After updating any logic**, check whether existing unit tests need to be updated. If so, do it.
- **Tests should live in a `/tests` folder** mirroring the main app structure.
  - Include at least:
    - 1 test for expected use
    - 1 edge case
    - 1 failure case
- **Include compliance-specific test cases** - test regulatory requirement parsing, compliance gap detection, consultation document analysis, and privacy controls.

## ✅ Task Completion

- **Mark completed major tasks in `Tasks.md`** when finishing phase-level development work
- **Use `internal/todos.md`** for granular work tracking and detailed improvements  
- **Add new sub-tasks or TODOs discovered during development** to `internal/todos.md` for detailed tracking
- **After completing batch of todos, recommend how Tasks.md should be updated** based on completed work, and seek confirmation before making changes

## 📝 Git Commit Guidelines

- **Use co-authorship for all commits**: When committing to GitHub, always use Co-authors: BD and Claude Code in the commit message.
- **Follow this commit message format**:
  ```
  Brief descriptive title
  
  Detailed description of changes...
  
  Co-authors: BD and Claude Code
  ```

## 📎 Style & Conventions

- **Use Python** as the primary language.
- **Follow PEP8**, use type hints, and format with `black`.
- **Use `pydantic` for data validation**.
- Use `FastAPI` for APIs and `SQLAlchemy` or `SQLModel` for ORM if applicable.
- **Use Poetry for dependency management** as specified in Planning.md.
- Write **docstrings for every function** using the Google style:
  ```python
  def example():
      """
      Brief summary.

      Args:
          param1 (type): Description.

      Returns:
          type: Description.
      """
  ```

## 📚 Documentation & Explainability

- **Update `README.md`** when new features are added, dependencies change, or setup steps are modified.
- **Comment non-obvious code** and ensure everything is understandable to a mid-level developer.
- When writing complex logic, **add an inline `# Reason:` comment** explaining the why, not just the what.
- **Document regulatory implications** - add comments explaining how code relates to specific FCA requirements, consultation document analysis, or Standards processing when applicable.

## 📋 Strategic Documentation Standards

- **Maintain brand consistency** across all documentation using `Brand.md` guidelines and positioning language.
- **Separate internal vs public** documentation - use `internal/` folder for sensitive strategy materials and stakeholder presentations.
- **Cross-reference strategic documents** - ensure alignment between `ComplianceTools.md`, `Brand.md`, and technical implementation.
- **Professional presentations** - create HTML versions for stakeholder presentations when needed, following brand guidelines.
- **Market positioning accuracy** - validate all external claims against `ComplianceTools.md` analysis and competitive research.
- **Attribution consistency** - include proper co-authorship attribution in About sections of all strategic documents.

## 🔒 Security & Privacy

- **Never log sensitive financial data** or personally identifiable information.
- **Implement privacy controls** for all memory and learning features as specified in Planning.md.
- **Use secure authentication patterns** following OAuth 2.1 framework.
- **Validate all inputs** especially when processing regulatory documents or customer data.

## 🤖 AI Behavior Rules

- **Implement MCP tools that turbocharge AI effectiveness** - ensure all compliance tools transform general AI agents into compliance experts with specialized intelligence
- **Support universal Standards processing** - design code to handle regulatory frameworks, industry codes, statutory requirements, international standards, jurisdictional regulations, and consultation documents

- **Never assume missing context. Ask questions if uncertain.**
- **Never hallucinate libraries or functions** – only use known, verified Python packages.
- **Always confirm file paths and module names** exist before referencing them in code or tests.
- **Never delete or overwrite existing code** unless explicitly instructed to or if part of a task from `TASK.md`.
- **When working with compliance logic, always reference specific FCA Handbook sections, consultation documents, or relevant Standards** and include source citations in comments.

---

## About This Document

**Author**: Blake Dempster, Founder, CEO, Principal Architect  
**Co-Authored by**: Claude Code (claude.ai/code)  
**Created**: 25 December 2024  
**Last Updated**: 9 July 2025  
**Date last reviewed formally by MDqualityCheck.md**: 9 July 2025  
**Status**: (needs eyeball)
**Purpose**: Development standards and conventions for the Universal_FSCompliance_MCP Project ensuring consistency, quality, and regulatory compliance across all code contributions.

*These rules ensure the Universal_FSCompliance_MCP Project maintains high standards for code quality, security, and regulatory compliance throughout development.*

---