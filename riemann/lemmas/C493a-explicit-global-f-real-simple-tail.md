# C493a — Explicit global real/simple tail for the theta heat family

## Hypotheses

Let F(lambda,z) be the exact theta heat family of L058, and let H_t
have exactly the source normalization used in L488 and L493. Set

    X_0=4*pi*exp(10000),       R_0=(X_0+3)/2.

Assume lambda is real and

    1/100<=lambda<=11/200.

Use L493's audited numerical strip-tail conclusion and the de Bruijn
strip theorem in the precise cited form below. The original strip
proof and the saddle estimates imported through L493 have not been
independently audited locally. No RH, reality of all zeros, initial
simplicity or absence of finite collisions is assumed.

## Conclusion

For every complex z,

    F(lambda,z)=0 and |Re z|>=R_0
        imply Im z=0 and F_z(lambda,z)!=0.

Thus the same explicit cutoff gives a real/simple tail throughout the
closed lambda band. Both spatial edges Re z=R_0 and Re z=-R_0 and
both time endpoints are included. There is no extra strip hypothesis
on z in this conclusion.

This is a known-method specialization, not progress beyond the checked
sources or a proof of RH. Its first separate critical application audit
passed on 2026-10-30, with the source qualifications retained below.
It gives no collision exclusion inside |Re z|<R_0, no
extension below lambda=1/100, and no zero-time conclusion.

## Proof

### Precise strip input and its initial hypothesis

