# Lemma 396: sharp fixed-head mollified carrier diagonal

## Hypotheses

Use L390's actual ordinary jets x=f, y=f'/L, z=f''/L^2,
K=((z-x/4)-iy)^2/2, E=R^2, L(t)=log(2+t), and L395's
mollifier P_H. Fix a positive integer N before H tends to infinity.
Write ell=log H, Y=H^(1/100), and

    p_H(a)=(log(Y/a)/log Y)^2       (1<=a<=Y),
    q_H(m)=(1-log(m)/ell)^2        (m>=1),
    Z_N(t)=sum_(r<=N) r^(-5/2-it).

All indices in sums are positive integers; the real cutoff Y is not
differentiated. No RH, zero simplicity, disjointness, sign, phase
independence, or growing-N hypothesis is imposed.

## Conclusion

Define the finite real arithmetic expression

    Q_N(H)=(1/2) sum_(r,s<=N; a,b<=Y; m,n>=1; mn b=rs a)
       mu(a)mu(b) p_H(a)p_H(b) q_H(m)q_H(n)
                /[(rs)^(5/2) sqrt(abmn)].                    (1)

Every collision is retained, without requiring coprimality or discarding
multiple representations of the same rational number. The constraint
implies mn<=N^2 Y, so (1) is finite. For each fixed N,

    H^(-1) integral_[H,2H] Re(K E Z_N^2)|P_H|^2
      = Q_N(H)
        + O_N(ell^(-1) + H^(-1)Y^(41/20)
                           + H^(-2/3)Y^(31/20))
      = Q_N(H)+o(1).                                      (2)

The power exponents after substituting Y are -1959/2000 and
-3907/6000, respectively, both strictly negative. Both endpoints are
sharp. No limit, value, positivity or negligibility of Q_N(H) is asserted.
The balanced mean and complete signed discriminant mean are not evaluated.
The separate step 66 critical audit below validates this local reproduction.
It gives no global sign, common-zero bound, extended zero-exclusion range
or RH result.

## Proof

The unchanged prior SPECIALIZE assessment is
`drafts/literature/2026-10-11-mollified-carrier-diagonal.md`.
We use its height-contour option. The application differs from the earlier
fixed-twist estimates by the growing square mollifier support and the
constant error scale. The uniform bounds below address those differences;
no fixed-twist implied constant is extended to growing twists.

The known analytic input for connectors is J. Bourgain, *Decoupling,
exponential sums and the Riemann zeta function*,
[arXiv:1408.5794v2, Theorem 5 (0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2).
Its unconditional exponent 13/84+epsilon, with epsilon=1/168, is less
than 1/6. L391's section on sharp connectors specializes this via the
standard strip Phragmen–Lindelof principle and Cauchy's estimate to
ordinary orders at most two. We reuse that bound, not its fixed-twist
signed mean theorem. The weighted jet bounds are the audited L395,
in particular its proof (4), importing Bui–Hall,
[arXiv:2304.05178v1, Proposition 1 and Section 3 (6)–(8)](https://arxiv.org/html/2304.05178v1#S3)
with exponent 1/100 and polynomial u^2. No reproof of either theorem is
needed. Bui–Conrey–Young Lemma 4.1, covered by the assessment, is an
alternative approximation tool and is not used in this proof; its
different cross-mollifier coefficient theorem is not imported.

### Exact ordinary-jet cancellation and weighted freezing

Use complex height tau and put B(tau)=zeta(1/2-i tau),
h_j(tau)=zeta^(j)(1/2-i tau), with complex s derivatives on the right.
On the rectangle H<=Re tau<=2H, 0<=Im tau<=delta=11/20,
the holomorphic reflected identity of L390 is f=-R^(-1)B.
The phase derivative is the exact holomorphic function

    Omega(tau)=[Psi(1/4+i tau/2)+Psi(1/4-i tau/2)-2 log pi]/4,
    R'/R=i Omega, L(tau)=Log(2+tau).

Here and below primes on functions of tau are ordinary height
derivatives. L381 Section 4 gives holomorphy: the possible zeta and
polygamma poles have Re tau=0, and the logarithm and denominators are
regular on a neighborhood of the rectangle. L391's controlled
polygamma formulas, reflected to this rectangle, give
Omega=O(ell), Omega'=O(H^(-1)). On its real bottom edge,
Omega/L=1/2+O(ell^(-1)) and L/ell=1+O(ell^(-1)).

Differentiating before dividing by L or L^2 gives exactly

    f'=-R^(-1)(B'-i Omega B),
    f''=-R^(-1)(B''-2i Omega B'+(-i Omega'-Omega^2)B).

