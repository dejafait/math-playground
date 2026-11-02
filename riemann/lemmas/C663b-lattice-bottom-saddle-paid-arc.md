# Corollary 663b: a signed bottom saddle supplies a paid arc for the fixed lattice

## Hypotheses

Use exactly L663's unit-residue lattice and C663a's notation:
n=6q+3, q>=1, d=5/4, x=-d, R=11/8, U=121/64, eta=1/100,
Y=9/20, h=27/(10n), a_l=x+i*l*h for -q<=l<=q, and
M=2q+1=n/3. Every residue is one. With every t_j=j/n, 0<=j<n,
retain

    B_u(v)=product_j R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    c_k(u)=R^(-1) sum_l W_(a_l)(u)*(a_l/R)^k,
    G(u,zeta)=sum_(0<=k<M)c_k(u)*zeta^k,
    D=sum_l mean_u |W_(a_l)(u)|^2/(U-|a_l|^2),
    H=max_u mean_zeta log|G(u,zeta)|.

Both circle means are normalized; logarithms are natural. In particular
1/u is the conjugated denominator angle. No pole is moved when u varies.
Let ell_0(u) be the constant coefficient of C663a's exact lower-edge
polynomial Bcal_n, whose bottom height is -2/25. Put

    lambda=20*pi/27, e_0=117/100, rho_bar=103/9375,
    rho_*=261/20000, gamma=29/1000, kappa=91/5000.

## Conclusion

There are absolute c>0, C and one onset along this sequence such that

    c_0(-1) >= c*sqrt(n)*exp(-rho_bar*n),                (1)
    |ell_0(-1)| >= c*sqrt(n)*exp(-rho_bar*n),             (2)
    H >= -rho_bar*n+(log n)/2-C.                        (3)

In particular rho_*-rho_bar=619/300000>0. There is a connected arc
I_n of normalized measure n^(-2) for which the complete paid expression
satisfies

    log mu(I_n)+2 mean_(I_n x T)log|G|-log D+n/16
                  >=(619/150000)*n-2log n-C.            (4)

Thus the approved arc criterion holds for this fixed unit lattice,
with C=0 in that criterion after an existential onset. The same lattice
fails the full-circle test by L663. These conclusions are compatible:
the arc is supplied by L658 at a maximum of the full spatial logarithmic
mean, not asserted to be centered at u=-1.

The first kernel frequency has a positive signed Gaussian limit after
a contour shift within L663's rectangle. All higher frequencies and
the entire top/side contribution are o(1) relative to its positive scale.
No saddle-only approximation or coefficient truncation is a premise.
This does not establish the criterion for arbitrary integer support,
Xi realization, matching upper bounds or signs. No effective numerical
onset or RH candidate is claimed. The conceptual audit in section 7
validates (1)--(4), including C663a's inherited remainder. It reuses
the cited source theorems and previously audited interval backend;
their source manuscripts and an independent backend are not audited.

## Proof

### 1. Source scope and the distinct test

