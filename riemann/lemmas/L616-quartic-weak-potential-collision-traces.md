# Lemma 616: quartic weak-potential balance and unequal collision traces

## Hypotheses

Use only L487's explicit polynomial, extended by the same formula to
the two-sided interval J=(-1/1000,1/1000):

    H(lambda,z)=z^4-(2+12lambda)z^2+1+4lambda+12lambda^2.

Let D={z: |z-1|<1/4}, dA=dx dy, z=x+iy, and epsilon>0. Set

    Q_epsilon=|H|^2+epsilon^2,
    S_epsilon=(1/4)log Q_epsilon,
    S=(1/2)log|H|,
    R_epsilon=H_zz conjugate(H)/Q_epsilon,
    B_epsilon=((S_epsilon)_z)^2,
    mu_epsilon=epsilon^2 |H_z|^2/Q_epsilon^2.

Wirtinger derivatives are partial_z=(partial_x-i partial_y)/2 and
partial_barz=(partial_x+i partial_y)/2. Time lambda is real. Tests are
C_c^infinity(J x D), or C_c^infinity(D) for a specified time slice.
Complex distributions act linearly on tests without conjugation.
For a complex distribution T, Re T means the complex-linear extension
of its real part on real tests: (Re T)(phi)=[T(phi)+conjugate(T(conjugate(phi)))]/2.
It does not mean Re(T(phi)) for a general complex test.
Pf(1/(z-r)^2) means the circular finite part, obtained by deleting
|z-r|<=rho before integration and taking rho down to zero. No square
of an already limiting distribution is assumed to exist.

## Conclusion

The following is a finite-model specialization, not an actual-Xi
statement, a positive collision-production law, or collision exclusion.

1. For every epsilon, the exact identities are

       (S_epsilon)_lambda=-(1/2)Re R_epsilon,
       (S_epsilon)_zz=R_epsilon/4-4B_epsilon,
       Delta S_epsilon=mu_epsilon,
       (S_epsilon)_lambda+2Re (S_epsilon)_zz+8Re B_epsilon=0,
       (S_epsilon)_lambda+(S_epsilon)_xx+8Re B_epsilon=mu_epsilon/2. (1)

   Thus the finite-degree second-derivative term is retained. The last
   equation includes every regularization term; discarding its right
   side at zeros is invalid.

2. S_epsilon tends to S in spatial L1 uniformly in lambda in J. In
   spacetime, R_epsilon tends in L1 to R=H_zz/H, defined arbitrarily on
   the measure-zero zero set and at lambda=0. Its spatial L1 norm is
   at most C(1+|log|lambda||) for lambda nonzero. The separate limits
   of (S_epsilon)_zz and B_epsilon exist as distributions. If r_j(lambda)
   are all four roots, then

       B=(1/16)[sum_j Pf(1/(z-r_j)^2)
                    +2 sum_{i<j} 1/((z-r_i)(z-r_j))],             (2)
       partial_lambda S=-(1/2)Re R,
       mu=Delta S=pi d lambda (delta_{r_+}+delta_{r_-}) on J x D.  (3)

   In (2), the pair kernels are ordinary locally integrable spacetime
   functions for lambda nonzero, extended across a null time slice.
   The finite parts are taken spatially before time integration. The
   two other roots lie outside D. In particular all terms in (1) have
   separate limits. There is no additional distribution supported
   solely on the collision time lambda=0. The positive divisor measure
   in (3) follows the roots on both sides, including simple roots.

3. Write w=z-1. On the fixed slice lambda=0, define

       R_0^fp=2Pf(1/w^2)+8/[w(w+2)]+2/(w+2)^2,
       T_0=-(1/2)Re R_0^fp,
       B_0=(1/4)Pf(1/w^2)+1/[2w(w+2)]+1/[4(w+2)^2].             (4)

   As epsilon decreases to zero on that slice,

       R_epsilon -> R_0^fp,
       (S_epsilon)_lambda -> T_0,
       B_epsilon -> B_0,
       mu_epsilon dA -> 2pi delta_1.                              (5)

   These are spatial distribution limits; they are not obtained by
   assigning a trace to the spacetime L1 function at a null slice.

