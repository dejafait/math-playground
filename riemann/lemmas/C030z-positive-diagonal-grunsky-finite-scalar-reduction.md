# Corollary C030z: positive-diagonal Grunsky compatibility reduces to a scalar test

## Hypotheses

Let A=S_2,B=S_3,C=S_4,D=S_5,E=S_6 be the actual reciprocal-Xi-zero
sums of L025. They are real and strictly positive by L027. Consider
real normalized formal jets

    f(z)=z+a_2*z^2+...+a_7*z^7+O(z^8),

with symmetric mixed coefficients defined by

    log((f(z)-f(w))/(z-w))=-sum_(m,n>=0)c_mn*z^m*w^n.

The zero-index coefficients are determined by f. There is no oddness,
convergence on the unit disk, or univalence hypothesis. The prescription is

    c_mn=delta_mn/m-tau*d_m*d_n*S_(m+n),
    m,n>=1, m+n<=6, tau>0, d_1=1, d_2,...,d_5>0.       (1)

For the separate analytic nonexistence conclusion, a unit-disk
realization means a holomorphic univalent f on |z|<1 with f(0)=0,
f'(0)=1 and the same mixed prescription (1), in this exact coordinate.
Local univalence or an unspecified smaller disk does not suffice.

## Conclusion

Define k=A/(2C) and the following functions of real x,p:

    V=p-k(1+x),
    J=V-xB/D,
    H=pJ-xVC/E+(1-x)pB^2/(2AE),
    L(x)=-Ek(1+x)+ExB/D+(1-x)B^2/(2A),
    N(x)=A(x^2+x+1)/3-Ek^2(1+x)^2.                    (2)

There exists a jet satisfying (1) if and only if there exist real x,p with

    x<1, p>0, V>0, J>0, H>0, pL(x)=N(x).             (3)

Given such x,p, one may take

    tau=(1-x)/A, d_2=sqrt(p), d_3=V,
    d_4=sqrt(p)*J, d_5=H.                             (4)

If L(x)!=0, the only candidate p is N(x)/L(x), subject to all strict
inequalities in (3). If L(x)=0,N(x)!=0, there is no candidate at that x.
If L(x)=N(x)=0, p remains free subject to those inequalities. In
particular the zero branch is not discarded. Under the conditional
actual-input arithmetic contracts below, calculation1309 proves (3)
**feasible**, with x=-16162/111 and p=N(x)/L(x) in the actual constants.
It also excludes every -1<=x<1 and every common L=N=0 branch.
Two other small cells remain unclassified; a complete solution set is
not claimed. Audit1311 accepts these finite claims under the retained
contracts and proves that **no unit-disk univalent realization of (1)
exists**: the classical necessary bound |c_11|<=1 contradicts the
uniform excluded range. This stops this precise positive-diagonal
linear prescription, not other representations or RH. No all-degree
positivity or infinite formal realization is established.

The same algebra holds for arbitrary positive real A,...,E. For that
larger parameter family, strict positivity alone permits both outcomes:
A=B=C=D=E=1 is incompatible, whereas A=B=C=E=1,D=3/2 is compatible.
Neither example is asserted to be actual Xi, or to satisfy the other
zero-location/product properties in L025's inherited inputs. This
comparison tests the finite signs alone; it is not a countermodel to
all those inherited properties.

Calculation1307, conditional on L037's documented arithmetic contracts,
encloses the actual S_2,...,S_6 strictly positively and excludes each
of x=-2,-1,0,1/2 in (3). That calculation alone is a four-point
exclusion. Calculation1309 below uses the same boxes for the separate
approved scalar-sign test. The earlier four exclusions are preserved.

## Proof