Reuse the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-localized-logarithmic-joint-moment.md`.
The proposed step remains its paid-arc target. L663 supplies the exact
finite contour and analytic clearances; C663a supplies the top/side
rate and original-bottom isolation. L658 supplies paid localization;
L661 supplies only its general squared-residue diagonal envelope.

The contour imports are R. W. Howell and J. H. Mathews,
*Complex Analysis*, online edition,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html)
and [Section 6.2, Theorems 6.2.18--6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html).
The spatial root identity is F. Brunault and W. Zudilin,
*Many Variations of Mahler Measures*, ISBN 9781108794459,
[Proposition 1.4, pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf),
including boundary roots. These already inspected imports are reused,
not reproved or independently audited. L658 retains L657's absolute
logarithmic integrability and nonzero-slice verification.

L659's finite anchor-phase resonant lattice has a different spacing;
its amplitude proof does not apply to this fixed lattice. L660 excludes
one retained monomial neutralizing the anchor phase, not a complex
contour saddle of the exact sampling kernel. The full-circle,
endpoint-dominance and finite-screen stops remain valid. None gives
(1). The finite-product proof below is needed for the changed spacing
and all its frequencies; no general steepest-descent theorem is invoked.
POTENTIALLY_NEW describes only the checked source scope, not originality.

### 2. An interior real saddle and a strict rate margin

For e in [e_0,d] define

    A_e(t)=1/(e-t), b_e(t)=t/(U-e*t),
    g(e)=integral_0^1 [A_e(t)+b_e(t)] dt.

All denominators are positive. Also b_e(t)<=A_e(t)/2: this is
equivalent to 3*e*t-2*t^2<=U, and the quadratic's maximum on the
real line is 9*e^2/8<=225/128<242/128=U. Differentiating the
integral, justified by uniform positive clearances on the compact set,
therefore gives

    -g'(e)=integral_0^1 [A_e(t)^2-b_e(t)^2]dt
       >=(3/4) integral_0^1 (d-t)^(-2)dt=12/5.         (5)

The integrand defining g is increasing in t: its derivative is
1/(e-t)^2+U/(U-e*t)^2>0. Exact 256-cell left/right sums prove

    21/10 < g(d) < 11/5,       g(e_0)>7/3.              (6)

The certificate in section 6 gives the complete rational terms and
outward-rounded sums. The classical Archimedes bounds 3<pi<22/7
imply 11/5<20/9<lambda<440/189<7/3. Thus continuity and (5)
give a unique e_* in (e_0,d) with g(e_*)=lambda. It is a fixed
constant independent of n. Set b_*=d-e_*, so 0<b_*<2/25, and

    rho=lambda*b_*-integral_(e_*)^d g(E)dE
         =integral_(e_*)^d [lambda-g(E)]dE >0.

From (5), g(E)>=g(d)+(12/5)(d-E). Consequently

    rho < (7/30)*b_*-(6/5)*b_*^2
          <= (7/30)*(2/25)-(6/5)*(2/25)^2
          =103/9375=rho_bar.                           (7)

The quadratic is increasing on [0,2/25], since its derivative there
is at least 7/30-24/125>0. All numerical comparisons here are exact.
In particular rho_bar<rho_*<gamma. The saddle is not selected from
an uncertified numerical maximization.

### 3. The full finite product on the shifted lower edge

For real |s|<=Y define

    W_n(s)=W_(-e_*+i*s)(-1),  W_n(0)>0,
    A_j=1/(e_*-t_j), b_j=t_j/(U-e_*t_j),
    Lambda_n=sum_j(A_j+b_j), V_n=sum_j(A_j^2-b_j^2).

Direct division of the original factors, including j=0, gives

    W_n(0)=product_j [(d-t_j)/(e_*-t_j)]
                       *[(U-e_*t_j)/(U-d*t_j)],
    W_n(s)/W_n(0)=product_j (1+i*b_j*s)/(1-i*A_j*s).     (8)

The first product is positive. Its continuum logarithm is
integral_(e_*)^d g(E)dE. L663's uniform absolute t-derivative bound
16 for its logarithmic product gives the two-sided left-sum error
at most 8, by integrating 16*(t-j/n) on every grid cell. Hence

    W_n(0)*exp(-lambda*n*b_*) >=exp(-8-rho*n)
                                           >=exp(-8-rho_bar*n). (9)

This is a lower bound for the complete finite product; no asymptotic
product constant is omitted. Ordinary Riemann sums, and the bounded
t-derivative of A_e+b_e, give

    Lambda_n=n*lambda+O(1), V_n/n -> V,
    V=integral_0^1(A_(e_*)^2-b_(e_*)^2)dt>=12/5.       (10)

All constants are absolute. For |s|<=1/16, A_j<6, b_j<=A_j/2<3,
so the logarithm power series with value zero at s=0 gives uniformly

    log[W_n(s)/W_n(0)]
           =i*Lambda_n*s-(V_n/2)*s^2+O(n*|s|^3).       (11)

Indeed both logarithm arguments have modulus below 1/2, and the
sum of terms of degree at least three is bounded by a constant
times |s|^3 per factor. No branch continuation beyond this small
interval is used.

A global modulus bound on the entire shifted segment follows from
(8), b_j<=A_j/2 and A_j>=4/5:

    log|W_n(s)/W_n(0)|
      =-(1/2)sum_j log(1+(A_j^2-b_j^2)*s^2/(1+b_j^2*s^2))
      <=-(1/2)sum_j (A_j^2-b_j^2)*s^2/(1+A_j^2*s^2)
      <=-n*s^2/40,               |s|<=Y.               (12)

For the last inequality use A_j^2-b_j^2>=12/25 and
1+A_j^2*s^2<1+36*(9/20)^2<9; thus the coefficient is at least
2/75>1/40. The preceding logarithmic inequality is
log(1+v)>=v/(1+v), v>=0, obtained by integrating 1/(1+v).

Equations (10)--(12) prove the following complete signed limit:

    sqrt(n)*integral_(-Y)^Y [W_n(s)/W_n(0)]
                                 *exp(-i*lambda*n*s) ds
           -> J:=integral_R exp(-V*z^2/2) dz >0.        (13)

For completeness, substitute z=s*sqrt(n) and extend the integrand
by zero outside [-Y*sqrt(n),Y*sqrt(n)]. On every fixed compact
z interval, (10)--(11) give uniform convergence to exp(-V*z^2/2):
the residual linear phase is O(|z|/sqrt(n)), and the cubic remainder
is O(|z|^3/sqrt(n)). Equation (12) bounds the absolute integrand by
exp(-z^2/40), whose tail integrals tend to zero. Compact convergence
plus these uniform tails proves (13). J is finite and positive; for
example its integral over [-1,1] is at least 2*exp(-V/2)>0.
The integral on the left is real because its values at s and -s
are complex conjugates. It is therefore at least J/2 for all large
n, not merely bounded below in modulus along a subsequence.

### 4. Every kernel frequency and every other edge

Replace the bottom height -2/25 of L663's rectangle by -b_*.
The new rectangle still encloses exactly the same lattice poles and
has the same top. Its vertical edges are subsets of the original
ones. The holomorphy and absence of boundary poles verified in L663
remain valid. Extract the constant spatial coefficient from the exact
finite contour identity. With the bottom oriented left to right,

    c_0(-1)=(1/(2*pi*i*R)) integral_(-Y)^Y
                    W_n(s)*K_n(s-i*b_*) ds + E_n,
    |E_n|<=C_* n^2 exp(-gamma*n).                       (14)

Here C_* is C663a's constant. Its proof establishes the pointwise
rate -gamma on the whole top and both original sides, with the
spatial cost retained; the same bound applies to the shorter sides
and to the constant coefficient. Thus (14) does not extrapolate a
bound on a sum of edges to its individual parts. There is no pole
crossing in the changed bottom strip.

For this fixed b_*>0 the exact geometric expansion is uniformly
absolutely convergent on the bottom segment:

    K_n(s-i*b_*)=i*lambda*n*sum_(m>=1)
                       exp(-m*lambda*n*b_*)*exp(-i*m*lambda*n*s).

Integration term by term is justified by that convergence on a compact
segment, with continuous W_n. The m=1 contribution in (14) is exactly

    [lambda*n/(2*pi*R)] W_n(0)*exp(-lambda*n*b_*)
          *integral_(-Y)^Y [W_n(s)/W_n(0)]exp(-i*lambda*n*s)ds.

By (13) it is positive and at least
lambda*J/(4*pi*R)*sqrt(n)*W_n(0)*exp(-lambda*n*b_*) eventually.
For all m>=2 together, (12) bounds their absolute contribution by

    C*sqrt(n)*W_n(0)*exp(-lambda*n*b_*)
                  *exp(-lambda*n*b_*)/(1-exp(-lambda*n*b_*)). (15)

This is o(1) times the positive leading scale. It controls every
higher frequency, irrespective of its oscillation. By (9), the ratio
of the error in (14) to that scale is at most
C*n^(3/2)*exp(-(gamma-rho_bar)*n), which tends to zero.
Finally c_0(-1) is real because the original lattice nodes occur in
conjugate pairs. Absorbing (15) and E_n proves (1) for every sufficiently
large n in the sequence. C663a's original-bottom coefficient bound
|c_0(-1)-ell_0(-1)|<=C_*n^2 exp(-gamma*n) then proves (2), reducing
c if necessary. This also verifies the bottom test in the checkpoint.

### 5. All spatial roots, diagonal cost and arc measure

For a nonzero complex polynomial P with nonzero constant coefficient,
the cited full root formula gives mean log|P|>=log|P(0)|: each
factor max(1,|alpha|) is at least |alpha|. Boundary roots and every
leading factor remain included. Apply this to the complete polynomial
G(-1,zeta), whose constant coefficient is positive by (1). This proves
(3), without an additive-logarithm comparison between G and Bcal_n.

L658 now gives an arc of measure n^(-2) whose paid logarithmic
expression is at least 2H-2log n-32*pi^2/9. L661's general envelope,
with the actual squared residues sum_l r_(a_l)^2=n/3, gives

    D<=n*exp(2*kappa*n+6)/(3*sigma^2), sigma^2=137/5000.

Combining these bounds with (3) yields an excess at least

    (1/16-2*kappa-2*rho_bar)*n-2log n-C
                      =(619/150000)*n-2log n-C,

as claimed. L658's full-polynomial nonzero and logarithmic-integrability
hypotheses hold for this admissible family by L663. No angular point
estimate is substituted for the paid arc mean.

### 6. Verification and limits

Run `python3 scripts/one-sided-hankel/lattice-bottom-saddle.py`.
The complete exact certificate is
`scripts/one-sided-hankel/lattice-bottom-saddle.json`. It records all
257 rational integrand values at each endpoint, with outward rounding
to denominator 10^12, and proves the 256-cell bounds

    33754371318213/16000000000000 <= g(d)
                       <=544830916701419/256000000000000,
    g(e_0)>=76605905174811/32000000000000.

All comparisons (6)--(7), the curvature/clearance bounds, and the exact
paid margin pass, with no failures. The full summary and check results
were inspected. The script does not verify the analytic contour shift,
signed limit, source manuscripts, or an effective onset. Those arguments
are written above and checked in section 7. C663a's inherited interval
aggregation is checked there without another interval-backend replay.

This is a local amplitude and paid-arc advance for the full-circle
countersequence, not a general-support theorem or progress beyond all
sources checked. L663's full-circle stop and C663a's endpoint-dominance
stop are preserved; the bottom saddle is precisely the contribution
they did not control.

### 7. Conceptual audit — 2 November 2026

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-02-lattice-bottom-saddle-audit.md`.
This audit accepts (1)--(4) with the stated existential onset and
unchanged constants, including C663a's inherited remainder. It
supplies no new inequality or certified originality. The wording
about relative error above is clarified to o(1), as already proved.

