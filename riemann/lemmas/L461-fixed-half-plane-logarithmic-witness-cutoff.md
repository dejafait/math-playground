# Lemma 461: fixed-half-plane anchors lower the logarithmic witness cutoff

## Hypotheses

Let Ξ(z)=ξ(1/2+iz) be L018's actual completion, and write, for real a,

    H_a(y)=Ξ(a+iy)Ξ(a−iy)=Σ_(n≥0) D_n(Ξ;a)y^(2n),
    T=2+|a|.

Assume precisely the external premise retained in L452: OpenAI,
*The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8*,
September 30, 2026, Theorem 1.1, at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`, specialized to ζ.
Thus ζ has no zeros in Re(s)>7/8, with its pole at 1 allowed.
The [external-input register](../foundations/2026-10-quasi-riemann-input.md)
records the exact [pinned source](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)
and trust qualifications. Its manuscript and formal import closure
remain locally unaudited. This lemma is conditional on that cited input;
it neither proves it independently nor excludes its boundary line.

Fix 3/8<η<R<1/2 and ε>0. All logarithms are natural. Constants may
depend on these fixed parameters and the retained input, but not on a,
the displacement of a putative zero, or central zero multiplicity.

## Conclusion

There are h>0 and C≥1 such that, for every real a, with

    A(a)=h T^(7/2+η−2ε) exp(−π|a|/2),
    p=η²/R²,    λ=R−η+4ε,

one has

    H_a(η)≥A(a)>0,
    max_(|y|=R)|H_a(y)| / A(a) ≤ C T^λ.                 (1)

Every hypothetical nonreal zero a+ib of Ξ therefore forces
D_n(Ξ;a)<0 for at least one integer

    1≤n≤ceil((λ log T+log(2C/(1−p)))/(2log(R/η))).       (2)

In particular, for each fixed c>3/16 there exists B_c>0 such that
every such zero forces a negative coefficient at some index

    1≤n≤ceil(c log(2+|a|)+B_c).                         (3)

The constants are existential and not numerically evaluated. These
statements include every real center a, also when Ξ(a)=0 with arbitrary
multiplicity. No claim is made at η=3/8 or c=3/16. This is a local
REPRODUCTION of an assessed source mechanism at changed anchors; the
separate critical audit below validates this conditional specialization.
It supplies no coefficient
sign, additional zero-exclusion interval, or RH candidate.

## Proof

### Two-sided subpower estimates with fixed margins

Put σ_η=1/2+η, so 7/8<σ_η<1. We first prove that for every ε>0
there is t_ε such that

    |t|^(−ε)≤|ζ(σ+it)|≤|t|^ε
                 (σ_η≤σ≤2, |t|≥t_ε).                 (4)

This uses the Littlewood logarithm mechanism inspected in
E. C. Titchmarsh, *The Theory of the Riemann Zeta-function*, second
edition revised by D. R. Heath-Brown (1986), Theorem 14.2 and proof,
[pp. 336–337, especially (14.2.5)–(14.2.6)](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=173).
That printed theorem assumes RH and is not imported with 7/8
substituted into its hypothesis. The following changed-domain proof
is needed because neither it nor L452's narrower derivative conclusion
states (4) on the present strip.

For positive large t center disks at w_t=2+it. Choose the fixed radii

    r₀=1/2,    r₁=2−σ_η,
    r₂=(r₁+9/8)/2,    r₃=(r₂+9/8)/2.

Then 0<r₀<1<r₁<r₂<r₃<9/8. The closed r₃ disk has a slightly
larger disk neighborhood in Re(s)>7/8, missing the pole for all
sufficiently large t. The external premise makes ζ holomorphic and
nonzero there. Its analytic logarithm f_t can be normalized by
f_t(w_t)=L(w_t), where L is L005's Euler logarithm. On the r₀ disk,
Re(s)≥3/2>1. The two analytic logarithms differ by a continuous
2πi-integer-valued function, which is zero at the center; hence they
agree on this connected disk. Absolute convergence gives

    max_(|s−w_t|≤r₀)|f_t(s)|≤log ζ(3/2),
    |f_t(w_t)|≤log ζ(2).                               (5)

No Euler series is continued to the left of one.

For completeness the growth input is L320's equation (5), valid for
Re(s)>0 away from 1:

    ζ(s)=s/(s−1)−s∫_1^∞ {u}u^(−s−1)du.                (6)

Its integral is locally uniformly analytic in that half-plane,
since compact subsets have the integrable majorants
u^(−1−δ)(1+log^k u) for each differentiated order k and some δ>0.
On the r₃ disk, its real parts range over a fixed compact positive
interval and its imaginary parts are t+O(1). Consequently
|ζ(s)|≤C₁t uniformly there for all sufficiently large t. Thus
Re f_t(s)≤log(C₁t). Borel–Caratheodory, applied from radius r₃
to r₂ with the bounded normalized center value in (5), gives

    max_(|s−w_t|≤r₂)|f_t(s)|≤C₂ log t.

All radius gaps are fixed and positive. Hadamard's three-circles
theorem between r₀,r₁,r₂ therefore gives

    max_(|s−w_t|≤r₁)|f_t(s)|≤C₃(log t)^θ,
    θ=log(r₁/r₀)/log(r₂/r₀),    0<θ<1.                (7)

If the inner maximum vanishes, the identity theorem makes f_t
identically zero and the bound is immediate; otherwise the usual
logarithmic form of three-circles applies directly. Every point
σ+it with σ_η≤σ≤2 belongs to the r₁ disk. Since
|log|ζ(s)||=|Re f_t(s)|≤|f_t(s)| and
C₃(log t)^θ≤ε log t eventually, (4) follows for positive t.
Conjugation of ζ, inherited from L018's completion identity and
reality (or the defining series and continuation), gives negative t.
In particular both the upper and reciprocal estimates have been
proved; nonvanishing alone was not used as a quantitative bound.

We shall extend (4) to all heights only on the two fixed lines
σ=σ_η and σ=σ_R=1/2+R, both strictly between 7/8 and 1.
Neither line contains the pole, and the external premise excludes
zeros on both, including at bounded heights. Continuity on their
compact remaining segments therefore gives, with constants depending
on the fixed lines and ε,

    |ζ(σ_R+it)|≤C₄(2+|t|)^ε,
    |ζ(σ_η+it)|≥c₄(2+|t|)^(−ε)>0   (t∈R).            (8)

No all-height bound on a strip containing the pole is asserted.

### Whole-strip growth and the complex circle

The completed formula in L018 and uniform complex Stirling give,
on the right boundary σ_R,

    |ξ(σ_R+it)|≤C₅(2+|t|)^q exp(−π|t|/4),
    q=7/4+R/2+ε.                                      (9)

Indeed |s(s−1)|=O((2+|t|)²), the π factor has constant modulus
on a fixed real part, and
|Γ(σ_R/2+it/2)|≍|t|^(σ_R/2−1/2)exp(−π|t|/4)
at large |t|. The power is 2+σ_R/2−1/2+ε=q.
This is the complex Stirling input from
[NIST DLMF 5.11.1 and 5.11.3](https://dlmf.nist.gov/5.11),
with its closed-sector condition |arg z|≤π−δ. All gamma arguments
here have fixed positive real parts, so one common closed sector
and the uniform remainders apply at large heights. Compact heights
are absorbed by continuity of ξ. Reflection gives the same bound
on σ_−=1/2−R.

To justify propagation through the full strip, not merely its
boundaries, first apply (6) for 1/2≤σ≤σ_R and |t|≥1.
It gives |ζ(σ+it)|=O(2+|t|). The completed formula and uniform
Stirling on this compact real strip give a fixed polynomial times
exp(−π|t|/4). Reflection and entirety of ξ extend such preliminary
growth to σ_−≤σ≤σ_R and all heights. Hence the holomorphic function

    G(s)=ξ(s)exp(−iπs/4)(s+R+1)^(−q)

has at most polynomial growth throughout the closed strip and is
bounded by a constant D on both vertical boundaries. The power
uses the analytic logarithm with Re(s+R+1)≥3/2, and its modulus
is |s+R+1|^(−q). The exponential cancels the decay in (9) for
t≥0 and increases it for t<0. These observations also justify
the boundary bound on G for both signs of t.

For τ>0 apply the maximum modulus principle on the rectangles
with these vertical boundaries and horizontal sides Im(s)=±Y to
G(s)exp(τs²). The horizontal supremum tends to zero as Y tends
to infinity, by preliminary polynomial growth and exp(−τY²).
On each vertical side the modulus is at most D exp(τd), where
d=max(σ_−²,σ_R²). At each fixed point s in the strip, first letting
Y tend to infinity gives

    |G(s)|exp(τRe(s²))≤D exp(τd).

Then let τ decrease to zero. Thus |G(s)|≤D throughout the strip.
Multiplying back gives the desired upper bound for t≥0, and
conjugation of ξ gives the one for t<0:

    |ξ(σ+it)|≤C₆(2+|t|)^q exp(−π|t|/4)
                         (σ_−≤σ≤σ_R, t∈R).            (10)

This is L320's damping argument with the newly justified boundary
power; no zero-free claim is needed inside this completed-function
strip, and no interchange of its two damping limits is made.

Write y=u+iv on the complex circle |y|=R. Its two factors are exactly

    ξ(1/2−u+i(a−v)),    ξ(1/2+u+i(a+v)).

Both real parts belong to the strip of (10). Moreover
|a−v|+|a+v|≥2|a| and
2+|a±v|≤(1+R/2)T. Since q>0, multiplying (10) yields

    max_(|y|=R)|H_a(y)|
       ≤C₇ T^(7/2+R+2ε) exp(−π|a|/2).                 (11)

This controls the complete complex circle at both shifted heights,
including when a shift crosses zero.

### The anchor at all real heights

Reality and reflection give

    H_a(η)=|Ξ(a+iη)|²=|ξ(σ_η−ia)|².

On this line σ_η is strictly between 7/8 and 1. The completed
formula has nonzero factors s(s−1), π^(−s/2) and Γ(s/2), and ζ
is finite and nonzero by the retained premise. Thus H_a(η)>0
for every real a, including a=0. Stirling and the lower bound in
(8) show, for sufficiently large |a|,

    H_a(η)≥c₈ T^(7/2+η−2ε) exp(−π|a|/2).             (12)

The power follows from squaring: the polynomial contributes four,
gamma contributes σ_η−1, and ζ contributes −2ε, totaling
3+σ_η−2ε=7/2+η−2ε. The ratio of H_a(η) to the positive model
in (12) is continuous and strictly positive on the remaining compact
interval. Taking its positive minimum and the large-height lower
constant gives one h>0 valid for all real a. This proves the anchor
part of (1). Dividing (11) by this lower model gives its ratio
part with exponent R−η+4ε, increasing C to at least one.

### Witness application and parameter order

The external zero-free premise, reflection and L018's exact zero
correspondence place every zero of Ξ in |Im(z)|≤3/8. For a
nonreal zero, conjugation permits 0<b≤3/8<η<R, with the same real
center a. Apply the general comparison in L266 with F=Ξ,
anchor η, lower bound A(a), and circle majorant M=C T^λ A(a).
All its hypotheses hold by (1). Its constant coefficient is
Ξ(a)²≥0 even at a central zero, and its proof never divides by
that value or by a central derivative. Substitution into its
ceiling formula is exactly (2).

Finally fix c>3/16. First choose

    3/8<η<min(1/2,2c).

Next take R>η sufficiently close to η, still R<1/2, so that

    α₀=(R−η)/(2log(R/η))<c;

this is possible because α₀ tends to η/2<c as R decreases to η.
Then choose a fixed positive ε satisfying

    4ε<2c log(R/η)−(R−η).

The right side is positive, and now α=λ/(2log(R/η))<c.
Only after fixing η,R,ε choose the corresponding h,C, and put

    B_c=log(2C/(1−p))/(2log(R/η))>0.

Since T≥2, α log T+B_c≤c log T+B_c. Monotonicity of the
ceiling in (2) proves (3) at every real height. None of these
choices depends on b, Ξ(a), its multiplicity, or a varying height.
No uniformity as η decreases to 3/8 or c decreases to 3/16 is claimed. ∎

L322's obstruction remains valid for its exterior anchors η>1/2.
Here both the admissible zero width and the quantitative anchor
domain have changed under the external premise. The new bound
reduces the required initial sign segment from every c>1/4 in
L320 to every c>3/16, conditionally. It proves none of those signs;
the later positive partial bands do not fill the initial segment.
Bounded-height sign coverage, global mixed positivity and selected-law
realization remain separate unresolved obligations. This is local
progress using known source methods, with no originality claim.

### Critical audit — 2026-10-25

**Verdict and scope.** Equations (1)–(3) pass this mathematical audit
with the hypotheses as written. No correction to the proof, additional
hypothesis or new mathematical dependency is needed. This discharges
the local correctness-review obligation for the cutoff, rather than
establishing a result beyond the cited source methods. The external
September 30 Theorem 1.1 and its formal import closure remain locally
unaudited. The audit is conditional on precisely that pinned premise;
it supplies neither initial signs nor an RH candidate.

**Logarithm neighborhood and quantitative control.** The radius r₁
equals 3/2−η and is strictly between 1 and 9/8. Set
δ=(9/8−r₃)/2>0. The enlarged disk of radius r₃+δ is contained in
Re(s)>7/8 and, for t>r₃+δ+1, misses s=1. Thus the logarithm exists
on a simply connected open neighborhood of every closed disk actually
used. No nonvanishing at the boundary 7/8 is presumed. L005 fixes
f_t(w_t), including its imaginary part; connectedness identifies the
inner branch with the convergent Euler logarithm on Re(s)≥3/2.
In particular its modulus is bounded independently of t, not just
its real part. Equation (6), justified by L320's absolutely convergent
counting integral and analytic continuation, gives O(t) growth
uniformly on the outer disk. Its compact differentiated majorants
are integrable for each fixed derivative order. Borel–Caratheodory
therefore bounds the complete logarithm on r₂, and three-circles
gives θ<1 with fixed constants. Since (log t)^(θ−1) tends to zero,
both inequalities in (4) follow for any fixed positive ε. Conjugation
covers negative t. The bounded-height extension (8) is made only on
the two fixed nonzero, pole-free lines strictly below one; it is not
an extension across the pole in the whole strip.

**Gamma powers and strip propagation.** The vertical gamma formula
used in (9) and (12) is also stated directly in
[NIST DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9), uniformly for
bounded real parts at both signs of infinite imaginary part. Here
the gamma real parts stay in a fixed positive compact interval.
Consequently the completed boundary power is
2+(σ_R/2−1/2)+ε=7/4+R/2+ε, and the squared anchor power is
4+(σ_η−1)−2ε=7/2+η−2ε. The factor 1/2 and the fixed π powers
affect only constants. The preliminary O(2+|t|) zeta estimate is used
only for |t|≥1, where the pole cannot occur. Entirety handles the
remaining compact rectangle, and reflection covers its left half.
Thus G has the asserted polynomial growth throughout the strip
before the maximum-modulus argument is invoked. Since q is real,
the analytic power has modulus |s+R+1|^(−q), with real part of
s+R+1 at least 3/2. Its size is comparable to (2+|t|)^(−q).
The other exponential has modulus exp(πt/4); on t<0 it reinforces
the preliminary decay. Both vertical boundary bounds are valid.
For each fixed τ>0 the horizontal boundary vanishes uniformly as
Y tends to infinity. Only afterwards is τ sent to zero at a fixed
interior point. Conjugation then recovers the bound for negative t.
There is no simultaneous-limit or unbounded-interior assumption.

On |y|=R the exact two heights are a−Im(y) and a+Im(y).
Their absolute values sum to at least 2|a| and their polynomial
factors are bounded by fixed multiples of T. As q>0, multiplication
preserves the inequality also when either height crosses zero.
The resulting power is 2q=7/2+R+2ε, so division by the anchor
model leaves precisely R−η+4ε. No extra power or exponential
loss is concealed in (1).

**Compact heights and central zeros.** At s=σ_η−ia every completed
prefactor is finite and nonzero: 0<σ_η<1 excludes s=0,1, and
Re(s/2)>0 excludes gamma poles, while gamma has no zeros. The
retained premise excludes zeta zeros there, including at a=0.
The identity H_a(η)=|ξ(σ_η−ia)|² therefore gives strict positivity
at every real height. Its ratio to the positive model in (12) has
a positive minimum on the remaining closed bounded interval. This
constructs a single h>0 independently of any central value Ξ(a).
If a is a real zero of Ξ, the anchor is still nonzero because its
imaginary displacement η exceeds the allowed zero width 3/8.
This reasoning imposes no bound on central multiplicity.

**Tail contradiction and ceiling.** Reflection and L018's exact
zero correspondence give |Im(z)|≤3/8, not a strict inequality at
that boundary. Conjugation puts a hypothetical nonreal zero at
a+ib with 0<b≤3/8<η<R. Recheck L266's general comparison with
M=C T^λ A(a), p=η²/R² and q_b=b²/R². The integer K in (2)
satisfies p^K≤A(a)(1−p)/(2M) and K≥1. If its first K nonconstant
coefficients were nonnegative, d₀=Ξ(a)²≥0 would give
S_η≥A(a)/2 and S_b≥(b/η)^(2K)A(a)/2. Cauchy's bound makes
the absolute omitted tail at b, divided by this last positive
quantity, at most

    (2M/A(a)) p^K q_b/(1−q_b)
       ≤ (1−p)q_b/(1−q_b) < p < 1.

Thus H_a(b)>0 contradicts the actual zero. This argument permits
arbitrarily small b>0 and never divides by Ξ(a) or a central
derivative. L266's exterior theta-anchor specialization is not used.

For each c>3/16, the open interval for η in the proof is nonempty.
Choosing η first makes η/2<c; the fixed-radius limit then permits
R, and finally ε, with λ/(2log(R/η))<c. The construction chooses
h,C only after those parameters are fixed. Hence B_c is a single
positive finite constant for all a,b and all central multiplicities.
The inequality of the real expressions inside the ceilings uses
log T>0; monotonicity of the ceiling needs no extra rounding term.
This proves the asserted quantifiers, but gives no uniform constant
as c decreases to 3/16 or η decreases to 3/8.

**Failure comparison and documentation.** L322 fixes exterior
anchors η>1/2, so its original obstruction is preserved. The audit
does not extend that obstruction to the present anchors or infer
the endpoint c=3/16. The central-denominator failure remains avoided
through the general L266 comparison. The DAG's existing L461 row
contains exactly the inputs used: Euler normalization, completion,
general witness comparison, preliminary growth/strip method and
the retained external premise. No edge changes are necessary.
Full matching Mathlib coverage and the supporting analytic APIs
remain unchecked as specified below.

## Mathlib

Full matching coverage of the conditional cutoff, uniform strip
argument and witness application has not been checked; absence is
not asserted. L005 records the supporting
[`riemannZeta_eulerProduct_exp_log`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/EulerProduct/DirichletLSeries.html#riemannZeta_eulerProduct_exp_log).
Supporting analytic-logarithm, Borel–Caratheodory, three-circles,
maximum-modulus, gamma and coefficient-bound API names are unchecked.
The external register's pinned
`OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re` is not a claim of
Mathlib inclusion or of a local build. Standard named complex-analysis
theorems and the precise Stirling citation above are the classical
inputs; their changed-domain applications are proved here.