We import N. C. de Bruijn, *The roots of trigonometric integrals*,
Duke Math. J. **17** (1950), 197–226, Theorem 13, in the form of
D. H. J. Polymath, *Effective approximation of heat flow evolution of
the Riemann xi function, and a new upper bound for the de Bruijn–Newman
constant*, Research in the Mathematical Sciences **6** (2019), article
31, [arXiv:1904.12438v2, 4 August 2019](https://arxiv.org/html/1904.12438v2),
Theorem 3.2, p.14 ([versioned PDF](https://arxiv.org/pdf/1904.12438v2)).
For real t_0 and y_0>0, if H_(t_0)(x+iy) has no zero for any real x
and any y>y_0, then for every t>t_0 it has no zero for

    y>sqrt(max(y_0^2-2*(t-t_0),0)).

This is an imported theorem, not a reproof of the original strip
argument. Source equations (1)–(4), pp.1–2, give

    H_0(w)=xi(1/2+iw/2)/8,
    H_t(w)=integral_0^infinity exp(t*u^2)*Phi(u)*cos(w*u) du.

The paragraph following (4) gives entirety and conjugation for real t.
These are the conventions used in L488 and L493. The opening of source
Proposition 3.3, p.15, applies Theorem 3.2 to this same initial strip.

To discharge the initial hypothesis explicitly, put w=x+iy. Then
Re(1/2+iw/2)=(1-y)/2. L018 gives that xi has no zero outside
0<Re(s)<1, including the boundary. Consequently H_0 has no zero
with |y|>=1, in particular none with y>1. Theorem 3.2 therefore
applies with t_0=0 and y_0=1.

For every t>0 its upper bound sqrt(max(1-2*t,0)) is at most 1.
It follows that H_t has no zero with Im w>1. If it had a zero with
Im w<-1, conjugation at this real t would give one with Im w>1,
a contradiction. Thus every zero at every positive t satisfies

    |Im w|<=1.                                            (1)

Only this weaker closed strip is needed. We do not infer exclusion of
any boundary from an unstated strict version of the imported theorem.
No assumption that any positive-time slice is already all-real occurs.

### Exact normalization and the positive spatial edge

Reuse L488, equation (11), the exact identity

    F(lambda,z)=8*H_(4*lambda)(2*z).                       (2)

Its change of variables was justified there by K(2*u)=4*Phi(u)
in the absolutely convergent defining integral of L058. This imports
the checked normalization; it introduces no new integral interchange.

Fix an arbitrary lambda in the stated closed band and a zero z of F
with Re z>=R_0. Put t=4*lambda and w=2*z. Exactly,

    4*(1/100)=1/25,       4*(11/200)=11/50,
    1/25<=t<=11/50,       H_t(w)=0,
    Re w=2*Re z>=2*R_0=X_0+3.

Since t>0, (1) gives |Im w|<=1. These are all the zero, time, strip
and height hypotheses of L493. Its conclusion makes w real and a
simple zero of H_t. Hence z=w/2 is real. Since H_t'(w)!=0,
differentiation of the entire identity (2) in the spatial variable gives

    F_z(lambda,z)=16*H_t'(2*z)!=0.                         (3)

Thus the nonzero constant and invertible spatial substitution preserve
simplicity explicitly. At Re z=R_0 the source height is exactly X_0+3;
L493 includes this equality, so no spatial slack is needed. The two
time endpoints likewise map exactly to L493's admitted endpoints.

### Negative spatial edge and completion

Suppose instead Re z<=-R_0 and F(lambda,z)=0. By L058 the entire
function F(lambda,.) is even at this real lambda. Thus -z is a zero,
and Re(-z)>=R_0. The positive-edge argument already proved that -z
is real and F_z(lambda,-z)!=0. Therefore z is real as well.
Differentiating evenness gives

    F_z(lambda,z)=-F_z(lambda,-z)!=0.

This also covers Re z=-R_0 exactly. As R_0>0, the two cases exhaust
|Re z|>=R_0. The argument starts with an arbitrary zero and uses a
strip theorem valid for every zero, so it has no hidden restriction
to an enumerated or sampled collection. It holds pointwise for every
lambda in the closed band with the same cutoff; no parameter limit,
continuation of zero branches or additional asymptotic threshold is used.

The only new assembly is the strip/normalization application of L493.
L488's existential constant is not assigned a numerical value, and
L493's quantitative exhaustion and its source estimates are not reproved.
The cutoff can be used in a later collision reduction on this band;
it supplies no estimate or sign inside it. This completes precisely
the stated specialization.

### Separate first critical application audit, 2026-10-30

Verdict: the stated closed-band application passes without a change to
its mathematical conclusion or inputs. This audits the assembly from
the accepted conclusions, not de Bruijn's original proof or the saddle
estimates retained by L493. The prior source comparison covers exactly
this replay. No additional numerical or asymptotic input is required.

For the all-zero premise, start at an arbitrary w=x+iy, not at an
enumerated zero or a continued branch. At t=0 the affine argument of
xi has real part (1-y)/2. For y>1 it is outside the open critical
strip, so L018 and H_0(w)=xi(1/2+iw/2)/8 give H_0(w)!=0. This is
precisely the hypothesis for t_0=0,y_0=1 in the cited Polymath
Theorem 3.2; it requires neither initial simplicity nor initial RH.
For every t>0 that theorem excludes y>sqrt(max(1-2t,0)), hence
excludes y>1. Conjugation of H_t at the same real t excludes y<-1.
Thus every zero of H_t, without a spatial restriction, satisfies
|Im w|<=1. The use of a weaker closed strip makes no claim about
an unproved strict boundary case.

Now fix any lambda in [1/100,11/200] and any F zero z with
Re z>=R_0. The accepted entire identity L488(11) gives
H_(4lambda)(2z)=0. Exactly 4/100=1/25 and 4*(11/200)=11/50,
so t=4lambda belongs to L493's closed time interval and is positive.
The all-zero strip just proved applies to w=2z. Moreover
Re w>=2R_0=X_0+3. These are every zero, strip, time and spatial
hypothesis of L493; no phase-center assumption, large-height slack
or extra unspecified onset remains. In particular Re z=R_0 maps
to L493's admitted equality, and each time endpoint maps exactly.

L493 now supplies reality of this w and H_t'(w)!=0. Since z=w/2,
z is real. With lambda held fixed, the entire chain rule applied to
F(lambda,z)=8H_t(2z) gives F_z(lambda,z)=16H_t'(2z)!=0.
Both constants are nonzero, so multiplicity is preserved; simplicity
has been obtained from L493, not presumed in transferring the zero.

For any zero with Re z<=-R_0, evenness gives an F zero -z with
Re(-z)>=R_0. The preceding argument applies at the same lambda,
including equality. Thus -z is real and F_z(lambda,-z)!=0.
Differentiating F(lambda,-z)=F(lambda,z) gives
-F_z(lambda,-z)=F_z(lambda,z), proving simplicity and reality at
z as well. Since R_0>0, these two cases cover the asserted domain.

The quantifiers remain one cutoff for every lambda in the closed
band and every zero in either closed spatial tail. There is no
parameter limit, continuation of all zeros, exchange of sums or
integrals, or sampling of heights. L488(11)'s justified change of
variables is reused, not reproved. The existential constant in L488
is never assigned a numerical value. The precise original strip
and saddle imports stay as qualified in the hypotheses; their local
application is what passes here. No theta-specific estimate inside
the cutoff, finite collision exclusion, smaller-time extension,
zero-time control or all-degree positivity follows from this audit.
Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage of this explicit global-tail statement has not
been checked. No absence claim or formal verification is made. The
underlying strip theorem and explicit H_t tail are accepted with the
source/audit qualifications above. Formal support for conjugation,
evenness and the affine chain rule was not looked up in this step;
these elementary applicability steps are written out here.
