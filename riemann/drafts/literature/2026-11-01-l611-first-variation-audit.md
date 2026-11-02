# L611 first-variation audit: approved bounded scope

TARGET: Audit L611's parameter differentiation, shifted-Xi normalization and uniform remainder at a hypothetical double real zero, keeping its missing sign input explicit.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused 2026-11-01-small-cutoff-multiple-zero-stability-review.md and 2026-11-01-reciprocal-cutoff-double-zero-variation.md, including their exact reciprocal-cutoff/first-variation searches and recorded failures; scoped local searches located L611's completed calculation and sign-input stop. No repeated external search or novelty inference.
SOURCE_EVIDENCE: Read L611 and L019/L020 completely, L016/L018 normalization and L610 definitions/qualification; reused the prior inspected Schnell Class 2, Theorem 2.8/proof, pp.2-4 (https://www.math.stonybrook.edu/~cschnell/mat545/class2.pdf), and Parusinski--Rainer manuscript 2024-10-07, Theorem 2.2/Puiseux discussion, p.7 (https://www.mat.univie.ac.at/~armin/publ/handbook_paper.pdf). These external sources were not fetched again; the prior assessment records the inspected primary hypotheses and proof cases.
COMPARISON: The saved scope uses precisely the previously assessed weight, fixed hypothetical double zero, one-sided parameter limit and compact-frequency remainder. L019/L020 supply the kernel bound and entire transform; standard dominated differentiation and Taylor's theorem supply the method. Verification of L611's particular constants, factors and determinant algebra remains the audit task, not a theorem imported from the comparison sources.
GAP: No essential source coverage is missing for this bounded correctness audit. Neither prior literature nor this scope comparison supplies the shifted-value sign, existence of a double zero, height-uniform thresholds or higher signs.
REASON: Approve verification of the new canonical calculation using unchanged adequate coverage; no new preservation theorem, source reproof or sign development is authorized.
SCOPE: Only replay L611's j<=2 right-parameter domination, shifted-Xi normalization, compact-frequency remainder, exact determinant remainder and both conditional strict-sign thresholds at a fixed hypothetical double real zero. Keep all unresolved sign and existence assumptions explicit.
LITERATURE_REASON: The invocation-start audit target was REVIEW_REQUIRED after L611 was newly written. This turn compares that exact scope with existing ready coverage; it does not add literature to a ready target or repeat browsing.

## Scope comparison and use

The main gap remains actual-Xi all-degree signs at unbounded heights.
The intermediate target is correctness of the conditional L611 diagnostic.
Its downstream use is to retain a reliable statement of the exact missing
small-cutoff sign input, or to remove an invalid diagnostic if the audit
finds an error. It cannot supply the missing sign by itself.

L019 states the positive kernel and its superexponential envelope. L020
states the entire cosine transform and locally uniform convergence of
every fixed frequency derivative. Its convention is Xi(z)=xi(1/2+iz),
as in L018, with L016's theta normalization. These are the same starting
inputs used by the prior ready calculation assessment; the audit introduces
no new parameter family or analytic extension. L610 supplies definitions
only, not its qualified numerical execution. Essential mathematical input
IDs are L019 and L020. The exact assumed configuration is real a with
Xi(a)=Xi'(a)=0 and Xi''(a) nonzero, and epsilon decreasing to zero through
positive values. Existence of a and the sign of Xi''(a) Re Xi(a+2i)
remain unresolved. There is no RH or cross-notebook input.

The prior primary-source comparison remains adequate. Schnell's theorem
assumes a holomorphic germ of finite distinguished-variable order and
gives preparation, without a real-root sign conclusion. Parusinski--Rainer
assumes hyperbolicity throughout a real parameter interval; its Puiseux
argument uses that reality assumption. Neither is an input to L611 or
grounds for extending a one-sided parameter derivative to a holomorphic
parameter family. The previous review also inspected de Bruijn 1950
Theorems 10-12, pp.203-205, and Newman 1976 Theorem 1, p.246: their
specified preservation multipliers are comparison results, not this
reciprocal weight. Their precise citations and inspected cases remain in
the reused review. No inaccessible collision source is essential here.

No theorem reproof is proposed. The local specialization is necessary
only to check the particular shift, factors, remainder constants and
first-form algebra already written in L611. No complete matching or
supporting Mathlib coverage was checked for this audit; unknown coverage
does not establish absence. L019/L020 keep their existing qualifications.

## Bounded test and disposition

The separate research turn should replay the majorants for j<=2, the shift
identity, the exact determinant remainder and both strict-sign thresholds.
Continue if each claim holds with constants allowed to depend on a fixed
compact frequency set; repair or reject any sign, factor or domination
error. Do not extend to height-uniform thresholds, zero splitting, equality
cascades or higher signs. The recorded sign-development stop in
ATTEMPTS/2026-11-01-reciprocal-double-zero-sign-input-stop.md remains in
place; a correctness audit does not reopen that inference.

This separate literature-only turn approves the saved exact audit scope.
It performs no independent proof audit, new calculation or lemma edit.
Outcome STALLED as mathematical progress: existing adequate coverage was
confirmed, with no new source result or sign evidence. Classification
REPRODUCTION describes the covered standard-method specialization, not
a mathematical reproduction completed in this source review. Literature
work does not spend or renew the mathematical exploration budget.

No justified creative mechanism is nominated: independent control linking
curvature at a hypothetical double zero to shifted Xi data is still
missing. The necessary correctness audit takes precedence; it must not
be relabeled creative to meet a scheduling preference.
