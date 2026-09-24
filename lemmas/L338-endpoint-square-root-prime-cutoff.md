# Lemma 338: endpoint scaling at a square-root prime cutoff

**Hypotheses.** Let r tend to infinity through real values and use
the endpoint weights and twisted sums of L335:

W_r(j,k)=(jk)^(−1/2)(1−log(jk)/(2r))_+^r,
J_r={j≥1: j<exp(3r/4)},
S_r[ω]=Σ_(j,k≥1)W_r(j,k)ω(j)conjugate(ω(k)),
T_r[ω]=Σ_(j,k∈J_r)W_r(j,k)ω(j)conjugate(ω(k)).

Here ω is completely multiplicative with |ω(m)|=1. Both sums are
finite and real. Put A=ζ(2)² and E_r=(1+r)²exp(−r/256).
For a fixed b>0 set y=exp(b sqrt(r)), and let Ω_(r,b) be the set
of such assignments satisfying ω(p)=−1 for every prime p≤y.
Let ω^+_(r,b) be the member that assigns +1 to every prime p>y.
For Re u>0 define the absolutely convergent integral

J_b(u)=∫_b^∞ exp(−u x) dx/x.

**Conclusion.** For every fixed b>0 there is a real constant C_b
such that

r S_r[ω^+_(r,b)]→C_b,   r T_r[ω^+_(r,b)]→C_b.        (1)

For any fixed α>0 it has the absolutely convergent representation

C_b=A sqrt(2/π)∫_ℝ exp(2(α+it)²)(α+it)²
                              ·exp(4J_b(α+it))dt.    (2)

The value does not depend on α. More strongly,

limsup_(r→∞) sup_(ω∈Ω_(r,b)) |r S_r[ω]+A/4|
 ≤A exp(2α²)(α²+1/4)[exp(4J_b(α))−1],               (3)

and the same bound holds for T_r. In particular C_b→−A/4 as
b→∞. With b=6, the right side of (3) is strictly less than A/14
when α=1/2. Consequently, for all sufficiently large r,

S_r[ω]≤−A/(8r),   T_r[ω]≤−A/(8r)
                         for every ω∈Ω_(r,6).       (4)

No numerical starting r is asserted. The margin in (4) dominates
E_r. Larger cutoffs also satisfy (4), since they constrain a subset
of Ω_(r,6). This reduces the sufficient exact prime cutoff from
log y=8 sqrt(r log r) in L336 to log y=6 sqrt(r), and allows every
unit-phase completion above y. The comparison with L336 is not a
use of its return estimate.

These are statements about phase assignments. No phase tolerance
or return time is asserted, and no value at the prescribed
a_n=sqrt(4π²exp(4r)−25), r=2n, is located. The endpoint arithmetic
margin at those pairs, low-index Laguerre signs and zero exclusion
are unchanged; this is not an RH candidate.

**Proof.** Write L=sqrt(r). We first prove the prime-tail limit
needed below from Mertens' third theorem, the named standard input
in foundations. Taking logarithms of that theorem and subtracting
the convergent prime-power sum gives

H(x):=Σ_(p≤x)1/p=log log x+B+o(1)  as x→∞.           (5)

Indeed Σ_p Σ_(m≥2)1/(m p^m) converges, by comparison with
Σ_(n≥2)1/[n(n−1)]. Thus its partial sums tend to a finite constant;
the logarithm of the asymptotic Mertens product has error o(1).
This also proves (5) for real cutoffs, using their integer parts.

For fixed u with Re u=α>0, Stieltjes integration by parts, with
H(exp(bL)) including an atom if the cutoff is a prime, gives

Σ_(p>exp(bL))p^(−1−u/L)
 =−exp(−ub)H(exp(bL))
   +(u/L)∫_(bL)^∞ exp(−u x/L)H(exp(x))dx.            (6)

The boundary term at infinity vanishes by (5). Write
H(exp(x))=log x+B+ε(x), where ε(x)→0. The log x+B terms in (6)
give exactly J_b(u). The remaining terms have modulus at most

sup_(x≥bL)|ε(x)| exp(−αb)(1+|u|/α),                 (7)

which tends to zero, uniformly when u ranges over a compact
subset of Re u>0. All integrals in (6) are absolutely convergent.
This proves

Σ_(p>y)p^(−1−u/L)→J_b(u).                            (8)

For σ=1+α/L also put

B_r=Σ_(p>y)Σ_(m≥1)p^(−mσ)/m.

The terms with m≥2 are at most
Σ_(n>y)1/[n(n−1)]=O(1/y). Therefore

B_r→J_b(α),                                         (9)

