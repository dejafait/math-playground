# Identity-cost Riccati source review1954

Literature-only completion of assessment1953. The central gap remains
L030-L032/C032a actual-Xi positivity and C028b's H_d=o(d). The exact
object is assessment1953's prescribed identity-cost equation and its
upper-left-block metric, retaining all states and all singular values.
No Riccati estimate or new mathematical result is derived here.

## Primary existence coverage and qualifications

Harald K. Wimmer, *On the algebraic Riccati equation*, Bulletin of the
Australian Mathematical Society 14 (1976), 457-461,
[version of record, DOI10.1017/S0004972700025387](https://doi.org/10.1017/S0004972700025387),
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9F85E0FCD2563ECBBA5EAEC50EAE0057/S0004972700025387a.pdf/div-class-title-on-the-algebraic-riccati-equation-div.pdf).
Read (1)-(3), p457; stable maximal-solution statement, p458;
controllability/observability definitions and Lemmas1-2, p459;
Theorem2 with both proof parts, pp459-460; Theorem3/full proof, p461.
For real square matrices his equation is A+WB+B^T W+WCW=0.
With symmetric A>=0, C<=0, controllable (B,C), and observable
stacked (B;A), Theorems2-3 give a unique positive definite solution,
the maximal solution, with B+CW stable. No diagonalizability is assumed.
The proof excludes imaginary Hamiltonian eigenvalues using the two
annihilator conditions, then applies an observable Lyapunov inertia
identity. Here substitute A=I_(2d), B=M_d, C=-I_(2d), W=X_d.
The input -I has full range and output I has zero kernel, so both
rank conditions hold for every actual real M_d. Thus this is matching
existence/positivity/stabilization coverage without actual-root premises.

