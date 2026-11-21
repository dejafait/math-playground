# Scalar theta-resolvent overlap — audit coverage1200

TARGET: Audit the scalar theta sign problem in Abdillah (8.16) against Polson v24 Theorem5.3 and positive W, checking normalization, differentiated Laplace convergence and the equivalent variance inequality for every r>0.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse review1200's theta/Hankel searches and new primary lead, plus assessments1108/1188/1198 for unchanged heat inputs. Scoped comparisons1117/1181 address stronger Stieltjes/all-order bridges, not this scalar normalization audit. No originality claim; this is a possible known-result overlap.
SOURCE_EVIDENCE: Polson1708.02653v24 Theorem5.3/(5)-(6)/complete proof p9, Theorem5.6(i)/proof p11, TheoremA p3/Section6.3 p15; Abdillah viXra2609.0027v1 Section5.3/(5.11)-(5.16) p17, Section5.5 p18, (6.12)-(6.15) pp20-21, (7.19)-(7.21) p25, (7.43)-(7.44) pp27-28, (8.16)/Section8.7 p30. C030b's normalization and C030g's conclusion inspected. Primary URLs/qualifications below.
COMPARISON: Polson supplies positive W and a Laplace representation of a logarithmic derivative. Abdillah supplies a theta expression and scalar sign question for a folded logarithmic derivative. Check their normalization and scalar specialization; no heat-block propagation or Stieltjes representation follows from source matching alone.
GAP: Audit logarithmic derivatives, representative/multiplicity factor, x=r^2 orientation, dominated differentiation for every x>0 and strict variance formulation. No pass verdict or new inequality is established here.
REASON: Different independently testable source-overlap audit after parking propagation. Reproduction prevents treating a potentially covered scalar condition as a new central input. Import source positivity; do not reprove its computational or near-time estimates.
SCOPE: One REPRODUCTION proof_audit for actual Xi, x=r^2>0 and unchanged actual theta law. Inputs C030b,C030g and named primary results; exclude r=0, all-order derivative claims, numerical scripts, generic-density extensions, matrix propagation and RH inference. Newly saved coverage needs separate next-turn approval.
LITERATURE_REASON: Review1200 discovered a new primary source whose scalar condition needs comparison with known heat inputs; target changes from matrix propagation to scalar overlap. No further search on ready coverage is requested.

## Prospective check, sources and use

[Polson v24](https://arxiv.org/pdf/1708.02653v24),11September2026,
Theorem5.3 states G'/G(u)=integral exp(-ut)W(t)dt on
Re(u)>-min Re(a_k). Its proof retains complex exponents, multiplicity
and absolute Fubini. TheoremA supplies W(t)>0 for all t>0, using finite
zero verification; C030b already imports sufficient positivity.
Theorem5.6(i)'s proof calls log G Bernstein when W>=0. These results
are imported, not independently reaudited. C030g supplies compact-time
convergence only; endpoint domination remains to check.

[Abdillah v1](https://vixra.org/pdf/2609.0027v1.pdf), *A Theta-Geometric
Framework for the Hankel Positivity Problem in the Riemann Hypothesis*,
September2026, uses S(r^2)=A'(r)/(2rA(r)),
A(r)=integral Phi(u)cosh(ru)du and F(r)=4A(r). Its push-forward law
omega_r in (7.43) uses y=r*u. Formula(7.44) writes the double kernel
integral as 2(E_omega a-Var_omega b), where
a(y)=y*tanh(y)-y^2*sech(y)^2 and b(y)=y*tanh(y).
Section8.7 retains the scalar sign question in this presentation.
No source error or overlap is yet concluded.

Success requires a justified identification of the scalar observables
and a dominated differentiated Laplace formula giving the corresponding
strict variance inequality for every r>0, relative to imported positive
W. Record any mismatch or missing domination exactly. Numerical samples
do not establish an all-r result. Source notes suffice if no separate
canonical lemma is useful; do not manufacture one to record overlap.

This calibrates which signed theta information is covered. It gives
no C_N, heat-block boundary reaction sign or all-degree mixed positivity.
A positive resolvent Laplace measure is not automatically a positive
reciprocal-zero Stieltjes measure; the parameter-dependent theta law is
not that fixed spectral measure. No proof of this specialization is
written or approved here. This is ordinary specialization, not creative
mathematics. Full Mathlib coverage is unchecked; no cross-notebook input.
