# Lemma 615: a three-packet counterexample to horizontal energy domination

## Hypotheses

Let K(z)=sin(pi*z)/(pi*z), with the removable value K(0)=1.
Use three packets with real parts x_1=-1, x_2=0, x_3=1,
depths u_1=0, u_2=h=1/10, u_3=0, and per-label
multiplicities m_1=2, m_2=1, m_3=2. Each packet contributes
m_j copies of EACH label x_j+i*u_j and x_j-i*u_j.
Thus Z consists of four copies of -1, one copy of each of i/10
and -i/10, and four copies of 1. Coincident labels retain their
full multiplicities. Define all sums over ordered occurrences:

    E(Z)=sum_(z,s in Z) K(z-s)^2,
    M(Z)=sum_(z,s in Z; Re z=Re s) 1.

The square is algebraic, not a modulus square. The real parts are
distinct and lie in [-2,2], the depths lie in [0,2], and all per-label
multiplicities lie in {1,2}. No zeta realization is assumed.

## Conclusion

For this allowed three-packet family E(Z) is real, M(Z)=36, and

    E(Z)-M(Z) < -380/132613 < 0.                         (1)

Consequently E>=M is false for the approved complete three-packet
family and for any unrestricted finite-multiset extension containing
this example. This is an obstruction to that generic energy/count
comparison, not a zeta-zero configuration or a disproof of RH.
It does not contradict the bounded two-packet result C614a.

## Proof

### Complete ordered-pair accounting

Write

    H(b)=(sinh(pi*b)/(pi*b))^2, H(0)=1,
    F=Re K(1+i*h)^2.

The horizontal multiplicities are 4,2,4, so M=4^2+2^2+4^2=36.
The within-packet energies are 16, 2+2H(2h), and 16.
Indeed K(2i*h)^2=H(2h); the middle packet has two equal-label
ordered pairs and two opposite-label ordered pairs.
The two outer packets contribute 32 ordered cross pairs, each zero
because K(2)=K(-2)=0.

The middle packet and the two outer packets contribute 32 ordered
cross pairs. Using the evenness K(-z)=K(z), exactly 16 have value
K(1+i*h)^2 and 16 have value K(1-i*h)^2. These values are conjugate
because K is real entire. Their sum is 32F. There are altogether
34+2+32+16+16=100 ordered pairs, as required for ten occurrences.
No signed cross term or coincident label is removed. Therefore E is
real and exactly

    E=34+2H(2h)+32F,
    E-M=2(H(2h)-1)+32F.                                 (2)

This direct finite calculation does not require a Fourier or norm
theorem. The assessed norm identity is compatible with (2), but its
nonnegativity alone cannot imply E>=M. L614 and C614a are contrasts,
not mathematical inputs to this counterexample.

### Upper bound for the positive self-packet surplus

For real y the standard absolutely convergent hyperbolic power series
and the double-angle identity give, with the removable value at zero,

    (sinh(y)/y)^2=(cosh(2y)-1)/(2y^2)
                 =sum_(k>=0) a_k y^(2k),
    a_k=2^(2k+1)/(2k+2)!.

Here a_0=1 and

    a_(k+1)/a_k=4/((2k+4)(2k+3))<=1/3   (k>=0).

Induction proves 0<a_k<=3^(-k). For 0<=y^2<3, comparison of
nonnegative convergent series consequently yields

    (sinh(y)/y)^2 <= sum_(k>=0)(y^2/3)^k=1/(1-y^2/3).   (3)

Use the classical Archimedean bound pi<22/7 and the exact rational
inequality (22/7)^2<10. At y=2pi*h=pi/5 we have y^2<2/5,
so (3) and the strict increase of 1/(1-r) for r<1 give

    H(2h)<1/(1-2/15)=15/13,
    2(H(2h)-1)<4/13.                                   (4)

All series used above converge absolutely at these arguments; no
infinite multiset sum or unbounded interchange is present.

### Negative cross-packet contribution

The elementary identity sin(pi*(1+i*h))=-i*sinh(pi*h) gives

    K(1+i*h)^2=-sinh(pi*h)^2/[pi^2(1+i*h)^2],
    F=-[sinh(pi*h)^2/pi^2]*(1-h^2)/(1+h^2)^2.

Since 0<h<1 and sinh(pi*h)>=pi*h by its positive power series,

    F<=-h^2(1-h^2)/(1+h^2)^2=-99/10201.                 (5)

The reversal in (5) is due to multiplication by the negative factor
-(1-h^2)/(1+h^2)^2. No modulus square is substituted.
Combining (2), (4) and (5) proves the exact bound

    E-M < 4/13-3168/10201=-380/132613<0.

