# Corollary C048n: actual Rice phase in the inner sector

## Hypotheses

Use C048a's meromorphic continuation of
\(I(p)=2\int_0^\infty u^{2p-1}\Phi(u)\,du\), initially for
\(\Re p>0\), C048j's principal main term

\[
 w=W_0(2p/\pi),\qquad
 S(p)=\frac{8\pi^{5/2}e^{9w/4}}{\sqrt{p(1+w)}}
       \exp\{2p\operatorname{Log}(w/2)-2p/w\},
\]

and C048m's normalization

\[
 B_d(s)=\frac{d!}{\prod_{k=0}^d(s-k)},\qquad
 F_d^I(s)=\frac{\sqrt\pi\,4^{-s}I(s+1/2)B_d(s)}
                         {Z\Gamma(s+1/2)},\qquad Z=\gamma_0>0.
\]

All logarithms and square roots have those results' principal branches.
Let d be a positive integer, p=s+1/2, rho=|s|, r=|p| and L=log r.
The region under consideration is

\[
 d^{1/3}\le\rho\le d^{2/3},\qquad
 \Im s\ge\rho/2,\qquad
 \Re p\ge-\frac r{8\log r},\qquad r>1.                 \tag{1}
\]

The last condition merely makes the displayed logarithmic boundary
unambiguous; it is automatic for all sufficiently large d. Reuse
C048j's value bound on its entire wider sector and C048m's phase
bound. No differentiated Mellin asymptotic, source second-derivative
constant, finite supplement, signed contour estimate or RH is assumed.

## Conclusion

There exists an integer d_0 such that, for every integer d>=d_0 and
every s satisfying (1), F_d^I is holomorphic and nonzero on a
neighborhood of s and

