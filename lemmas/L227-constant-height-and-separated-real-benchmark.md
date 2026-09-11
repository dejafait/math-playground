# Lemma 227: constant height and separated real benchmark

**Hypotheses.** Use the interior box and scales of L221, the exact
rounded endpoints of L220, T of L223, and L226's selected candidates
I_b. All assertions are for sufficiently large real N. Put

H_0=min(2,4/C_R), L=length(J)=h/(4 pi),
C=sum_(a,c,d) (phi(a)/a) sum_(b in Bset) I_b,
B_0=4N^4 L [sum_(a in A) phi(a)^2/a^3]
                 [sum_(c,d in [8N/5,17N/10]) 1/(cd(cd+1))].

All displayed sums are over integers in the stated boxes.

**Conclusion.** Uniformly in the fixed scale constants,

Z_full=H_0 C+O(N³), T=H_0 B_0+O(N³),
E_full=H_0(C-B_0)+O(N³).                                  (1)

Moreover B_0 is between cN²h/log N and CN²h. Thus
E_full=o(T) if and only if C-B_0=o(B_0). The error in (1)
divided by T is O(log N/sqrt(N)). This is an error bound for
simplifying the discrepancy, not a bound making C-B_0 negligible.

**Proof.**

For m in J, its distance to either stationary endpoint is at least
h/(8 pi). Therefore the magnitudes of the stationary cutoffs
m²-a−² and a+²-m² are bounded below by a positive constant
times N²h. They exceed R and 2m rho+rho² eventually. Consequently
L220's rounded endpoints satisfy

B_m=min(R,2m rho+rho²)+O(1),
A_m=-min(R,2m rho-rho²)+O(1).

These errors are uniform since each ceiling or floor moves its
argument by at most one, and minima and maxima are Lipschitz in
the maximum norm. Also min(R,x) is 1-Lipschitz in x. It follows that

H_m=(B_m-A_m)/R
   =2 min(R,2m rho)/R+O((1+rho²)/R)
   =H_0+O(N^(-1/2)),                                    (2)

using m=2N²+O(h), rho=N^(-1/2), and h comparable to N^(3/2).
This proof covers a tie between the two active cutoffs, including
C_R=2; no differentiability of the minimum is used.

By L224's candidate interval count there are O(h/N+1) possible
b per triple. There are O(N³) triples. Thus C=O(N²h), and
multiplying (2) by the nonnegative selection and weights proves
Z_full=H_0 C+O(N^(-1/2)N²h)=H_0 C+O(N³).
The strict occupancy and gcd condition have not been changed.

For the benchmark, L223 gives exactly, with v=cd,

F_m=H_m [(m²+(A_m+B_m)/2)/(av(v+1))-1/(a(v+1))].

Here av(v+1) is comparable to N^5, |A_m+B_m|<=2R,
and m²=4N^4+O(N²h)=4N^4+O(N^(7/2)). Substitution of (2)
therefore gives uniformly

F_m=H_0 4N^4/[av(v+1)]+O(N^(-3/2)).                     (3)

There are O(N³h) possible a,c,d,m tuples; dropping gcd only in
this absolute error bound and using phi(a)/a<=1 shows that
its aggregate error is O(N³).

For each a, finite Möbius inversion gives

#{m in J: gcd(a,m)=1}=L phi(a)/a+O(tau(a)).              (4)

Indeed the count of multiples of each divisor e of a in the closed
interval J is L/e+O(1), including integer endpoints. Sum with
coefficient mu(e), and use sum_(e|a) mu(e)/e=phi(a)/a.
Inserting (4) into the main term of (3) gives H_0 B_0.
The error is bounded by a constant times

N^4 [sum_(c,d) 1/(v(v+1))] [sum_(a in A) tau(a)/a].

The first bracket is O(N^(-2)). Pairing complementary divisors
proves tau(a)<=2 sqrt(a), so the second bracket is O(sqrt(N)).
This error is O(N^(5/2)), absorbed into O(N³). This proves
both benchmark identities and their subtraction in (1).

L223's bounds cN²h/log N<=T<=CN²h, together with H_0>0
fixed and N³=o(N²h/log N), give the asserted bounds for B_0.
In particular T/(H_0 B_0) tends to one. Divide (1) by T to
obtain the equivalence and the stated relative simplification error.

## Qualifications and verification

The extra factor phi(a)/a in B_0 comes from counting coprime m
in the real benchmark, not from assigning a coprimality probability
to occupied cells. The count C retains gcd(a,k_b)=1 and both strict
cell endpoints. No distribution or independence is assumed.
The estimate C-B_0=o(B_0), other progression terms, the signed
comparison, and RH remain unproved.

Verification is analytic: inactive stationary cutoffs, Lipschitz
minimum bounds at ties, the exact area expansion, finite Möbius
inversion with closed endpoints, and the displayed error totals.
Existing exact cell and overlap tests check the retained definitions;
no numerical test establishes the missing asymptotic. Formalization
would require uniform eventual bounds in (2)–(3), finite divisor
inversion and interval counting, and the relative-error limit.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