Since B'=-i h_1 and B''=-h_2, substitution into z-x/4-iy yields

    z-x/4-iy=R^(-1) A_H,
    A_H=h_2/L^2+(2 Omega/L^2+1/L)h_1
                      +[(Omega/L+1/2)^2+i Omega'/L^2]h_0,
    K E=A_H^2/2.                                         (3)

In particular the Omega' term and all ordinary derivative signs remain
in this identity. It holds at zeros too. Neither P_H nor a divisor has
been differentiated as part of a physical jet.

Now freeze only the bounded coefficients, setting

    C_H=h_0+2h_1/ell+h_2/ell^2,
    S_H(t)=sum_(j=0)^2 |h_j(t)|/ell^j.

On [H,2H], the separate estimates above imply

    |A_H-C_H| <= C ell^(-1) S_H,
    |A_H|+|C_H| <= C S_H.                              (4)

By zeta conjugation, L395's proof (4) applies equally to h_j at negative
height. The elementary square-of-a-sum inequality therefore gives

    H^(-1) integral_[H,2H] S_H^2 |P_H|^2 = O(1).

Also |Z_N|<=zeta(5/2), uniformly in N. Factoring A_H^2-C_H^2 and
using (4) proves that the left side of (2) differs by O(ell^(-1))
from

    (1/(2H)) Re integral_[H,2H] C_H(t)^2 Z_N(t)^2 |P_H(t)|^2.
                                                               (5)

Thus the freezing error is controlled in the actual growing weight;
no unweighted error estimate or differentiated asymptotic is substituted.

### Holomorphic finite weight and both sharp connectors

For this fixed H define the holomorphic function

    W_H(tau)=sum_(a,b<=Y) mu(a)mu(b)p_H(a)p_H(b)
                                  (ab)^(-1/2)(b/a)^(i tau).

It equals |P_H|^2 on the real axis. It is a product of two finite
holomorphic sums, not the nonholomorphic expression |P_H(tau)|^2.
Let F_H=C_H^2 Z_N^2 W_H, holomorphic on the same rectangle.
The cutoffs and ell are constants during the height-contour shift.

For tau=u+iv on either vertical edge, 0<=v<=delta, L391's
subconvex/interpolation/Cauchy estimate, with conjugate height, gives

    |h_j(tau)|/ell^j <= C_j H^((5/18)(3/5-v)),   j<=2.   (6)

Indeed the real part is sigma=1/2+v in [1/2,21/20]; interpolate
between 1/2 and 11/10, and use disks of radius 1/ell. Their small
excursions left of 1/2 are covered by the functional equation, exactly
as in L391. Thus the disk loss is bounded independently of H. At all
these v, |C_H|^2<=C H^(1/3), a deliberately coarse uniform bound.
The fixed head has |Z_N|<=C_N. Since |mu|,p_H<=1,

    |W_H(u+iv)|
      <= (sum_(a<=Y) a^(-1/2+v))(sum_(b<=Y) b^(-1/2-v))
      <= C Y^(1+v) <= C Y^(31/20).                    (7)

The first sum is at most C Y^(1/2+v), uniformly on this compact
v interval, and the second is at most 2 sqrt(Y). Each connector has
length delta, so its integral is O_N(H^(1/3)Y^(31/20)). Cauchy's
theorem with both endpoints retained consequently gives

    integral_H^(2H) F_H(t) dt
      = integral_H^(2H) F_H(u+i delta) du
                   + O_N(H^(1/3)Y^(31/20)).            (8)

There are no residues or endpoint averaging assumptions. The error is
an absolute bound on both signed connector integrals.

### Complete collision sum and uniform off-diagonal error

On the top edge sigma=1/2+delta=21/20>1. Absolute convergence of
the zeta derivative series gives

    C_H(tau)=sum_(m>=1) q_H(m)m^(-1/2+i tau).

Thus each term of F_H on that edge is

    A_(r,s,a,b,m,n) exp(i tau lambda),
    A=mu(a)mu(b)p_H(a)p_H(b)q_H(m)q_H(n)
                                  /[(rs)^(5/2)sqrt(abmn)],
    lambda=log(mn b/(rs a)).                            (9)

For ell>=1, |q_H(m)|<=(1+log m)^2. Hence the entire absolute
coefficient mass on the top, including every m,n and twist, is bounded
by

    sum |A| exp(-delta lambda)
      <= C_N (sum_(a<=Y) a^(-1/2+delta))
             (sum_(b<=Y) b^(-1/2-delta))
             [sum_(m>=1) (1+log m)^2 m^(-21/20)]^2
      <= C_N Y^(21/20).                                (10)

The b sum is bounded by zeta(21/20). All constants are independent
of H. This proves absolute uniform convergence on the top edge and
justifies its termwise integration; no long series on the critical
line is being summed absolutely.

For nonzero lambda, put A_int=mn b and B_int=rs a<=N^2 Y.
If their ratio is outside [1/2,2], then |lambda|>=log 2.
Otherwise integrality and the mean value theorem for log give

    |lambda| >= |A_int-B_int|/max(A_int,B_int)
              >= 1/(2N^2 Y).

Consequently |lambda|^(-1)<=C_N Y for every off-diagonal term,
uniformly over the unbounded m,n support. The exact primitive on the
sharp interval satisfies

    |integral_H^(2H) exp(iu lambda) du| <= 2/|lambda|.

Together with (10) this bounds the entire off-diagonal top integral
by O_N(Y^(41/20)). This bound is summed over the growing support,
rather than asserting uniformity of a fixed-twist theorem.

The zero-frequency terms in (9) are exactly mn b=rs a. On them
exp(-delta lambda)=1, so their top integral is exactly H times
the finite coefficient sum 2Q_N(H). All coefficients in that sum
are real. Thus (8) proves (5) equals

    Q_N(H)+O_N(H^(-1)Y^(41/20)+H^(-2/3)Y^(31/20)).

Adding the independently bounded freezing error proves (2).
The three errors tend to zero with N fixed. In particular no
positivity argument is used to remove signed endpoints, no rational
collision is lost, and the physical carrier has not been discarded.
Its unevaluated signed diagonal remains in full. L395 permits a later
response-tail comparison, but that comparison alone would not evaluate
this diagonal or the independent balanced term.

### Separate critical audit — 2026-10-11, step 66

The prior SPECIALIZE assessment
`drafts/literature/2026-10-11-mollified-carrier-diagonal-audit.md`
authorizes this REPRODUCTION audit. The fixed-N conclusion (2) passes
with its existing hypotheses and errors. We import only the Bourgain
and Bui–Hall statements cited above, through the audited applications
in L391 and L395; no growing-twist version of a fixed-twist theorem is
being inferred. This is verification of a local specialization, not a
new analytic source result or an evaluation of Q_N(H).

**Ordinary derivatives and carrier.** Set V=R^(-1), so V'=-i Omega V.
Since f=-VB, direct product differentiation gives

    f'=V(i Omega B-B'),
    f''=V[(Omega^2+i Omega')B+2i Omega B'-B''].

Substitute B'=-i h_1 and B''=-h_2. The three contributions to
z-x/4-iy are respectively

    V[h_2+2 Omega h_1+(Omega^2+i Omega')h_0]/L^2,
    V h_0/4,
    V(h_1+Omega h_0)/L.

Their sum is exactly V A_H in (3), including the positive sign of
both the h_1/L term and i Omega'/L^2. As E=R^2 and K is half the
ordinary square, K E=A_H^2/2 without conjugation or a modulus square.
No derivative of L, P_H or Y is taken. The holomorphic reflection
identity holds on a neighborhood of the rectangle, by L390; its root
R is nonzero there. In particular this computation does not divide by
f, B or a jet and remains valid at their zeros.

**Actual weighted freezing.** On the real interval, the coefficients
of h_j/ell^j in A_H are

    a_2=(ell/L)^2,
    a_1=(ell/L)(2 Omega/L+1),
    a_0=(Omega/L+1/2)^2+i Omega'/L^2.

The separate carrier bounds give a_2=1+O(1/ell),
a_1=2+O(1/ell), a_0=1+O(1/ell), uniformly on [H,2H]. Hence
(4) holds pointwise. Complex conjugation gives
|h_j(t)|=|zeta^(j)(1/2+it)| at this same t; it does not change the
weight or require a moment theorem at a different weight. L395 (4)
and S_H^2<=3 sum_(j=0)^2 |h_j/ell^j|^2 therefore give its claimed
O(1) weighted mean. With |Z_N|<=zeta(5/2), the absolute weighted
mean of (A_H^2-C_H^2)Z_N^2 is O(1/ell), uniformly in N. This
justifies (5) even though these complex squares need not be positive.

**Holomorphy and two endpoints.** On the real line the product of
P_H(t) with its conjugate is exactly W_H(t), with frequency log(b/a).
For complex height it is the finite product in the proof, not a
complex modulus. All other factors of F_H are holomorphic on a
neighborhood of the rectangle; zeta's pole has real height zero.
At tau=u+iv, the reflected zeta argument has real part 1/2+v and
imaginary part -u. Conjugation permits precisely L391's interpolated
bound at this negative height. Its Cauchy disks of radius 1/ell have
real parts at most 21/20+1/ell<11/10 for large H. Left excursions
below 1/2 are covered by its functional-equation estimate, with only
H^(O(1/ell)) loss. The same estimates hold at u=H and u=2H,
including the disks' height excursions. This proves (6) for every
j<=2, without logarithmic losses after division by ell^j.

Uniformly for 0<=v<=11/20, the first sum in (7) is
O(Y^(1/2+v)) and the second is at most 2 sqrt(Y). Thus W_H is
O(Y^(31/20)), while C_H^2 is O(H^(1/3)). The finite Z_N is
bounded by an N-dependent constant on the entire rectangle.
The two connectors each have length 11/20 and the same absolute
bound O_N(H^(1/3)Y^(31/20)); retaining both gives (8), with no
assumption about their signs and no smoothing of the endpoints.

**Complete top sum.** At sigma=21/20 the differentiated Dirichlet
series converges absolutely; its coefficient is
1-2 log(m)/ell+log(m)^2/ell^2=q_H(m). For ell>=1 the majorant
(1+log m)^2 m^(-21/20) is summable. The top-edge mass factors as
in (10): the a sum costs O(Y^(21/20)), the b sum is bounded,
and the fixed r,s factors cost only C_N. These bounds give uniform
absolute convergence in u on the whole top interval, justifying
both products of infinite series and termwise integration.

For a nonzero frequency, A_int=mn b and B_int=rs a are distinct
positive integers and B_int<=N^2Y. If 1/2<=A_int/B_int<=2,
then |log(A_int/B_int)|>=1/(2N^2Y). Outside this interval it is
at least log 2. Consequently the reciprocal-frequency bound is
uniform even when m,n are unbounded. The complete off-diagonal
integral is at most C_N Y times the top absolute mass, giving
O_N(Y^(41/20)). There is no unsupported separation bound for an
unbounded denominator: the bounded integer here is specifically rs a.

Zero frequency means precisely mn b=rs a. Its vertical multiplier
is one, its sharp integral is H, and mn<=N^2Y makes this sub-sum
finite. Expanding the products has already included every ordered
representation of r,s,a,b,m,n. Grouping or restricting to reduced
fractions is unnecessary and would risk losing multiplicity. The
factor 1/2 in (5) is exactly the factor in (1); real coefficients
justify taking the real part without changing this diagonal.

After division by H, the errors are exactly O(ell^(-1)),
O_N(H^(-1959/2000)) and O_N(H^(-3907/6000)). All tend to zero
with N fixed. No uniformity as N grows, limiting coefficient, sign
of the finite sum, or balanced-term evaluation follows. Those are
separate obligations before a complete signed physical mean can be
used. L395's tail estimate remains available but cannot replace them.

## Mathlib

Full matching coverage of this mollified ordinary-jet contour reduction
has not been checked. No Lean verification or library absence is claimed.
Supporting ingredients are standard complex differentiation, Cauchy's
theorem and estimate, absolute convergence, and integral inequalities;
they do not replace the cited analytic bounds. This is a local
known-tool specialization, not a claim of a new source theorem or a
solution of RH. The separate step 66 audit validates (2) at fixed N;
it supplies no formal Mathlib verification.