**Imported identities.** Reuse only C030y's general identities and
formal reciprocal convention, not its fixed-weight substitutions or
contradiction. Their standard source is L.-P. Teo, *Analytic functions
and integrable hierarchies—characterization of tau functions*,
Lett. Math. Phys. 64 (2003), 75–92,
[arXiv:hep-th/0305005v2](https://arxiv.org/html/hep-th/0305005v2),
Sections 2.1–2.2, equations (2.3)–(2.4), (2.8)–(2.12), preprint
pp. 2–6 (low coefficients on p. 5, formal-series extension at the end
of Section 2.2). The leading coefficient is one and the coefficients
are symmetric, not multiplied by the Faber factor m. C030y also gives
the finite extraction of c_24 and the truncation justification.
No general Grunsky theorem is reproved here.

Write

    g(Z)=1/f(1/Z)=Z+b_0+b_1/Z+...+b_5/Z^5+O(Z^(-6)).

The mixed coefficients agree with those of f, and b_0 is arbitrary.
Every choice of real b_0,...,b_5 gives a unique real normalized jet
through a_7 by taking the formal reciprocal. Terms omitted here
cannot affect mixed total degree at most six. The nine unordered entries are

    c_1n=b_n (1<=n<=5),
    c_22=b_3+b_1^2/2,
    c_23=b_4+b_1*b_2,
    c_24=b_5+b_1*b_3+b_2^2/2,
    c_33=b_5+b_1*b_3+b_2^2+b_1^3/3.                 (5)

**Necessary reduction.** Suppose (1) holds and put

    t=tau, x=1-tA, u=d_2, p=u^2, v=d_3,w=d_4,h=d_5.

Then x<1,p>0,u>0, t=(1-x)/A, and the first row forces

    b_1=x, b_2=-tuB, b_3=-tvC, b_4=-twD, b_5=-thE. (6)

Subtracting (1) from the four remaining entries of (5) gives residuals

    R_22=(x^2-1)/2+tC(p-v),
    R_23=t[D(uv-w)-xuB],
    R_24=t[E(uw-h)-xvC+tpB^2/2],
    R_33=t[E(v^2-h)-xvC+tpB^2]+(x^3-1)/3.         (7)

Because t,C,D,E are positive, the first three equations R=0 determine

    v=p+(x^2-1)/(2tC)=p-k(1+x)=V,
    w=u(v-xB/D)=uJ,
    h=uw-xvC/E+tpB^2/(2E)=H.                      (8)

The equality in the first line uses tA=1-x; no division by x, 1+x,
v or a jet coefficient is needed. Strict positivity of v,w,h is
exactly V,J,H>0, since u>0.

Substitute the last line of (8) into R_33 and divide only by t>0:

    R_33/t=E(v^2-uw)+tpB^2/2+(x^3-1)/(3t).

Here uw=pv-xpB/D, v-p=-k(1+x), and
(x^3-1)/(3t)=-A(x^2+x+1)/3. Consequently

    R_33/t=-Ek(1+x)[p-k(1+x)]+ExpB/D
            +(1-x)pB^2/(2A)-A(x^2+x+1)/3
           =pL(x)-N(x).                            (9)

This proves necessity of (3), including the possibly zero L branch.

**Sufficiency and exceptional cases.** Conversely suppose (3). Set
the positive parameters by (4), take any real b_0, and define the
remaining b's by (6). The formal expression

    f(z)=z/(1+b_0*z+x*z^2-tuB*z^3-tvC*z^4-twD*z^5-thE*z^6)

has a real normalized expansion through z^7 because its denominator
has constant term one. Its mixed coefficients through degree six
are (5). Equations (8) make R_22,R_23,R_24 zero, and (9), together
with pL=N, makes R_33 zero. All first-row coefficients are already
correct by (6). Thus all nine entries and their symmetric counterparts
satisfy (1). This proves the converse without assuming convergence or
univalence. Splitting pL=N into the three listed L,N cases is exhaustive.
The cases x=0 and x=-1 are retained. The boundary x=1 corresponds
to the excluded tau=0; zero weights are excluded only by the stated
strict inequalities. Possible zero a_j or b_j impose no extra division.

**What the imported finite signs do not decide.** For the positive
parameter specialization A=B=C=D=E=1, direct substitution in (2) gives
L(x)=0 and N(x)=(x-1)^2/12>0 for every x<1. Hence no jet exists.
For A=B=C=E=1,D=3/2, choose x=-1,p=1. Equations (2) give

    L=N=1/3, V=1,J=5/3,H=11/3.

Thus tau=2,d_2=d_3=1,d_4=5/3,d_5=11/3 are strictly positive and
satisfy every condition. For b_0=0 the exterior coefficients are
b_1=-1,b_2=-2,b_3=-2,b_4=-5,b_5=-22/3. Their first row is prescribed;
the remaining four entries computed from (5) are -3/2,-3,-10/3,-5/3,
respectively, exactly their prescribed values. This is an exact
formal witness for those parameters only. It shows why importing
S_2,S_3>0 as in the fixed-weight stop is insufficient by itself to
decide the adjustable-weight test. The actual values A,...,E and
their additional inherited structure have not been replaced by this
example. That algebra alone left actual feasibility open; the
conditional actual-input specialization1309 below now supplies a witness.

**Verification and evidence limits.** Reproduction command:

    python3 scripts/grunsky/positive-diagonal-degree-six-1304.py

The complete exact Laurent-polynomial certificate is
[certificate1304](../scripts/grunsky/positive-diagonal-degree-six-certificate-1304.json).
It stores all nine coefficients, prescriptions and residuals, all branch
conditions and both sign-only parameter tests. The first eight residuals
are identically zero after (8); the ninth equals t(pL-N). There are
eleven zero verification residuals: these nine identities and two
specialization identities for the incompatible example. All eleven,
the full L,N coefficients, the complete branch conditions and the
compatible example's nine zero residuals were inspected. This is exact
algebra supporting the displayed proof, not a decision procedure for
actual S_k or formal verification. No new enclosure algorithm, floating
sample, actual-Xi ratio inequality or source-wide preprint audit is used.
The previous assessment did not identify a theorem deciding this
specialization; no certified originality is claimed.

**Actual singleton calculation1307, 17 November 2026.** Assume exactly
L037's arithmetic contracts, retaining correctly rounded nearest
Decimal exponentials widened by adjacent representables, directed
basic operations, rejection of exceptional arithmetic and of divisors
containing zero. All three contexts have precision 100. This section
specializes the audited L917 method; it does not independently verify
the arithmetic library or reprove its documented contracts. The
calculation was covered before invocation by SPECIALIZE assessment
`drafts/literature/2026-11-17-actual-xi-grunsky-ball-input-1305.md`.
No new general quadrature theorem or Grunsky theorem is asserted.

The actual coefficients satisfy the following **strict outer rational
bounds** (all finite decimals here denote exact rationals):

| Quantity | Lower bound | Upper bound |
| --- | ---: | ---: |
| S_2 | 3.7172599285e-5 | 3.7172599286e-5 |
| S_3 | 1.4417393139e-7 | 1.4417393141e-7 |
| S_4 | 6.6303168020e-10 | 6.6303168031e-10 |
| S_5 | 3.2136641485e-12 | 3.2136641527e-12 |
| S_6 | 1.5876934435e-14 | 1.5876934595e-14 |

These magnitudes refine existing finite positivity; L027 already proves
the signs. They are local numerical inputs, not progress beyond known
RH results. The following strict margins exclude the four nominated
points. In every row the computed L has strictly negative upper
endpoint, so there is no exceptional division in defining p=N/L.

| x | Necessary quantity | Certified strict upper bound | Required |
| --- | --- | ---: | --- |
| -2 | p | -175484.66 | p>0 |
| -1 | p | -80930.55 | p>0 |
| 0 | V | -27516.33 | V>0 |
| 1/2 | V | -4838.88 | V>0 |

For x=0,1/2 the p box is strictly positive, so those exclusions use
V, not a claimed failure of p. All four trials also give negative J
and H upper endpoints; their full intervals are retained but unnecessary
for these exclusions. No point in this fixed test is left numerically
undecided. At the end of calculation1307 all other real x<1, possible
zeros of L, and the free-p L=N=0 case were untested. Four exclusions
alone do not decide the prescription; the separate calculation1309
follows below.

**Enclosure justification.** Use L019's actual positive K and L021's
moment expansion. At lambda=0, F(0,z)=Xi(z) and L025 identifies its
normalized local-log coefficients with actual reciprocal-zero sums,
without any real-zero hypothesis. The tilt factor is identically one;
no deformed-zero product is used. On [0,2] retain theta terms n=1,...,4.
For i=0,...,255 use the exact dyadic panel
[2i/256,(2i+2)/256], center (2i+1)/256 and half-width h=1/256.
The finite integrands u^k sum_(n=1)^4 K_n(u), k=0,2,...,12, are C8.
The inspected L037 primitives compute the normalized derivative jets
through order 8 at the center and on the entire closed panel. Specifically,
K_n=exp(u/2)(8v^2-12v)exp(-v), v=pi*n^2*exp(2u), with the enclosing
96-term rational Machin pi bound. The power jet is
binom(k,j)u^(k-j) for j<=k and zero otherwise, retaining j<=8 even
for k=10,12. L036's product and exponential recurrences enclose those
jets; its Taylor integral has weights 2h^(j+1)/(j+1), j=0,2,4,6,
and symmetric error at most (2h^9/9) times the largest absolute
endpoint of the full-panel eighth normalized coefficient.

Summing all 256 panels gives a finite integral enclosure for each of
the seven moments. Add [0,E_space+E_theta] using the complete L917
degree-twelve positive-tail bounds, with beta=119/40, without changing
their constants or dropping either component. Lambda=0 belongs to
their proved band [0,1/20], and u<=2,n<=4 are unchanged, so the
specialization applies directly. The total tail bound is <4.389e-23
for every moment; its spatial component is <4.447e-50. The nonnegative
discarded mass follows from positivity of each K_n. Possible double
counting in L917's upper bound remains harmless. This proves enclosure
of the full actual moments. M_0's saved lower endpoint exceeds 0.49712,
so normalization divides only by a strictly positive interval.

Apply L917's complete six finite Newton/log polynomials to
e_n=M_(2n)/((2n)!M_0). Their identification with L025's S_n follows
from the normalized analytic logarithm; it requires neither RH nor
Hankel positivity. Interval inclusion gives all the displayed actual-sum
bounds, in particular positive lower endpoints for every denominator
A,C,D,E in (2). Evaluate (2) at the four exact nominated x. Since L
excludes zero at each, p denotes the exact N/L in the actual constants,
and pL=N holds by definition. This is not established by a rounded
residual containing zero. Inclusion for p,V,J,H then gives the stated
negative upper margins and contradicts a necessary strict inequality
in every row. C030z's necessity argument, already proved above, gives
the exclusions. Tau=(1-x)/A remains strictly positive; its positivity
cannot repair a failed weight condition. No square root is needed
because no trial yields a compatible positive-weight witness.

**Complete evidence and verification.** Reproduce from this notebook:

```text
python3 scripts/grunsky/actual-singleton-1307.py
python3 scripts/grunsky/actual-singleton-replay-1307.py
```

The full output is
[certificate1307](../scripts/grunsky/actual-singleton-certificate-1307.json),
with all 256 closed spatial panels, all 1,792 panel integrals and
remainder records, all seven full moment boxes and summed remainders,
the complete tails, normalized coefficients, S1--S6 and each trial's
k,L,N,p,V,J,H,tau, failed inequalities and branch status. No uniform-H2
certificate is overwritten or retested. The
[exact-rational replay](../scripts/grunsky/actual-singleton-replay-1307.json)
passes with zero failures. It checks exact panel endpoints, integration
weights, all saved polynomial sums and remainder bounds, moment/tail
addition, normalization, all six complete log polynomials, all trial
values, branch decisions and displayed strict rational bounds. The
complete tails are additionally enclosed by L917's rational positive
exponential series with geometric remainder and reciprocation. Input
hashes, all 100-digit contexts, traps and false exceptional flags are
checked. The inherited finite-log polynomial residuals are all zero.

The full seven moment and remainder boxes, all normalized coefficients,
S1--S6, tails and arithmetic flags, and every value in all four trials
were inspected; the replay's complete check results were inspected.
The checker uses exact Fraction endpoint arithmetic for these finite
operations, with full rational evidence saved to disk. It checks saved
jet outputs against L036's arithmetic formula; it does not independently
reimplement those jets or verify Decimal.exp. Analytic inclusion is the
L036/L037 argument above with L917's audited tails. Python3.15.2 was
recorded. No further panel count, parameter sweep, higher degree,
all-branch elimination, convergence or univalence was tested. This is
a known-method specialization and informative four-point failure,
not a proof against the weighted representation in full or against RH.

**Actual scalar sign calculation1309, 17 November 2026.** This calculation
assumes the five strict outer rational boxes displayed in calculation1307
and their inherited L037 arithmetic contracts. No actual coefficient is
replaced by its midpoint. The result holds uniformly for all parameter
tuples in the closed outer boxes and therefore for the actual tuple.
Assessment1308, saved before this attempt, covers this one finite
specialization. No new quadrature, precision refinement, higher jet,
univalence theorem or all-degree sign is used.

First write

    l0=-Ek+B^2/(2A), l1=-Ek+EB/D-B^2/(2A),
    n0=n2=A/3-Ek^2, n1=A/3-2Ek^2.

Then L(x)=l0+l1*x and N(x)=n2*x^2+n1*x+n0 exactly. The change
z=1/(2-x) is bijective from x<1 onto 0<z<1, with inverse x=2-1/z.
It introduces no extra finite endpoint, and its denominator is positive.
Define the following polynomials, with coefficients in the actual real
constants:

    l(z)=-l1+(l0+2l1)z=zL(x),
    n(z)=n2+(-4n2-n1)z+(4n2+2n1+n0)z^2=z^2 N(x),
    v(z)=n(z)-k(3z-1)l(z),
    j(z)=v(z)-(B/D)(2z-1)l(z),
    h(z)=n(z)j(z)-(C/E)(2z-1)v(z)l(z)
          +(1-z)(B^2/(2AE))n(z)l(z).                 (10)

For l!=0, substitution into (2) gives exactly

    p=n/(zl), V=v/(zl), J=j/(zl), H=h/(z^2*l^2).    (11)

For example, x=(2z-1)/z, 1+x=(3z-1)/z and
1-x=(1-z)/z. Hence the numerator of pJ is nj, that of -xVC/E
is -(C/E)(2z-1)vl, and that of the last term of H is
(1-z)(B^2/(2AE))nl, all over z^2*l^2. This verifies the final
identity. The other identities follow by the displayed substitutions.
A Laurent-polynomial computation also verifies all five cleared
identities with zero residuals, treating the nonzero denominator l
as an independent variable w before specializing w=l(z). Its divisions
are only by monomials in the positive A,C,D,E and nonzero z,w.
Thus it assumes neither l's sign nor square-freeness of a polynomial.

The sign of each of p,V,J is the product of the signs of its
numerator n,v,j and l; the sign of H is the sign of h. This uses
z>0 and z^2*l^2>0. We certify signs with exact Fraction endpoint
operations on the outer boxes. Interval multiplication takes the
minimum/maximum of all four endpoint products, division is allowed
only when the denominator excludes zero, and repeated parameters
are enlarged by inclusion, never regarded as independent actual values.
An inequality certified uniformly on the enlarged box applies to the
actual tuple. The denominators A,C,D,E are strictly positive throughout.

On any rational cell [a,b] subset [0,1], expand a polynomial
P(z)=sum c_r*z^r as P(a+(b-a)t)=sum q_s*t^s, where

    q_s=sum_(r>=s)c_r*binom(r,s)*a^(r-s)*(b-a)^s.

For d=degree(P), write beta_i=sum_(s<=i) q_s*binom(i,s)/binom(d,s).
The exact finite binomial identity

    P(a+(b-a)t)=sum_(i=0)^d beta_i*binom(d,i)*t^i*(1-t)^(d-i)

holds: expanding the right side gives the stated power coefficients
(equivalently, sum_(i=s)^d binom(i,s)binom(d,i)t^i(1-t)^(d-i)
=binom(d,s)t^s). For 0<=t<=1 its weights are nonnegative and
sum to one. Therefore the minimum lower endpoint and maximum upper
endpoint of all beta_i enclose P throughout the closed cell. This is
only a finite polynomial interval certificate for this instance, not a
new root-isolation theorem. The saved polynomials have degrees1,2,2,2,4
with strict nonzero leading coefficients; no generic exact-real oracle
or arbitrary coefficient precision is assumed.

The single pass subdivided [0,1] into29 dyadic cells, depth at most16
(approved maximum256 cells). Nine have l,n,v,j,h all positive, hence
are uniformly feasible by (11). Eighteen are excluded by a strictly
negative necessary quantity. The only unclassified cells are

    [439/65536,55/8192], [2131/32768,4263/65536].    (12)

The first lacks a certified n sign, the second a certified l sign;
neither is declared an exact equality locus. Their endpoints are
retained in the closed bounds. The existential result below does not
require classifying them, and no further subdivision or precision
refinement was attempted.

All L=0 cases are checked separately. The interval coefficients of l
have signs +,-. Descartes' rule of signs (Basu, Pollack and Roy,
*Algorithms in Real Algebraic Geometry*, second edition2006,
Theorem2.33, p43; [primary-hosted text](https://www.cs.umd.edu/~gasarch/COURSES/752/S25/slides/AlgorithmsInRealAlgGeom.pdf))
gives exactly one positive root, counting multiplicity. In this linear
case it is explicitly z0=-l(0)/l'(z), and the slope is strictly
negative on the entire parameter box. Exact interval evaluation gives

    0.065<z0<0.066, n(z0)>6*10^(-7)>0.             (13)

Thus this is indeed the unique L root in the domain, N=n/z0^2>0
there, and pL=N is impossible. The L=0,N!=0 branch is rejected;
the L=N=0 free-p branch is empty, proved uniformly rather than
discarded by division. No non-linear multiple-root theorem is needed.

Both limits are covered. On [0,1/256], l>0,n<0, so p<0 at every
positive z there, including all x<=-254. On [1/2,1], l<0,j>0,
so J<0 for 0<=x<1. The excluded z=0 and z=1 themselves are not
candidate points. On [1/4,1/2], l<0,v>0,j>0,h<0, so no solution
exists there either. Consequently every -1<=x<1 (z>=1/3) is
excluded, including x=-1. These are uniform cell certificates, not
conclusions from a finite cutoff or sampled signs.

The first feasible cell is [55/8192,7/1024]. Its rational center
z*=111/16384 gives x*=-16162/111<1. For the actual constants,
define p*=N(x*)/L(x*) exactly; its L enclosure is strictly positive.
Direct evaluation of (2), independently of using (11) for selection,
gives the strict rational lower margins

    p*>11509, V*>4000000, J*>10000000,
    H*>24800000000000, tau*=(1-x*)/A>3940000.       (14)

All endpoints and margins are exact rationals. In particular the
needed pL=N equality is true by definition, not inferred from an
interval residual containing zero. Taking the positive real square
root u=sqrt(p*) and d2=u,d3=V*,d4=uJ*,d5=H* gives the positive
weights in (4); C030z's already proved sufficiency supplies a real
formal jet through a7 satisfying all nine prescribed entries. Thus
actual finite feasibility is decided positively under the retained
input contracts, despite the earlier four-point failures.

This witness has c11=x*<-1. The calculation does not assert its
univalent realizability or any disk contraction property. Indeed the
entire scalar range -1<=x<1 was excluded. At the completion of1309,
interpreting that exclusion against analytic Grunsky hypotheses was
left for a separate audit; audit1311 below now supplies that step.
All-degree compatibility, convergence,
identification with a suitable analytic map, and actual-Xi all-degree
positivity remain separate gaps. No complete RH candidate is proposed.

Reproduction commands from the active notebook:

```text
python3 scripts/grunsky/actual-sign-1309.py
python3 scripts/grunsky/actual-sign-replay-1309.py
```

The complete [sign certificate1309](../scripts/grunsky/actual-sign-certificate-1309.json)
stores input hashes, the five outer boxes, all formal definitions and
five zero residuals, every polynomial coefficient and every Bernstein
coefficient/range for all29 cells, the full exceptional-root intervals,
both tails, both unresolved cells and every direct witness interval.
The [replay1309](../scripts/grunsky/actual-sign-replay-1309.json) passes
with zero failures: all29 cells and145 polynomial sign bounds are
checked using a separately implemented rational interval primitive
and a direct Bernstein weighted-sum formula, without rerunning the
adaptive search. It also checks full-domain partition, both tails,
root exclusion, actual-input box containment, all direct witness
values and (14). These full load-bearing values, complete cell/sign
decisions, five formal residuals, polynomial coefficients and complete
replay check results were inspected. The replay imports saved
polynomial coefficients; their formula provenance is (10), the producer
and the Laurent identities, not an independent formalization. The
independent direct evaluation of (2) is sufficient for the strict
existence certificate. Actual-input inclusion still depends on
calculation1307 and L037's unverified arithmetic-library contract.
This is local specialization of known methods, without a novelty claim;
the following audit accepts its stated conditional scope.

**Critical proof audit1311, 17 November 2026.** The audit was covered
before invocation by SPECIALIZE assessment1310. It accepts the scalar
equivalence, actual-input specialization1307, strict witness1309,
uniform exclusion and exceptional-branch conclusions, with L037's
arithmetic-library contracts unchanged. No precision, panel, sign-cell
or degree refinement was made. The following are the load-bearing
checks, beyond merely reading the previous replay status.

L019's kernel is exactly exp(u/2)(8v^2-12v)exp(-v), summed over n,
with v=pi*n^2*exp(2u). Its terms are positive for u>=0. At lambda=0
the finite integration contains no tilt. L021 and L025 identify the
normalized logarithm with the actual S_n by compact convergence near
zero, without a global logarithm, a deformed-zero product, or RH.
L917's seven complete tails apply because 0 lies in [0,1/20]; its
positive discarded mass includes both the spatial complement and
all omitted theta terms. All six finite-log polynomials were checked
against their exact formal-log extraction, not truncated numerically.

Inspection of the implementations confirms directed endpoint basic
operations, neighbor-widened nearest exp, exact sign changes and
rational Machin pi bounds. The normalized product/exponential jets
are L036's recurrences, evaluated both at each midpoint and on its
whole closed panel. Reproduction at the original parameters matches
all 1,792 saved moment-panel jet records: four even midpoint
coefficients and the full-panel eighth coefficient in each, for
8,960 interval comparisons. All saved tails, pi, integration weights,
contexts and exceptional flags also match. This reproduces the jet
provenance with the inspected implementation; it is not an independent
Decimal implementation or a proof of library correctness. The original
1307 Fraction replay was rerun once and checks all finite sums,
remainders, tails, normalizations, S1--S6, four trial branches and
strict outer-box inclusions. Its six formal residuals are empty.

The nine coefficient equations, the derivation of pL=N and the reverse
construction were checked directly above. The change z=1/(2-x) has
exact range (0,1), and all five identities (10)--(11) hold algebraically.
The audit independently reconstructs the 16 interval coefficients of
l,n,v,j,h from the five fixed rational outer boxes using the inspected
Fraction primitive and (10); they match the certificate. Thus the
sign replay's previously imported polynomial coefficients have checked
formula provenance. The rerun1309 replay checks every saved Bernstein
coefficient and all145 polynomial ranges, contiguous closed coverage
of [0,1], all sign decisions, the direct witness values and the unique
linear root. In particular 0.065<z0<0.066 and n(z0)>6e-7: there is
no common L=N=0 branch. At nonzero L the equality pL=N is definitional.
The direct margins (14) verify the positive square root and all five
weights, without inferring equality from a small interval residual.
Both unresolved cells (12) are retained, and neither is used as a
certified root or feasible/excluded set.

For the analytic application, only the final two closed cells
[1/4,1/2] and [1/2,1] are needed. Their complete rational Bernstein
ranges imply the convenient weaker strict bounds

    l(z)<-3*10^(-11), j(z)>5*10^(-7), 1/4<=z<=1.  (15)

Audit1311 checks both comparisons exactly. Hence every -1<=x<1 has
z in [1/3,1), l!=0 and J=j/(zl)<0, contrary to the necessary J>0.
This includes x=-1 and both cell endpoints, and covers the limit
x->1 from below. The excluded endpoint x=1 would have tau=0; the
excluded z=0 is not a finite x. No unclassified cell intersects the
range used here, and no exceptional division is hidden in (15).

**Exact analytic import and obstruction.** Use the classical Grunsky
inequality in M. Obradovic and N. Tuneski, *Some application of Grunsky
coefficients in the theory of univalent functions*, Ann. Univ.
Paedagog. Crac. Stud. Math.25 (2025), 23--30, definition of the
normalized disk class S on p23 and the coefficient definition and
equation(1.4) on p25,
[DOI10.2478/aupcsm-2025-0005, primary PDF](https://studmath.uken.krakow.pl/article/download/12363/10958/47182).
For f holomorphic and univalent on the full unit disk, f(0)=0,f'(0)=1,
their mixed coefficients omega_pq use the positive logarithmic sign.
Thus omega_pq=-c_pq in (1), for p,q>=1. For any finitely supported
sequence u the cited inequality is

    sum_(q>=1) q*|sum_(p>=1) omega_pq*u_p|^2
       <= sum_(p>=1) |u_p|^2/p.

Take u_1=1 and every other u_p=0. Each summand on the left is
nonnegative, so its q=1 term gives |omega_11|^2<=1, equivalently
|c_11|<=1. This is an application of the cited theorem, not a reproof
or an assumption of its conclusion for formal jets. The source's
subsequent odd-function transform is not used. Neither a disjoint
conformal-welding pair, zero-area complement, strict contraction nor
an operator equality is needed.

If an analytic realization of (1) existed, c_11=1-tau*A=x is real
and x<1 because A>0,tau>0. The necessary bound forces -1<=x<1.
Its Taylor coefficients satisfy the same finite mixed identities,
so (3) is necessary; (15) contradicts J>0. This excludes every
positive choice of the weights and tau, not just the particular
witness. The necessity calculation only uses the prescribed real
b_1,...,b_5; the free b_0 cancels. Thus allowing a complex b_0 for an
analytic map cannot evade the contradiction. No domain rescaling is
made. A compatible formal germ, even one analytic near zero, does
not contradict the obstruction on the full unit disk.

The finite witness therefore survives the audit while this exact
analytic representation route stops. The conditional nature of the
actual boxes survives too. This is an informative instance-specific
negative from known Grunsky theory and the checked local calculation,
not a new general theorem, a disproof of actual Hankel positivity,
or a proof or disproof of RH. Other prescriptions and other analytic
domains have not been tested.

Audit commands, from the notebook, are

```text
python3 scripts/grunsky/actual-singleton-replay-1307.py
python3 scripts/grunsky/actual-sign-replay-1309.py
python3 scripts/grunsky/actual-sign-audit-1311.py
```

The complete [audit1311](../scripts/grunsky/actual-sign-audit-1311.json)
records every jet comparison, all reconstructed polynomial coefficients,
the exact two-cell evidence for (15), inherited full replay checks,
input hashes, arithmetic flags and an empty failure list. The complete
check fields, exceptional-root evidence, coverage/sign decisions and
strict margins were inspected. All four original input certificates
are unchanged. No numerical preview is used as proof.

## Mathlib

Full matching coverage is not checked. No claim of absence, Lean
verification, or matching univalent-realization theorem is made. The
result uses the cited known formal identities and finite real algebra.
The singleton quadrature and trial certificate are not formalized in
Lean; full matching Mathlib coverage remains unchecked. L036/L037's
conditional library qualifications are retained. Calculation1309's
finite interval/sign certificate is not Lean formalized; full matching
Mathlib coverage remains unchecked.
The audit and the cited analytic necessary-condition specialization
are also not Lean formalized. Full matching Grunsky/actual-Xi coverage
in Mathlib remains unchecked; no absence claim is made.
