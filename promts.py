"""
Prompt templates for the microfinance loan decision-support pipeline.

Evolution notes:
- SUMMARY_PROMPT went through two versions. V1 was a naive one-line instruction
  ("Summarize this:") with no role or constraints, it produced inconsistent
  length and occasionally invented/embellished details. V2 added an explicit
  role (assistant to a loan officer), hard constraints (factual, neutral, no
  invented details, 3-4 sentences), and was run at temperature=0 for consistency.

- EXTRACT_PROMPT was designed from the start with a strict JSON schema, one
  few-shot example (using a letter NOT in the evaluation set, to avoid
  contaminating the test), an explicit "use null, do not guess" instruction,
  and temperature=0. This was necessary because free-form extraction without
  a schema and example produced inconsistent field names and occasional
  invented values for fields the letter didn't state.

- BRIEF_PROMPT was built last, taking both the raw letter and the extracted
  JSON as input. It explicitly forbids the words "approve"/"reject" and states
  that the human officer makes the final decision, to keep the system as
  decision SUPPORT rather than a decision-maker.
"""
