# 2026-10-03 — One more agreement: coefficient-fiber source review

Completed exactly one literature-only step for the saved A=k+1 target.
Read the shared/local instructions, complete argument overview, ID-only DAG,
pinned model, existing assessment and endpoint result; preserved all existing
changes. The prior A=k coverage was reused, with additional reading justified
by the new coefficient constraint and missing subgroup fiber comparison.

The [completed assessment](../drafts/literature/2026-10-03-root-product-one-more-agreement.md)
records the primary queries and statements: Zhu-Wan's subgroup subset-sum
estimates, Li-Wan's exact full-nonzero-field formula and scalar coefficient
dictionary, and the already known common-pivot construction. Full-field,
subgroup and coset assumptions are separated. A possible subfield instance
is covered for a later test, with the ambient field retained in epsilon* q;
no instance or count has been calculated. The exact saved target is unchanged
and now has DECISION: SPECIALIZE, with preapproved applicability subtargets.

Outcome: EXPLORATION; STEP_KIND: LITERATURE; classification:
NOVELTY_UNCHECKED. This is new source coverage and a continuation decision,
not a new bound, negative theorem or claimed novelty. The cited constructions
and counts are known; the later local application should be REPRODUCTION.
Exploration turns remain 0/3 because this review spends no calculation budget.

The main gap remains t_star below the unsafe endpoint in the smaller-field
regime. The next mathematical test is a common-center coefficient-fiber list
at k+1 agreements with the strict degree/domain/tuple checks and a count
compared with the actual threshold. An unsafe witness could constrain the
boundary; an unsuccessful lower certificate would not establish safety.
The full boundary, general cover and ABF26 comparison remain unresolved.
The parked source-recovery failure was not retried. No complete candidate
appeared; STATUS stays IN_PROGRESS.

Only the assessment, current checkpoint and this history were edited.
PROOF.md and DAG.md retain the same assembled mathematics. Preservation
hashes confirm all 30 existing overview, lemma and script files are unchanged.

Validation: `PYTHONDONTWRITEBYTECODE=1 python3 ../scripts/docs/check_structure.py --problem reed-solomon-list-decoding`
passed with 12 nodes and 9 edges; `git diff --check -- .` passed. Required
fields are unique and NEXT_REVIEW matches the verbatim Next action with
SPECIALIZE coverage. The checkpoint has 15 lines and the overview 97.
No mathematical/computational check was needed for this source-only step.
