# Theta-heat mixed recurrence: completed source and duplicate comparison

TARGET: Assess primary coverage for a Jacobi-theta-heat-equation recurrence for L030–L032 mixed forms, determining whether its first nontrivial case closes without an unsigned boundary or theta-index residual.
CHECKED: 2026-11-08
DECISION: IMPORT
SEARCH_EVIDENCE: Step140 searched reciprocal-zero power sums/Hankel/theta heat recurrences and stronger Toda results; exact local comparison located already audited L874 and its unpaid contact sign. Reused the October31 Jacobi-heat and November6 reciprocal-contact/score assessments; queries and reading limits below.
SOURCE_EVIDENCE: NIST DLMF v1.2.8 Sections20.1/20.2.3/20.2(ii)/20.13.1-2/20.7.32; Polymath arXiv:1904.12438v2 Proposition3.1(i)-(ii), (28)-(33), complete simple/repeated-zero proofs; Csordas arXiv:1309.0055v2 Theorems4.5-4.6, (4.9)-(4.10), Proposition4.9, printed pp11-12, with earlier associated-kernel coverage reused.
COMPARISON: Jacobi lattice heat is not Xi heat time or reciprocal-zero degree. L874 already treats the latter evolution and retains an unpaid coefficient/sign even at scalar contact. L040 supplies signed Newton recurrence; L825 and L738 stop only the specific common-symbol and generic-shape shortcuts.
GAP: No inspected source pays L874's actual-theta signed contact bound or supplies a closed sign-producing recurrence for L030 forms. Propagation, initialization, equality cases and endpoint continuation remain unproved; no impossibility or negative actual form is established.
REASON: Import only known identities and their scope; retire this recurrence nomination as overlap without a new independent sign input. Do not repeat L874's audited derivation, the stopped Jacobi L2 factor or exhausted Hall calculation. Nominate a distinct operator-pair source lead separately, without approving mathematics.
LITERATURE_REASON: The startup REVIEW_REQUIRED target lacked this exact primary/duplicate comparison; ready contact and Jacobi assessments were reused without reconstructing their mathematics.
SCOPE: Completed literature-only source comparison. IMPORT authorizes known-source scope conclusions only, not a contact sign, new recurrence specialization, lemma, mathematical script or all-degree argument.

## Original nomination (preserved; comparison completed below)

Main gap: L030–L032/C032a all-degree actual-Xi mixed positivity. A closed
signed recurrence might transfer known base signs to further mixed forms;
whether it exists or pays its residual is unknown. This is a proposed
direction to assess, not an assertion of novelty or a mathematical result.

Start with the precise definitions in L030–L032 and actual-theta
conventions in L019/L020. Search those exact statements and the narrowly
relevant local failures, including L825 and L738, before primary-source
comparison. No cross-notebook input is proposed. Retain any heat identity's
parameter, boundary, interchange and summability hypotheses explicitly;
do not identify heat evolution with a positivity-preserving operation
unless the source proves the required statement for these mixed forms.

Continue toward a separate creative target only if inspected coverage
identifies an explicit first nontrivial recurrence and a bounded test of
its signed residual, independently of the desired positivity. If only a
formal identity, a known obstructed common-symbol mechanism, an unsigned
boundary term or an uncontrolled theta-index residual is available, record
that obstacle and retire this nomination. Do not derive and approve new
recurrence mathematics in the source turn. All other mixed degrees,
global iteration and any link from a finite test to RH remain unresolved.
Full/supporting Mathlib coverage for this target is not checked.

## Completed comparison — 8 November 2026, step140

The main gap remains L030-L032/C032a: every actual reciprocal-zero
Hankel form must be nonnegative. The intermediate target was an explicit
signed recurrence whose first case closes independently of the desired
sign. Such closure could support propagation while leaving global
iteration and initialization open. The nomination's retirement test is
met: the relevant exact recurrence is already canonical and its sign
remains unpaid. This is routing evidence, not a new mathematical result.

### Exact objects, duplicates and recorded failures

Read L019/L020 and L030-L032/C032a completely. The mixed forms use
reciprocal-zero S_k and algebraic squares, not the positive moments of K.
Theta-moment Gram positivity addresses a different matrix. L040's full
Newton recurrence already converts ordinary moments to S_k with signed
coefficients, without proving mixed positivity.

Read L825 and L738 including their qualifications. L825 stops a common
constant-coefficient symbol for the fixed centered degree2/3 factors,
not every degree-dependent recurrence. L738 refutes a generic shape
implication, not actual theta. Neither supplies a positivity input.

The exact duplicate screen located
`2026-11-06-reciprocal-hankel-heat-contact.md` and
`2026-11-06-actual-theta-contact-score-pairing.md` in this directory.
Their ready primary assessments are reused. Read L874's complete proof
and separate step11 audit: it already gives normalized logarithmic heat
evolution, the finite null-contact contraction and its actual-theta
response/score formulas, with endpoint domination. Its full-degree
contact retains a nonzero coefficient outside the finite matrix.
At the hypothetical scalar contact, the required bound is
m_6>=15m_2^3; the recorded Cauchy--Schwarz bound is only 9m_2^3.
No actual contact existence or violation follows. These are citations
to canonical L874, not new derivations, calculations or a fresh audit.

