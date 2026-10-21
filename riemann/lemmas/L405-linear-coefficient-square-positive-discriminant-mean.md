# Lemma 405: complete linear-coefficient-square discriminant benchmark

## Hypotheses

Use the fixed actual real functions F=F_0,G, positive gamma envelope A,
and ordinary height derivatives of L369/L370 on t>=40. Set

    T=1+t, L=log(2+t), f=F/A, g=G/A, q=(log A)'',
    X=(x,y,z)=(f,f'/L,f''/L^2), U=x^2+y^2+z^2,
    v_j=g^(j)/(T^2 L^j), j=0,1,2,
    Bcal=(2F'G'-FG''-F''G)/(A^2 T^2 L^2),
    Delta=[(2F'G'-FG''-F''G)^2
           -4(F'^2-FF'')(G'^2-GG'')]/(A^4 T^4 L^4).

Bcal denotes exactly L369's mathcal B, not an asymptotic surrogate.
Divisors are applied after ordinary differentiation. Let

    R=exp(i phi), Z=zeta(5/2+it),
    a=Re(RZ), h=Im(RZ), c=1/(4pi), ell=log H.

R is the actual gamma carrier in L390/L401. Use L401's arithmetic scalar

    B(h0,k0)=product_(p^e || h0 k0) [1+e(p-1)/(p+1)],
    gcd(h0,k0)=1, B(1,1)=1,
    Psi=sum_(m,n>=1) tau(m)tau(n)(mn)^(-5/2)
                 B(m/d,n/d)/sqrt((m/d)(n/d)), d=gcd(m,n).

L401 proves absolute convergence and Psi>=1. All constants concern this
fixed actual family; H tends to infinity through real values. There is no
RH, zero, phase independence, clipping, growing-head or favorable pencil
margin assumption.

## Conclusion

The complete sharp limit is

    lim_(H->infinity) (1/(H ell^4))
       integral_[H,2H] Delta(t) Bcal(t)^2 dt
       =233 c^4 Psi/(4989600 zeta(2))
       =233 Psi/(1277337600 pi^4 zeta(2)) > 0.       (1)

This is a local REPRODUCTION specialization of audited L401 and its
known-source tools. The separate step-102 critical audit below validates
this specialization. It evaluates the full square, not either sign-clipped
square. It gives no positive liminf for the negative-Bcal clipped mean,
regulator scale, total L367 signed margin/remainder, common-zero upper
count, global mixed positivity, extended zero-exclusion range or RH
candidate. Constants and onset are unevaluated.

## Proof

The pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-13-linear-coefficient-full-square-benchmark.md`.
The target-specific discovery and comparison are reused without another
search: the target and all fixed-jet/twist assumptions remain within its
scope. L394/L399/L400 are narrower failed weights, not inputs for (1).
The family-specific physical replacement below is necessary because
L401's weight itself has no derivative replacement.

### Exact physical weight and its absolute replacement

L369 (7), equivalently L370's common-envelope polarization, gives exactly

    Bcal=2y v_1-x v_2-z v_0-2q x v_0/L^2.          (2)

For completeness this follows by writing F=Af,G=Ag in the numerator:
after division by A^2 it is 2f'g'-fg''-f''g-2qfg.
Both first-envelope-derivative terms cancel. Equation (2) makes no
division by f,g or a Wronskian and holds at their zeros.

L390's ordinary response triple, with the complete Dirichlet series and
its first two derivatives retained, satisfies uniformly

    (v_0,v_1,v_2)=(ca,-ch/2,-ca/4)+O(1/L),
    |v_j|<=C, |a|+|h|<=C, q=O(T^(-2)).             (3)

Its errors include derivatives of the exact quadratic response factor
and of R, with all pointwise divisors taken afterwards. Define

    b=z-x/4, W=ab+hy,
    B0=-c W=c[a(x/4-z)-hy].                        (4)

Substitution into (2) and (3) gives, at every sufficiently large t,

    |Bcal-B0|<=C sqrt(U)/L,
    |Bcal|+|B0|<=C sqrt(U),
    |Bcal^2-B0^2|<=C U/L.                         (5)

Indeed the three response errors are at most
C(|x|+|y|+|z|)/L. The curvature contribution is bounded by
C|x|/(T^2 L^2), which is also at most C sqrt(U)/L.
The leading response values are bounded by the absolute right-line
series, so the second and third bounds follow. No infinite derivative
tail is truncated in this replacement.

L390, or audited L401 (4), proves the complete physical bounds

    |Delta|<=C U, (1/H) integral_[H,2H] U^2=O(ell^4). (6)

The Delta bound retains the exact common-envelope correction
4q(x v_1-y v_0)^2/L^2 from L370. Since L is comparable to ell on the
whole sharp interval, (5)–(6) yield the absolute, signed-weight-safe bound

    (1/H) integral |Delta(Bcal^2-B0^2)|=O(ell^3).   (7)

Thus the physical-weight error is o(ell^4). This uses four critical
factors and only the covered quartic norms; no sixth or higher critical
moment or unproved uniform integrability is introduced.

### Exact L401 specialization and scalar coefficient

Take the fixed vectors

    u=(-1/4,0,1), v=(0,1,0),
    theta=(-1/4,0,1,0,1,0)^T.                     (8)

Then L401's exact W_(u,v) is W in (4), so B0^2=c^2 W_(u,v)^2.
In particular the sign of B0 in (4) introduces no sign ambiguity in
this full-square specialization. L401 (1), including its already audited
physical discriminant, gives

    (1/H) integral Delta B0^2
       =(c^4 Psi/zeta(2)) (theta^T C theta) ell^4
                                           +o(ell^4). (9)

There are two separate c^2 factors: the response discriminant factor in
L401 and the factor from B0^2. It would be incorrect to retain only c^2.
Using the printed matrix of L401, all six nonzero contributions are

    theta^T C theta
      =1/71680 +19/4838400 -257/319334400
         +1/20160 +1/113400 -209/7257600
      =233/4989600 > 0.                           (10)

As a direct consistency check using L401's full quartic table, the
balanced polynomial for p=b,r=y is

    P=S b^2+T_* y^2+(b^2 y^2)/2
      =3x^4/2048+x^3 z/128+x^2 y^2/64-7x^2 z^2/64
         +3x y^2 z/8+x z^3/8-y^4/8+y^2 z^2/4+3z^4/8.

Applying its universal functional mu, in this monomial order, gives

    mu(P)=1/8192-1/30720+1/46080-1/36864-1/53760
            -61/29030400-1/53760+19/14515200+17/28385280
         =233/4989600.

These are all signed terms, not just selected positive contributions.
They agree with (10); no phase independence or replacement of an
arithmetic square by a modulus square is used.

### Imported analytic scope, endpoints and full tails

No new carrier theorem or source reproof is needed: W in (8) is precisely
a fixed vector inside the entire audited L401 family. Its complete formula
retains the balanced term and both nonzero actual-carrier projections.
Its primary inputs are cited precisely:

- C. P. Hughes and M. P. Young, *The twisted fourth moment of the Riemann
  zeta function*, J. reine angew. Math. 641 (2010), 203–236,
  [arXiv:0709.2345v2, Theorem 1.1/(16)–(17), pp. 4–5 and holomorphy remark](https://arxiv.org/pdf/0709.2345v2#page=4).
  Fixed coprime twists, shifts O(1/ell), fixed relative smooth endpoint
  widths and the complete holomorphic six-term total cover (8).
- H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function Z(t)*,
  [arXiv:2304.05178v1, Theorem 3, defining asymptotic and Proposition 3](https://arxiv.org/html/2304.05178v1).
  Only fixed ordinary jet orders zero through two and quartic norms are
  used, as already converted and audited in L390/L401.
- A. Sourmelidis, J. Steuding and A. I. Suriajaya,
  [arXiv:2007.14008v2, Section 3 between (35)–(36), both modified-Gonek branches](https://arxiv.org/html/2007.14008v2#S3),
  and J. Bourgain,
  [arXiv:1408.5794v2, Theorem 5/(0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2),
  are used only through L401's audited fixed-head signed primitives and
  connectors on its unchanged pole-free height rectangle.

The vectors in (8) are independent of H and add no critical factor,
derivative order or growing twist. Thus all hypotheses are unchanged.
L401's exact sharp formula already bounds signed omitted endpoint strips
by an absolute U^2 majorant; it does not bracket the signed polynomial
as a nonnegative integrand. For eta_N=sum_(n>N)n^(-5/2), its separate
balanced and projected full-tail errors are <=C_(u,v) eta_N ell^4,
uniformly in N. The arithmetic head scalar tends to Psi by its summable
majorant. At fixed vector, head and smoothing width, take the all-real-H
height limit, then remove width and finally head. Multiplication by the
fixed c^2 from B0^2 preserves each bound and these quantifiers. Equation
(7) applies directly to the full physical functions before any head
limit. No rate for a growing head or width is assumed.

Combining (7), (9), (10), c^4=1/(256pi^4), and Psi>=1 proves (1).
The positive full-square coefficient does not control how its signed
integral is divided between Bcal<0 and Bcal>0. The separate clipping
source blocker is unchanged; the total regulator pencil and RH remain open.

### Finite verification and qualifications

Run `python3 scripts/discriminant/check_linear_coefficient_square.py`.
It uses exact Fraction arithmetic on L401's saved matrix, independently
expands the displayed balanced polynomial, and sums all nine moment
contributions. The full certificate is
`scripts/discriminant/linear-coefficient-square-certificate.json`.
All six nonzero matrix contributions and all nine signed moment rows
were inspected, as were the zero polynomial residual and matching values.
The analytic bounds in (2)–(9) are proved above or imported from L401;
the script does not certify them.

The initial script mistakenly asserted a negative sign although the target
prescribed only evaluation. That assertion failed while both exact sums
already agreed on the positive value. The original diagnostic certificate
is preserved as `scripts/discriminant/linear-coefficient-square-initial-sign-test.json`;
the corrected script tests agreement and reports the sign without imposing
that unwarranted assertion. This was a verification-assertion error, not a
negative coefficient, analytic failure or source obstruction.

### Separate critical audit — 2026-10-13, step 102

This REPRODUCTION proof_audit uses the pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-13-linear-coefficient-square-critical-audit.md`.
The complete assertion (1) passes without a change to its hypotheses,
coefficient or direct mathematical inputs. The source theorems cited above
are imported through the already audited L390/L401 applications. This is
verification of a local specialization, not a new source theorem or RH
candidate. The following checks concern the full physical statistic.

**Ordinary jets and the weighted error.** Put alpha=A'/A. Directly,
F'/A=f'+alpha f and F''/A=f''+2alpha f'+(alpha^2+q)f;
the same holds for g. Substitution in the physical polarization cancels
every alpha term and leaves 2f'g'-fg''-f''g-2qfg. Dividing afterwards
by T^2 L^2 gives (2), including its minus curvature sign. In contrast,
the discriminant's envelope correction has the plus sign
4q(xv_1-yv_0)^2/L^2. These are different identities, both retained.

The exact response factor used in L390 is
(t^2/4-3/16-it/2)/pi. Its first two derivatives and the complete
right-line Z derivatives are included in L390's displayed product rules.
With phi'/L=1/2+O(1/L), phi''=O(1/t), these give precisely
(ca,-ch/2,-ca/4)+O(1/L), uniformly before any truncation. Inserting
this triple into (2) yields c(ax/4-hy-az)=-c(ab+hy).
The three response errors contribute C(|x|+|y|+|z|)/L and the remaining
curvature contributes C|x|/(T^2 L^2). Thus (5) holds even at vanishing
jets. In particular no relative bound against Bcal or B0 is used.

The complete discriminant satisfies |Delta|<=CU by L390's quadratic
minor identity with a bounded response triple and bounded q/L^2.
Consequently the absolute integrand error is <=CU^2/L. The imported
ordinary fourth moments of f,f'/L,f''/L^2 give integral U^2=O(H ell^4),
so its integral is O(H ell^3)=o(H ell^4). This is a quartic estimate;
there is no hidden sixth moment, sign restriction, or small-denominator
exception. The physical replacement holds for the full response itself.

**Independent carrier-polynomial and scalar checks.** To check the
balanced polynomial directly from physical minors, write
A_0=(z+x/4)^2-y^2 and b=z-x/4. The leading discriminant is

    d/c^2=A_0 a^2+2by ah+xz h^2,
    W^2=b^2 a^2+2by ah+y^2 h^2.

For the exact finite harmonic expansion with a+ih=RZ, the constant
harmonics of a^4,h^4,a^2h^2 are respectively
3|Z|^4/8,3|Z|^4/8,|Z|^4/8; a^3h and ah^3 have zero constant
harmonic. This is a polynomial identity in R, not averaging an
independent random phase. The constant coefficient of their product is

    [3A_0 b^2+A_0 y^2+4b^2 y^2+xz b^2+3xz y^2]/8
      =S b^2+T_* y^2+b^2 y^2/2.

This reproduces every monomial of the displayed P. The nonconstant
harmonics remain present and are controlled by L401, not discarded by
this coefficient extraction. All nine signed moment values were checked
against L401's complete table. The six nonzero matrix contributions
correspond exactly to (00),(02),(04),(22),(24),(44); off-diagonal entries
are multiplied by two. Their full sum and the nine-term polynomial sum
both equal 233/4989600. Finally B0^2=c^2 W^2 supplies a second c^2
beyond L401's discriminant factor. Since 4989600*256=1277337600,
both forms of the coefficient in (1) agree.

**Sharp endpoints, arithmetic and quantifiers.** The vector in (8) is
fixed, so it lies literally in L401's audited family. Its two nonzero
carrier integrals at each fixed head have sharp bounds O_N(H ell^3)
and O_N(H), with O_N(H^(2/3)) connectors. These are o(H ell^4).
For the balanced polynomial, |P||Z_N|^4<=CU^2. L401's nonnegative
endpoint majorant b_delta and untwisted fourth-moment formula give
limsup integral b_delta U^2/(H ell^4)<=C delta, with C independent
of N and delta. The source error may depend on delta, which is fixed
until after the height limit; a whole-dyadic norm alone is not used to
assert this endpoint control.

Telescoping the four bounded response values bounds each harmonic's
full-minus-head integrand by C eta_N U^2, independently of N. These are
value tails only; the full response derivatives already occur in the
physical replacement above. Every arithmetic summand is bounded by
16(mn)^(-3/2), including all product and reduced-ratio collisions.
Thus Psi_N tends to finite Psi>=1. With kappa=233/4989600, the normalized
mean I_H in (1), after the fixed-head height limit and width removal,
satisfies for every fixed N

    limsup_(H->infinity) |I_H-c^4 kappa Psi/zeta(2)|
      <=C eta_N+c^4 |kappa| |Psi_N-Psi|/zeta(2).

The physical error has already vanished here. The right side tends to
zero. Equivalently, choose N for a prescribed tolerance, then a fixed
small width, and finally sufficiently large real H. Neither N nor the
width is allowed to depend on H inside a source asymptotic. This verifies
the complete sequential limit, not merely a subsequence or growing-head
heuristic.

**Finite evidence and limitations.** The exact-arithmetic verifier was
read and rerun successfully. The full six matrix and nine moment rows,
empty polynomial residual and both exact rational totals were inspected
with the scoped JSON inspector. Its arithmetic agrees with the direct
checks above; its printed analytic error is a reference to this proof,
not a computational certificate for an asymptotic. The preserved initial
diagnostic has the same two positive totals and only the unwarranted
`strict_negative_coefficient` assertion fails. No evidence is discarded.

This validates the unclipped benchmark only. A positive sum of the two
sign-restricted signed integrals does not determine either summand.
Sign imbalance, regulator scale, the total L367 margin/remainder and
actual common-zero upper counts remain independent unresolved issues.

## Mathlib

Full matching coverage for (1), the shifted twisted fourth moment,
ordinary Hardy quartic jets and signed primitives is not checked.
Supporting finite polynomial algebra and real inequalities alone do not
formalize the imported analytic inputs. No Lean verification, library
absence, originality beyond sources checked or RH resolution is claimed.