Vladimir Kucera, *A Review of the Matrix Riccati Equation*, Kybernetika9
(1973), 42-61,
[journal PDF](https://www.kybernetika.cz/content/1973/1/42/paper.pdf).
Read equation(9), p43; definitions and the diagonalizable-Hamiltonian
convention, p44; Theorem3 statement/necessity, p46; Theorem5 and its
short proof, p48. Theorem5 states the usual stabilizable/detectable
existence and uniqueness conclusion. The p44 simplifying convention
is expressly nonessential, but its removal is not proved by that
sentence. Wimmer's unrestricted algebraic result above resolves this
scope issue; no diagonalizability claim about M_d or its Hamiltonian
is imported from the survey.

Frank M. Callier, Joseph Winkin and Jacques L. Willems, *Convergence
of the time-invariant Riccati differential equation and LQ-problem:
mechanisms of attraction*, International Journal of Control59(4)
(1994), 983-1000,
[publisher version in authors' institutional repository](https://pure.unamur.be/ws/portalfiles/portal/36913958/00207179408923113.pdf),
Section2, assumptions(A)/(B), (9)-(10), p985, and Proposition2, p986,
inspected. Its stabilizing convention agrees with M_d-X_d. Its
finite-system horizon convergence is not a degree-uniform estimate
for this sequence, nor a bound on the prescribed full defect.

## Norm inputs and what still needs calculation

Reuse Schmeisser2002 Lemma1, pp211-212, and the norm coverage in
source-notes1523/1947, as recorded canonically in C029b. The height
comparison uses any positive metric and all algebraic multiplicities;
it does not say that the Riccati metric pays the upper majorant.

John Watrous, *The Theory of Quantum Information*, 2018 author version,
[Section1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf),
printed pp32-34, (1.165)-(1.181): reuse assessment1523's inspected
Schatten monotonicity, Frobenius formula and ideal inequality; newly
reinspected (1.175), p33, and (1.179)-(1.181), pp33-34. These permit
p=2 as well as p=1, with no dimension factor in the ideal inequality.
A future full-matrix trace/Frobenius calculation is elementary
specialization of these norms, not a new general norm theorem.

Wimmer does not evaluate the actual k_d^R. Neither a degree-uniform
condition bound for X_d/G_d^R nor a resulting cost estimate has been
proved in this review. The proposed bounded test first seeks scalar
spectral bounds directly from the prescribed equation and C029b's
proved ||M_d||_op<=A=exp(b_1)F(1), then compares full Frobenius size
with the similarity-invariant trace of C_d squared. These are future
calculations, not asserted inequalities or an approved solution.
If they give a positive liminf for the complete k_d^R, stop this
prescribed metric; such a floor cannot lower-bound H_d. If they do
not, record exactly the failed relative estimate before considering
further work. No terminal compression or computed finite sample
can certify the requested o(1) alternative.

## Searches, overlap and sources not imported

Queries actually issued included:

- continuous algebraic Riccati equation stabilizable detectable positive
  definite unique stabilizing solution theorem Q I R I;
- algebraic Riccati equation A transpose X X A minus X squared plus
  identity bounds nonnormal skew symmetric commutator;
- Kucera review matrix Riccati equation1973 theorem5 stabilizable
  detectable pdf;
- Riccati equation bounds solution identity Q B identity singular
  values skew Hermitian part nonnormal matrix;
- "Jensen polynomials" "Riccati"; "Riccati" "Jensen polynomial";
- "Riccati" "companion matrix" symmetrizer trace norm;
- algebraic Riccati equation eigenvalue bounds P Q identity B identity
  lambda min symmetric part A upper lower solution;
- "Riccati" "Frobenius" "skew" "bound";
- "Riccati" "trace norm" "companion";
- "bounded condition number" "similarity" "departure from normality";
- "Riccati" "companion" "Frobenius norm" "bound";
- "imaginary part" "Frobenius norm" "trace" "A^2" matrix.

The bounded search found matching existence theory, not an evaluation
of this actual-family full-cost sequence. Failed searches do not imply
novelty. Generic eigenvalue localization, numerical-radius bounds,
state-dependent Riccati problems and operator gap-angle theorems
are not matching trace-norm decay results.

Read C029b's definitions, conclusions, imported inputs and complete
coefficient norm argument; C028b's height criterion/convergence scope;
C028h/i's exact hypotheses/conclusions; C029a's branch hypotheses and
conclusion; source-notes1947/1523; and stops1948/1949/1951. Narrow
Riccati/LQR and bounded-conditioning/Frobenius searches in companion,
metric and Gramian assessments/attempts found no assessed matching
Riccati full-cost test in those paths. C028h/i allow unbounded
diagonal/shear metrics, C028o/p have prescribed theta measures, and
C029a has a two-site cancellation branch. None identifies G_d^R with
its restricted family. The flat-horizon stops remain intact and do
not settle this changed metric. No cross-notebook input is used.

Haqiri-Poloni, arXiv1509.02015v2 (18March2016),
[Introduction, pp1-3](https://arxiv.org/pdf/1509.02015v2), was inspected
only to distinguish stabilizing conventions from numerical verification.
Its introduction flags diagonalization restrictions in several methods
and a different method without that restriction. No algorithm theorem
or implementation is imported; a floating-point CARE solve is not a
certificate. Its detailed verification cases remain unread.

The search lead *Eigenvalue Bounds in the Lyapunov and Riccati Matrix
Equations* (1981), Zenodo1280577, could not be fetched as a readable
PDF. The 2011 *New Lower Solution Bounds for the Continuous Algebraic
Riccati Equation*, a 2022 upper-bound paper, and Wonham1968 (publisher
page indicates a correction) are unread quantitative/original-source
leads, not imported theorems. They are not essential blockers: existence
is covered by Wimmer and the proposed test needs only elementary
spectral specialization plus already covered norm facts. No API key,
paid access or numerical solver was used. The shell PDF download also
failed DNS; primary text was retrieved through the web tool.

## Decision and continuation gate

SPECIALIZE for one bounded full-matrix obstruction calculation with
the exact actual matrices and prescribed metric. Import Wimmer for
finite existence and the reused Schmeisser/Watrous inputs. Do not
reprove their general results. The remaining difference is the explicit
degree estimate, including every singular value and the upper-left
principal-block convention. Save it in its own canonical result only
after a research turn establishes it.

The new assessment1954 nominates this calculation; the supervisor's
separate next-turn approval is still required. Because a routine
conditioning/trace obstruction may decide the proposal, this review
does not manufacture a creative classification or assert a positive
central-gap mechanism. A creative positive-metric attempt remains
unjustified until this discriminating screen is resolved. Actual signs,
H_d=o(d), RH and full matching Mathlib coverage remain unresolved;
Mathlib was not checked for the Riccati result. PROOF/DAG are unchanged.