and in particular B_r stays bounded. Neither (8) nor (9) uses a
prime-number-theorem error estimate or a claim about oscillations.

For Re s>1 define the absolutely convergent series

F_ω(s)=Σ_(m≥1)ω(m)m^(−s),
F_λ(s)=ζ(2s)/ζ(s),

where λ is the Liouville assignment. The second identity, its
nonvanishing in this half-plane, and the local expansion

F_λ(1+w)=ζ(2)w+O(w²)                                (10)

on a fixed disk about w=0 are proved in L335. For ω∈Ω_(r,b),
absolute Euler products give

F_ω(s)=F_λ(s)R_ω(s),
R_ω(s)=∏_(p>y)(1+p^(−s))/(1−ω(p)p^(−s)).            (11)

Use the analytic logarithm specified by its absolutely convergent
power series. It satisfies

log R_ω(s)=Σ_(p>y)Σ_(m≥1)
              [(-1)^(m+1)+ω(p)^m]p^(−ms)/m.

For Re s=σ, the logarithm of
Q_ω(s):=R_ω(s)R_(conjugate ω)(s) has modulus at most 4B_r,
uniformly in Im s and every allowed completion. Hence

|Q_ω(s)|≤exp(4B_r),
|Q_ω(s)−1|≤exp(4B_r)−1.                             (12)

For the particular +1 completion its exact logarithm is

log Q_+(s)=4Σ_(p>y)Σ_(m≥1, m odd)p^(−ms)/m.

The contribution with m≥3 is O(1/y), uniformly on Re s≥1.
Equations (8) and (9) therefore prove

Q_+(1+u/L)→exp(4J_b(u)),                             (13)

uniformly for u on compact subsets of Re u>0. Estimates (12),
which remain valid outside these compact sets, will control the
contour tails. The product is an analytic product at one argument,
not a modulus square there.

We now establish the needed Mellin estimates on a different line
from the one used in L304. Fix α>0, put c=1/2+α/L and σ=1+α/L,
and define

K_(r,α)(v)=Γ(r+1)(2r)^(−r)exp(2r(c+iv))
                              ·(c+iv)^(−r−1)/(2π).

L298's scalar inversion and the absolute-majorant argument of L303
give, for every unit assignment,

S_r[ω]=∫_ℝ K_(r,α)(v)F_ω(σ+iv)
                              F_(conjugate ω)(σ+iv)dv. (14)

For clarity, the integral of the sum of absolute Dirichlet
integrands is bounded by ζ(σ)² times the kernel's finite absolute
integral. Thus Fubini is valid even when the assignment and line
depend on r. Inserting (11) into (14) yields F_λ²Q_ω as its
arithmetic factor. No series on Re s=1 is being summed.

Let u=α+it. Stirling's formula and the convergent logarithm
expansion at 1 give, pointwise in t,

k_r(t):=K_(r,α)(t/L)/L
 →sqrt(2/π)exp(2u²).                                 (15)

Indeed the relevant exponential is
exp(2Lu−(r+1)log(1+2u/L)), whose exponent tends to 2u²;
the remaining prefactor tends to sqrt(2/π). This convergence is
uniform for t in compact real intervals. To control its tails,
write

|K_(r,α)(v)|=P_(r,α)(1+(v/c)²)^(−(r+1)/2).

Here Stirling also gives

P_(r,α)=L/(c sqrt(2π))
 ·exp(2αL−r log(1+2α/L))(1+O(1/r))=O_α(L).          (16)

For large r, 1/2<c≤1. On |v|≤c, log(1+x²)≥x²/2 for |x|≤1
therefore bounds

|K_(r,α)(v)|≤C_α L exp(−rv²/4).                     (17)

For |v|>c, splitting off the power r/4 as in an elementary
Student-type tail estimate gives, for r≥6,

|K_(r,α)(v)|≤C_α L 2^(−r/4)(1+(v/c)²)^(−2).        (18)

Choose a fixed δ∈(0,1/4) small enough for (10) throughout
|w|≤2δ. For large r and |v|≤δ, w=α/L+iv lies in this disk, so

r |F_λ(σ+iv)|²≤C_α(α²+(Lv)²).                      (19)

Equations (17) and (19), after t=Lv, supply the integrable
majorant C_α(α²+t²)exp(−t²/4) on |t|≤δL. On |v|>δ the
Dirichlet bound |F_λ(σ+iv)|≤ζ(σ)≤1+L/α applies. Splitting the
Gaussian in (17), and using (18) for |v|>c, shows

r∫_(|v|>δ)|K_(r,α)(v)||F_λ(σ+iv)|²dv
                       =O_α(r^(5/2)exp(−κr))=o(1)  (20)

