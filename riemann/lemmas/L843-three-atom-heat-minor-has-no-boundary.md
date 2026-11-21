# Lemma 843: the fixed three-atom heat minor has no zero boundary

## Hypotheses

Let \(a=p_0>0\), \(b=p_1>0\), \(c=p_4>0\), with \(a+b+c=1\). Define

\[
q_n(t)=\frac{a\,0^n+b e^t+c e^{4t}4^n}{(2n)!},\qquad n\ge0,
\]

where \(0^0=1\), and set

\[
M(t)=(q_{2+i-j}(t))_{i,j=0}^2,\qquad B(t)=\det M(t).
\]

The weights are normalized only at \(t=0\); no division by their
time-dependent total mass is made. This is the explicitly defined
atomic law on \(\{0,1,4\}\), not the theta density or a compensated
reciprocal-moment law.

## Conclusion

\[
B(0)\ge \frac{671116}{14515200}c^3>0.
\]

Consequently the approved test has no solution: its simultaneous
requirements \(B(0)=0\), \(\operatorname{rank}M(0)=2\), all proper square minors
positive, and \(B'(0)>0\) cannot hold. This conclusion does not determine
all proper minors, establish a general invariant cone, or decide any
actual-Xi sign. No larger support or rank is covered.

## Proof

**Source use and specialization.** The heat coefficient shift and the
row-replacement identity are the known differentiation tools in Pulin
Shi, *Coefficient Dynamics and Consecutive Toeplitz Minors for the de
Bruijn–Newman Family*,
[Hexagon2610.00521v1](https://hexagonmath.org/pdf/2610.00521v1), PDF dated
24 October 2026, Corollary 3.2, (3.4)–(3.5), Proposition 3.3, (3.6),
pp5–6, and Proposition 9.1, (9.1), p12 (Remark 9.2, p13).
Reuse the inspected theorem/proof coverage recorded in
`drafts/literature/2026-11-06-three-atom-heat-minor-boundary-flux.md`
and its parent comparison. Only those algebraic tools are used, not
a claimed positivity theorem. The fixed-family determinant sign below
is a conventional finite specialization not decided by those identities.
Its explicit verification is needed because the source does not sign
the cofactors. Finite sums need no interchange or tail estimate.

**All coefficients and the time convention.** At zero the coefficients
needed for the matrix and its derivative are exactly

\[
q_0=a+b+c,\quad q_1=(b+4c)/2,\quad q_2=(b+16c)/24,
\]
\[
q_3=(b+64c)/720,\quad q_4=(b+256c)/40320,\quad
q_5=(b+1024c)/3628800.
\]

Differentiating each finite term gives, at every real \(t\),

\[
q_n'(t)=\frac{b e^t+4^{n+1}c e^{4t}}{(2n)!}
       =(2n+2)(2n+1)q_{n+1}(t).
\]

In particular the full derivative matrix at zero is

\[
M'=\begin{pmatrix}
30q_3&12q_2&2q_1\\
56q_4&30q_3&12q_2\\
90q_5&56q_4&30q_3
\end{pmatrix}.
\]

Writing \(R_i\) for row \(i\) of \(M(0)\) and \(R_i'\) for the
corresponding displayed derivative row, the cited identity specializes
to the sum of exactly three terms

\[
B'(0)=\det(R_0',R_1,R_2)+\det(R_0,R_1',R_2)
                         +\det(R_0,R_1,R_2').
\]

The certificate retains each term and checks its sum against direct
time differentiation of the determinant polynomial. Thus no missing
cofactor or factorial is being suppressed. No derivative sign will be
needed: the zero-determinant prerequisite is already impossible.

**Exact expansion and strict positivity.** The matrix is

\[
M(0)=\begin{pmatrix}q_2&q_1&q_0\\q_3&q_2&q_1\\q_4&q_3&q_2\end{pmatrix}.
\]

Its six-term determinant expansion, before any substitution, is

\[
B=q_2^3-2q_1q_2q_3+q_1^2q_4+q_0(q_3^2-q_2q_4).
\]

Put \(D=14515200\). Substituting the exact coefficients gives

\[
DB=a(13b^2-496bc+53248c^2)
       +313b^3+3117b^2c-84048bc^2+1282048c^3.
\]

Every sign needed here follows from the explicit identities

\[
13b^2-496bc+53248c^2
  =13(b-20c)^2+24bc+48048c^2,
\]
\[
313b^3+3117b^2c-84048bc^2+1282048c^3
  =313b^3+3117c(b-14c)^2+3228bc^2+671116c^3.
\]

All terms on the right are nonnegative for positive \(a,b,c\), and
the final \(671116c^3\) is strictly positive. This proves the stated
bound. In fact the matrix is invertible, so there is no rank-two zero
boundary to which a proper-minor or positive-flux filter could apply.
The probability constraint only restricts the domain further; it is
never used to change a coefficient or normalize a derivative.

**Certificate and limitations.** Reproduce with
`python3 scripts/heat/three_atom_boundary_flux_20261106.py`.
Full exact coefficients, determinant expansion, the two positive
decompositions, all three row derivatives, their sum and seven equality
checks are saved in
`scripts/heat/three-atom-boundary-flux-20261106.json`.
The reported status is `FIXED_SUPPORT_NO_BOUNDARY`, with no failures.
All relevant coefficient/determinant/row-derivative values and checks
were inspected in full; the displayed polynomial identities also give
a standalone proof independent of a numerical search. The program uses
Python integer/Fraction arithmetic; its runtime is not formally verified.

An initial rational boundary-elimination diagnostic produced negative
values for \(a/c\) at every tested positive \(b/c\); those points were
invalid weights and are not witnesses. The exact identities above,
rather than that diagnostic or a near-zero determinant, prove
nonexistence. The abandoned diagnostic is recorded in the working note.
This negative result retires only this discriminator. It does not
refute the possibility of backward heat descent under other premises,
prove invariance even for this family from general cone hypotheses, or
license a new support/rank sweep. Actual-theta signed estimates,
all-order transfer, realization and the RH gap remain unresolved.
This is local reproduction/specialization, not a claim of mathematical
novelty beyond the inspected sources.

**Independent audit, 6 November 2026.** The audit script
`scripts/heat/l843_independent_audit_20261106.py` does not import the
original polynomial engine. For each of the six signed permutations
\(\sigma\in S_3\), put \(n_i=2+i-\sigma(i)\). For each ordered atom
assignment \((y_0,y_1,y_2)\in\{0,1,4\}^3\), its determinant contribution
is exactly
\[
 \operatorname{sgn}(\sigma)
 \prod_{i=0}^2\frac{p_{y_i}y_i^{n_i}}{(2n_i)!}.
\]
This is the finite distributive expansion of the Leibniz formula,
including every assignment with zero contribution. In a derivative
replacing row \(i\), multiply this contribution by \(y_i\); the sum
of the three replacements multiplies it by \(y_0+y_1+y_2\).
Thus a monomial \(a^\alpha b^\beta c^\gamma\) has derivative
multiplier \(\beta+4\gamma\), independently checking the time convention.
All 162 assignment contributions are retained in the audit certificate.

The recovered coefficients of \(DB\), in the order
\[
(a^3,a^2b,a^2c,ab^2,abc,ac^2,b^3,b^2c,bc^2,c^3),
\]
are
\[
(0,0,0,13,-496,53248,313,3117,-84048,1282048).
\]
They agree with the expansion above, including all three absent
monomials. Direct binomial expansion independently recovers the two
square identities: the first square contributes \(-520bc+5200c^2\)
besides \(13b^2\); the second contributes
\(-87276bc^2+610932c^3\) besides \(3117b^2c\).
Adding their displayed positive terms gives exactly the claimed
coefficients and the retained lower-bound term \(671116c^3\).
For positive masses all square terms and remaining terms have the
required nonnegative signs. No normalization constraint, proper-minor
claim or flux sign is used to obtain the strict determinant bound.

The complete audit certificate is
`scripts/heat/l843-independent-audit-20261106.json`, status `AUDIT_PASS`,
16 checks and no failures. Complete coefficient, row-derivative and
square-term tables were inspected; the exhaustive finite expansion
above justifies the enumeration rather than inferring correctness from
a preview. The audit confirms this already stated finite result and
retires the fixed witness family; it establishes no stronger sign
theorem or new mathematical novelty. The direct local input list
remains empty. Formal runtime and Mathlib qualifications remain below.

## Mathlib

Full matching fixed-support theorem: not checked. Supporting determinant
multilinearity, finite-sum differentiation and rational polynomial
identities were verified here informally/exactly, without a Mathlib
dependency. Unchecked availability is not evidence of absence.
