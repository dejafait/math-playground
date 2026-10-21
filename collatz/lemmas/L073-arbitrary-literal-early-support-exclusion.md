# L073 — Arbitrary literal early-support exclusion

## Hypotheses

Keep L055's 25 indexed integer pairs J_i,H_i in literal order, i=0,...,24.
Let b_i be nonnegative integers with sum b_i=9250245 and
sum_(i=0)^22 b_i>=1. Put a_i=2+18b_i. Suppose real junctions
s_i>=540/11 satisfy s_25=s_0 and every exact L051 endpoint

\[
s_{i+1}=2^{-a_i}\left(G_i s_i-\frac{12}{11}(3/2)^{H_i}-1\right)
                 +\frac{23}{11},\qquad
G_i=(27/16)^{J_i}(3/2)^{H_i},
\]

and every own-input non-strict J guard

\[
4J_i\log2\le\log s_i+\log(11/4),\qquad 0\le i\le24.
\tag{1}
\]

All logarithms are natural. No H guard, seed, minimum location,
integer/parity/residue/valuation realization, actual-word hypothesis,
primitive count or count-ray premise is imposed.

## Conclusion

No such tuple exists, for any allocation in the stated integer simplex.
Under the endpoint/domain/J assumptions, all extra tail budget must
therefore lie in rows 23 and 24. This is only a restriction for the fixed
pairs in literal order; it supplies no nonliteral-order exclusion,
integer realization, unrestricted cycle exclusion or universal descent.
The two previously known rational witnesses have no early support and
remain valid. The separate critical audit below found no defect within
this fixed-pair, literal endpoint/domain/J scope.

This is local REPRODUCTION of known affine machinery with a newly
justified uniform allocation comparison, under the prior SPECIALIZE
assessment `drafts/literature/2026-10-16-arbitrary-tail-literal-early-support.md`.
No originality beyond inspected sources is asserted.

## Proof

### A bound at input zero conditioned on all J guards

Put n_i=s_i-23/11>=47 and

\[
\eta_i=\frac{23}{11}-\frac{12}{11}(16/27)^{J_i}
                     -(16/27)^{J_i}(2/3)^{H_i},\qquad
c_i=\frac{3^{3J_i+H_i}}{2^{4J_i+H_i+a_i}}.
\]

As in L055, 0<eta_i<23/11 and the exact local coordinate match gives
n_(i+1)=c_i(n_i+eta_i). The standard formal affine composition input is
Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Its prescribed nonempty word has K=397573379 odd letters and
N=630138897 total letters here. These totals follow from L055's table
and sum a_i=50+18*9250245=166504460. Thus changing the allocation
does not change prod c_i=3^K/2^N. L055's audited count-dependent bound
gives Lambda=N log2-K log3>lambda_-=10584/10^14>0. The denominator
in the source fixed-point formula is nonzero; only formal affine
composition is imported, not any parity interpretation or integer orbit.
The following product and comparisons justify the changed-allocation
specialization rather than reprove the general coding theorem.

Multiply n_(i+1)/n_i=c_i(1+eta_i/n_i) over all 25 endpoints.
Closure and positivity justify cancellation, including the closing edge,
and taking logarithms gives

\[
\Lambda=\sum_{i=0}^{24}\log(1+\eta_i/n_i).
\tag{2}
\]

For i>=1 the literal table has J_i>=15. Exponentiating (1) gives
s_i>=(4/11)2^{4J_i}, hence

\[
n_i\ge\frac{4\cdot2^{60}-23}{11}>0.
\]

Using log(1+x)<x for x>0 in (2), define

\[
E=\frac{24\cdot23}{4\cdot2^{60}-23}
  =\frac{552}{4611686018427387881}<\lambda_-.
\]

Every summand with i>=1 is strictly below E/24; the remaining one is
strictly below 23/(11n_0). Consequently

\[
\lambda_-<\Lambda<\frac{23}{11n_0}+E,
\qquad
s_0<\frac{23}{11(\lambda_--E)}+\frac{23}{11}
=\frac{1325859730438202850942226985830949}
       {67113790726173775832193}<20\cdot10^9.
\tag{3}
\]

All denominators are positive. L064 certifies log(20*10^9)<24 by a
finite lower sum for exp(24). Thus log s_0<24. This uses the proposed
solution's guards as necessary premises in a contradiction; it does not
assume that zero is a minimum or that any arbitrary-tail row grows.

### The first recipient gives a failed guard

Let j be the least index in {0,...,22} with b_j>=1. It exists by
the early-support hypothesis and integrality. For every t<j the tail
is exactly 2, while a_j>=20. For a row write

\[
Q_i=(12/11)(3/2)^{H_i}+1,\qquad
F_{i,a}(s)=2^{-a}(G_i s-Q_i)+23/11.
\]

On s>=540/11, the bracket G_i s-Q_i equals
G_i(n+eta_i)>0. Therefore F_(i,a)(s) is decreasing in a on this
domain. Every H_i>=40, and the exact inequality

