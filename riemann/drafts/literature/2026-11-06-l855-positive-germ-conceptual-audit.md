# L855 positive radial germ — approved conceptual-audit coverage

TARGET: Independently audit L855's primitive/monomial positive radial germ for every fixed finite multiplicity n>=1, checking joint holomorphic normalization, both inverse domains, original angular orientation and the exact full density with its retained Jacobian zero.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed search in 2026-11-06-transverse-divisor-nonlinear-local-realization.md and the unchanged approved 2026-11-06-primitive-monomial-local-germ.md; this is the first audit of that construction's result with unchanged pair hypotheses and analytic tools, not a fresh novelty search or a new mechanism.
SOURCE_EVIDENCE: Lebl CA v1.10 Theorem2.4.7 pp49-50 and Corollary3.2.12 pp67-68 https://www.jirka.org/ca/ca.pdf ; Lebl SCV v4.4 Theorem1.2.1/proof pp20-21 https://www.jirka.org/scv/scv.pdf#page=20 ; Chaperon 9January2007 Section1 Corollary1/real-complex justification p2 https://webusers.imj-prg.fr/~marc.chaperon/Chaperon_Cauchy_Kowalevski.pdf#page=2 ; Forstneric AIF37(1)(1987) Section2 Lemma8/determinant proof and monomial models pp14-16 https://users.fmf.uni-lj.si/forstneric/papers/1987Ann.Inst.Fourier.pdf#page=15 . Reuse the prior actual primary reading; no new external retrieval is claimed.
COMPARISON: The same inspected standard tools cover factorization, joint power series, analytic inverses and the known graph-model method. They do not certify L855's chosen tangent, exact orientation or density; those specialized claims require independent mathematical checking, not import of a general positive-germ theorem.
GAP: Independently check L855(3)-(11), including simultaneous domains, all n>=1, the central J zero and punctured-neighborhood sign. No independent audit was performed in the construction turn, and no global extension or all-degree conclusion is covered.
REASON: Separate literature approval completed on 2026-11-06: unchanged prior primary-source coverage is adequate for exactly this first conceptual audit. Proceed next to the mathematical audit without another source approval; this decision does not approve L855's correctness.
SCOPE: Exactly TARGET and the explicit nonzero pair hypotheses of L855, actual G,R,C of L775/L847 and original angular orientation. No prescribed collar tangent, particular L853 pair, numerical verification, new mechanism, global torus or other order/shift.

## Audit boundary and discriminator

L855 is a completed local proof attempt, not an RH candidate. Its
specialization supplies a possible local building block near a divisor
crossing; global matching and the link to L030-L032/C032a remain open.
The audit is REPRODUCTION under SPECIALIZE. Full matching Mathlib
coverage remains unchecked. No cross-notebook input is proposed.

Check the local factorization at the explicitly hypothesized zero and
the nonvanishing of H on a single product neighborhood. Check joint
holomorphicity of the parameter-dependent primitive, the derivative
and domains of its complex inverse, and the base-point identities.
Then check the monomial surface and its actual, full pullback, including
the factor w^n. For the original angular map check the real derivative,
its positive determinant, the real inverse domain and the normalization
of u by R. Retain the complete J formula at the center; a formal jet,
an orientation reversal, or positivity after deleting a zero fails.

Accept only if one open neighborhood for each fixed pair and n has
all claimed properties simultaneously. Correct an identified error or
record the first unrepairable condition with its precise scope. Neither
audit outcome implies a result about prescribed boundary data or RH.
The prior source comparison already explains why generic complex-point
and Stein-isotopy results provide no automatic solution; no additional
theorem import is needed for this bounded audit.

The independent audit has not been carried out here. The separate source
gate is now satisfied for the unchanged TARGET; the next turn is the
mathematical audit, not another literature approval.

## Separate source approval — 6 November 2026

Reused the complete primary-source reading in the two named assessments,
including the repaired direct URLs and versions; no new external retrieval
or new source result is claimed. Read L855 in full to compare its stated
uses with that coverage, and narrowly checked L775's normalization and
L847(1)–(3) and the local differential passage. This is scope comparison,
not independent verification of L855's calculations.

The audit's source obligations are covered as follows:

- Lebl CA Theorem 2.4.7 covers finite-multiplicity factorization; the
  finite multiplicity and nonzero pair remain explicit hypotheses.
- Lebl CA Corollary 3.2.12 applies on a star-like plane domain; Lebl
  SCV Theorem 1.2.1 supplies the separate joint-series tool on a
  polydisc with closure inside a larger holomorphic neighborhood.
  Joint parameter dependence is an audit obligation, not an imported
  consequence of the one-variable primitive theorem.
- Chaperon Section 1 Corollary 1 covers both analytic inverse uses.
  The complex derivative, real angular derivative, their inverse
  domains and a common final neighborhood require independent checks.
- Forstneric Section 2 Lemma 8 and its examples cover model terminology
  and the graph method only. No index bound, positivity theorem or
  global extension is being imported from them.
- L847 supplies the original local full-form convention. Its global
  periodic hypotheses must not be silently imposed on this local
  target; the later audit must justify exactly the local identity it
  uses, retaining both divisor and Jacobian zeros.

The targeted duplicate/failure comparison reuses the completed
transverse-divisor search and reads the generic-complex-point scope-stop
and primitive-model recovery-parking records. Neither establishes an
L855 audit or excludes it. The earlier parking was procedural and the
fixed-cutoff linear-range stop concerns a different mechanism. No new
search or novelty conclusion is needed for this unchanged first audit.

Acceptance still requires all of L855(3)–(11) on one common neighborhood
for every fixed pair and finite n>=1, with the original orientation and
central J zero. Any failed hypothesis or identity is to be recorded
precisely. No L853 crossing, numerical certificate or step433 input is
required. Full matching Mathlib coverage remains unchecked. This approval
adds no lemma, proves no identity, and provides no global or RH advance.