**Saddle and finite-product phase.** The inequality b_e<=A_e/2
follows from 3*e*t-2*t^2<=9*d^2/8<U on the full parameter range.
Thus -g'(e)>=12/5 throughout. Increasing t makes the exact left/right
sums genuine integral bounds. The reproduced sums bracket lambda
between g(d) and g(e_0), giving a unique fixed e_* and fixed b_*>0.
Integrating the curvature bound in the correct direction gives (7);
its quadratic is increasing on the whole permitted interval. Exactly,

    gamma-rho_bar=1351/75000>0,
    rho_*-rho_bar=619/300000>0.

At u=-1 each factor divided by its s=0 value is precisely
`(1+i*b_j*s)/(1-i*A_j*s)`, including `1/(1-i*s/e_*)` at j=0.
W_n(0)>0, so no constant phase is missing. Its logarithmic t-summand
has derivative of absolute value at most 16 in L663's rectangle;
cellwise integration gives the error bound 8 in both directions,
justifying the lower direction in (9). The t-derivative of A_e+b_e
is bounded on the compact range, so Lambda_n-n*lambda=O(1).
Consequently the finite-product phase discrepancy vanishes on the
Gaussian scale; V_n/n tends to the strictly positive V.

For |s|<=1/16 the logarithm series is in its disk of convergence
with value zero at zero, and its quadratic term has the negative
sign in (11). On the entire segment the exact modulus formula gives
coefficient at least `(1/2)*(12/25)/9=2/75>1/40` in (12).
After z=s*sqrt(n), the residual linear and cubic terms vanish on
each compact interval, and exp(-z^2/40) is a global integrable
majorant. Compact convergence and its uniform tails prove (13).
Reflection s->-s conjugates the integrand. The integrals are real
and eventually at least J/2, not merely large in modulus along a
subsequence. No effective onset is inferred from the scalar checks.