4. The one-sided time traces after taking epsilon to zero differ:

       lim_{lambda -> 0^sigma} R(lambda)=R_0^fp-2pi sigma delta_1,
       lim_{lambda -> 0^sigma} partial_lambda S=T_0+pi sigma delta_1,
       lim_{lambda -> 0^sigma} B(lambda)=B_0-(pi/8)sigma delta_1,   (6)

   where sigma=+1 on the positive side and -1 on the negative side.
   Equivalently, in spatial distributions,

       S(lambda)=S(0)+lambda T_0+pi |lambda| delta_1+o(|lambda|).   (7)

   The regularized derivative on the collision slice is the average
   of the two traces, not either trace. The cusp (7) creates no atom
   in the first time derivative. A terminal divisor mass, a one-sided
   trace defect and a spacetime event atom are different objects.

## Proof

### Known calculus, normalization and reason for specialization

The standard comparison is Hall–Ho, *Letters in Mathematical Physics*
115:60 (2025), Proposition 4.1 and its proof, equation (4.2),
[version of record](https://link.springer.com/article/10.1007/s11005-025-01946-9).
For degree N, their p_tau=p_zz/(2N) and S=log|p|^2/N give
S_tau=(S_z)^2/2+S_zz/(2N) off roots, with complex Wirtinger time.
Here N=4 and tau=-8lambda, so differentiation along real lambda is
-8(partial_tau+partial_bartau). The corresponding real identity is
S_lambda=-8Re(S_z)^2-2Re S_zz. We do not apply that off-root identity
to S_epsilon without calculation.

The linear divisor normalization is the one-variable Lelong–Poincare
formula, Delta log|z-r|=2pi delta_r, with multiplicities. A primary
reference is El Amrani–Jeddi, *A geometric proof of the Lelong-Poincare
formula*, Proyecciones 32(1) (2013), 1–13, unnumbered theorem p. 2;
integrability, branching and multiplicity proof cases pp. 4–8,
[primary PDF](https://www.scielo.cl/pdf/proy/v32n1/art01.pdf),
DOI 10.4067/S0716-09172013000100001. Neither source states the
prescribed finite-epsilon collision traces. The direct estimates below
are needed for that specialization, especially real-time integrability
and the order of limits; this is not a reproof of a general weak heat
theorem or a novelty claim. The prior assessment is
`drafts/literature/2026-11-01-weak-log-potential-finite-test.md`.

L487's polynomial gives H_lambda=-H_zz by differentiation. Also

    (S_epsilon)_z=H_z conjugate(H)/(4Q_epsilon),
    (S_epsilon)_zz=H_zz conjugate(H)/(4Q_epsilon)
                         -H_z^2 conjugate(H)^2/(4Q_epsilon^2),
    (S_epsilon)_zbarz=epsilon^2 |H_z|^2/(4Q_epsilon^2).

These and the real-time chain rule prove (1). In particular an epsilon
term does not survive in the pure Wirtinger balance, but it does in
the real-x balance because 2Re S_zz=S_xx-(Delta S)/2. For smooth real
S_epsilon, 8Re B_epsilon=2[(S_epsilon)_x^2-(S_epsilon)_y^2].
This signed difference will be defined by the common-epsilon limit,
not by subtracting undefined squares of distributions.

### Root geometry and real-time estimates

Put u=1+6lambda, d=8lambda(1+3lambda), gamma=1+4lambda+12lambda^2.
The roots are r_+, r_-, -r_+, -r_-, where

    r_+^2=u+sqrt(d),   r_-^2=u-sqrt(d).

Choose principal square roots near 1, with sqrt(d) positive real for
lambda>0 and positive imaginary for lambda<0. Since
|u+-sqrt(d)-1|<1/10 on J and these square roots have positive real
part, |r_+-1|<1/10 and |r_--1|<1/10. The two negative roots stay outside D, at distance
at least 33/20 from any point of D. All roots are simple when lambda
is nonzero. At zero, each of 1 and -1 has multiplicity two.

More explicitly r_+=c+a and r_-=c-a, where

    c=sqrt((1+6lambda+sqrt(gamma))/2),
    a=sqrt(d)/(2c),
    a^2=2lambda(1+3lambda)/c^2.

Here c is positive real analytic, c(0)=1, and c-1=O(lambda). The local
root separation eta=2|a| is comparable to sqrt(|lambda|). Also

    H=[(z-c)^2-a^2]G_lambda(z),
    G_lambda(z)=(z+r_+)(z+r_-)
              =z^2+2cz+sqrt(gamma),

and |G_lambda| has a uniform positive lower bound g on J x D.

For every t>0, the spatial area where |H|<t is at most 2pi t/g:
the product |z-r_+||z-r_-| is then less than t/g, so at least one
factor is less than sqrt(t/g). The union of the two corresponding
disks gives the bound even at the multiple root. Layer cake gives

    integral_D |S_epsilon-S| dA
      <= (2pi/g)epsilon integral_0^infinity (exp(4v)-1)^(-1/2) dv
      <= C epsilon.                                              (8)

The last integral is finite at both endpoints. Translated logarithms
are uniformly locally integrable for roots in this compact set, so
S is uniformly spatially L1 and is continuous in lambda with values
in L1(D). This also follows directly from continuity of translations
of the locally integrable function log|z|. Thus (8) proves the stated
uniform convergence, including the terminal slice.

For simple roots the algebraic identity

    H_zz/H=2 sum_{i<j} 1/((z-r_i)(z-r_j))                         (9)

is exact. Products involving a remote root have uniformly bounded
spatial L1 norm, since the other possible singularity is a translated
simple pole. The only delicate product is the local pair. Its L1
norm on D is at most C(1+|log eta|). To see this, use disks of radius
eta/4 around each local root: the other denominator is at least
3eta/4, so each integral is bounded uniformly. In the rest of the
disk |z-c|<=2eta both denominators are at least eta/4, giving another
uniform bound by its area. For |z-c|>2eta, the product is at most
C/|z-c|^2, whose area integral to a fixed radius is logarithmic.
This proves the bound on R in the conclusion. Since
integral_0^h |log lambda| d lambda is finite, R is spacetime L1.

Away from the null zero set, R_epsilon tends to R and
|R_epsilon|<=|R|. Dominated convergence therefore gives spacetime L1
convergence, not a restriction of an almost-everywhere complex-time
theorem. Together with (8) and (1), this proves
partial_lambda S=-(1/2)Re R as a spacetime distribution. The derivative
has an L1 representative and has no event atom at lambda=0.

### Separately defined quadratic limit and divisor measure

For K_r(z)=1/(z-r), the standard Cauchy-kernel identities with the
present area normalization are

    partial_z K_r=-Pf(1/(z-r)^2),
    partial_barz K_r=pi delta_r.                                 (10)

For clarity, the finite part exists because the constant term of a
test has zero angular integral against 1/(z-r)^2, while subtracting
that constant leaves an absolutely integrable O(1/|z-r|) integrand.
Integration by parts outside a radius-rho circle gives the first
identity with vanishing boundary term. The boundary terms for
partial_z and partial_barz are respectively

    (1/2) integral_0^(2pi) exp(-2i theta) phi(r+rho exp(i theta)) d theta,
    (1/2) integral_0^(2pi) phi(r+rho exp(i theta)) d theta.

They tend to zero and pi phi(r), respectively. This is also the local
Cauchy/divisor normalization of the cited linear current formula.

The root factorization gives

    S_z=(1/4)sum_j K_{r_j},
    S_zz=-(1/4)sum_j Pf(1/(z-r_j)^2)                              (11)

in spatial distributions at every time. The finite-part test pairing
is bounded uniformly in the root position: by (10) it is the pairing
of K_r with a first derivative of the test, and translated simple
poles have a uniform L1 bound on a fixed compact set. Hence (11)
can be integrated over real time without any singular time measure.

Now (1), (8) and the L1 convergence of R_epsilon prove separately

    B_epsilon -> R/16-S_zz/4.

Combining the independently defined (9) and (11) gives precisely (2).
This is not just a declaration that the total PDE residual vanishes:
each diagonal finite part and each distinct-root product has been
defined and bounded. In a time strip |lambda|<b, the bound on its
pairing with any fixed smooth test is O(b(1+|log b|)); diagonal terms
are O(b). These estimates exclude a hidden distribution concentrated
at lambda=0 in B or S_zz as well as in R.

By (8), Delta S_epsilon tends to Delta S as a distribution. The
linear divisor formula applied at each time gives (3), since S is
one half the logarithm of the monic polynomial modulus. Positivity
of mu_epsilon also makes this convergence local weak convergence of
measures. At zero time the multiplicity-two mass in D is 2pi delta_1.
In spacetime (3) is integrated against Lebesgue time, so that single
slice has no extra mass. This completes all spacetime limits in (1).

### Fixed collision slice

At lambda=0, H=w^2(w+2)^2. Let

    rho_epsilon=|H|^2/(|H|^2+epsilon^2).

Then R_epsilon=rho_epsilon H_zz/H and
B_epsilon=(rho_epsilon^2/16)(H_z/H)^2. The corresponding meromorphic
expressions are

    H_zz/H=2/w^2+8/[w(w+2)]+2/(w+2)^2,
    H_z/H=2/w+2/(w+2).                                          (12)

To check the limiting prescription, compare rho_epsilon with the
radial cutoff

    rho_epsilon^rad=16|w|^4/(16|w|^4+epsilon^2).

On a fixed small disk, log(|w+2|^4/16)=O(|w|). The function
v -> exp(v)/(1+exp(v)) has bounded derivative, uniformly in v;
therefore |rho_epsilon-rho_epsilon^rad|<=C|w|, uniformly in epsilon.
The same bound holds for their squares. Dividing this difference by
w^2 yields an integrable bound C/|w|, and the difference tends to zero
pointwise off zero. Its tested integral tends to zero by dominated
convergence. For the radial cutoff, subtract the constant test value
using a radial cutoff equal to one near zero. The constant angular
integral vanishes exactly; the remainder is dominated by C/|w|.
Thus rho_epsilon/w^2 and rho_epsilon^2/w^2 tend to Pf(1/w^2), with
no added delta. All simple-pole and smooth terms in (12) converge by
ordinary dominated convergence. These facts prove the first three
limits (5) and the coefficients (4). The divisor limit on that slice
was proved independently above. No differentiation at a terminal
slice has been interchanged with an unproved trace operation.

### One-sided traces and the cusp

The only pair product whose trace is not an ordinary L1 or smooth
limit is

    P_lambda=1/((z-c)^2-a^2)
             =[K_c(z-a)-K_c(z+a)]/(2a).                         (13)

Translations of a distribution are differentiable as distributions,
as follows by differentiating the translated smooth compact test.
In fact, writing K(z)=1/z, the difference quotients in (13) equal

    -(1/2) integral_(-1)^1 (partial_x K)(z-c-t a) dt       (a real),
     (i/2) integral_(-1)^1 (partial_y K)(z-c-i t b) dt     (a=i b).

These identities hold after spatial testing, by the fundamental
theorem of calculus applied to translated tests. They also give
uniform bounds in one spatial derivative of the test from the local
L1 bound for K. For lambda>0 their limit is -partial_x K_1; for
lambda<0 their limit is i partial_y K_1.
The shift c-1=O(lambda)=O(|a|^2) does not affect these limits: the
centered difference quotient has uniformly bounded test pairings of
fixed derivative order, and translating its center by c-1 tends to
the same distribution. Equivalently both limits are

    -partial_z K_1-sigma partial_barz K_1
       =Pf(1/w^2)-pi sigma delta_1.                             (14)

Each local-remote product converges in L1: the remote factor is
smooth uniformly with bounded derivatives, and translated simple
poles converge locally in L1. Remote-remote products converge
smoothly. In (9), the local pair occurs with coefficient two, so
(14) proves the R trace in (6). The diagonal finite parts in (11)
are continuous under root translation, hence (2) proves the B trace
with coefficient -pi sigma/8. The real-time identity gives the T
trace with coefficient +pi sigma. This proves all signs and constants
in (6), including the distinction from the fixed-slice limits (5).

Finally, for each real spatial test phi, F(lambda)=integral S(lambda,z)
phi(z) dA is continuous by (8) and logarithmic translation continuity.
Its distributional derivative is the L1 time function
-(1/2)Re integral R(lambda,z)phi(z) dA, so F is absolutely continuous.
Explicitly, integrate this L1 function from any fixed time: subtracting
that absolutely continuous primitive from F gives a distribution with
zero time derivative, hence a constant. Continuity of F identifies
the equality at every time, including zero, without choosing a trace
of R at the null slice.
On either side of zero this derivative has the limit (6). Integrating
from zero and dividing by lambda proves (7). For phi(1) nonzero the
two derivatives differ, so there is no two-sided derivative there.
The absolute-continuous cusp has a jump in its derivative trace, not
a delta in its first derivative. The signed correction in B cancels
the trace correction in T in (1); it supplies no coercive sign law.
Complex tests follow by linearity from their real and imaginary parts.

### Qualification and route consequence

The tested balance exists with separately checkable terms. Its
positive source in real-x coordinates is the usual divisor measure,
present before, at and after collision. No additional first-order
spacetime collision source was found: (2)–(3) exclude one for this
prescription. Treating the fixed-slice derivative as a one-sided heat
trace loses the explicit point mass in (6). This is a local negative
test for that inference, not a ban on different observables, higher
time derivatives, additional hypotheses or actual-Xi mechanisms.
Coercivity, realization by Xi, infinite-zero limits, tails, zero time
and initial signs remain unresolved. No other part of L487 is audited here.

### Independent conceptual audit, 2026-11-01

The audit under `drafts/literature/2026-11-01-l616-collision-trace-audit.md`
checks (1)–(14) and the conclusion without changing their statements.
For the source convention, N=4 gives S_tau=H_zz/(32H) off roots;
the real lambda derivative is -8(S_tau+S_bartau), hence
-(1/2)Re(H_zz/H), as in (1). The scalar-epsilon identities are checked
directly, independently of that off-root comparison.

For the numerical geometry, |u+-sqrt(d)-1| is bounded by
6/1000+sqrt(8(1/1000)(1+3/1000))<1/10. Dividing by |r_++1| or
|r_-+1|, each at least one, proves the stated root disks. Thus
g=(33/20)^2 is a permissible lower bound for |G_lambda| on D.
The local pair bound is uniform for both splitting directions: its
two near-root disks, the remaining O(eta^2)-area central region, and
the outer annulus give respectively O(1), O(1), and O(1+|log eta|).
Since eta is comparable to sqrt(|lambda|), the common-epsilon
domination is in real time. The diagonal finite parts are
bounded after spatial testing; the distinct-root pair part is time
integrable. These separate facts, rather than cancellation in the
total equation, exclude an extra time-supported distribution.

On the fixed slice the radial cutoff and its square annihilate the
constant angular mode of 1/w^2 exactly. Their differences from the
specified scalar cutoff are O(|w|), so those differences divided by
w^2 vanish in L1 by domination. This checks the absence of an added
point mass in (5). For the time traces the displayed integral formulas
for (13), together with both boundary terms in (10), check the
opposite signs in (14). The local pair has coefficient two in R and
coefficient 1/8 in B; applying -(1/2)Re to the R trace gives the
coefficient in the time derivative. Thus the defects relative to (4) are exactly
-2pi sigma, -pi sigma/8, and +pi sigma, in R, B, and the time derivative
respectively. Their cancellation in (1) is exact. The divisor mass
is pi per simple root and 2pi on the double-root slice.

Finally the absolute-continuity argument above justifies integrating
the two derivative traces to obtain (7). For complex tests every step
uses the complex-linear real-part convention in the hypotheses, or
separate real and imaginary parts; taking the real part of a complex
test pairing would be incorrect. The audit found no failing coefficient,
limit or real-time estimate. It supplies independent local verification,
not a stronger theorem, an independent audit of the general cited
manuscripts, or an actual-Xi consequence. Mathlib coverage is unchanged.

## Mathlib

Full matching theorem and supporting distribution/current coverage
have not been checked. Unknown availability is not evidence of
absence. The present proof is informal and uses the precisely stated
standard calculus and linear current normalization above.
