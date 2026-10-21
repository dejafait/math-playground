# Nonnormal certification — completed source comparison

TARGET: Assess whether a generalized norm-relation theorem for nonnormal L96 provides an unconditional square-class certification route for the 96a1 branch.
CHECKED: 2026-10-11
DECISION: IMPORT
SEARCH_EVIDENCE: Searched generalized/generalised norm relations for non-Galois fields and unconditional class/unit certification; located Etienne arXiv:2411.13124v2 and followed its essential analytic reference; checked local norm assessments, history/143 and ATTEMPTS/020-021 for overlap and preserved stops.
SOURCE_EVIDENCE: Etienne v2, April 23, 2025, Definitions 2.4,2.9 and Proposition 2.7 with proof pp.12-15, Definition 2.12 and Theorem 2.16 pp.16-19, Proposition 3.5 and Remarks 3.6-3.7 p.22, Algorithms 4.1,4.3,4.6 and Theorems 4.2,4.4,4.7 with complete accompanying proofs pp.23-27; Belabas-Friedman arXiv:1305.0035v1, April 30, 2013, Introduction and Theorem 1 pp.1-2 and essential GRH proof cases pp.6-8.
COMPARISON: Generalized relations permit nonnormal L96, but Theorem 4.4 expressly assumes GRH and Algorithm 4.6 invokes a GRH-dependent analytic residue estimate; no unconditional complete square-class certificate for L96 follows from these inspected guarantees.
GAP: Relation existence and complete auxiliary arithmetic are unknown; unconditional certification premises, class torsion lifts, support/norm maps and complete descent comparison remain missing.
REASON: Import precise source qualifications and park these algorithms as unconditional certificates; retain the independent relation-existence criterion as a bounded feasibility target, without deciding it here.
LITERATURE_REASON: The nonnormal mechanism lies outside the earlier normal-extension assessments; its primary algorithms and essential analytic dependency were unread at invocation start.
SCOPE: Source-level guarantees and limitations only; IMPORT does not authorize a square-class import, relation construction, field computation or lemma.

## Target, inputs and preserved stops

The main gap is unconditional global emptiness of L032's 96a1 branch,
with other twists and residual Beal signatures independently unresolved.
The intermediate target was an unconditional nonnormal-field certification
interface. Its downstream use is a complete upper square-class group for
the descent, followed by full-disk disjointness. The test requires actual
unconditional completeness, not an internally saturated subgroup or a
GRH computation.

Read L051's exact degree-36 L96=K96(T) model and L054's full relative
normality proof. They give the two actual smaller fields K96 and F=Q(T),
of degrees twelve and three. Reuse the certificate obligations in
`drafts/literature/2026-10-10-ninety-six-unconditional-selmer-certificate-scope.md`
and BFHP coverage in the square-class and relative-base assessments.
L053/L054 and ATTEMPTS/020-021 park two normal-extension variants only.
L052's Minkowski cutoff is preserved without asserting a necessary
complexity bound. No cross-notebook input or GRH premise is introduced.

## Primary result and completeness qualifications