**Contour and inherited error.** The lower edge of the positively
oriented rectangle runs left to right. Its move from -2/25 to -b_*
crosses no real sampling pole and leaves the same 2q+1 poles, each
of residue one. L663's clearances exclude every zero or pole of W
in the strip. The first kernel frequency has factor i*lambda*n;
division by 2*pi*i*R therefore leaves the positive real prefactor.

C663a's bounds hold pointwise on the whole top and both sides.
Its vertical monotonicity charges the spatial derivative above v=0,
bounded by 4/15<3/10, and the kernel derivative below v=0, where
lambda>9/4. Thus the certified derivative bounds place each side's
maximum at v=0. L663's uniform angular second-derivative bound gives
the chord charge even when an edge maximizer changes. All three
charged maxima are strictly below -29/1000. Restriction to shorter
sides preserves these pointwise bounds. Edge length, M=n/3 and
coefficient extraction give the same C_* n^2 exp(-gamma*n) in (14).
A bound on a cancelled sum or only two endpoints is not substituted
for this argument. C663a's reverse-triangle transfer and its
coefficient-to-Mahler bound also retain their stated costs and scope.

For fixed b_*>0 the complete geometric kernel expansion is uniformly
absolutely convergent, justifying termwise integration. For all m>=2,
(12) bounds each oscillatory integral by C/sqrt(n). Their sum has
the relative geometric factor in (15), tending to zero. The other
edges relative to the lower leading scale cost at most
`C*n^(3/2)*exp(-(1351/75000)*n)`. Both errors are therefore absorbed
for all sufficiently large n. Conjugate pairing makes c_0(-1) real.
The original-bottom coefficient differs by the C663a error, proving
(2); the shifted and original bottom integrals are not equated
without paying that difference. Every kernel frequency is retained.

