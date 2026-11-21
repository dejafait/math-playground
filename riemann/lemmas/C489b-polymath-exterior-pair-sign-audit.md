# C489b — Exterior-pair arithmetic in Polymath's barrier proof

## Hypotheses

Use the source function H_t throughout. The external inputs are D. H. J.
Polymath, *Effective approximation of heat flow evolution of the Riemann
ξ function, and a new upper bound for the de Bruijn–Newman constant*,
[arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2), 4 August 2019:
Proposition 3.1(i), equation (28), with its opposite-zero summation
convention; Theorem 3.2; and the first-contact setup of Proposition 3.3,
printed pp.15–16 ([versioned PDF](https://arxiv.org/pdf/1904.12438v2)).
No notebook normalization or other local lemma is an input.

Retain Proposition 3.3's parameters t_0,X>0, 0<y_0<=1 and all three
zero-free premises. In its nontrivial range 0<t_0<1/2, these are:

1. At time 0: 0<=u<=X, sqrt(y_0^2+2t_0)<=v<=1.
2. At time t_0: u>=X+sqrt(1-y_0^2),
   y_0<=v<=sqrt(1-2t_0).
3. At every 0<=t<=t_0: X<=u<=X+sqrt(1-y_0^2),
   sqrt(y_0^2+2(t_0-t))<=v<=sqrt(1-2t).

Each listed region contains no zero H_t(u+iv). The source's strip bound
|Im ρ|<=sqrt(max(1-2t,0)) follows from Theorem 3.2 and the unconditional
initial strip |Im ρ|<=1. Consequently the upper caps in these premises
may be removed in this range. Times t_0>=1/2 already have no positive
height zeros by that theorem; no interpretation of nonreal square-root
endpoints in the printed premises is needed for the audit.

At the source's putative first contact t_1>0, suppose the contact zero
z=x+iY is simple, where 0<x<X and
Y=sqrt(y_0^2+2(t_0-t_1))>0. Retain the first-contact consequence that
there is no zero with |Re ρ|<=X and Im ρ>Y. Zeros external to the
selected zero may be nonreal and repeated and are counted with
multiplicity. The contact necessarily has t_1<1/2 and Y<1 by the strip
bound. This is an audit of this simple-contact step, conditional on
the source setup, not a fresh proof of every case of Proposition 3.3.

## Conclusion

For a conjugate pair u±ib with b>Y, put A=(x-u)^2 and
P=(A+(Y-b)^2)(A+(Y+b)^2)>0. Its contribution to Im z'(t_1) is -2S,
where

    S = (Y-b)/(A+(Y-b)^2) + (Y+b)/(A+(Y+b)^2)
      = 2Y(A+Y^2-b^2)/P.

Thus this contribution is nonpositive exactly when b^2<=A+Y^2.
The original barrier geometry supplies that inequality. All pairs
together, including the selected zero's symmetries, give

    Im z'(t_1) <= -1/Y - Y/(x^2+Y^2) < -1/Y = Y'(t_1).

In contrast, the displayed difference in the accessible HTML and PDF
text extraction has numerator 2b(Y^2-b^2-A), so its asserted equivalence
to the geometric condition is false. The local repair is to replace
the displayed difference <=0 by the displayed sum >=0. This validates
the simple-contact mechanism under its original hypotheses; it neither
invalidates the barrier theorem nor establishes any missing barrier.

## Proof

### Source comparison and exact finite algebra

The HTML display immediately after (34), and the extracted text of
printed PDF p.16, both show a minus between the fractions and <=0.
They then state b^2<=A+Y^2 as an equivalent condition. PDF rendering
was **not** independently inspected: screenshot calls returned no
image, a direct-URL call reported screenshots disabled/non-PDF, and
terminal download failed DNS resolution. The comparison certifies
agreement of the two accessible text representations only. The
following algebra independently audits the represented argument.

Equation (28) has summand 2/(z-ρ). For ρ=u+ib its imaginary part is
-2(Y-b)/(A+(Y-b)^2); for its conjugate replace b by -b. Therefore the
two fractions must be added before multiplication by -2. Clearing
the positive common denominator gives

    (Y-b)(A+(Y+b)^2) + (Y+b)(A+(Y-b)^2)
      = 2YA + (Y-b)(Y+b)((Y+b)+(Y-b))
      = 2Y(A+Y^2-b^2).

Because Y>0, S>=0 is equivalent in both directions to b^2<=A+Y^2;
the negative prefactor -2 reverses the velocity comparison.

For the printed difference D, the same calculation gives

    P D = -2bA + (Y-b)(Y+b)((Y+b)-(Y-b))
        = 2b(Y^2-b^2-A) < 0.

Here A>=0 and b>Y>0, so D<=0 imposes no geometric restriction.
For example, A=0, Y=1/4, b=1/2 gives D=-16/3 but S=-8/3 and
b^2>A+Y^2. This is an exact arithmetic witness to non-equivalence,
not a proposed configuration of actual H_t zeros or a counterexample
to Proposition 3.3.

### The original geometry gives the repaired sign

Write w=sqrt(1-y_0^2). Consider a zero u+ib with b>Y. First contact
excludes |u|<=X; symmetry in the imaginary axis and premise (iii)
exclude X<=|u|<=X+w. The latter uses the strip bound to cover its
upper cap, and keeps the exterior multiplicity without restriction.
Hence |u|>X+w. Since 0<x<X, this implies

    |x-u|>w >= sqrt(1-Y^2),

where the last comparison uses Y>=y_0 and Y<1. Thus
A+Y^2>1. On the other hand, Theorem 3.2 gives
b^2<=1-2t_1<1. In particular b^2<A+Y^2. This proves the required
pair sign, and is a slightly stronger distance estimate than the
weakened one printed in the source. Premise (ii) is retained for
the source's final exterior coverage; it is not a payment for (iii).
Premise (i) and first-contact compactness supply the initial setup;
they are not deduced from isolation of the selected orbit.

### Regrouping and strictness

The complex velocity series in (28) uses opposite-zero grouping.
Conjugate regrouping of its imaginary part needs justification.
All zeros at t_1 have |Im ρ|<=1. For fixed z=x+iY and sufficiently
large |ρ|, the absolute imaginary part of 1/(z-ρ) is O(|ρ|^(-2)):
its numerator is bounded and its squared real separation is
comparable to |ρ|^2. The order-one zero-count estimate in source
Section 3 gives, for example, N(R)=O(R^(3/2)). On dyadic annuli
the resulting absolute sum is bounded by a constant times
sum_m 2^(-m/2)<infinity. The finite remaining terms have nonzero
denominators because the selected zero is simple. Consequently
the imaginary-part series is absolutely convergent; its sum equals
the imaginary part of the convergent opposite-grouped series, and
may be regrouped by conjugates with multiplicity.

Any remaining zero u+iv with |v|<=Y has Y-v>=0 and hence a
nonpositive vertical contribution. The selected orbit consists of
four distinct simple zeros because x,Y>0 and H_t is even and real
under conjugation. Excluding z itself, their contributions are

    ρ=x-iY:   -1/Y;
    ρ=-x+iY:   0;
    ρ=-x-iY:  -Y/(x^2+Y^2).

All other zeros with |v|>Y form conjugate pairs handled above.
Adding these terms proves the claimed strict velocity bound.
For the simple branch the derivative of Im z(t)-Y(t) at t_1 is
negative; since the difference is zero at t_1, it is positive just
before t_1, contradicting first contact. Local continuity keeps
the real coordinate in (0,X). This is exactly the simple-contact
role required by (34).

The separate repeated-contact sentence on p.15 uses y_0 where the
preceding contact is at Y(t_1), as already noted in the earlier
assessment. Its proof is not newly audited here; Proposition 3.1(ii)
remains the cited source for that separate case. No real collision
exclusion, uniform limit y_0->0, zero-time sign or arbitrary isolated
orbit estimate follows from this calculation. In particular, none
of premises (i)–(iii) has been independently certified here.

## Mathlib

Full matching coverage of the source zero-motion/barrier theorem is
not checked. The finite identities are elementary rational algebra,
and the summability argument uses a stated source zero-count bound;
no named Mathlib theorem for their full specialization was checked.
This is a reproduction and local repair of a known proof mechanism,
not a claim of new mathematics beyond the sources assessed.