Fabrice Etienne, *Computing class groups by induction with generalised
norm relations*, [arXiv:2411.13124v2](https://arxiv.org/abs/2411.13124v2),
April 23, 2025, [versioned primary PDF](https://arxiv.org/pdf/2411.13124v2).
Printed page numbers here are one above PDF page indices. The accessible
Bordeaux manuscript has different numbering: its Theorem 2.20 becomes
Theorem 2.21 in v2. Use v2 consistently.

Definitions 2.4 and 2.9 take a finite Galois overfield Omega containing
K and the auxiliary fields Li, with G=Gal(Omega/Q), H fixing K and Ji
fixing Li. The relation is N_H=sum ai N_Ji bi in Q[G], ai,bi in Q[G].
K itself need not be normal. Thus L053 and L054 do not invalidate this
framework. Proposition 2.7 characterizes existence by a surjection from
finite copies of Q[G/Ji] onto Q[G/H], equivalently by coverage of every
simple constituent with H-invariants. Its complete proof was read,
including the converse assembling simple constituents and the two-sided
ideal/idempotent equivalence. It establishes no relation for L96.

Theorem A in the introduction promises a full S-unit basis from full
auxiliary S-unit bases and a generalized relation. Detailed Algorithm
4.3 takes irreducible field polynomials, rational-prime support S, and
complete bases of O_(Kj,S)^*. It uses every compositum and prime-power
saturation. Theorem 4.4, printed p.24, explicitly assumes GRH for its
correctness and polynomial complexity. Retain that stated hypothesis;
the introduction is insufficient for an unconditional import. Read the
full proof, including Mackey transfer, basis construction and saturation.
Theorem 2.16 bounds the optimal coefficient by |G|^2, where G is the
closure group, not [K:Q]. The printed correctness proof also writes an
integral composition as identity although Definition 2.12 uses c times
identity. No correction, unstated strengthening or original reproof is
attempted here.

Algorithm 4.6 and Theorem 4.7, printed pp.25-27, give the practical
class-group alternative. They require a relation, actual auxiliary
S-unit generators, image valuations at every supported prime, power
tests and an h_K Reg_K comparison. Read the full correctness argument:
insufficient power tests and insufficient class support are claimed to
change that product in the same direction, preventing cancellation.
Theorem 4.7 says correctness if the algorithm terminates, but step 2
specifically invokes reference [1]'s analytic approximation. That is not
an independent unconditional guarantee for its input. Neither termination
nor a certificate for L96 is supplied. A class-group structure alone also
omits the principal witnesses and torsion lifts needed by the descent.

Reference [1] is Karim Belabas and Eduardo Friedman, *Computing the
residue of the Dedekind zeta function*, Mathematics of Computation
**84** (2015), 357-369, [DOI](https://doi.org/10.1090/S0025-5718-2014-02843-3).
The inspected [primary preprint](https://arxiv.org/pdf/1305.0035v1),
April 30, 2013, Theorem 1, printed p.2, takes degree n>1, field
discriminant Delta_K, residue kappa_K at 1 and X>=69. Its explicit
log-residue error bound assumes zero-freeness of both zeta_K and
zeta_Q in Re(s)>1/2. Lemma 3 and following estimates, printed pp.6-8,
use GRH for continuation and real zero ordinates; this is not merely
a running-time assumption. Algorithm 4.6's specified analytic certificate
is therefore conditional. A different unconditional analytic input or
exact transfer certificate needs separate review.

## Decision and independent continuation

NEGATIVE source comparison: nonnormality is allowed, but the inspected
algorithms do not meet the unconditional square-class threshold. Park
their use as completed unconditional certificates. This is local routing
evidence from known literature, not a new impossibility theorem or an
assertion that every generalized mechanism requires GRH.

The independent finite question is whether a generalized relation exists
using the already available K96 and F. Proposition 2.7 and Algorithm
4.1/Theorem 4.2 give unconditional algebraic criteria, needing neither
class generators nor a residue estimate. All conjugate composita and
full permutation modules must be retained; a trace of one generator,
a guessed closure group or an ordinary-subfield dimension count is not
sufficient. Their field-specific outcome is not derived. A separate
continuation assessment records the narrow target for later approval.
Failure parks only this auxiliary pair. Success still requires separate
unconditional certification and the downstream descent obligations.

Exact queries: `generalised norm relations non Galois number fields
class groups units unconditional certification`; `generalized norm
relations nonnormal fields Etienne`; `Belabas Friedman Computing residue
Dedekind zeta function 2015 GRH theorem pdf`; `Fabrice Etienne generalized
norm relations unconditional GRH theorem 4.4`. Snippets and software
overviews were discovery leads only. The Belabas author PDF and repository
link were unavailable through the browser; versioned arXiv supplied the
essential primary statement and proof cases. A shell download failed DNS
resolution; no local PDF or certificate was produced. No persistent
essential-source blocker remains for this comparison. Mathlib coverage
is not checked. No new lemma, mathematical script, relation, certificate,
DAG edge or proof assembly was written.