This proves (1) for one exact allowed point, which is sufficient to
refute the universal three-packet assertion; a parameter grid is
unnecessary. Each two-packet comparison can spend the middle packet's
self surplus, but adding both comparisons would spend it twice.
The full accounting above exhibits the failure of that inference.

### Verification, source comparison and limits

Run from the active notebook:

    python3 scripts/aggregate-energy/certify_three_packet_witness.py

The script uses exact `Fraction` arithmetic. It enumerates every
ordered difference of all ten occurrences, retains coincident labels,
checks the coefficients in (2), M=36, the allowed parameter constraints,
and every rational bound in (4)--(5) and (1). The complete difference
table, rational bounds, script hash and failures are saved in
`scripts/aggregate-energy/three-packet-witness.json`. The run reports
100 ordered pairs and zero failures. This checks the discrete accounting
and rational arithmetic; the analytic identities and all-k coefficient
comparison are proved above. No floating transcendental evaluation is
used. This construction certificate alone does not verify the analytic
identities; the separate proof/code audit is recorded below. No formal
runtime verification is claimed.

The prior EXPLORE assessment is
`drafts/literature/2026-11-01-three-packet-horizontal-energy-test.md`.
It found no matching theorem or certified obstruction among the sources
checked, which does not establish originality. The counterexample does
not reprove the known Fourier/norm identities or improve a cited zeta
theorem. General energy/count domination in this scope is now stopped;
comparisons under additional zeta-specific restrictions, actual-zeta
weights, charge conversion, exceptional centers and Xi signs remain
unresolved. The two-packet theorem and its unfinished first certificate
are preserved unchanged.

### Separate proof and certificate audit — 1 November 2026

STEP_ID: 2026-11-01-l615-independent-audit-01.
The audit found no mathematical correction necessary. It reused the
unchanged EXPLORE assessment for precisely the same three-packet target;
no larger family or new sign input is approved by this review.

The ten occurrences were reconstructed explicitly, without importing
the construction generator. All 100 indexed ordered pairs, including
the coincident outer labels, were matched against the COMPLETE original
difference table. The nine difference classes have counts 16 at each
of (+-2,0), 8 at each of (+-1,+-1/10), 1 at each of (0,+-1/5), and
34 at (0,0). Evenness maps the four off-axis classes into two conjugate
kernel values, each with count 16. The charge condition is dx=0,
including the opposite middle labels, and gives 34+1+1=36.
Thus the certificate checks (2), rather than an absolute-square sum
or a sum with multiplicities suppressed.

The analytic review checked the removable value at zero, integer sinc
zeros, conjugation, the sine identity and the real part of
(1+ih)^(-2). In the self-energy comparison a_0=1 exactly, and

    (2k+4)(2k+3)-12=4k^2+14k>=0 for EVERY integer k>=0.

Consequently a_(k+1)/a_k<=1/3 is an all-k statement, not a truncated
series test. The double-angle series is absolutely convergent, and its
nonnegative coefficients license the comparison in (3). The standard
Archimedean pi bound and (22/7)^2<10 give the STRICT inequality
y^2<2/5; hence (4) stays strict even though (3) is nonstrict.
For (5), h=1/10 makes the multiplier of sinh(pi*h)^2 negative, so its
lower bound yields an upper bound for F. The exact final comparison
is 4/13-3168/10201=-380/132613<0. There is no rounding or hidden limit.

Reproduce the independent finite replay from this notebook:

    python3 scripts/aggregate-energy/audit_three_packet_witness.py

The replay checks the entire original difference table, all energy
categories and rational bounds, admitted packet parameters, conjugation,
and the construction-script hash. It saves every indexed pair and all
19 passing checks in `scripts/aggregate-energy/three-packet-audit.json`;
there are zero failures. The original construction script was also
replayed successfully. Analytic identities and the all-k reasoning
remain prose proofs, not assertions established by running the code.
This is an independent reconstruction in a separate session, not an
external referee report, formal runtime verification or Lean proof.

The strict counterexample therefore survives review. It closes this
universal domination claim; it establishes no actual-zeta realization,
no Xi sign, and no originality beyond the literature checked. L614 and
C614a remain contrasts only, so the empty L615 input row is unchanged.

## Mathlib

Full matching coverage for this explicit energy/count counterexample is
not checked. Supporting finite-sum, complex-sine, hyperbolic-series and
Archimedean-bound results have not been checked for this specialization.
Unknown coverage is not evidence of absence. No Lean verification is
claimed.
