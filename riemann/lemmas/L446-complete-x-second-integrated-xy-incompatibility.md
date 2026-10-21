# Lemma 446: the unchanged complete x-second fails exact integrated xy compatibility

## Hypotheses

Use precisely L443's complete family and L445's specified pointwise
conditional density q_H(t)=integral x^2 dnu_(H,t), on an eventual
real-H ray. Write ell=log H, L(t)=log(2+t), and E_H=H^(-1)
integral_[H,2H]. Keep the high and both signed intermediate components,
all remaining probabilities, translation, normalization and constant
covariance correction. Use any one original admissible L429 sequence
B_j and its cutoff j(H). In particular

    B_(j+1)>=2B_j, log B_j>=M_j^8,
    M_j=product_(p<=p_j)(1+p^(-1/2))/(1-p^(-1/2)).

No thresholds are increased for this proof. All H-dependent parameters
are held fixed when differentiating in t. There is no inter-H
consistency, covariance feasibility or actual sine-limit assumption.

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-complete-x-second-integrated-xy-compatibility.md`.
This is a REPRODUCTION using known weak-derivative and endpoint
calculus and the finite-product method already used in L440.
It claims no new general theorem or established originality.

## Conclusion

At each fixed sufficiently large H, every integrable raw cross entry
r_H satisfying all temporal x-squared identities

    E_H[a' q_H+2L a r_H]=0 for every a in C_c^1((H,2H))       (1)

equals q_H'/(2L) almost everywhere. This entry exists and is integrable.
Define, with the actual closed-interval endpoint values,

    J(H)=q_H(2H)/L(2H)-q_H(H)/L(H)
                +integral_H^(2H) q_H(t)L'(t)/L(t)^2 dt.     (2)

Then exact compatibility with L443's additional constraint E_H r_H=0
holds if and only if J(H)=0. For the unchanged complete density,

    (1/B_j) integral_(B_j)^(2B_j) J(H)cos(H log 2)dH
                       =-1/sqrt(2)+o(1) as j->infinity.    (3)

Consequently, for every sufficiently large j there is a positive
Lebesgue-measure set of H in [B_j,2B_j) for which

    |J(H)|>1/(4sqrt(2)),
    |E_H r_H|>1/(8sqrt(2)H).                              (4)

In particular no family of integrable cross entries meets both
requirements for every sufficiently large real H with this unchanged
x-second density, even if arbitrary growth of the entries is allowed.
The separate step-283 critical audit below validates this result.

The obstruction preserves L443's finite-block compatibility and
L445's fixed-H regularity. It strengthens the stopping conclusion
for this unchanged density beyond L444's bounded-repair restriction.
It does not exclude a changed x-second density or another law, and
does not assert failure at every H. Covariance realization, other
occupation identities, actual clipping, capped nondegeneracy,
L413's full-error margin, global mixed positivity and RH remain open.

## Proof

### Weak uniqueness and the exact endpoint constraint

L444 gives exactly the necessary identity (1). L445 proves that the
specified q_H itself is Lipschitz on the closed interval, including all
branch values. Thus it is absolutely continuous with an integrable
a.e. derivative. Import J. K. Hunter, *Notes on Partial Differential
Equations*, revision 2014-06-18,
[Definition 3.1, printed pp. 47--48, and Theorems 3.60, 3.62--3.63,
pp. 79--80](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf):
the AC derivative is the weak derivative, and AC integration by parts
retains both endpoint products. Uniqueness can equivalently be read
from Jordan Bell, *Sobolev spaces in one dimension and absolutely
continuous functions*, 2015-10-21,
[Section 1, Theorem 1 and the following derivative-uniqueness
paragraph](https://jordanbell.info/LaTeX/mathematics/sobolev1d/).

Indeed, restricting (1) to smooth compactly supported a gives
integral a(2L r_H-q_H')=0. The function in parentheses is locally
integrable, and Bell's theorem makes it zero a.e. Conversely
r_H=q_H'/(2L) is integrable on this compact interval, since L is
smooth and strictly positive. AC integration by parts proves (1)
also for every stated C_c^1 test. This uses only weak uniqueness,
not a trajectory or covariance converse.

Apply Hunter's endpoint formula to q_H and 1/L, both AC on [H,2H].
Since (1/L)'=-L'/L^2, it gives exactly

    2 integral_H^(2H) r_H(t)dt = J(H).                    (5)

The mean matrix in L443 (17), with K_11=1 and K_12=0 as displayed
in L421, gives E_H q_H=ell and the required E_H r_H=0.
Hence (5) proves the claimed equivalence. Endpoint redefinitions on
null sets would not change r_H, but (2) uses the unique continuous
representative already identified pointwise in L445.

Nonnegativity of q_H and L'(t)=1/(2+t) also give the exact bound

    0<=integral_H^(2H) q_H L'/L^2
      <=H ell/((H+2)ell^2)<=1/ell.                       (6)

Thus this entire moving-weight term is retained and controlled.
No endpoint equality or vanishing has been assumed.

### One original stage and its finite Fourier estimates

For this subsection put B=B_j, lambda=log B, y=p_j, P=P_j and
omega=log 2. Except possibly at the upper endpoint, all H in [B,2B]
have j(H)=j because B_(j+1)>=2B_j. The original bound gives
M_j<=lambda^(1/8). As in L440, the geometric expansion shows

    M_j>=product_(p<=y)(1-p^(-1/2))^(-1)
         >=sum_(n<=y)n^(-1/2)>=sqrt(y),

since every positive integer n<=y has all prime factors at most y.
Therefore y<=lambda^(1/4).

Use the finite Poisson character formula imported in L429/L440 from
C. Aistleitner, I. Berkes and K. Seip,
*GCD sums from Poisson integrals and systems of dilated functions*,
JEMS 17 (2015), 1517--1546, DOI 10.4171/JEMS/537,
[Section 3, p. 1527, identity preceding Lemma 1 and (23)](https://ems.press/content/serial-article-files/32047?nt=1).
Each radius p^(-1/2) is strictly below one and the product is finite.
In the present notation its absolutely convergent Fourier expansion is

    P(t)=sum_(k in Z^j) a_k exp(it sum_(p<=y)k_p log p),
    a_k=product_(p<=y)p^(-|k_p|/2), sum_k a_k=M_j.        (7)

No infinite critical-line Euler product is used. The change from
L440 is only the endpoint scaling t=cH, c=1,2, and the outer
sharp average in H. The following estimates verify that change.

Put K0=ceil(16 log(lambda)/log 2), and retain |k_p|<=K0 in each
coordinate, giving a finite polynomial P_tr. The same geometric-tail
union bound, now with lambda fixed over the stage, gives

    ||P-P_tr||_infinity
       <=C M_j y 2^(-K0/2)<=C lambda^(-61/8).             (8)

For clarity, one coordinate has omitted sum
2r_p^(K0+1)/(1-r_p); multiply by the complete other-coordinate
sums and use r_p<=2^(-1/2). Summing over at most y coordinates
proves (8), including all omitted multiindices.

Write D=product_(p<=y)p^K0. A retained frequency is log(n/m)
with n,m<=D, and

    log D<=K0 y log y=O(lambda^(1/4)(log lambda)^2)
                          =o(lambda).                  (9)

After t=cH and optional multiplication by cos(omega H), every
frequency is log(n^c/m^c) or log(2n^c/m^c) or log(n^c/(2m^c)).
For c=1,2 both positive integer arguments in these ratios are at
most 2D^2. A nonzero such frequency has absolute value at least
1/(2D^2): integrate 1/v between the two unequal integers.
Direct sharp integration, retaining both endpoints, gives

    |B^(-1) integral_B^(2B) exp(iuH)dH|<=2/(B|u|).

Since the total coefficient mass, also after cosine multiplication,
is at most M_j, all nonzero terms cost at most 4D^2 M_j/B.
Together with (8), define a common bound

    delta_j=C lambda^(-61/8)+4D^2 M_j/B=o(1).             (10)

Unique prime factorization makes the constant coefficient of
P_tr(cH) equal to one for both c. For P_tr(H)cos(omega H),
the two matching prime-2 exponents are +1 and -1, with no other
prime exponents. Each contributes half of 1/sqrt(2), so the
constant is 1/sqrt(2). For P_tr(2H)cos(omega H), a matching
exponent would require 2k_2=1 or -1, impossible for integral k_2.
There are no other resonances. Thus, with A_j denoting
B^(-1) integral_B^(2B) in the remainder of this proof,

    A_j P_j(cH)=1+O(delta_j), c=1,2,
    A_j[P_j(H)cos(omega H)]=1/sqrt(2)+O(delta_j),
    A_j[P_j(2H)cos(omega H)]=O(delta_j).                 (11)

These statements use only the original cutoff growth bound.
No new averaging test has been inserted into the thresholds.

### Absolute endpoint control for the entire density

The parameters ell=log H now vary over the outer interval [B,2B).
They satisfy lambda<=ell<=lambda+log 2. At an endpoint t=cH
with c=1 or 2, L(cH)=ell+O(1), uniformly, and L(cH)>=ell.
The actual critical triple X0(t) in L445 depends on t alone.
Set u(t)=|X0(t)|^2 and V_H(t)=max(ell^6,sqrt(2)u(t)).

L445 (6) and L438's uniform component bounds give, at every point
and branch, with one constant independent of the stage,

    q_H(t)=u(t)x0(t)^2/V_H(t)
       +sqrt(ell)[(4/9)F_+/h_++F_- (n_-)_1^2/h_-]
       +w(t)[ell P_j(t)/N_H+(A_H)_11+m_1(t)^2],          (12)

    0<=u x0^2/V_H<=u^2/ell^6,
    p=u^2/V_H^2<=u^2/ell^12,
    k_++k_-<=C ell^(-5/2), 1-w=p+k_++k_-,
    |F_+|/h_++|F_-|/h_-<=C,
    |(A_H)_11|<=C sqrt(ell), |m_1|<=C.                 (13)

Here F_+ and F_- are the positive and negative parts of the
complete calibrated F_H, and both direction denominators retain
their exact positive margins. These bounds do not discard a
signed component, replace a conditional probability by its average,
or differentiate a selection branch.

The original stage averaging guarantee is
|E_H P_j-1|<=epsilon_j, epsilon_j=1/(j+4), for every H>=B_j.
On the present stage L438's complete mass bound therefore yields

    |N_H-1|<=epsilon_j+E_H[(1-w)P_j]
             <=epsilon_j+C ell^(-19/8),
    1/2<=N_H<=2                                          (14)

eventually, uniformly in H in [B,2B). In particular this retains
the high probability loss as well as both intermediate losses.

Subtract ell P_j/N_H from (12), divide by L(cH), and use
(13)--(14), P_j<=M_j and L(cH)>=ell. This gives

    |q_H(cH)/L(cH)-(ell/L(cH))P_j(cH)/N_H|
       <=C[u(cH)^2/ell^7+ell^(-1/2)
                +M_j u(cH)^2/ell^12+M_j ell^(-5/2)].     (15)

The actual fourth-moment input used in L421 is
T^(-1) integral_T^(2T) |X0(t)|^4 dt=O((log T)^4)
for every sufficiently large real T. Changing variable t=cH
for c=1,2 gives

    A_j u(cH)^2=O(lambda^4).                            (16)

Thus the A_j average of the right side of (15) is
O(lambda^(-3)+lambda^(-1/2)+lambda^(-63/8)
+lambda^(-19/8))=O(lambda^(-1/2)).
This controls endpoint samples by actual fourth moments on the
two full intervals [B,2B] and [2B,4B]; it assumes no pointwise
smallness of the high state and no inter-H law consistency.

Finally,

    |(ell/L(cH))/N_H-1|
       <=C(epsilon_j+lambda^(-19/8)+lambda^(-1)).

To remove this factor, use positivity and the first line of (11):
A_j |P_j(cH)|=1+O(delta_j), bounded independently of j.
Multiplying the preceding bound by this L1 norm, rather than by
the growing supremum M_j, proves

    A_j |q_H(cH)/L(cH)-P_j(cH)|
                         =O(epsilon_j+lambda^(-1/2))=o(1),
                         c=1,2.                        (17)

All translation, constant covariance, high and both intermediate
terms have been estimated in absolute value. No cancellation of
unevaluated endpoint errors is needed.

### The compatibility decision

The defining parameter integrals in L438 are jointly Borel and
locally bounded on the eventual parameter domain, as also verified
in L443. L445's formula therefore makes the endpoint functions
in (2) Borel and finite. Bounds (6), (15)--(16) prove their
integrability on each outer interval. An exceptional cutoff value
at H=2B has measure zero and does not affect any outer integral.

Combine (6), (11), (17), and |cos(omega H)|<=1:

    A_j[J(H)cos(omega H)]
      =A_j[(P_j(2H)-P_j(H))cos(omega H)]+o(1)
      =-1/sqrt(2)+o(1).

This proves (3). In particular A_j |J|>=1/(2sqrt(2)) eventually.
If |J|<=1/(4sqrt(2)) almost everywhere on such an interval, its
average could not satisfy that bound. Therefore the set where
|J|>1/(4sqrt(2)) has positive measure. Equation (5) gives (4).
Since B_j tends to infinity, these incompatible heights are
arbitrarily large. This is enough to refute compatibility throughout
an eventual real-H ray, without deciding individual remaining heights.

The obstruction is a nonzero stage-averaged endpoint harmonic in
the exact scalar compatibility constraint. It neither uses L444's
uniform-size restriction nor repeats the singular-variation test
closed by L445. It supplies no changed law or global realization.

### Separate critical audit — 2026-10-20, step 283

The audit uses the separately saved SPECIALIZE scope
`drafts/literature/2026-10-20-integrated-xy-incompatibility-critical-audit.md`.
It checks the complete assertion against the input formulas, not against
the step-281 summary or failure record. No hypothesis, coefficient,
cutoff threshold or direct mathematical input changes.

**Weak equation and representative.** L444 (3) uses x'=Ly, so its
factor is 2L and its sign is positive. L445 (6), including its
pointwise branch conventions, is Lipschitz on the closed interval.
For fixed H the difference 2Lr-q' is locally integrable. Bell's cited
local uniqueness theorem applies to its integral against every smooth
compactly supported test, giving r=q'/(2L) a.e. Conversely that entry
is integrable and satisfies every C_c^1 test by AC integration by parts.
Neither implication requires positive covariance or a trajectory.
Hunter's cited endpoint formula applies to q and the smooth positive
reciprocal 1/L. Its derivative is -L'/L^2, so the integral term in
(2) has the stated plus sign. Exactly 2H E_H r=J(H), not 2 E_H r=J(H).
L443 (17) preserves the complete integrated matrix ell K, whose
entries K11=1 and K12=0 are explicit in L421. Hence E_H q=ell,
and positivity gives (6). Arbitrary endpoint changes would invalidate
this use of integration by parts; L445 has already excluded them by
identifying the specified density itself with its continuous representative.

**Both endpoint frequencies and complete tails.** For B=B_j the
half-open interval [B,2B) lies entirely in stage j, even when
B_(j+1)=2B. Set lambda=log B. The bound M_j<=lambda^(1/8) follows
at B, and the elementary integer sum gives p_j<=lambda^(1/4).
The omitted mass per coordinate, divided by that coordinate's full
mass (1+r)/(1-r), is 2r^(K0+1)/(1+r). A union bound over at most
p_j coordinates therefore gives (8), with exponent
1/8+1/4-8=-61/8. It bounds the entire omitted Fourier series, also
after either endpoint substitution and multiplication by the cosine.

For the retained series, log D<=K0 p_j log p_j=o(lambda).
After doubling and either cosine shift, both numerator and denominator
are positive integers at most 2D^2. For unequal integers a,b in that
range, |log(a/b)|>=|a-b|/max(a,b)>=1/(2D^2).
The sharp interval integral is at most 2/(B|log(a/b)|).
The sum of absolute coefficients after the cosine is at most M_j;
thus 4D^2 M_j/B controls all nonzero modes without a separate
dimension factor. This term is exp(-lambda+o(lambda)), so it tends
to zero under the original thresholds.

Unique prime factorization gives only k=0 for the unweighted
constant coefficient at either endpoint. At H, the cosine adds
exactly the two prime-2 indices k_2=+1 and -1, with all other
indices zero; their halves sum to 1/sqrt(2). At 2H the equations
2k_2=+1 or -1 have no integral solution. There is no hidden
denominator resonance. These facts verify all three lines of (11),
including the bounded positive L1 averages at both endpoints.

**Actual fourth moment and changing outer height.** The actual triple
is X0(t)=(f,f'/L,f''/L^2), with ordinary differentiation before
division. The exact constant-sign identity f=-sigma Z recorded in
L389 holds also at critical zeros. The known moment used through
L421/L418 is Bui--Hall, *On the derivatives of Hardy's function Z(t)*,
Bull. Lond. Math. Soc. 55 (2023), 2304--2323,
[arXiv:2304.05178v1 (11 April 2023), Theorem 3 and the preceding
defining fourth-product asymptotic](https://arxiv.org/html/2304.05178v1),
[DOI 10.1112/blms.12859](https://doi.org/10.1112/blms.12859).
Its fixed ordinary orders d=0,1,2 give
integral_0^(2T)|Z^(d)|^4=O(T(log T)^(4d+4)).
On [T,2T], division by L(t)^(4d)>=log(T)^(4d) gives an
O(T(log T)^4) bound for each normalized coordinate. The inequality
|X0|^4<=(3 sum_d |f^(d)/L^d|^4) then gives (16).
This is the necessary normalization specialization, not a reproof
of the source theorem. The source's omitted Proposition 3 proof,
recorded in the approved assessment, remains an imported-source
qualification; this audit does not independently prove that theorem.

More explicitly,

    B^(-1) integral_B^(2B) u(cH)^2 dH
      =(cB)^(-1) integral_(cB)^(2cB) |X0(t)|^4 dt
      =O(lambda^4), c=1,2.

Thus the upper endpoint uses [2B,4B], not a typical conditional
sample in [H,2H]. Every denominator ell=log H can be bounded
below by lambda and above by lambda+log 2. No parameter of the
conditional law is differentiated with respect to H.

**Complete density error.** L445 (6) agrees with (12) pointwise:
the high contribution is u x0^2/V, the positive intermediate has
first-coordinate square 4/9, the negative one has (n_-)_1^2<=1,
and the full bulk contribution is w(ell P_j/N_H+A_11+m_1^2).
L438 (10)--(15) give both positive denominator margins, bounded
F_H, w in [1/4,1], bounded m and ||A_H||=O(sqrt(ell)).
L441/L443 change no entry 11. The high mass need not be uniformly
small, so its loss must be kept as p=u^2/V^2<=u^2/ell^12.
The high raw entry is at most u^2/ell^6; the two intermediate raw
entries together are O(sqrt(ell)).

After division by L(cH)>=ell, the high raw entry costs
u(cH)^2/ell^7. Intermediate, covariance and translation entries
cost O(ell^(-1/2))+O(ell^(-1)); the latter is absorbed in the
former. Removing w from the leading Poisson term costs at most
C M_j(u(cH)^2/ell^12+ell^(-5/2)). Thus (15) keeps all terms.
Their outer L1 bounds, in the order just used, are

    O(lambda^-3), O(lambda^(-1/2)),
    O(lambda^(-63/8)), O(lambda^(-19/8)).

The normalization is uniformly controlled because the original
threshold tests E_H P_j at every real H>=B_j, and L438 gives
E_H(1-w)=O(ell^(-5/2)). Thus
|N_H-1|<=epsilon_j+C ell^(-19/8) and N_H>=1/2 eventually.
Also L(cH)-ell=log(c+2/H) is bounded for c=1,2. Consequently
the remaining multiplicative error has supremum
O(epsilon_j+lambda^(-19/8)+lambda^-1).
It multiplies A_j P_j(cH)=1+O(delta_j), a bounded L1 mean.
It does not multiply M_j. This verifies (17) with its stated
O(epsilon_j+lambda^(-1/2)) bound even without a rate relating
epsilon_j to lambda. All constants are uniform in the stage and
outer height after the common onset.

**Signed limit and quantifiers.** The Borel parameter formulas of
L438 and the preceding absolute estimates make J measurable and
integrable on each stage interval. The integral in (2) contributes
at most 1/lambda to its cosine average. Combining the two complete
endpoint bounds with (11) gives (3), with total error bounded by
C(delta_j+epsilon_j+lambda^(-1/2)+lambda^-1), tending to zero.
Thus A_j|J|>=1/(2sqrt(2)) eventually. If the set
{|J|>1/(4sqrt(2))} had measure zero, this last inequality would
fail. Its positive measure and 2H E_H r=J imply exactly (4).
Since B_j tends to infinity, this refutes one family satisfying both
requirements on any whole eventual real-H ray. It does not assert
failure at each H, a uniform proportion of incompatible heights,
or inter-H consistency.

The audit passes. This is verification of the local known-tool
specialization, not a new general theorem or a result beyond the
checked sources. The unchanged-density extension is stopped even
without a growth bound on r. Changed densities and other laws remain
different targets; all realization, clipping, regulator and mixed
positivity gaps stated above remain unresolved.

## Mathlib

Full matching coverage of this complete-law incompatibility statement
has not been checked; no absence claim is made. The external inputs
are the cited AC/weak-derivative results and finite Poisson character
formula, with local actual-moment bounds imported through L421.
No formalized conditional law, exact theorem name in Mathlib, or
formal verification of the stage-average proof is asserted.
