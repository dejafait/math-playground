# Clustered-pole Newton test — working record, step672

Approved target: Test whether Newton-Hermite coordinates remove inverse individual pole-gap factors from L834's relative error bound at fixed k=6002, retaining explicit contour constants and r-dependence and stating the overlap test against m+1<=pi H.

The invocation-start SPECIALIZE assessment is
`literature/2026-11-05-clustered-pole-overlap-scope.md`. Main gap:
actual-Xi all-degree mixed positivity. Intermediate purpose: a quantitative
fixed-shift relative matrix estimate, potentially connecting L834's ray
to a separately justified finite-PF range. Growing shifts, all other
minors and RH remain open. Stop if the result contains only an unnamed
constant, unproved individual gap bounds or the earlier hybrid ratio.

Read the full L834 proof and L832, and compared the step659 hybrid stop
and the fixed-shift/projection assessments. No external source refresh is
needed: de Boor's contour divided differences and Beck et al.'s residue
theorem are covered by the supplied assessment. No cross-notebook input.

## Saved unfinished reasoning

Reverse the reciprocal block's columns to obtain a Hankel moment block
with exponent N=r+k-1. Scale the poles by R, putting x_l=p_l/R in (0,1),
and use Newton polynomials b_i(x)=prod_(a<=i)(x-x_a), 0<=i<k.
Write pi(x)=prod_(a<=k)(x-x_a), J(x)=F(Rx)/pi(x). The coefficient of
b_i(z) in (pi(z)-pi(t))/(z-t) is
lambda_i(t)=prod_(a=i+2)^k(t-x_a). These are finite products, with no
node-gap denominator. Inverse interpolation suggests

    (Q_Newton^(-1))_ij
      = - DD_(x_1,...,x_k)[t^(N+1) J(t) lambda_i(t) lambda_j(t)].

This must still be checked against all scaling, reversal and transpose
factors. Its contour lies at q<s<1 and encloses zero: the numerator has
positive exponent N+1, so no origin pole. The remainder moment block
has an outer contour |u|=1 with integrand
u^(-N-1)b_i(u)b_j(u)/F(Ru); its origin residue supplies the original
coefficient block and must be retained. The product of these two
matrices should be similar to L834's relative matrix. Need an explicit
row-sum bound and the overlap obligation, not just finiteness.

This is unfinished reasoning, not a proved result or a certified onset.

## Completed attempt

The saved derivation is completed in canonical
`../lemmas/L835-fixed-shift-newton-contour-relative-bound.md`; that file
contains the hypotheses, all scaling and transpose factors, precise
source citations, complete proof, qualifications and Mathlib status.
No duplicated proof is maintained here. The admitted interpolation
test passes: a genuine similarity has norm at most
`C(s) s^(r+k+1)`, where every factor of C(s) is an explicit contour
extremum or finite positive product. There is no inverse individual
pole difference or inverse residue derivative. This is standard-method
specialization, not new interpolation theory.

The original column reversal is retained in S_0=W D C^T. The additional
positive diagonal weighting uses Lambda_i=prod_(a=i+2)^k(s+x_a).
The inner contour's length gives the extra power of s; the outer
contour retains the origin residue. These checks give exponent
r+k+1, hence m+k+2 at the first rank beyond a PF_m range.

A separate two-node algebra check verifies the inverse orientation:
with d=x_2-x_1 and u_l=x_l^(N+1)J(x_l), direct inversion of
V diag(A_l x_l^(-N)) V^T, V=[[1,1],[0,d]], gives
[[d u_1,-u_1],[-u_1,(u_1-u_2)/d]]. Substituting lambda_0(t)=t-x_2
and lambda_1(t)=1 in the divided-difference formula gives precisely
these four entries. This is an exact sign/transpose check, not evidence
for the actual 6002-dimensional contour constants or any onset.

The analytic ratio M_s/m_1 and packet-to-complement geometry remain
unbounded numerically. No value of r_* or overlap is certified, no
larger PF cutoff is proved, and actual all-degree positivity remains
open. The proof is unaudited. No mathematical script or numerical
certificate was needed. No route stop or historical work was removed.