\[
 \Im\frac{(F_d^I)'(s)}{F_d^I(s)}\ge\frac1{60\log|p|}>0.  \tag{2}
\]

This is the approved bounded REPRODUCTION specialization under
assessment1669. It is local analytic progress, with no claim of a
result beyond the inspected sources. The source's Appendix C.1
differentiation case assumes Re p>=-5 and does not cover (1).
We instead import the standard closed-disk Cauchy estimate and verify
its applicability to the existing local value bound. Independent
conceptual audit1672 below accepts this transfer and its essential
C048m phase input without correction. No signed-integral or actual-Xi
sign conclusion is asserted.

## Proof

### A complete Cauchy neighborhood

For the moment let p satisfy the inner-sector inequality in (1) and
L>=13, without reference to d. Put

\[
 R=\frac r{32L},\qquad D=\{z:|z-p|\le R\}.
\]

For every z in this closed disk, since R<r/4,

\[
 \frac{3r}4<|z|<2r,\qquad
 \Re z\ge-\frac r{8L}-R=-\frac{5r}{32L},\qquad
 \log|z|>L-1\ge12.                                   \tag{3}
\]

The function x/log x is increasing for x>e. Applying it to |z| and
3r/4, whose logarithm is positive and less than L, gives

\[
 \frac{|z|}{4\log|z|}
 \ge\frac{3r}{16\log(3r/4)}
 >\frac{3r}{16L}=\frac{6r}{32L}.
\]

Consequently Re z> -|z|/(4log|z|). Thus the entire D lies strictly
inside the radial and angular conditions of C048j's wider sector,
including when p is on the closed boundary in (1).

C048a gives a single meromorphic I with possible poles only at
nonpositive integers; none is in this wider sector. Its principal
Lambert branch is analytic near every such point. C048j supplies the
same locally analytic, nonzero S there, with its specified logarithm
and square-root branches. Hence

\[
 E(z)=I(z)/S(z)-1
\]

is holomorphic on an open neighborhood of D. Here the quotient uses
the canonical functions, so the local neighborhoods agree on overlaps.
Alternatively the strict inequalities above place D in the open
interior of that sector. No moving-height integral is differentiated.

### Full-circle value control and a derivative estimate

At every z in D, C048j gives

\[
 |E(z)|<\frac{17}{10}\frac{(\log|z|)^{9/2}}{|z|}.
\]

Since |z|<2r and L>=13, log|z|<L+1<=13L/12. Also
|z|>r/2. The elementary rational inequality
\((13/12)^{9/2}<(13/12)^5<2\) therefore yields the full disk bound

\[
 \sup_D|E|\le 7\frac{L^{9/2}}r.                       \tag{4}
\]

Indeed the intermediate coefficient is at most
\((17/5)(13/12)^{9/2}<34/5<7\). The bound is on the entire
circle required by Cauchy, not just at p or on a ray.

Import the named Cauchy estimates, A. Nagel, *Math722: Complex
Analysis*, Spring2012, Corollaries3.11--3.12, printed pp10--11
([primary notes](https://people.math.wisc.edu/~nagel/Math722Spring2012.pdf)).
For a function holomorphic on an open neighborhood of a closed
radius-R disk, its first derivative at the center is at most R^(-1)
times its supremum on the circle. The hypotheses have just been
verified, so (4) gives

\[
 |E'(p)|\le\frac{224L^{11/2}}{r^2}.                   \tag{5}
\]

This theorem is imported without reproof. Source-notes1670 records
the inspected theorem and the narrower scope of the preprint's own
differentiation case.

Choose a single real L_*>=13 large enough that, for every L>=L_*,

\[
 7L^{9/2}e^{-L}\le\tfrac12,\qquad
 26880L^{13/2}e^{-2L}\le1.                            \tag{6}
\]

Such a choice exists: exponential growth dominates each fixed power.
Explicitly e^L>=L^6/6! and e^(2L)>=(2L)^8/8! show that both
left sides tend to zero. Both are decreasing for L>=13, since
their logarithmic derivatives are 9/(2L)-1 and 13/(2L)-2.
Thus (6) is a common eventual ray bound, not a pointwise choice.

By (4),(6), |E(p)|<=1/2, so I(p)=S(p)(1+E(p)) is nonzero.
By continuity this also holds on a neighborhood of p. The exact
quotient derivative, with no choice of a global logarithm of I, gives

\[
 \left|\frac{I'(p)}{I(p)}-\frac{S'(p)}{S(p)}\right|
 =\left|\frac{E'(p)}{1+E(p)}\right|
 \le\frac{448L^{11/2}}{r^2}
 \le\frac1{60L}.                                    \tag{7}
\]

The final inequality is precisely the second condition in (6),
with r=e^L. No value asymptotic has been formally differentiated.

### Transfer and a uniform integer onset

Choose an integer d_0 at least exp(36) and at least
\((e^{L_*}+1/2)^3\). For any d>=d_0 and s in (1),

\[
 r\ge\rho-1/2\ge d^{1/3}-1/2\ge e^{L_*}.
\]

In particular L>=L_* and all the bounds above apply. The same s
satisfies C048m's wider-sector hypotheses. Its sufficient onset
d>=exp(36) therefore supplies

\[
 \Im\frac{(F_d^S)'(s)}{F_d^S(s)}\ge\frac1{30L}.
\]

Since Im s>=rho/2>0, no s-k is zero and p is not a gamma pole.
The finite B_d is nonzero and holomorphic near s; gamma is finite
and nonzero near p, as used in C048m (DLMF5.2(i)). All other
prefactors are nonzero. Together with I(p)!=0 this proves the
local holomorphy and nonvanishing asserted for F_d^I. Exactly,

\[
 F_d^I(s)=F_d^S(s)(1+E(s+1/2)),\qquad
 \frac{(F_d^I)'(s)}{F_d^I(s)}
 -\frac{(F_d^S)'(s)}{F_d^S(s)}
 =\frac{E'(p)}{1+E(p)},
\]

where dp/ds=1. Taking imaginary parts and using (7) proves (2).
This is uniform in d and s, including the annular endpoints and
closed angular boundaries. No explicit or optimal d_0 is claimed.

The inequality excludes a stationary point of this actual integrand
in the stated region. It does not estimate a signed integral along
any contour: direction, amplitude, endpoints, global coverage, and
a sufficient Xi/height transfer remain separate unresolved steps.
The fixed-d absolute-opening stop1657 and theta-crossing stop1667
are unaffected. The main L030--L032/C032a positivity gap remains open.

### Independent conceptual audit1672 — 19 November2026

The full proof and C048m's full phase proof were reviewed under the
unchanged SPECIALIZE assessment1669. Reused source-notes1670's exact
closed-disk Cauchy hypotheses and source-notes1663's digamma remainder.
Read C048a's continuation statement and branch proof, C048j's full
assembly and audit, and C048l's exact derivative and gamma identities.
The existing C048j component results remain inputs; this is not a new
audit of their separate quantitative certificates. No mathematical
correction to this transfer or to C048m was required.

**Entire disk and branches.** For L>=13, R=r/(32L)<r/4.
Every z in the closed disk has |z|>3r/4 and log|z|>L-1>=12.
Since x/log x is increasing for x>e,
|z|/(4log|z|)>6r/(32L), whereas Re z>=-5r/(32L).
There is therefore strict clearance from both boundaries of C048j,
including when the center is on the nominated closed angular boundary.
No negative real point is in this wider sector: for z=-a<0 its
inequality would require log a<=1/4, contradicting log a>12.
Thus C048a's only possible Mellin poles are absent on a neighborhood
of the disk, and the principal Lambert branch is available there.

The square root is also a genuine analytic choice on that neighborhood.
C048j's audited branch identity gives
sqrt(p(1+w))=w sqrt(A_0)/2, where |arg w|<pi/4 and Re A_0>0.
Its right side has argument strictly between -pi/2 and pi/2;
consequently p(1+w) avoids the square-root cut and zero.
The other logarithm has Re w>0. Strict inequalities and compactness
give one open neighborhood of the entire closed disk. These are the
canonical principal functions, so the quotient E is single-valued
and holomorphic there; it is not assembled from unrelated local signs.
No nonvanishing of I is assumed in defining E.

**Whole-circle Cauchy bound and nonvanishing.** On the disk,
log|z|<L+1<=13L/12 and |z|>r/2. The elementary bound
(13/12)^(9/2)<(13/12)^5=371293/248832<2 gives the
coefficient (17/5)(13/12)^(9/2)<34/5<7. Thus (4) holds on
the whole required circle. Nagel Corollary3.12 applies with its
closed-disk hypothesis just verified; dividing by R gives precisely
224L^(11/2)/r^2. Once 7L^(9/2)exp(-L)<=1/2, I(p) is
nonzero because S(p) is nonzero and |1+E(p)|>=1/2. The logarithmic
derivative difference is the exact quotient E'/(1+E), with bound
448L^(11/2)/r^2. No logarithm of I or differentiated value
asymptotic has been silently assumed.

**Common onset and exact target.** Both scalar functions in (6)
decrease for L>=13 and tend to zero. Their common eventual ray can
be fixed before d and s are chosen. The integer ceiling of the
maximum of exp(36) and (exp(L_*)+1/2)^3 is a valid d_0.
The entire nominated annulus then has r>=exp(L_*), while its
angular condition is stronger than C048m's. The independently checked
C048m margin is 1/(30L). The second condition in (6) is exactly
448L^(11/2)/r^2<=1/(60L), since 60*448=26880.
Subtracting this error leaves the required 1/(60L).

The exact shift p=s+1/2 has derivative one. Im s>0 excludes all
finite-kernel and gamma poles; their nonzero factors and I(p)!=0
give local holomorphy and nonvanishing of F_d^I. This covers the
closed annular and angular endpoints with a single onset. The audit
does not claim an effective optimized onset, a contour integral
estimate, or progress beyond the inspected sources. Stops1657/1665/1667
and the unpaid signed/Xi bridge remain. No new mathematical script
or numerical sample was needed for these analytic and exact checks.

## Mathlib

Full matching coverage of this actual-Rice phase specialization has
not been checked; availability is unknown. Supporting mathematics
is the precisely cited standard Cauchy estimate and the local
continuation, value and phase inputs. No formal verification or
absence from Mathlib is claimed. The specialization is needed because
the inspected source differentiation case does not have the curved
left boundary (1). No mathematical script or numerical sample is
evidence for the uniform statement.
