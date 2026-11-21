# Corollary C035b: the positive two-frequency cosine test has no exterior witness

## Hypotheses

Let a,c>0 and T>1/2 be real. Define the even real entire functions

    F(z)=cos(az)+c cos(2az),
    A(w)=sum_(n>=0) (-1)^n a^(2n)(1+4^n c) w^n/(2n)!,
    F(z)=A(z^2),                 F''(z)=B(z^2).

Primes on F are ordinary z derivatives; primes on A and B are w
derivatives. Define, as in C034z,

    theta_T=2 arctan(1/(2T)),
    K_T={w: Re(w)>=0, |Im(w)|<=tan(theta_T) Re(w)}.

The global strip premise is that every F zero satisfies |Im(z)|<1/2.
The premise RH_2^F(T) is that every F'' zero with |Re(z)|<=T is real.
The cone and height window are closed; the strip is open. All zero
statements include multiplicities.

## Conclusion

For d>0 put

    p(d)=(sqrt(1+8d^2)-1)/(4d),
    q(d)=(sqrt(1+8d^2)+1)/(4d).

For 0<d<1 put beta(d)=arcosh(q(d))>0. The two premises hold
simultaneously if and only if the applicable row below holds:

    0<c<1/4:     a>2 beta(c) and aT<pi;
    1/4<=c<1:    a>2 beta(c);
    c>=1:        no additional restriction on a,T.

Here a,c>0 and T>1/2 are retained in every row. In every admissible
case Z(A'') is contained in K_T. In fact for c>=1/4 all zeros of A''
are positive real numbers, without requiring the strip premise.
Thus this exact family cannot supply the proposed exterior-zero
witness to the inverse step of C034z. This is not a general inverse
preserver theorem and does not settle that step for actual Xi.

## Proof

### Imported tools and scope