Read the recorded contact-score automatic-sign stop and the October31
Jacobi-heat assessment, its L2-factor stop and L600's precise profile
and endpoint argument. The modular zero-mode contribution cannot be
dropped. Corrected profiles remain possible, but no specified correction
with a paid residual was found. The parameter-wide first-mixed GHS stop
retains its independent source/cone limits and supplies no closure here.

### Inspected primary statements and essential cases

[NIST DLMF](https://dlmf.nist.gov/20.13), v1.2.8 (15 September2026),
20.1/20.2.3/20.2(ii), fixes Im(tau)>0, q=exp(i pi tau), the theta3
series and analytic domains. Equations20.13.1-2 give
partial_tau theta=-(i pi/4)partial_z^2 theta and diffusion coefficient
pi/4 at tau=i t. Equation[20.7.32](https://dlmf.nist.gov/20.7#E32)
uses tau'=-1/tau, principal square root, a Gaussian multiplier and
transformed elliptic argument z tau'. These exact formulas were read.
At tau=i exp(2u), finite real u meets the lattice-domain hypothesis;
the singular endpoint is not a supplied boundary condition. Both
transformed factors must be retained in elliptic differentiation.
None of these statements signs reciprocal-zero Hankel forms or
identifies lattice time with Xi heat time. Cite, rather than reprove,
these formulas; no new specialization was derived.

D. H. J. Polymath,
[*Effective approximation of heat flow evolution of the Riemann xi
function, and a new upper bound for the de Bruijn-Newman constant*,
arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2),
4 August2019, Proposition3.1(i)-(ii), (28)-(33): inspected the full
simple and repeated-zero proofs. The real base time is arbitrary;
complex zeros are permitted. Simple roots use implicit continuation
and paired Hadamard logarithmic derivatives; repeated roots require
Hermite rescaling and a Rouche count, with multiplicity-dependent
errors. The PDE proof uses rapid decay for differentiation. This
supplies dynamics, not a finite-Hankel boundary sign. No zero-sum
interchange or new parameter rescaling is performed here. The proof's
PDE paragraph says t>=0 although the proposition allows real t_0;
only positive-contact-time comparison is needed here.

George Csordas,
[*Fourier transforms of positive definite kernels and the Riemann
xi-function*, arXiv:1309.0055v2](https://arxiv.org/pdf/1309.0055v2),
21 February2014, printed pp11-12, Theorems4.5-4.6, (4.9)-(4.10) and
Proposition4.9: newly inspected the statements and heat differentiation
passage; reuse the October31 assessment for associated-kernel proof
coverage. Admissibility is distinguished from positive definiteness.
The heat parameter weights Phi by exp(t s^2); multiple-zero behavior
is qualified by the transition constant. Neither statement signs the
actual reciprocal forms or pays a theta-index residual. Historical
open problems and numerical bounds are not evidence of present
nonexistence of a theorem.

### Bounded searches and limitations

Queries actually issued included:

- `Riemann xi reciprocal zeros power sums Hankel determinant theta heat equation recurrence`;
- `Jacobi theta heat equation Hankel positivity recurrence Riemann hypothesis`;
- `"Riemann" "power sums" "recurrence" "heat"`;
- `"xi" "Hankel" "Toda" theta recurrence positivity`;
- `"Riemann" "Jacobi" "heat" "recurrence" "mixed"`;
- `"Riemann xi" "reciprocal" "heat" "Hankel"`.

Stronger-result leads included a claimed fourth kernel derivative
Toda-Hankel sign (Koide, secondary index only), self-weighted Hamburger
rigidity (secondary abstract), and complex orthogonal-polynomial Toda
identities. These remain uninspected leads, not inputs. A kernel
derivative determinant is not identified with L030's reciprocal form.
The OUP primary kissing-polynomial page failed to fetch. DLMF TeX
endpoints were unsupported; the required formulas were subsequently
read in primary HTML. Neither failure blocks an essential premise.
Early oversized status/search output was followed by exact-path reads;
no conclusion rests on truncated output. No exhaustive-search or
novelty claim is made, and no cross-notebook input was used.

NEGATIVE records that this nomination overlaps an already audited
reduction and fails its sign-closure continuation test without new input.
It is not new mathematics beyond checked sources, an actual-theta
counterexample or progress on RH signs. No lemma, mathematical script,
DAG or PROOF change is warranted. No mathematical EXPLORATION budget
is spent or renewed. Full/supporting Mathlib coverage for the desired
closure remains unchecked, not absent.

### Distinct continuation lead, not approved mathematics

A search surfaced H. Hedenmalm,
[*Spectral interpretation of Riemann zeta zeros*, arXiv:2606.17494v1](https://arxiv.org/abs/2606.17494v1),
16 June2026. Only its primary abstract/version metadata was read: it
describes the theta-dependent pair (LD,L) and pair self-adjointness.
Its theorems, domains and proof cases remain unread. Exact title/ID
searches in local literature, attempts and foundations found no matching
assessment; the older Hedenmalm-Lindqvist-Seip inputs concern another
work. The actual-pair/de Branges construction stop was checked: an
independent positive realization remains required, not supplied by a
formal spectral interpretation.

The separate REVIEW_REQUIRED nomination asks for its precise domain
and boundary-form condition, then an independent bounded sign test
or a scope stop. It approves no mathematics. Missing source coverage
and an independent sign mechanism presently block justified creative
proof routing. An initially considered L903 audit was withdrawn after
its completed step132 history was located; the overview's old label
does not authorize a repeat audit.
