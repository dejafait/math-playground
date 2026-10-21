# Normal-closure degree test — source coverage

TARGET: Compute the exact relative and absolute degrees of L090's G_o^nor and their 2-,3-,5-primary valuations, comparing [G_o^nor:F_tpd] with C_0=2|GL_2(F_3)||GL_2(F_5)| and [G_o^nor:Q] with Corollary 2.2(ii)'s delta=2^12*3^3*5*6, without inferring local ramification from total degree.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the fresh step364 exact normal-closure/Legendre/torsion searches and the duplicate/failure comparison in 2026-10-20-normal-closure-repair-scope.md; L090's ambient group, full pointwise stabilizers and core were read through the complete finite calculation. No exact degree-versus-estimate verdict was identified in those inspected records or sources.
SOURCE_EVIDENCE: Milne Fields and Galois Theory v5.10 Theorem 3.17(b–d), Remark 3.18(a,b), printed pp.39–40, freshly read in step364; IV April 2020 reproduction Theorem 1.10 proof (i),(ii) pp.23–24 and Corollary 2.2 proof p.44, with step350's displayed delta definition pp.41–42. See the repair-scope assessment for direct links, qualifications and proof-use ledger.
COMPARISON: Standard finite Galois correspondence supplies the entire general method; L090 supplies the exact actual ambient group and core. The remaining work is the same-field index/cardinality specialization and comparison with two different source thresholds, not a new closure theorem.
GAP: No repaired-field degree or valuation has been computed in this literature turn. Preservation of actual local bounds and the full initial-data/numerical argument are outside this test.
REASON: The concrete degree test is independently decidable from checked inputs and can discriminate a lost sufficient group-size argument from a bound with remaining slack.
SCOPE: Exactly TARGET for each ordering of one original L089 survivor as in L090 and L091, in the same closure. Permit finite group cardinalities, subgroup indices and integer factorization only; no new curve family, local inertia computation, different estimate, native field reinterpretation or essentiality verdict.

This newly written ready continuation is submitted for the supervisor's
separate next-turn approval. No mathematical specialization is made here.

The main gap remains original finite B>=A. A plausible downstream use
is deciding whether a normal-closure repair needs a different degree
argument before attempting local ramification preservation. This is
useful even while independent applicability and essentiality remain open.

Use L089 for the unchanged survivor/family and L090 for its canonical
fields, full ambient Galois group, actual kernels and common core;
L091 supplies the qualified same-member corollary context. Retain
c,h,d_*,e_*, both domains, d=6, epsilon_d=1, all six full-coordinate
fields and the fixed algebraic closure. The symbol T=F_tpd is the
root field, not the ell-division field called K in IV. Every normal
closure here is over the proved F_mod=Q.

Import [Milne v5.10](https://www.jmilne.org/math/CourseNotes/FT.pdf),
Theorem 3.17(b–d) and Remark 3.18(a,b), pp.39–40; no reproof is needed.
Its finite Galois hypotheses are supplied by L090. Compute indices
in that actual ambient group; do not assume a generic radical degree
or discard either scalar sector. The cardinality formula used for C_0
is the inspected (E3). The source version and derivation of the two
comparison thresholds are recorded in the companion repair review,
not asserted for a repaired field.

Continuation/abandonment test: give exact degrees, prime valuations and
ratios to both thresholds for the unchanged fields. If the relative
degree exceeds C_0, report only loss of that source group-size input;
if the absolute degree remains within delta, explicitly retain that
slack. Neither outcome alone settles a local different bound. Stop
and narrow if any actual ambient/core hypothesis fails. Do not invent
an enclosure violation or attempt a full repair theorem in this step.

Unresolved assumptions: IV reproduction authentication/current-version
applicability, the explicit def= convention, alternative models and
repairs, the height-selected prime and independent initial-data outputs,
native input/action/factorization/pilot transport, essentiality and
original finite B>=A. No prime-seven substitution. Full matching and
supporting Mathlib coverage remains unchecked.

Expected classification is REPRODUCTION: the general method is known;
only a specified arithmetic specialization is proposed. This coverage
is not a proof of its outcome or a claim of mathematical originality.
