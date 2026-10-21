# Retained component-specialization label — source review

Step 211 is literature-only, for the exact TARGET in
`drafts/literature/2026-10-14-retained-component-specialization-label.md`.
No adjacent-component identity, new lemma or mathematical script is asserted.
The main gap is original finite B>=A with actual input/action/pilot/essentiality.
The intermediate target could close the local native label, independently of
global selected/theta compatibility.

## Local comparison and preserved failures

Inspected L053's actual subgroup, P,Q and abstract Phi calculation;
L056's model, h,kappa,a',gamma and exact factor identity; L057's
hypotheses, actual graph indexing and deck comparison. The supplied full
PROOF and DAG provide orientation. ATTEMPTS/031 and steps 204/206
retain two incomplete marked-coordinate attempts: no relabeling, inferred
atlas or abstract point-group upgrade is allowed. The new test requires
an actual regular-model contraction, origin and translation equivariance.
Existing notebook changes are preserved; no cross-notebook input is used.

The assessment at invocation was REVIEW_REQUIRED. This record completes
that source review only. General theorems below are known inputs; their
specialization to the actual maps is reserved for a subsequent research
turn. No absent search match is evidence of originality.

## Primary component and algebraic-isogeny inputs

[J. E. Cremona, Computing in component groups of elliptic curves,
author preprint](https://johncremona.github.io/papers/component.pdf),
section 2.1, unnumbered theorem and complete proof, printed pp.2–3.
For a finite extension of Q_p with normalized discrete valuation v,
the standard Tate curve of parameter t, 0<|t|<1, has component
homomorphism [z] -> v(z) modulo v(t); the unit classes give E^0.
The proof handles positive valuations below the half-period, negative
valuations by inversion, and the even half-period separately. It also
gives tangent-line valuation tests. These are not a theorem about the
retained seven-gon. The author copy has six pages and no inspected
revision date; publication is ANTS VIII, LNCS 5011 (2008), pp.118–124,
confirmed by the author's bibliography. Journal/book byte identity was
not checked. Its section 2.2 general-equation test was inspected but is
not needed as a substitute for the fixed standard Tate isomorphism.

[John Tate, A review of non-Archimedean elliptic functions,
24-page manuscript](https://people.math.harvard.edu/~ctm/home/text/others/tate/tate-unif/tate-unif.pdf),
section “Isogenies”, printed pp.16–17, unnumbered theorem and full proof;
also the differential identity immediately before it, p.15.
Over a complete nonarchimedean field k, with 0<|t_1|,|t_2|<1 and
t_2^a=t_1^b, the representative map z -> z^b induces an algebraic
k-isogeny alpha_(a,b):E_(t_1) -> E_(t_2) of degree ab for positive
a,b. The section constructs the algebraic map using periodic rational
functions, then proves the classification; its proof distinguishes the
prime-to-field-characteristic and inseparable prime-degree cases.
Only characteristic-zero existence, degree and representative
compatibility are needed here. The standard invariant differential
pulls back to dz/z under Tate parametrization. This supplies an actual
algebraic isogeny input unavailable from L053's abstract Phi alone;
it does not identify Q with any formal section. The manuscript's dated
revision and publication byte identity were not established.

Applicability: k=N is a finite extension of Q_3; the changed r=q_0
and r^7 are nonzero topologically nilpotent elements of N. The source's
condition is an equality of actual parameters, not merely valuations.
The degree-seven power map is therefore within its theorem's scope.
Matching it with L056's a_N through the fixed origin normalization
remains a specialization obligation. The source differential criterion
and L056's characteristic-zero map comparison are available for that
test, without importing an unverified annular atlas. No equality of the
retained maps or value of Q's component is derived in this review.

## Primary regular-model and contraction inputs

[Qing Liu, Algebraic Geometry and Arithmetic Curves, OUP,
2006 paperback text](https://rexresearch1.com/GeometryLibrary/AlgebraicGeometryArithmeticCurvesLiu.pdf),
Example 8.3.53, pp.365–367; Lemma 10.3.21 and proof, pp.513–514;
Corollary 10.3.25 and proof, p.515. The copy's title/copyright pages
identify the 2002 first edition and 2006 paperback, ISBN 0199202494.
The host is a third-party mirror of the primary book; provenance and
byte identity with an OUP distribution remain unverified.

Corollary 10.3.25 assumes a semistable projective curve over a
one-dimensional Dedekind scheme, smooth generic fiber, and a split
ordinary double point of thickness e. Its minimal desingularization
replaces that node by e-1 multiplicity-one projective lines over the
residue field, in a transverse rational chain, with self-intersection -2.
No exclusion of residue characteristic 3 or divisibility of e occurs.
Read the underlying three blowup charts in Example 8.3.53, including
e=1, e=2, e=3 and the recursion decreasing e by two, and the completion
comparison in Lemma 10.3.21. The corollary's minimality proof is read;
its separately cited general intersection/minimality results are not
reproved. The author's [errata page](https://www.math.u-bordeaux.fr/~qliu/Book/errata.html)
says first-edition corrections are incorporated in the paperback; no
independent exhaustive errata audit is claimed.

[Brian Conrad, Minimal models for elliptic curves,
November 21, 2015](https://math.stanford.edu/~conrad/BSDseminar/refs/minimalmodel.pdf),
Definition 3.6, Proposition 3.7 and its factorization discussion,
pp.7–8; Theorem 3.10, Remark 3.11 and resolution/uniqueness discussion,
pp.8–9; Definition 5.1 and Theorem 5.4, pp.13–14.
A normal proper curve over a henselian DVR admits contraction of any
proper subset of its special-fiber components. The contracted subset
determines the map uniquely; maps constant on its connected pieces
factor uniquely through it. Positive-genus smooth curves have a unique
minimal regular proper model. Its smooth locus is the Neron model;
the Neron mapping property supplies unique extensions on smooth sources.
These statements cover contractions and isomorphism/translation
comparison, not functorial extension of arbitrary finite maps between
regular models. Remark 3.14 explicitly warns against that inference.
Theorem 5.4 cites BLR, Neron Models, 1.5/1, for its general proof;
that book proof was not newly read. No new proof of these standard
theorems is proposed.

[Kestutis Cesnavicius, A modular description of X_0(n),
arXiv:1511.07475v2, October 5, 2017](https://arxiv.org/pdf/1511.07475v2),
section 3.2.1, pp.19–20 (PDF indices 18–19), especially (3.2.1.1)–(3.2.1.2).
For a generalized elliptic curve and a finite locally free subgroup G
in its smooth locus, contraction discards exactly the geometric
components disjoint from G and identifies the remaining smooth locus
with that of the contraction as a group scheme. The construction is
unique up to unique isomorphism, depends only on the components met
by G, and commutes with arbitrary base change. The cited foundations
are Conrad p.218 and DR IV.1.2, not an original result of this notebook.
Inspected also the standard polygon and its translation action,
Definition 2.1.1, Remark 2.1.2 and section 2.1.5, pp.5–6.
The latter inverse gluing concerns the special polygon only; it is
not a verification or repair of ATTEMPTS/031's formal overlap.
Equivariance for the retained contraction still needs an applicability
argument using uniqueness and the actual preserved component subset.

Reuse Conrad, Arithmetic moduli of generalized elliptic curves,
July 18, 2006 author version, Theorem 2.5.2 and its complete proof,
pp.17–18, and Theorem 3.2.4, pp.24–25, from L056's ready coverage.
Reinspected the first theorem: contraction away from the fibral
identity components gives the standard one-gon of the full parameter,
respecting the formal group at the origin. This does not equate a
regular model with the retained seven-gon. No problematic extracted
overlap formula is used. The earlier author/journal qualifications
remain in force.

## Source restrictions, search record and comparison

Queries on 2026-10-14 included “Tate curve reduction component group
valuation map Z ord q Neron model”; “generalized elliptic curve contraction
Neron model component group functoriality”; “John Cremona computing in
component groups elliptic curves pdf”; “Cesnavicius generalized elliptic
curves contraction”; “xy uniformizer minimal resolution chain semistable
curves”; “minimal desingularization node thickness chain”; and the exact
Liu Corollary 10.3.25 reference and book title. Primary passages above,+rather than search snippets, supply coverage.

The accessible [Fiore–Yelton, arXiv:2403.19700v2, May 12,
2026](https://arxiv.org/pdf/2403.19700v2), sections 1.5.1 and 2.1.1–2.1.2,
pp.7,10–12, was used to locate Liu. Its conventions include algebraically
closed residue field of characteristic 2. It is not imported as a
theorem over N. Alper's May 21, 2024 moduli draft provided another
search lead; its exact paragraph/hypotheses were not successfully
retrieved, so it is not coverage. The Silverman publisher chapter
retrieval failed; the primary Tate/Cremona statements above remove
the need for that access. A mistyped arXiv identifier led to an
unrelated paper; no result from it is used. The Cesnavicius author-site
retrieval failed, but the versioned arXiv text was accessible.
There is no essential source-access blocker for the bounded test below.

DECISION: SPECIALIZE. This is a known-method route, not evidence of
new mathematics. The sources separately supply algebraic Tate maps,
component specialization, split-node resolution and actual contractions.
They do not state the unchanged notebook's marked-map conclusion.
Local source coverage has improved; no progress beyond these known
inputs, no native label and no original finite B>=A result is claimed.

## Approved bounded specialization and its stopping test

Retain L053,L056,L057; inherited L045,L048,L051,L054,L055; and L058
as audited context only. Keep all the snapshot's actual data and maps:
E_0/Q, F=Q(zeta_60,E_0[30]), K_glob=F(E_0[7]), Omega,u,w,H subset N,
M>=max(M_tors,31), full 30-torsion, fixed pointed Tate isomorphism,
changed r=q_0 in Q_3 with v_3(r)=30,v_3(3)=1, U,alpha,psi,gamma,
0_B,Q=alpha(P), and L057's c. Do not assume K_glob=N, r=3^30,
c(1)=plus-or-minus Q, or the marked atlas.

The future attempt must verify the model hypotheses before invoking
Liu: proper/projective semistable model, smooth generic fiber, split
nodes and their actual thickness. It must relate the regular resolution
and its Neron smooth locus to the actual retained contraction, including
the strict transforms of all seven marked components and the origin.
Use the source algebraic isogeny theorem to test the power-map
normalization, rather than promote Phi by definition. Verify the
geometric cyclic order through the split-node charts; an abstract cyclic
group and a representative valuation are not the desired conclusion.
Check extension/transport of translation by Q and contraction
equivariance before transferring the action through L057's c.

These are unproved specialization obligations, not a derivation in
this literature turn. A positive test must establish adjacent-component
rotation up to orientation on the actual retained cycle. An arbitrary
nonzero component generator, an unmatched contraction or an argument
depending on the old atlas fails the test. If the attempt cannot supply
that comparison in one bounded step, preserve the exact obstruction;
do not repeat the parked coordinate mechanism without a new verified
input. No theorem about arbitrary finite-map extension, fixed field
enlargement, global selected/theta data or the original numerical
comparison is within the approved scope. Full matching Mathlib coverage
is not checked. No general theorem is to be reproved for novelty.

Reuse step 195's same-day verification of the official 2023-07-07
challenge announcement and current prize page, recorded in
`drafts/2026-10-14-retained-degree-seven-extension-source-notes.md`,
lines 156–159. The precise challenge version and mathematical scope
remain those of foundations/01. This source-only step changes neither
the mathematical overview nor the DAG.
