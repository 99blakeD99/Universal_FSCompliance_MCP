# The Universal_FSCompliance_MCP Project Development Rules

This document establishes granular coding conventions for the Universal_FSCompliance_MCP Project to ensure consistency and quality. The project builds AI-native compliance intelligence for financial services regulatory requirements. For strategic guidance and architecture, see CLAUDE.md.

## 🔄 Project Context

- **Read `CLAUDE.md` first** for architecture and implementation guidance
- **Use standard-specific tool naming** with prefixes: `FCA_quickly_check_compliance`
- **Database table prefixes**: `fca_`, `mifid_`, `sec_` per `DatabaseStrategy.md`

## 🧱 Code Structure & Modularity

- **File size guidelines**: 500 lines preferred, 1000 lines maximum. Split larger files into modules.
- **Organize code into clearly separated modules**, grouped by feature or responsibility
- **Use clear, consistent imports** (prefer relative imports within packages)
- **Maintain LLM architectural independence** - MCP servers operate independently from enterprise AI agent LLM choices

## 🧪 Testing & Reliability

- **Create Pytest unit tests** for all new features
- **Tests in `/tests` folder** mirroring app structure
- **Minimum coverage**: Expected use + edge case + failure case
- **Test compliance-specific cases**: regulatory parsing, gap detection, privacy
- **Test multi-server independence** and AI agent tool discovery

## ✅ Task Management

- **Mark major tasks in `Tasks.md`** when completing phase-level work
- **Use `internal/todos.md`** for granular work tracking
- **Add discovered sub-tasks** to todos for detailed tracking

## 📝 Git Commit Guidelines

```
Brief descriptive title

Detailed description of changes...

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

## 📎 Style & Conventions

- **Python 3.11+** as primary language
- **Follow PEP8**, use type hints, format with `black`
- **Use `pydantic v2`** for data validation
- **Use `FastAPI`** for APIs, **Poetry** for dependency management
- **Google-style docstrings** for every function:
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

## 📚 Documentation Standards

- **Comment non-obvious code** with `# Reason:` explaining why, not what
- **Document regulatory implications** - relate code to specific regulatory requirements when applicable
- **Reference regulatory sections** in compliance logic with source citations

## 🔒 Security & Privacy

- **Never log sensitive financial data** or PII
- **Implement privacy controls** for all memory/learning features
- **Use secure authentication patterns** (OAuth 2.1)
- **Validate all inputs**, especially regulatory documents and customer data

## 🤖 AI Development Guidelines

- **Never assume missing context** - ask questions if uncertain
- **Never hallucinate libraries** - only use verified Python packages
- **Confirm file paths exist** before referencing in code/tests
- **Never delete existing code** unless explicitly instructed or part of defined task
- **Reference specific regulatory sections** in compliance logic with source citations

---

## About This Document

**Author**: Blake Dempster, Founder, CEO, Principal Architect  
**Co-Authored by**: Claude Code (claude.ai/code)  
**Created**: 25 December 2024  
**Last Updated**: 19 July 2025  
**Date last reviewed formally by MDqualityCheck.md**: 19 July 2025  
**Status**: (okay) - Streamlined to focus on granular coding conventions  
**Purpose**: Granular coding conventions and development practices for Universal_FSCompliance_MCP Project. For strategic guidance and architecture, see CLAUDE.md.

---