\[
\frac{23}{11}2^{20}<\frac{12}{11}(3/2)^{40}+1
\tag{4}
\]

shows that F_(i,20) has strictly negative shifted affine offset.
The offset of F_(i,2) is also strictly negative, since
Q_i>(23/11)2^20>(23/11)2^2.
Set c_i^*=G_i/4. For t<j the actual endpoints thus obey
s_(t+1)<c_t^* s_t; at the first recipient,

\[
s_{j+1}=F_{j,a_j}(s_j)\le F_{j,20}(s_j)
                <2^{-18}c_j^*s_j.
\]

All multipliers and actual junctions are positive. Induction, including
the case j=0 with an empty preceding prefix, and (3) now give

\[
\log s_{j+1}
 <24+\sum_{t=0}^j\bigl(J_t\log(27/16)+H_t\log(3/2)-2\log2\bigr)
       -18\log2.
\tag{5}
\]

Only the first recipient's tail was replaced by a smaller comparison
tail. Later tails remain arbitrary and enter the full product (2).
No small-tail offset or growth bound is applied to those later rows.

### All 23 possible first recipients

Import L064's certified outward logarithm constants with S=10^12:
E_-=693147180559, E_+=693147180560,
T_-=1098612288668, T_+=1098612288669 and D_+=1011600911679.
They satisfy E_-/S<log2<E_+/S, T_-/S<log3<T_+/S and
log(11/4)<D_+/S. In particular
A_+=3T_+-4E_-=523248143771 and
B_+=T_+-E_-=405465108110 are strict scaled upper bounds for
log(27/16) and log(3/2). There is no fresh numerical logarithm assumption.

For each j=0,...,22 define the exact integer

\[
U_j=24S+\sum_{t=0}^j(J_tA_++H_tB_+-2E_-)
        -18E_-+D_+-4J_{j+1}E_-.
\]

Equation (5), with the negative coefficients bounded using E_-, gives

\[
\log s_{j+1}+\log(11/4)-4J_{j+1}\log2<U_j/S.
\tag{6}
\]

These are exactly the 23 upper-margin numerators displayed in L064's
complete finite guard comparison. Their maximum is
U_4=-9322534135606, so every U_j/S<-9.32<0. The certificate below
recomputes all 23 from the literal table. Hence (6) contradicts the
required non-strict guard at the first recipient's next input j+1.
Every admitted allocation has one such first recipient, so this proves
the exclusion on the entire simplex, without enumerating allocations.

Reproduce the finite arithmetic with
`python3 scripts/postspell-word-count/certify_arbitrary_literal_early_support.py`.
Its full certificate is
`scripts/postspell-word-count/arbitrary-literal-early-support-certificate.json`.
It contains 26 exact rational comparisons and five integer checks, all
passing, with complete operands for (3)–(4) and every U_j. All those
checks and all 23 margin records were inspected in full. It imports the
already certified logarithm enclosures; it does not certify a general
theorem by sampling. The written first-recipient argument provides the
universal allocation coverage. L064's small-tail root/growth conclusions
and L068/L072's restricted-family exclusions are not invoked here.

### Independent critical audit — 2026-10-16

The prior SPECIALIZE assessment
`drafts/literature/2026-10-16-arbitrary-literal-early-support-critical-audit.md`
approved exactly this audit, with REPRODUCTION classification. The audit
found no defect. It verifies the existing exclusion, without enlarging
its allocation/order hypotheses or adding a realization consequence.
The standard affine and positive-real logarithm inputs are reused from
that assessment; the finite specializations are checked independently.

L051 (3)–(4) supply precisely the displayed J guard and endpoint.
Their other real-system premises are not used. L055's table has J_0=8,
J_i>=15 for all 1<=i<=24, and H_i>=40 throughout. Its integer sums
give K=397573379 and N=630138897 for every allocation in the stated
simplex, including the closing row's actual tail. Thus the count-dependent
Lambda estimate applies without transferring any old allocation's root,
minimum or growth estimate.

For the symbolic coordinate check, c_i=2^(-a_i)G_i and

\[
c_i\eta_i=(23/11)c_i
 -2^{-a_i}\bigl((12/11)(3/2)^{H_i}+1\bigr).
\]

Subtracting 23/11 from the endpoint therefore gives exactly
n_(i+1)=c_i(n_i+eta_i). Each n_i>=47 is positive. Both factors
(16/27)^{J_i} and (2/3)^{H_i} lie strictly between zero and one,
so the two subtracted terms defining eta_i have positive sum strictly
less than 23/11. This proves 0<eta_i<23/11 without any tail bound.
Multiplying all 25 positive endpoint ratios cancels every n_i, including
the closing edge, and yields (2). The strict inequality log(1+x)<x
applies to each x=eta_i/n_i>0, as in the assessed
[DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1).

Exponentiating each nonzero-index guard gives exactly
n_i>=(4*2^{4J_i}-23)/11>=(4*2^{60}-23)/11. Hence the sum
of those 24 logarithms is strictly less than E, with no minimum-location
assumption. The independently checked residual denominator is

