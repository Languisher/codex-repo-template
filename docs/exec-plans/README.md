# Execution Plans

Use execution plans for broad, risky, or multi-step work that needs durable
state across a task.

Plans should include:

- goal;
- current context;
- constraints;
- preflight checks;
- implementation steps;
- validation commands;
- risks;
- done condition.

Store active plans under `docs/exec-plans/active/` if the project wants to keep
them in version control, or keep them outside git for temporary planning.
