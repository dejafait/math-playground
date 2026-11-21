# Primitive remainder: source-approved specialization2090

TARGET: Audit the GC13/GC18 primitive-remainder decomposition at q=2 for C034r's fixed bump, including the claimed error O(C_h(0)X^(-1/2)K^(3/2)log^2(2K)) uniformly for 1<=K<=X, before any cumulative-energy use.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused source-notes2080/2082 and stop2089; searched the exact theorem label/GC13 and squarefree coprime-count terminology, plus November21 local references and C034 lemma files. Located Molteni Proposition3.2; no canonical local remainder audit or independently matching weighted remainder was found in this bounded search. Queries and limits: drafts/literature/2026-11-21-primitive-remainder-source-notes-2090.md.
SOURCE_EVIDENCE: Van Hemert v1.0.0,11October2026,DOI10.5281/zenodo.23295277, tagged paper.tex https://raw.githubusercontent.com/LeonardSEO/riemann-xi-zero-detection/refs/tags/v1.0.0/paper/paper.tex ; full thm:log-primitive-remainder/proof/GC12-GC18 lines11613-11717 and preceding GC1-GC11 theorem/proof lines11382-11612 inspected. Molteni Analytic Number Theory Spring2026 rev9.0 Proposition3.2/full floor-sum proof pp68-69; Lee-Leong arXiv2208.06141v5 Theorem2.2(18)-(23)/Table1 inspected. Exact links, hypotheses and reading limits: source-notes2090.
COMPARISON: GC13 already states the desired remainder for the unprojected norm and all h in E; Molteni covers its elementary inner coprime count, not the weighted two-index estimate. GC18 additionally uses GC6 and GC14, retaining both signed sectors. C034r's actual bump lies in E, but its Fourier projection is not GC13's sector. No mathematical audit is completed by this comparison.
GAP: Reproduce the compressed endpoint and uniformity estimates, explicitly handle 1<=X<2 given the gamma setup's X>=q, and distinguish the exact source split from GC18's separate gamma-energy premise. Both signed uppers, cumulative energy and mixed transfer remain unresolved.
REASON: A narrowly justified reproduction checks an unaudited manuscript assertion and its actual-input specialization; the complete proof and primary arithmetic input are now available. This could pay one finite-scale energy-assembly error without closing independent upper-bound gaps. No novelty or new proof is claimed by this literature approval.
LITERATURE_REASON: The change from complete diagonal continuation to the finite-scale GC13/GC18 audit lacked essential exact-audit coverage at invocation. Review2090 supplies that coverage while reusing2080, without repeating the screened Landau or additive-series campaigns; unchanged scope now defaults to mathematics.
SCOPE: q=2, the exact g,h,f,C_h of C034r/C034s, real X>=1 and integer 1<=K<=X, including empty intervals and endpoints. Approves reproduction of GC13 and the source-sector part of GC18; any completed gamma-head conclusion must verify or explicitly assume the separate GC6 energy transfer with its selected cap and input-family hypotheses. No projected-sector replacement, primitive upper, cumulative-energy claim, RH or rightmost-zero premise is approved.

## Approved unchanged target; no mathematics performed here

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. C034r's conditional detector supplies the downstream reason
to test the energy decomposition. C034s fixes the actual GC12 kernel.
C034t and stop2089 are contrasts motivating a different target, not
mathematical inputs proving the remainder. No cross-notebook input.

The separate literature comparison2090 preserves the audit target
verbatim. Source-notes2090 records the exact theorem, corrected full
reading range, essential proof cases and primary arithmetic comparison.
Distinguish the primitive cutoff K from the Fourier band parameter in
C034r. Do not infer a signed primitive upper from an identity or its error.

The prospective audit's discriminating test is whether the exact
claimed error is uniform over the whole stated range, with no hidden
dependence on K, no discarded finite endpoint, and no assumed sign or
subpower upper for either primitive term. A valid reproduction may
leave those independent upper bounds unresolved. A precise failed
inequality or missing hypothesis would instead park that source
specialization. The nomination2089 approved no mathematics; this
separate literature turn2090 now approves one reproduction audit under
SPECIALIZE, with REPRODUCTION classification. The small-X extension
and gamma-energy premise are audit obligations, not conclusions of
this approval. Full matching Mathlib coverage is unchecked.
