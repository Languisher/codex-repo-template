# Debugging Workflow

1. Capture the exact symptom, command, input, and expected behavior.
2. Reproduce with the narrowest command possible.
3. Trace the failing path through source, tests, schemas, and configs.
4. Identify the broken invariant.
5. Add regression coverage when practical.
6. Fix the root cause with the smallest coherent change.
7. Rerun the failing command and then broader verification.