for some fixed κ>0. Enlarging the polynomial prefactor in this
bound is harmless. Equations (9) and (12) give the same vanishing
bound when an additional factor |Q_ω| or |Q_ω−1| is included,
uniformly over all completions. These estimates justify every
limit below; pointwise kernel convergence alone would not suffice.

By (10), (15), (17)–(20) and dominated convergence,

r∫_ℝ |K_(r,α)(v)||F_λ(σ+iv)|²dv
 →A sqrt(2/π) exp(2α²)∫_ℝ(α²+t²)exp(−2t²)dt
 =A exp(2α²)(α²+1/4).                               (21)

For the +1 assignment, insert (13) in (14) and use the same
majorant. This proves the first limit in (1) and formula (2).
The integral in (2) is absolutely convergent since
|J_b(α+it)|≤J_b(α). It is real by conjugation and t↔−t.
Each α gives the limit of the same sums, proving independence
of α without shifting through any pole.

For the uniform assertion, subtract (14) with ω=λ, and apply
(12) before integrating. This gives the finite-r inequality

sup_(ω∈Ω_(r,b)) |S_r[ω]−S_r[λ]|
 ≤[exp(4B_r)−1]∫_ℝ |K_(r,α)(v)||F_λ(σ+iv)|²dv.     (22)

L335 proves rS_r[λ]→−A/4. Combining that fact with (9), (21)
and (22) proves (3). The appearance of −1/4 can also be checked
directly: the Gaussian integral
sqrt(2/π)∫exp(2(α+it)²)(α+it)²dt equals −1/4.
To see this, move the vertical Gaussian line to α=0; the horizontal
ends vanish by Gaussian decay. The remaining integral is minus
the normalized second moment of exp(−2t²), which is 1/4 by
integration by parts. This is a signed moment, not a positive
averaging measure.

L303's discrete omitted-index bound uses only the nonnegative
weights, so for every unit assignment, uniformly,

|T_r[ω]−S_r[ω]|=O(r exp(−9r/128))=o(1/r).           (23)

It gives the second limit in (1) and the assertion (3) for T_r.
No control of the phases of omitted indices is needed.

Finally J_b(α)≤exp(−αb)/(αb), obtained by replacing 1/x by
1/b in its defining integral. This tends to zero as b→∞, proving
C_b→−A/4 from (3). For b=6 and α=1/2 we have

J_6(1/2)≤exp(−3)/3<1/60,
exp(2α²)(α²+1/4)=exp(1/2)/2<1,
exp(4J_6(1/2))−1<exp(1/15)−1<1/14.                 (24)

The strict inequalities use exp(3)>20, exp(1/2)<2 and
exp(x)<1/(1−x) for 0<x<1. The first follows already from the
exponential series through degree eight; the other two follow
by comparison of that series with the geometric series. Thus
the uniform limsup in (3) is less than A/14, and

1/4−1/14=5/28>1/8.

There is therefore an r_0 independent of the completion for which
(4) holds for both sums whenever r≥r_0. Since rE_r→0, the margin
is larger than the assembled endpoint error. Exact constraints on
these primes do not show that the actual phases m^(−ia_n) satisfy
them or a suitable neighborhood. No conclusion at the coupled
heights or about Laguerre signs follows. ∎

**Mathlib.** Full statement: not checked. Coverage of Mertens'
third theorem, the prime-tail limit, the moving-line Mellin limit,
and the uniform phase-completion estimate is not checked; no full
matching theorem or absence from checked sources is claimed.

Mertens' standard unconditional main term is recorded in
foundations and stated in Ross G. Pinsky, *Probabilistic Proofs of
Some Generalized Mertens' Formulas Via Generalized Dickman
Distributions* (2018), [equation (1.1), p. 2](https://arxiv.org/pdf/1809.04888#page=2).
That equation was checked as a mathematical reference. It supports
(5), not the full statement (1)–(4). The prime-tail and contour
estimates are proved above, not cited as library facts.

The supporting nonvanishing theorem inherited through L335 was
recorded as present in L001:
[`riemannZeta_ne_zero_of_one_lt_re`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#riemannZeta_ne_zero_of_one_lt_re).
That source was not rechecked; it supports the earlier quotient
identity, not the cutoff theorem. The scalar inversion and
discrete tail are supplied by L298 and L303, whose full library
coverage is not checked. `scripts/laguerre/check_endpoint_sqrt_prime_cutoff.py`
checks finite Euler-factor algebra and rational margin comparisons;
it is not a numerical certificate for these asymptotic statements.