\[
\lambda_- - E
=\frac{6101253702379434166563}
       {57646075230342348512500000000000}>0.
\]

It is legitimate to rearrange
lambda_- - E<23/(11n_0) and invert its positive sides. This gives
exactly (3), including the addition of 23/11. The fraction displayed in
(3) and its strict comparison with 20*10^9 both check. No assumption
about which junction is smallest enters this argument.

For the first-recipient argument, the least j<=22 with b_j>=1 exists
because the b_i are nonnegative integers and their early sum is positive.
All earlier b_t are zero, and a_j>=20. On every actual input's domain,
G_i s_i-Q_i=G_i(n_i+eta_i)>0; increasing the tail therefore decreases
the endpoint value at that same input. The exact comparison for the
tail-20 offset has operands

\[
\frac{23}{11}2^{20}=\frac{24117248}{11}
 <\frac{36472999400827762787}{3023656976384}
 =\frac{12}{11}(3/2)^{40}+1.
\]

Since H_i>=40, this implies both needed negative offsets, for tails
20 and 2. The tail-20 map is only a comparison at s_j; it need not
be an actual new trajectory. All actual endpoints remain positive by
hypothesis. Multiplication by positive prefix coefficients and monotonicity
of log prove (5), including j=0, whose preceding prefix is empty.
The actual later tails can be arbitrarily large and need not have negative
shifted offsets or growing endpoints. They have already been retained
in the cyclic product and are not used in this prefix estimate.

The independent program
`python3 scripts/postspell-word-count/audit_arbitrary_literal_early_support.py`
neither imports nor executes the original certifier. It independently
transcribes all 25 pairs and compares them with L055 and the original
certificate. It checks all integer sums and minimum parameter bounds.
For each t=2,3,11/4, use the assessed positive-real expansion
[DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4) with x=(t-1)/(t+1).
The already justified finite-series remainder enclosure, here with 128
unrounded rational terms, is

\[
P=2\sum_{m=0}^{127}\frac{x^{2m+1}}{2m+1},\qquad
P<\log t<P+\frac{2x^{257}}{257(1-x^2)}.
\]

All three arguments have 0<x<=1/2, so the remainder denominator is
positive. These independent intervals verify every L064 grid constant
used above and the L055 Lambda interval, using opposite interval ends
in N log2-K log3. The full Lambda fractions were inspected. The exact
41-term sum used for exp(24) is

\[
\sum_{k=0}^{40}\frac{24^k}{k!}
=\frac{202750314819830504045671593478515759301}
       {7661655986496068058455078125}>20\cdot10^9.
\]

Positivity of the remaining terms in the assessed
[DLMF 4.2.19](https://dlmf.nist.gov/4.2.E19) proves log(20*10^9)<24.
No floating-point logarithm or approximate cyclic root is used.

To check each margin independently of the original recursive formula,
set p_j=sum_(t=0)^j(3J_t+H_t) and
q_j=sum_(t=0)^j(4J_t+H_t+2). Direct summation gives

\[
U_j=24S+p_jT_+-(q_j+18+4J_{j+1})E_-+D_+.
\]

The positive p_j multiplies an upper log3 bound; the negative coefficient
of log2 multiplies a lower bound. This agrees with (6) at every one of
the 23 positions. All original prefix and margin records, all 26 rational
comparisons with their full operands and differences, and all five integer
checks were reconstructed and checked. The 23 published L064 numerators
match exactly. A second evaluation uses the unrounded log intervals
directly in 24+p_j log3-(q_j+18+4J_{j+1})log2+log(11/4);
each resulting strict upper bound is smaller than U_j/S and below -9.32.
The largest grid upper bound remains -9322534135606/10^12 at j=4.
Every allowed first recipient therefore contradicts its own next-input
non-strict guard. Existence of that first recipient exhausts the simplex;
no enumeration of allocations or sampled feasibility test is involved.

The full independent evidence is
`scripts/postspell-word-count/arbitrary-literal-early-support-audit-certificate.json`:
133 exact checks pass, with no failures. It retains the original
certificate's SHA-256, every unrounded logarithm term, remainder and
interval, all independent margin operands, all reconstructed original
comparisons and the 41 exponential terms. Its complete selected summary
and Lambda interval were inspected; the original certificate is unchanged.

The direct mathematical inputs remain L051, L055 and L064. Both known
no-early-support rational witnesses and prior method failures remain
valid. No H/seed, minimum, integer/parity/valuation, actual-word or
primitive/count-ray premise is added. Nonliteral orders, integer
realization, other indexed pairs and universal eventual descent remain
unresolved by this audit. The main argument and DAG require no change.

## Mathlib

Full matching coverage is unchecked; no absence claim is made. The
certificate verifies finite rational and integer comparisons accompanying
the written proof, not a Lean theorem. The source's formal affine result
does not supply integer realization, and no integer-cycle computational
threshold is used in this necessary-subsystem exclusion.
