# C029m — Eventual tilted-Xi Hermite index at most one implies RH

## Hypotheses

Use Kuznetsov's exact family, including its odd coefficients:

    p_k(t)=P_k^(3/4)(t/2;pi/2),
    T_N(t)=sum_(k=0)^N [N!/((N-k)!N^k)] beta_k p_k(t),  N>=1.

Here beta_k is b_k of Theorem 2.1, equations (3)–(4), of Alexey
Kuznetsov, *Expansion of the Riemann Xi Function in Meixner-Pollaczek
Polynomials*, Canad. Math. Bull. 51(4) (2008), 561–569,
[DOI and source](https://doi.org/10.4153/CMB-2008-055-0).
For an explicit finite specification, put, with the usual Bernoulli numbers,

    u_n= -n!/sqrt(2) * sum_(h=0)^n
      4^h (4^(h+1)-1) B_(2h+2) (2pi)^(h+1)
      * sin(pi(n-h)/2+pi/8) / ((n-h)! (2h+2)!),
    beta_n=4n(n-1)u_(n-2)+(8n^2+12n+7)u_n
           +(2n+3)(2n+5)u_(n+2).

These are source equations (13), p566, and (4), p563, with u_n the
source's tilde-b_n. For n=0,1 the first term is omitted; no negative
index is evaluated. The basis satisfies p_(-1)=0, p_0=1 and source (2):

    (k+1)p_(k+1)(t)=t p_k(t)-(k+1/2)p_(k-1)(t).

For every N for which T_N is nonconstant let d_N be its actual degree.
List its roots alpha_(N,h), 1<=h<=d_N, with algebraic multiplicities.
Set s_(N,k)=sum_h alpha_(N,h)^k, with s_(N,0)=d_N, and define

    H_N=(s_(N,a+b))_(0<=a,b<d_N).

Assume there exists N_0 such that, for every N>=N_0 for which T_N is
nonconstant, H_N has at most one strictly negative eigenvalue, counted
with multiplicity. This is the **unproved eventual index hypothesis**.
No simplicity, nonsingularity, exact degree N or effective N_0 is assumed.

## Conclusion

Under this hypothesis RH holds. This is only a conditional implication;
it supplies no estimate of H_N and is not a proof of RH. The index
hypothesis is sufficient here; no converse is claimed.

## Proof

**Imported analytic inputs.** Write

    xi(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)/2,
    Xi(t)=xi(1/2+it),     F(t)=exp(-pi*t/4)Xi(t),

using the removable values in xi. Kuznetsov, p561, uses precisely this
normalization. We import the compact convergence of T_N to F on all of
C from his explicit Jensen-weighted statement on p568 (weighted passage
continuing onto p569). It is an unnumbered source assertion; its proof
is not separately displayed there. Theorem 2.1 supplies the ordinary
expansion. We do not infer the weighted assertion from fixed-column
multiplier limits or reprove the parked summability specialization.
The source results are imported without claiming an independent audit
of its upstream reference [9]. The conclusion here is relative to this
named analytic input, not to numerical root observations on p569.

For the classical completed-zeta facts we import E. C. Titchmarsh,
*The Theory of the Riemann Zeta-function*, 2nd ed., revised by
D. R. Heath-Brown, Oxford, 1986, Sections 2.1–2.2 and 2.12,
equations (2.1.12)–(2.1.15), (2.2.1), (2.12.4), Theorem 2.12 and the
following zero-location and symmetry paragraphs, printed pp29–31
([primary text](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf)).
They give that xi is entire,

    xi(1-s)=xi(s),   xi(conj(s))=conj(xi(s)),
    xi(0)=xi(1)=1/2,    xi(x)!=0 for every real x,

and identify its zeros with the nontrivial zeta zeros. The real-axis
assertion includes every case: the source's strip confinement and
trivial-zero/gamma-pole cancellation exclude exterior real zeros;
(2.12.4), with the positive alternating series from (2.2.1), excludes
0<x<1; the displayed endpoint values exclude x=0,1. No unproved
nonvanishing on the critical line or simplicity is being imported.
These are cited classical inputs, not new real-axis estimates.

**Polynomial and limit hypotheses.** Formula (13) is a finite real sum,
so every u_n and beta_n is real. The displayed recurrence implies by
induction that p_k has real coefficients (and leading coefficient 1/k!).
Thus T_N has real coefficients and degree at most N, but cancellation
may lower its actual degree. All its Hermite matrices are real symmetric
because conjugate roots have conjugate power sums, with equal
multiplicities. No assertion d_N=N is needed.

Entireness of xi gives entireness of Xi and F. At the two endpoint
arguments, the cited xi values give

    F(i/2)=exp(-i*pi/8)/2,
    F(-i/2)=exp(i*pi/8)/2,
    F(i/2)-F(-i/2)=-i sin(pi/8)!=0.

In particular F is not identically zero and is nonconstant. More
explicitly let delta=|sin(pi/8)|>0. Compact convergence at the two
fixed points provides N_1 such that for every N>=N_1 both errors
|T_N(±i/2)-F(±i/2)| are less than delta/4. The triangle inequality
then gives

    |T_N(i/2)-T_N(-i/2)| > delta/2.

Consequently every such T_N is nonconstant. This checks the eventual
degree premise rather than adding it as an assumption. Discarding the
finite initial segment N<N_1 preserves compact convergence. The
eventual index hypothesis now applies to every member of this tail.
All hypotheses of C029l hold with the actual degrees d_N, arbitrary
nullity and algebraic multiplicities in the Newton sums. Therefore F
has at most two distinct nonreal zeros. This invokes C029l's proved
Hermite/Rouché interface, without repeating its proof or claiming a
bound on algebraic multiplicities of the limit zeros.

**Removal of the tilt and all orbit cases.** The identity
exp(z)exp(-z)=1 shows that exp(-pi*t/4) has no zeros for complex t.
Thus F and Xi have exactly the same zero locations. F itself is not
asserted even. Directly from the cited xi functional equation,

    Xi(-t)=xi(1/2-it)=xi(1/2+it)=Xi(t).

Also

    conj(Xi(t))=xi(1/2-i*conj(t))
               =xi(1/2+i*conj(t))=Xi(conj(t)).

Hence the Xi zero set is stable under negation and conjugation.
For t=iy, y real, the argument s=1/2-y is real. The imported real-axis
nonvanishing of xi gives Xi(iy)!=0 for every y. This explicitly includes
t=0 and t=±i/2 (s=1/2,0,1), as well as the real-s exterior and trivial
zero cancellation cases. Thus a nonreal zero t=a+ib of Xi must satisfy
both b!=0 and a!=0. Its four orbit points are

    a+ib,  a-ib,  -a-ib,  -a+ib.

They are pairwise distinct because both coordinates are nonzero, and
all are nonreal because their imaginary parts are ±b. They are zeros
of Xi by the two symmetries, and therefore zeros of F. This contradicts
the bound of two distinct nonreal zeros. The argument uses distinctness
only; multiple zeros give the same contradiction without extra hypotheses.
The only possible orbit collapses would have a=0 or b=0; the former
was excluded, while the latter is already a real t-zero.

It follows that every zero t of Xi is real. If rho is any nontrivial
zero of zeta, the cited zero correspondence makes xi(rho)=0. The
unique corresponding variable is t=(rho-1/2)/i, with
Im(t)=1/2-Re(rho). Its reality forces Re(rho)=1/2, which is RH.

**Scope.** This completes only a standard conditional specialization
covered by assessment2007. The eventual uniform index bound for this
exact coefficient family remains completely unproved. Numerical
degrees through 20, an uncomputed degree24, and generic polynomial
countermodels supply no such premise. This proof neither reopens the
parked runtime/summability attempts nor asserts a new unconditional
zero-free region, positivity theorem or RH candidate.

## Mathlib

Full matching theorem, Hermite transfer, completed-xi symmetry and
real-axis exclusion coverage not checked. No availability or absence
claim is made; the analytic inputs above are imported by precise
citation, and C029l is the local conditional interface.
