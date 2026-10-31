# Approved periodic commutator attempt — working record

2026-10-30. Gate: the pre-existing EXPLORE assessment
`literature/2026-10-30-l522-periodic-commutator-hypothesis-test.md`.
The exact target is the bounded L2 commutator form of h(A_I) with
D_per, h(s)=s/(1+s^2), for L522's full signed killed operator.
No nullvector, H1 regularity, favorable sign or periodic replacement
of A_I is assumed. L516/L521/L522 specify the operator. The saved
collective-source comparison and generic pole-resolvent stop were
checked. Prior unfinished work is preserved.

Main gap: actual-Xi all-degree positivity. Intermediate target:
one finite form bound, or normalized periodic H1 pairs with exact
form values diverging. A bound would supply only the first regularity
premise of a possible Mourre application; C2, the local estimate,
renewal compatibility, realization and Xi transfer remain open.
Failure parks this h/D_per implementation, not all generators.

Initial route: direct endpoint-trace arguments for B=h(A_I) cannot
use L513/L515 without proving bounded forcing and nonzero trace for
the selected output. L2 resolvent control alone does not provide
those hypotheses. No such implication is asserted.

Boundary-packet test now being developed: scale smooth packets at
distance comparable to epsilon from an endpoint, with frequency scale
epsilon^(-1). G_I has leading scalar log(1/epsilon) on this scale.
Seek a rigorously controlled h(A_I) expansion whose second term
detects the missing interaction across the periodic seam. Error must
be o(log(1/epsilon)^(-2)) before a commutator scale epsilon^(-1)
can be used. Full signed perturbation and low spectral leakage must
be controlled; a formal multiplier expansion does not pass the test.

## Candidate closure found during this attempt

Choose nonnegative real unit L2 bumps f in C_c^infinity(-1,1),
f(0)>0, and g in C_c^infinity(2,3). Let phi_e be the periodic
epsilon-scaled f packet crossing the seam, and psi_e the scaled g
packet just to its right. Put alpha_e=epsilon phi_e' and
beta_e=epsilon psi_e'. All four zero extensions are sums of scaled,
translated fixed piecewise smooth profiles with Fourier decay O(1/|xi|).
Thus ||(A_I-log(1/epsilon))p_e||_2 is uniformly bounded for each
of the four families. These residuals converge weakly to zero:
test against a compact interior smooth function, use self-adjointness,
and note eventual disjoint supports for the scalar term.

The full operator has compact resolvent: bounded graph norm controls
the logarithmic form, whose Fourier tails vanish uniformly, while
fixed frequency truncations of zero extensions from a bounded interval
are compact. The exact twice-expanded resolvent identity consequently
gives, for any two of the four families and L=log(1/epsilon),

    <p,h(A)q>=h(L)<p,q>+h'(L)<p,(A-L)q>+o(L^-2).

This controls low spectral leakage without an unjustified inverse
power series. For the real packets the commutator form equals
-i/epsilon times <phi,h(A)beta>+<alpha,h(A)psi>.
The scalar contribution is zero. Since psi has compact interior
support, A psi'= (A psi)' up to and including the endpoint limits.
Integration by parts gives

    <phi,A beta>+<alpha,A psi>
       =epsilon phi(0)[(A psi)(ell)-(A psi)(0)]
       -> kappa=(f(0)/2) integral_2^3 g(v)/v dv >0.

The kernel n supplies the displayed limit; all prime endpoint samples
are zero for sufficiently small epsilon (including equality atoms),
the scalar samples are zero, and the continuous signed convolution
and opposite-end n term are O(sqrt(epsilon)). Thus the candidate
exact form asymptotic is (i kappa/(epsilon L^2)) times (1+o(1)).
The complete proof is now canonical in
[L529](../lemmas/L529-killed-periodic-commutator-boundary-obstruction.md);
it remains unaudited. No endpoint trace of h(A) applied to arbitrary
L2 data is used. This working record preserves the initial failed
trace shortcut and development, without replacing the canonical proof.
