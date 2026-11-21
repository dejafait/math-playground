# One-sided Fourier and diagonal period test: source comparison

TARGET: Test whether angular Fourier compatibility of L868's C1 closure system and vanishing of q,r on the actual diagonal force K>=-|M|, without radial growth assumptions.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact/stronger searches for Fourier compatibility of closed forms, diagonal restriction, product Fejer reconstruction and positive trigonometric polynomials; inspected primary passages and queries below. Reused the named one-sided calibration assessment and checked the L868 period-gap record; no matching sharp-period theorem located and no novelty inferred.
SOURCE_EVIDENCE: Grafakos, Classical Fourier Analysis 3rd ed. (2014), Definition1.2.15 p26, Theorem1.2.19(2)/proof pp27-29 (author's corrected pages), Definition3.1.8/Remark3.1.9/Proposition3.1.10 pp180-181, Corollary3.2.2/proof p183, Theorem3.3.9(a)/proof pp196-197; Rudin, Principles of Mathematical Analysis 3rd ed. (1976), Theorem9.42/proof pp236-237; Dritschel-Rovnyak arXiv:0903.3639v1 Section5 Theorem5.1 and final d=2 proof; Dritschel-Klep-McCullough-Volcic arXiv:2608.23073v1 Theorem1.1 and Section4 Corollary4.1. Links, inspected scope and exclusions below.
COMPARISON: Product Fejer reconstruction and compact parameter differentiation supply the missing C1 source coverage for a mode/trace attempt, without assuming absolute summability. Positivity factorization results concern polynomials at fixed radial parameters and do not supply closure compatibility or K>=-|M|. L868's existing weaker mean bound and zero-period example remain unchanged; L867 stops only its stated subclass.
GAP: Establish whether the exact global closure system plus the actual diagonal zeros and domination control K at -|M|; no inspected theorem supplies that conclusion. Finite approximants cannot be presumed feasible under the fixed |F| bound or exact zero constraints; any limiting argument must retain the original constraints.
REASON: Essential reconstruction/trace and positivity comparisons for the unchanged TARGET are complete. EXPLORE supports one bounded mathematical attempt after separate approval of this changed assessment; it approves no target-specific identity, period inequality, certificate, or novelty claim.
SCOPE: L868(3)-(4) on all R2 times T2, real C1 q,r,h, h>=0, q^2+r^2<=|F|^2 for L847's actual F, constant K=mean(q+h), M=mean F; every F/J zero retained, fixed orientation, no added radial growth, finite angular bandwidth or holomorphicity.

The two nomination sections below preserve the pre-review requirements;
their missing-coverage statements are superseded by the completed review
and current fields above. They are not instructions for another search.

## Relevance and precise continuation boundary

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. The intermediate target concerns the certificate class
for L847's fixed coupled graph problem. A sharp bound K>=-|M| would
stop this entire certificate class; a rigorous admissible example
with K<-|M| would obstruct all real nonnegative coupled graphs by
L868's audited compact-Stokes comparison. Neither conclusion would
settle Xi's higher signs or RH.

The proposed new control is the interaction of angular modes of the
closure equations with the actual diagonal z1=z2, on which the
audited modulus constraint forces q=r=0. It is not another
holomorphic reduction, a radial-independent specialization or the
already constructed zero-period bump. It has not been derived or
tested in this invocation. The earlier working note's Fourier
suggestion is an untested mathematical lead, not evidence of success.

Essential local inputs are L868's complete audited coefficient and
period statement and L847's exact actual F and compact homotopy.
L867 is only the stopped absolute-class comparison. All other F
zeros remain constraints on any proposed example, even if only the
diagonal is used for a sufficient no-gain proof. No cross-notebook
input is proposed. Mathlib coverage is unchecked.

## Required source comparison and bounded test

Search the exact periodic first-order system and standard results
on Fourier compatibility for closed forms, diagonal restriction and
positive angular functions. Read primary statements and relevant
proof cases at C1 regularity. Distinguish individual coefficient
identities from convergence of a reconstructed series on a diagonal;
do not assume absolute convergence of a two-dimensional C1 Fourier
series or commute a trace with an unjustified limiting operation.
An approximation theorem can be imported only with its preservation
and convergence hypotheses checked for the uses proposed here.

Compare with the previously inspected null-Lagrangian and calibration
theorems before claiming a new mechanism. They were not a theorem
classification of this variable-coefficient class. Do not repeat
their unchanged source review merely to fill a literature quota.
No source is currently known to be inaccessible; missing inspection
is REVIEW_REQUIRED, not SOURCE_BLOCKED.

If coverage permits research, one bounded test should ask whether
the mode constraints and diagonal data control the constant K at
the exact threshold -|M|. Continue only with a quantitative mean
bound or a precise new compatibility obstruction that could affect
that threshold. If the passage leaves an uncontrolled zero mode,
requires an unproved growth or summability hypothesis, or supplies
only mode identities with no period control, save that exact failure
and do not repeat the same mechanism unchanged. A formal series or
a solution on a bounded radial region is not a global certificate.

At nomination the next turn was theorem comparison, not a creative proof
attempt. No justified new central mechanism was established during
the completed audit, and this specific proposed refinement then
lacked source coverage. Any later creative routing must name a new
central obstruction and bounded test on their mathematical merits.

## Completed literature-only review, 6 November 2026

The fields above replace the nomination's REVIEW_REQUIRED state.
TARGET and SCOPE are unchanged. No mode equation, period estimate,
counterexample, lemma or mathematical script was derived in this turn.
PROOF.md and DAG.md were left unchanged because the mathematical
argument and dependencies have not changed. This is preparation for a
test, not progress beyond a known theorem or a resolution of the target.

### Local comparison and exact diagonal

Read the complete canonical L868, including its independent audit;
read L847's actual-function hypotheses and graph/Stokes and periodic
derivative-moment interfaces. Checked the named parent assessment
`2026-11-06-oriented-one-sided-dual-period-test.md`, its completed
calibration/null-Lagrangian comparison, the L868 audit assessment,
`../../ATTEMPTS/2026-11-06-one-sided-dual-reduction-period-gap.md`,
and the saved L868 working note. The two named one-sided histories
record no Fourier theorem or completed Fourier/diagonal test. Reuse
the parent's inspected sources at their stated scopes; no repeated
calibration browsing was needed.

L868(3)-(6) is the essential mathematical input. The actual zero
divisor z1=z2 has x1=x2 AND y1=y2 modulo 2pi. Equal angles at unequal
radii are not this diagonal. The modulus hypothesis forces q=r=0
there; it does not force h=0. All other F zeros and all J zeros
remain in scope. L868(11) has a weaker threshold, and its bump has
K=0. L867's absolute-class stop does not settle radial-dependent h.
No cross-notebook input was read or proposed.

### Primary theorem coverage

Loukas Grafakos, *Classical Fourier Analysis*, third edition,
GTM249, Springer (2014), DOI10.1007/978-1-4939-1194-3:
[author's corrected pp27-29](https://grafakos.missouri.edu/Books_Correction_Pages/CFA-Page27-29.pdf)
and [textbook pp26,180-184,196-197](https://www.math.stonybrook.edu/~bishop/classes/math638.F20/Grafakos_Classical_Fourier_Analysis.pdf).
Read Definition1.2.15; Theorem1.2.19(2) and its uniform-convergence
proof; Definition3.1.8, Remark3.1.9, Proposition3.1.10 and proof;
Corollary3.2.2 and proof; Definition3.2.3; and Theorem3.3.9(a) and
its periodic integration-by-parts proof. Approximate identities have
bounded L1 norms, mass one and vanishing mass away from the identity.
The product Fejer kernels are nonnegative approximate identities on
T^n; their convolutions converge uniformly for continuous functions.
The smoothness theorem supplies Fourier differentiation/decay under
its stated derivative hypotheses. None of these is a period inequality.
Use this edition's numbering, not the second edition's Corollary3.1.11.

Walter Rudin, *Principles of Mathematical Analysis*, third edition,
McGraw-Hill (1976),
[Theorem9.42 and proof, pp236-237](https://djvu.online/file/cNW6EtZ7m9PIB).
Read the whole theorem/proof in the book text. It permits parameter
differentiation of a finite Riemann-Stieltjes integral when the
parameter derivatives exist near the chosen interior point and are
continuous there uniformly in the integration variable; the slice
integrals must exist. Continuous partial derivatives on the rectangle
suffice. The proof uses uniform convergence of difference quotients.
Take the increasing integrator to be the coordinate itself; real and
imaginary parts can be handled separately. No noncompact integral
version is imported.

Michael A. Dritschel and James Rovnyak,
[*The Operator Fejer-Riesz Theorem*, arXiv:0903.3639v1,
Section5, Theorem5.1](https://arxiv.org/html/0903.3639v1#S5).
Read the statement, preceding multivariable qualifications and the
final d=2 proof following Lemma5.2. A Laurent polynomial with
operator coefficients, uniformly bounded below by delta I for some
delta>0 on T^d, is a finite sum of analytic polynomial squares.
The final perturbation step uses that strict margin. This is not a
factorization theorem for arbitrary C1 functions. Its polynomial
degrees cannot be assumed to remain bounded in every variable.
The internal Schur-complement lemma was not independently audited
and no factorization proof is imported into the notebook.

Michael Dritschel, Igor Klep, Scott McCullough and Jurij Volcic,
[*Addendum to “Factoring non-negative operator valued trigonometric
polynomials in two variables”*, arXiv:2608.23073v1, 24 August 2026,
Theorem1.1 and Corollary4.1](https://arxiv.org/html/2608.23073v1).
Inspected these statements, their introduction and Theorem3.1's
hypotheses. Theorem1.1 gives a rectangular analytic polynomial
factor B with A=B*B for a positive semidefinite finite matrix Laurent
polynomial on T^2, with some finite output degree. The introduction
reports a counterexample to the older degree bound. Thus the
non-strict polynomial case is not an absent theorem; neither a
uniform degree bound nor a C1 parameter-dependent factorization is
provided by the stated conclusion. The algebraic proof and older
counterexamples were not audited or imported; no claim about their
exact counterexample mechanism is used.

### Applicability boundary for the proposed attempt

For each compact radial rectangle, the original C1 q,r,h and their
first derivatives are continuous on its product with the angular
torus. This checks the compactness/uniform-continuity hypotheses for
the proposed use of the cited Fourier approximation and finite
parameter differentiation. Normalize angles by y/(2pi) to match
Grafakos's unit torus and use normalized Haar measure. No bound on
all of R2 is required for these compact operations; none follows.

Use the original functions for the exact closure and domination
constraints. The cited reconstruction permits finite product Fejer
sums followed by uniform limits, including restriction to a compact
piece of the actual diagonal. It does not require an absolutely
convergent double Fourier series. Any first-derivative or radial
coefficient interchange must be checked using the C1 compact
hypotheses and the cited differentiation theorem. No target-specific
commuted identity was established here. In particular do not
differentiate the closure equations a second time classically
without additional regularity or a justified weak formulation.

A positivity-preserving averaging theorem does not state that
averaging a function vanishing on a thin diagonal preserves that
zero set, or that it preserves domination by a fixed nonconstant
|F|. These extra preservation statements have not been established.
Finite approximants are reconstruction tools, not certified feasible
solutions. Do not replace the original all-X problem by a finite
bandwidth problem or replace Fejer-weighted finite diagonal sums
by unweighted infinite sums without independent justification.

The polynomial factorization statements are possible comparisons
for a nonnegative angular polynomial at a fixed radial slice; the
unknown h need not be a polynomial or strictly positive. Even a
factorization at each slice would still require compatible radial
regularity and the original coupled closure equations. The current
sources therefore settle neither K nor graph realization. No new
factorization or approximation lemma is proposed. Mathlib coverage
of the full target and the supporting results was not checked;
unknown coverage is not evidence of absence.

### Bounded search record and decision

Queries actually issued included:

- `"Fourier series" "closed forms" torus diagonal restriction Fejer C1`
- `multidimensional Fejer theorem continuous functions torus uniform convergence lecture notes pdf`
- `"Grafakos" "Fejer" "uniformly" "Tn"` (also accented Fejer)
- `"closed forms" "Fourier" "torus" differential forms lecture notes`
- `"Fourier" "positive" "diagonal" "null Lagrangian" calibration`
- `"Fourier" "r_x" "q_y" closed form`
- `"r_{x_j}" "q" "h" Fourier`
- `"closed" "two-form" "diagonal" "Fourier" positivity period`
- `"calibration" "Fourier" "torus" "one-sided"`
- `"closed differential forms" "nonnegative" "period" torus domination`
- `"Fourier" "diagonal restriction" "Fejer"`
- `Dritschel Rovnyak operator Fejer Riesz theorem 5.1 multivariable strictly positive`
- `"Rudin" "9.42" "integral" differentiating`

Search snippets, third-party theorem pages and unrelated hits were
not used as theorem evidence. The closed-form cohomology lead of
Dattori da Silva-Meziani was not inspected at theorem level and is
not an input. No exact or stronger applicable sharp-period theorem
was located in this bounded review; that does not establish novelty.
An attempted local curl download failed DNS, but all essential
passages above were accessible through web retrieval. There is no
persistent source blocker and no reason to repeat the same search.

DECISION is EXPLORE for the exact saved target, with adequate source
coverage for one mathematical attempt after separate approval.
Seek either the exact K>=-|M| inequality or an explicit compatibility
obstruction affecting that threshold. Check the zero mode rather
than treating its constancy as its control. If the method supplies
only identities, leaves K uncontrolled, requires extra radial growth
or relies on unproved summability/preservation, save that failure
and abandon this mechanism unchanged. A local or numerical ansatz
does not meet the global certificate threshold K<-|M|.

The downstream use remains L868's obstruction of real nonnegative
coupled L847 graphs if a strict-gain certificate exists; a no-gain
theorem would instead stop this certificate class. Higher-order Xi
signs and RH remain independent. This is development of an existing
certificate route, not a justified creative mechanism at the central
mixed-positivity gap. No such central mechanism was prepared by
this focused source review; the discovery priority remains with the
supervisor. Further literature needs a changed hypothesis, essential
unread source or specific new relevant lead.