Use NIST DLMF [4.14.2](https://dlmf.nist.gov/4.14.E2),
[4.19.2](https://dlmf.nist.gov/4.19.E2),
[4.20.1--2](https://dlmf.nist.gov/4.20),
[4.21.28](https://dlmf.nist.gov/4.21.E28),
[4.21.38](https://dlmf.nist.gov/4.21.E38) and
[4.23.24--25](https://dlmf.nist.gov/4.23) for complex cosine,
its series, differentiation, double angle and inverse values.
These identities were inspected in source-notes2184; they are
imported, not reproved. The reduction below checks the entire zero
sets, rather than retaining only a principal inverse value.

Use Young-One Kim and Jungseob Lee, *A note on the zeros of Jensen
polynomials*, [arXiv:2105.05386v1](https://arxiv.org/pdf/2105.05386v1),
12 May 2021, Theorem 4 and its complete proof p3, final remark p4.
The exact part used is: for an even transcendental real entire E of
order<2 whose nonreal zeros satisfy |Im(z)|<1/2 and |Re(z)|>=S,
S>=1/2, write E(z)=e(z^2). Every derivative of e has zeros in the
closed convex sector with angle 2 arctan(1/(2S)). This is the
forward square-transform derivative conclusion of the proof and
final remark, not an inverse Rolle assertion. The inputs below
actually have |Re(z)|>S whenever a nonreal zero occurs. No Jensen
degree claim or inverse-Euler theorem is needed here.

The ready assessment certified-test2184 permits this family-specific
specialization. C035a's polynomial obstruction does not meet these
restricted hypotheses. L530/L738 were checked as contrasts in the
assessment, not used as mathematical inputs. The calculation below
is a reproduction/specialization of inspected elementary and forward
tools; no originality or complete literature classification is claimed.

### Complete zero sets and multiplicities

For G_d(t)=cos(t)+d cos(2t), double angle gives

    G_d(t)=2d(cos(t)-p(d))(cos(t)+q(d)).             (1)

Both algebraic roots are distinct since 1+8d^2>0. Rationalizing
shows p(d)=2d/(sqrt(1+8d^2)+1), so 0<p(d)<1. Comparing q(d)
with 1 gives q(d)>1 for d<1, q(1)=1, and 0<q(d)<1 for d>1.
Indeed q(d)=1 is equivalent to sqrt(1+8d^2)=4d-1 and hence
d=1; directly the same comparison has the indicated signs on
either side (for 4d-1<=0, q(d)>1 is immediate).

Here is a full branch enumeration. For any real r, cos(t)=r is
equivalent, with v=exp(it)!=0, to v^2-2rv+1=0. For -1<r<1
the roots v are exp(+/- i arccos(r)), and all their exponential
preimages are t=2k pi +/- arccos(r), k in Z. For r=-1 the
single v=-1 gives t=(2k+1)pi. For r=-q<-1 the two distinct
values v=-exp(+/- beta), beta=arcosh(q)>0, give precisely
t=(2k+1)pi +/- i beta. These lists exhaust all branches because
the kernel of the complex exponential is 2pi i Z. They can also
be checked directly by the cited real/imaginary decomposition.

Consequently G_d has the following full zero sets:

    all d>0:    t=2k pi +/- arccos(p(d));
    0<d<1:     additionally t=(2k+1)pi +/- i beta(d);
    d=1:       additionally t=(2k+1)pi;
    d>1:       additionally t=2k pi +/- arccos(-q(d)).

All zeros are simple except the additional zeros in the d=1 row,
which are exactly double. To check this, the two factors of (1)
cannot vanish together. At a preimage of a root other than -1,
sin(t)!=0, so that factor vanishes simply. At t=(2k+1)pi,
cos(t)+1 has a double zero with nonzero quadratic coefficient,
while the other factor is nonzero. No zero occurs at t=0 since
G_d(0)=1+d>0. The k and sign repetitions in the d=1 row are
listed once; they do not introduce extra multiplicity.

Ordinary differentiation gives

    F''(z)=-a^2[cos(az)+4c cos(2az)]=-a^2 G_(4c)(az).          (2)

The substitutions t=az with a>0 and the nonzero scalar -a^2
preserve multiplicities. For c<1, all nonreal F zeros therefore
have imaginary part +/- beta(c)/a. The open strip is equivalent
to beta(c)/a<1/2; equality fails. For c>=1 all F zeros are real,
including the double zeros when c=1, so the strip is automatic.

For c<1/4, (2) has nonreal zeros with real parts (2k+1)pi/a.
The smallest absolute real part is pi/a. RH_2^F(T) is therefore
equivalent to T<pi/a. Equality fails because the height window
includes its endpoints and beta(4c)>0. For c>=1/4 all F''
zeros are real, including its double zeros when c=1/4. Thus
RH_2^F(T) is automatic. This proves the complete premise table.
There is no claim that its first row is nonempty for every fixed
c,T; it is exactly the simultaneous inequalities, with no endpoint
silently included.

### Forward control in the range 0<c<1/4

Suppose both premises hold and c<1/4. The first row gives aT<pi.
Every nonreal F zero has |Re(z)|>=pi/a>T by the full enumeration.
Every F zero also satisfies the open strip premise. F is even,
real entire, and has order at most one: for |z|<=R,

    |F(z)|<=(1+c) exp(2aR).

The entire cosine series shows that all coefficients of z^(2n)
are nonzero; thus F is transcendental. The same series defines A
entirely and gives F(z)=A(z^2), with no global square-root branch.
All Kim--Lee hypotheses for E=F and S=T are now checked. Their
forward square-transform derivative conclusion yields
Z(A'') contained in K_T. Nothing has been inferred by undoing
differentiation of F''.

### Real zeros of A' in the range c>=1/4

Here differentiation and the double-angle sine identity give

    F'(z)=-a sin(az)(1+4c cos(az)).                         (3)

Define the even entire function, with its removable value at zero,

    H(z)=(sin(az)/(az)) (1+4c cos(az))=-2A'(z^2)/a^2.

The complex zeros of sin(az) are the real points k pi/a.
Dividing by az removes precisely the simple zero at zero.
The other factor in H has zeros given by cos(az)=-1/(4c),
whose right side belongs to [-1,0). The full cosine preimage
enumeration above proves these zeros are real as well. For c>1/4
they are simple and disjoint from the sine zeros. For c=1/4 they
are double at odd multiples of pi/a, overlapping the simple sine
zeros there, so H has triple zeros at those points. Its other
nonzero sine zeros are simple. In every case H(0)=1+4c>0, and
there are no nonreal zeros or unaccounted origin zeros.

For large |z|, the exponential definitions bound H by a constant
times exp(2a|z|)/|z|; its removable value controls a neighborhood
of zero. Thus H has order at most one, is real and even, and is
transcendental. For the last assertion the series for A gives
infinitely many nonzero coefficients of A', hence of H. For
every real S>1/2, H satisfies Kim--Lee's nonreal-zero hypotheses
vacuously. Its square transform is h(w)=-2A'(w)/a^2; the imported
derivative conclusion gives

    Z(A'')=Z(h') contained in K_S, for every S>1/2.            (4)

The intersection of these cones is [0,infinity): they all have
nonnegative real part, their slopes tan(2 arctan(1/(2S))) tend
to zero as S tends to infinity, and every nonnegative real point
belongs to each cone. Applying (4) to each fixed zero therefore
places it on that ray. Moreover

    A''(0)=a^4(1+16c)/12>0,

so no such zero is zero. This proves the stronger positive-real
assertion, and hence containment in K_T for the stipulated T.
There is no interchange of a zero limit with a function limit:
(4) holds for the same entire function and each fixed zero.

### Scope and stopping consequence

Both parameter ranges cover all c>0. All global premises and
the exceptional cases c=1/4,c=1 have been included, so an exterior
disk certificate is unnecessary: no admissible exterior zero exists
in this family. For reference the ordinary/square relation remains
B=2A'+4wA'' and B'=2(3+2w d/dw)A'', but neither identity was
inverted in this proof.

The model is the cosine transform of the positive atomic measure
delta_a+c delta_(2a), with moments a^(2n)(1+4^n c). This explains
its coefficient convention, not an identification with the actual
smooth theta kernel or the actual moments in L021. The first range
was controlled because this particular family's F and F'' have the
same smallest nonreal-zero real part; the second range was controlled
by its special factorization (3). Neither feature is asserted for Xi.
The universal polynomial obstruction C035a remains valid. Actual
RH_2(T), actual inverse Euler transfer, the remaining review of C034z,
and L030/L032/C032a all-degree mixed positivity and descent remain
unresolved. This closes the approved diagnostic only.

### Independent critical audit2188 (21 November 2026)

The complete classification and both forward applications pass. This
validates the existing specialization; it supplies no stronger theorem.
The audit used the separately approved obstruction-audit2186 coverage,
reused source-notes2184, and checked Kim--Lee v1's defining strip on p2,
the complete Theorem4 proof on p3 and the square-transform remark on p4.
The relevant conclusion is in that proof/remark, not merely in the
theorem's Jensen-polynomial statement. No inverse result is imported.

For the algebraic enumeration, the two roots of 2d u^2+u-d are
p(d) and -q(d); their sum is -1/(2d) and product is -1/2.
The exponential substitution never introduces v=0, since its quadratic
has constant term one. Both exponential preimages and all integer
translates are retained. At d=1 the inverse branches coalesce at -1:
cos((2k+1)pi+u)+1=u^2/2+O(u^4), giving multiplicity exactly two.
This also verifies the otherwise simple branches and the absence of
any zero at the origin. Replacing d by 4c checks the complete F'' set.
In particular the first row requires both strict inequalities as stated;
neither the strip boundary nor the closed-height endpoints are lost.
At c=1, F has double real zeros; at c=1/4, F'' has double real zeros.
Both are permitted by the respective premises.

For the first forward application, every nonreal F zero has absolute
real part at least pi/a>T. The nonreal zeros lie strictly inside the
strip by the other premise. Its growth bound and infinitely many
nonzero even coefficients verify all remaining input hypotheses.
The square transform has order at most 1/2: for any |w|<=R choose
either square root z; then |z|<=sqrt(R) and
|A(w)|=|F(z)|<=(1+c)exp(2a sqrt(R)). This pointwise choice does
not posit a holomorphic square-root branch. Thus A is precisely the
order-below-one transform in the source, and its second derivative
is among the controlled functions.

For the second application, sin(az)/(az) extends with value one.
The extra factor has value 1+4c at zero, so no zero survives there.
At c=1/4 its double zeros at odd nonzero multiples of pi/a combine
with simple sine zeros to give exactly the stated triples. For c>1/4
the two real zero sets are disjoint. The growth bound for |z|>=1
and continuity on |z|<=1 give a global exponential-type bound for H.
Its nonzero series coefficients verify transcendence, and evenness
identifies its square transform as h=-2A'/a^2, with order at most 1/2.
No hypothesis about F's strip is needed in this application.

For a fixed zero w=x+iy of A'', (4) holds for every S>1/2 with
this same function and zero. Since the cone slope is
4S/(4S^2-1), it gives x>=0 and |y|<=4Sx/(4S^2-1) for all such S.
Letting the scalar S tend to infinity forces y=0, including when x=0.
The separately recomputed A''(0)=a^4(1+16c)/12 excludes x=0.
There is no moving-zero, function-limit, or origin-removal exception.

No defect, changed hypothesis, numerical check, or new dependency was
needed. C034z, C035a and L021 remain interface/contrast references,
not mathematical premises of this self-contained family proof. The
actual-Xi and all-degree gaps listed above remain unresolved.

## Mathlib

Full matching Mathlib coverage for this family classification and
Kim--Lee's square-transform theorem has not been checked. No absence
claim is made. This is an exact informal proof using cited primary
tools, not a numerical root experiment or a Lean verification.