**All roots and paid costs.** Eventual c_0(-1)>0 makes the spatial
polynomial nonzero. The complete root formula bounds its constant
coefficient by its Mahler measure, including the leading factor,
degree drops and boundary roots. It does not replace G by a constant.
L658 applies to this integer family. The required spatial nonzero
slices follow by N<=M and Lagrange interpolation; angular slices
have distinct uncancelled exterior poles with nonzero coefficients.
The nonzero cleared numerator and bounded denominator logarithm
justify the cited integrability and every Fubini step even at torus
zeros. Localization at a maximizing angle retains normalized measure
n^(-2) and loss 32*pi^2/9. It need not be centered at u=-1.

Only L661's audited general envelope is imported; its different
half-turn census is not a premise. Original squared masses sum to
n/3 here. Substitution of the upper bound on D and lower bound on H
leaves

    2H-2log n-C-log D+n/16
       >=(1/16-2*kappa-2*rho_bar)*n-2log n-C.

The +log n from 2H cancels -log n from D, leaving the stated measure
cost. The linear coefficient is exactly 619/150000. No logarithmic
comparison of G and Bcal_n near their zeros is used. L663's
full-circle stop and C663a's endpoint-dominance stop remain valid.

**Complete arithmetic replay and limits.** Read and reran both
existing programs named in section 6 and C663a section 5. The scalar
program recomputes all 514 rational integrand values, their outward
roundings, both full integral enclosures and every scalar check.
The edge program compares all 513 four-edge rows with their prior
replay, checks the inherited complete 8192-box derivative replay
status and global bounds, and checks all three charged bounds on
all 512 intervals. Both outputs are PASS with empty failure lists.
Complete summary values and C663a's full check map were inspected
with `../scripts/loop/inspect_json.py`; the large arrays were processed
in full by the inspected programs, not inferred from a preview.
No independent interval backend or fresh replay of L661's already
audited Bernstein certificate was needed. Neither scalar program
proves the analytic signed limit; that is checked above. Source
manuscript proofs, general support, Xi realization, matching upper
bounds, signs and an effective onset remain outside this audit.

## Mathlib

Full coverage of this finite lattice, signed contour limit and rate
comparison has not been checked. The reused assessment inspected
[Mathlib.Analysis.Polynomial.MahlerMeasure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html),
including `Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`
and `Polynomial.norm_coeff_le_choose_mul_mahlerMeasure`. These support
the univariate root/coefficient comparison, not (13)--(15). No new
Mathlib lookup or absence claim is made. Nonzero-polynomial hypotheses
and the analytic interpretation of logarithms at boundary roots remain
essential.
