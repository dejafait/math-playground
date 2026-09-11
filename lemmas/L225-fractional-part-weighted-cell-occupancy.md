# Lemma 225: fractional-part weighted cell occupancy

**Hypotheses.** Use L224's interior box, scales, J=[j0,j1],
D(a,c,d), Z_a and T_a. Retain L220's exact rounded A_m,B_m
and L223's aggregate S,T. Fix a,c,d, and put v=cd. Let Bset be
the integers b in [N,2N] that satisfy L224's strict interval (6).
For each b in Bset define

alpha_b=sqrt(avb-R), beta_b=sqrt(a(v+1)b+R-1),
ell_b=beta_b-alpha_b, theta_b=1-{alpha_b},
k_b=floor(alpha_b)+1, delta_b=2 alpha_b theta_b+theta_b².

All assertions below are for sufficiently large N.

**Conclusion.** Uniformly over Bset, 0<ell_b<3/4. Define W_b=0
if k_b is not in J or gcd(a,k_b)>1. Otherwise define

W_b=R^(-1) [min(B_(k_b),ab+R-1-delta_b)
                         -max(A_(k_b),R-delta_b)]_+,       (1)

where [x]_+=max(x,0). Then the exact fractional-part formula is

Z_a=sum_(b in Bset) W_b 1_{theta_b<ell_b},
D(a,c,d)=sum_(b in Bset) W_b 1_{theta_b<ell_b}-T_a.        (2)

Equivalently the indicator is 1_{{alpha_b}>1-ell_b}.
In particular fractional part zero is excluded. With all triples
restricted to the box, put

E_occ=sum_(a,c,d) (phi(a)/a)
                  [sum_(b in Bset) W_b 1_{{alpha_b}>1-ell_b}-T_a]. (3)

Then S=E_occ exactly, and S=o(T) is equivalent to E_occ=o(T).
The stronger bound E_occ=o(N²h/log N) is not proved here;
it would imply S=o(T) by L223's lower bound for T.

**Proof.**

First extend L224's short-cell estimate to every candidate b,
whether or not the cell is occupied. Interval (6) implies

avb > (v/(v+1))(j0²-R+1),
avb < j1²+R.

Here j0,j1=2N²+O(h), v is comparable to N², h is comparable
to N^(3/2), and R=O(N^(3/2)). Thus avb=4N^4+O(N²h),
uniformly; both alpha_b and beta_b are 2N²+O(h). Positivity
of their radicands follows eventually. Rationalizing gives

ell_b=(ab+2R-1)/(alpha_b+beta_b)
       <= ((12/5)N²+2R)/(4N²+O(h))=3/5+o(1).

The numerator is positive eventually, proving 0<ell_b<3/4.

The first integer strictly above alpha_b is k_b, including when
alpha_b itself is an integer. Its displacement is theta_b in (0,1].
Because ell_b<1, the open interval (alpha_b,beta_b) has an integer
if and only if theta_b<ell_b, and that integer must be k_b.
The inequality is strict even when beta_b is an integer. Substituting
theta_b=1-{alpha_b} proves the alternate indicator. No assertion
about the distribution of these fractional parts is involved.

Since k_b²=avb-R+delta_b, direct subtraction gives

avb-k_b²=R-delta_b,
a(v+1)b-k_b²-1=ab+R-1-delta_b.

Equation (1) is therefore exactly f_(k_b)(b) when the J and gcd
conditions hold, using both rounded endpoints and the minus one.
All positive terms f_m(b) in Z_a have b in Bset and m in the
open cell by L224. Conversely the unique cell candidate, when
selected and in J and coprime to a, contributes exactly (1).
The weight can vanish even in an occupied cell: membership alone
does not imply positive overlap with the narrower rounded cutoffs.
Finite reindexing now proves (2). Multiplying by phi(a)/a and
summing proves (3) from L223's identity S=sum (phi(a)/a)D.
Its lower bound T>=cN²h/log N proves the stated sufficient criterion.

## Qualifications

This is a weighted phase discrepancy identity, not a cancellation
estimate. The weight uses the candidate integer k_b and hence its
fractional-part displacement; the gcd condition also depends on that
integer. Replacing the indicator by ell_b while treating W_b as an
independent weight is unjustified, and need not reproduce T_a.
The exact benchmark in (3) remains the real mass T_a. The other
progression terms, signed comparison, and RH remain unresolved.

## Verification and formalization

`python3 scripts/heat/check_fractional_cell_occupancy.py` checks the
candidate, strict endpoint conventions and weighted reindexing by
integer arithmetic on finite fixtures. It does not verify asymptotic
cancellation. Analytic verification above establishes the uniform
cell estimate on the whole candidate set. Formalization would require
floor and fractional-part identities for square roots, strict open
interval counting, exact overlap algebra and finite reindexing.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
