# Corollary 645j: the total-count envelope misses the sparse disk census

## Hypotheses

Use L018's entire completion xi, its open-strip zero correspondence,
and its multiplicity-preserving reflection and conjugation symmetries.
All logarithms are natural. Fix

    0<delta<1/2, gamma>=e^5, R=3/2-delta/2,
    n=floor(log gamma), kappa=delta/[16(1+log(256R/delta))].

Let M count every xi zero w, with its order, in the closed disk
|w-(2+i gamma)|<=R. No zero at the disk center or at the proposed
anchor is assumed. In particular the result applies conditionally
when rho=1/2+delta+i gamma is a zero, of any multiplicity.

Import Chiara Bellotti and Peng-Jie Wong, *Improved estimates for the
argument and zero-counting function of the Riemann zeta-function*,
arXiv:2412.15470v2 (7 July 2025), [Theorem 1.1, printed p.1](https://arxiv.org/pdf/2412.15470v2):

    |N(H)-F(H)|<=E_i(H), H>=e, i=1,2,
    F(H)=H/(2*pi)*log(H/(2*pi*e)),
    E_1(H)=0.10076 log H+0.24460 log log H+8.08344,
    E_2(H)=0.11200 log H+0.12567 log log H+3.77417.

Here N(H) counts nontrivial zeros with 0<Im(w)<=H, with orders.
The saved assessment `drafts/literature/2026-11-01-zero-centered-sparse-census.md`
inspected the primary statement and essential height cases in Section 5,
pp.23--24. L467's audited source-convention argument in Section 3,
p.9, and its inclusive-count extension are reused. The source's full
analytic proof and numerical computations are cited inputs, not rerun
or independently audited. No use is made of Corollary 1.6, whose saved
displayed-factor discrepancy remains unresolved.

## Conclusion

Put

    v=sqrt(R^2-1), a=gamma-v, b=gamma+v,
    E_*(H)=min(E_1(H),E_2(H)),
    U_delta(gamma)=[F(b)-F(a)+E_*(a)+E_*(b)]/2.

There is the full finite-height bound

    M <= floor(U_delta(gamma)),                            (1)
    U_delta(gamma)
      <= min_(i=1,2) [v/(2*pi)*log(b/(2*pi))+E_i(b)].       (2)

Despite retaining reflection and the narrower geometric enclosure,
this particular envelope cannot certify C645h's M<=kappa*n:

    U_delta(gamma)>0.080608*n>kappa*n                      (3)

at every permitted height. Taking the integer part does not rescue
the certificate: floor(U_delta(gamma))>floor(kappa*n).
For each fixed delta its exact leading coefficient is

    lim_(gamma->infinity) U_delta(gamma)/floor(log gamma)
       = c_delta := sqrt(R^2-1)/(2*pi)+0.10076
       > 3/(8*pi)+0.10076 > kappa.                        (4)

These are statements about an upper envelope. They give no positive
lower bound for M, no actual off-line zero, and no counterexample to
the desired sparse census. This is a known-count-theorem specialization,
not a new local zero-density theorem or an RH resolution candidate.

## Proof

### Geometry and multiplicities

The parameter range gives 5/4<R<3/2 and 3/4<v<sqrt(5)/2<3/2.
Every disk zero w=beta+i t has beta>=2-R>1/2. By L018, beta<1.
Consequently

    (t-gamma)^2 <= R^2-(2-beta)^2 < R^2-1=v^2.

Thus all counted zeros have a<t<b, including any zeros on the disk
boundary. L018 sends w to 1-conjugate(w), with the same positive
ordinate t and the same order. These reflected zeros have real part
1-beta<1/2, hence lie outside the disk. The reflection is injective,
so the disk multiset and its image are disjoint multisets in [a,b].
This proves

    2M <= N(b)-N(a-).                                    (5)

No simplicity premise, choice of a favorable ordinate, or identification
of distinct zeros sharing an ordinate is used. Compact-strip finiteness
follows from L018: xi is entire, not identically zero, and has all its
zeros in the bounded real-part strip. Therefore both multisets are finite.

### Source heights and closed endpoints

Since e>2, gamma>=e^5>32, while v<3/2. Thus a>30>e and a>2*pi
(the elementary e<3 and pi<4 suffice). Both source heights a,b exceed e.
For 0<epsilon<a-e, apply the source lower estimate at a-epsilon
and upper estimate at b. Both estimates hold with E_* since each
of E_1,E_2 bounds the same absolute error. Hence

    N(b)-N(a-epsilon)
      <= F(b)-F(a-epsilon)+E_*(b)+E_*(a-epsilon).

L467's endpoint method applies without change: compact-strip finiteness
gives N(a-epsilon)->N(a-) as epsilon decreases to zero. E_* is
continuous on H>=e, being the minimum of two continuous functions.
Passing to the limit and using (5) proves M<=U_delta(gamma).
M is an integer, yielding (1). The inclusive-count source convention
also covers an upper-endpoint zero, by the right-limit extension
already justified in L467. Thus no boundary-zero convention is hidden.

For (2), F'(H)=log(H/(2*pi))/(2*pi) is increasing. Integration on
[a,b], whose length is 2v, gives

    [F(b)-F(a)]/2 <= v/(2*pi)*log(b/(2*pi)).

Both E_i are increasing on H>=e: their derivatives are
alpha_i/H+beta_i/(H log H)>0, where alpha_i,beta_i are the
displayed positive coefficients. Therefore
[E_*(a)+E_*(b)]/2<=E_i(b) for each i. This proves (2).

### Finite-height failure and integer rounding

For H>=e, log log H>=0, and all constant terms are positive.
Both errors therefore satisfy E_i(H)>=0.10076 log H, and so does
E_*. Since F is increasing on [a,b],

    U_delta(gamma)>=0.10076 log a.

Also a>gamma/2, log 2<1, and log gamma>=5, whence

    log a>log gamma-1>=(4/5)log gamma,
    U_delta(gamma)>0.080608 log gamma>=0.080608 n.          (6)

The denominator defining kappa exceeds 16, so kappa<1/32. This
proves (3). To check rounding even at small n, the stronger bound
kappa<1/224 is convenient. Indeed R/delta>5/2, hence
256R/delta>640>e^6 and 1+log(256R/delta)>7. The elementary
inequality e<11/4 gives e^6<(11/4)^6<640. Since delta<1/2,
kappa<1/224 follows.

If 5<=n<=223, kappa*n<1. At the stipulated anchor, M>=1 would
already make the requested census impossible; without an anchor we
still check the envelope itself. For all such n, F(b)-F(a)>0 and
E_*(a)>3.77417, E_*(b)>3.77417, so U_delta(gamma)>3.77417.
Thus floor(U_delta(gamma))>=3>0=floor(kappa*n).
If n>=224, (6) instead gives

    U_delta(gamma)-kappa*n
       >(0.080608-1/224)*n
       >=224*0.080608-1=17.056192>1.

Taking integer parts again yields the asserted strict inequality.
These comparisons concern the numerical certificates, not actual M.

### Asymptotic coefficient

Fix delta. The difference

    E_2(H)-E_1(H)
      =0.01124 log H-0.11893 log log H-4.30927

tends to positive infinity. Thus E_*=E_1 at both endpoints beyond
an onset; no effective location of that switch is needed for (1)--(3).
Uniformly for x in [gamma-v,gamma+v],
log x=log gamma+O_delta(1/gamma). Integrating F' and substituting
the displayed E_1 give

    U_delta(gamma)
      =c_delta log gamma+0.24460 log log gamma
         +8.08344-v/(2*pi)*log(2*pi)+O_delta(1/gamma).

For the log-log substitution, the mean value theorem bounds its
endpoint error by O_delta(1/(gamma log gamma)), also covered by the
displayed remainder. Since floor(log gamma)=log gamma+O(1), division
proves (4), including the floor rather than replacing it silently.
Finally v>3/4 gives the stated lower comparison, and c_delta>0.10076
while kappa<1/32. All limits fix delta; none assumes infinitely many
off-line zeros at that displacement.

### Interpretation and limits

C645h is a comparison target, not an input to this count proof. Even
this reflection-halved, horizontally narrowed use of the total count
has an insufficient coefficient. A smaller upper bound might hold
for actual M: neither U>kappa*n nor its asymptotics reverse the
inequality M<=U. Independent horizontal localization, a stronger
Hankel estimate, or another mechanism would be required. C645i's
audited synthetic counterfamily to the arbitrary-C extension is
unaffected. Clearance, the full pole set, interpolation, a useful
independent boundary upper bound, initial signs and all-degree
mixed positivity remain separate. No source reproof is warranted:
the necessary new work here is only geometry, endpoint application
and the exact threshold comparison not stated by the cited theorem.

## Mathlib

Full matching coverage is not checked; availability is unknown.
No formal theorem for these explicit constants, this disk specialization,
or the threshold comparison is claimed. Supporting analytic facts are
used informally as specified above; documentation validation is not
Lean verification.
