# Corollary 969a: the one-coordinate marginal has a negative diagonal tail

## Hypotheses

Use the actual positive theta function A of L019 and H_r of L966.
Fix only n=2 and L969's prescribed parameters and normalization:

    b=1/4, h=5184, q=72, Delta=h-b=20735/4,
    a_r=integral_0^infinity A(w)H_r(b,w)dw,
    c_r=integral_0^infinity A(w)H_r(h,w)dw       (r=0,1),
    gamma=1/[2(c_0+c_1)],
    d_1=4h^2/Delta^2, d_2=h/Delta.

Keep all the factors of L969(5), with no further boundary replacement:

    B_0=gamma[H_0(h,.)+H_1(h,.)],
    B_1=2H_0(b,.), B_2=4H_1(b,.),
    C_0=B_0+2Delta H_0(h,.),
    C_1=2H_0(h,.)+2Delta H_1(h,.),
    Psi_tilde_2=d_1 Sym_3(B_1,B_0,C_0)
                 +d_2 Sym_3(B_2,B_0,C_0)
                 -d_2 Sym_3(B_1,B_1,C_0)
                 -d_1 Sym_3(B_0,B_0,C_1).

Sym_m is the average over all m! labeled permutations, including
repeated factors. Define the exact marginal

    J_2(u,v)=integral_0^infinity A(w)Psi_tilde_2(u,v,w)dw.

No RH, simplicity, positive Stieltjes representation, numerical moment
or normalization bound, or sign of the integrated numerator is assumed.

## Conclusion

Every fixed slice defining J_2 is absolutely integrable. The marginal
is continuous on the positive quadrant and has the complete formula
(2) below. For E(t)=t exp(qt),

    lim_(t->infinity) J_2(t,t)/E(t)^2
      = h gamma^2/(12Delta^2)
          [2a_0+(Delta/h)a_1-(2+4Delta)c_0-6Delta c_1]
      <= -h gamma^2/(12Delta)
          [4c_0+(6-1/h)c_1] < 0.                            (1)

Thus J_2(t,t)<0 for all sufficiently large t, and J_2 is negative
on a nonempty open subset of (0,infinity)^2 with positive A-product
measure. This disproves global pointwise nonnegativity of this fixed
marginal. It does not sign its double integral, which is still exactly
L969's M_2=Q_eta(2)I_0(b)^2 I_0(h). All-index L966(16), actual-Xi
mixed positivity and RH remain open. This is a local obstruction,
written in step180 and independently audited in step182 on
10 November 2026. No statement or formula correction was required.

## Proof

### Exact contraction of the complete kernel

L019 and the hyperbolic formulas for H_0,H_1 first give
0<a_r,c_r<infinity for r=0,1: the integrands are positive for w>0
and bounded by a polynomial times exp((q+9/2)w-pi exp(2w)).
Hence 0<gamma<infinity. The same formulas now bound A(w) times
each of B_0,B_1,B_2,C_0,C_1 in absolute value by

    C(1+w^2) exp((q+9/2)w-pi exp(2w)),

for a finite C depending only on the fixed parameters and gamma.
This is bounded near zero and integrable at infinity. For any fixed
u,v, each summand of the slice integral is one such integrable factor
in w times finite factors evaluated at u,v. This proves absolute
integrability for every slice, not merely almost everywhere.

Set S(f,g)(u,v)=[f(u)g(v)+g(u)f(v)]/2 and write the exact moments as

    m_0=integral A B_0=1/2,
    m_1=integral A B_1=2a_0,
    m_2=integral A B_2=4a_1,
    v_0=integral A C_0=1/2+2Delta c_0,
    v_1=integral A C_1=2c_0+2Delta c_1.

These follow directly from the displayed factors and the actual
normalization. The h-origin contribution remains in v_0, and both
parts of the h derivative remain in v_1.

For any three labeled integrable factors f,g,k, collecting the two
permutations with each chosen factor in the w coordinate gives

    3 integral A(w) Sym_3(f,g,k)(u,v,w)dw
      =(integral A f) S(g,k)+(integral A g) S(f,k)
         +(integral A k) S(f,g).

The identity retains repeated contributions when two labels denote
the same function. Apply it separately to all four signed tensors:

    3J_2=(d_1 m_1+d_2 m_2) S(B_0,C_0)
           +(d_1 m_0-2d_2 m_1) S(B_1,C_0)
           +d_2 m_0 S(B_2,C_0)
           +d_1 v_0 S(B_1,B_0)+d_2 v_0 S(B_2,B_0)
           -d_2 v_0 B_1(u)B_1(v)
           -2d_1 m_0 S(B_0,C_1)-d_1 v_1 B_0(u)B_0(v).     (2)

In particular both distinct contractions of the even-block subtraction and
all three labeled contractions of the distant subtraction are present.
Equation (2), a finite sum of products of continuous functions, proves
continuity. The same factor bounds give absolute integrability of the
full three-variable kernel and of A(u)A(v)J_2(u,v). Fubini's theorem
for absolutely integrable functions, applied to the finite measures
A(u)du, therefore gives the asserted double-integral identity from
L969(3). This reuses the assessed integration theorem; it imports no
positivity theorem and performs no new boundary transfer.

### The complete diagonal limit and actual moment comparison

Use the fixed-parameter limits already proved in L969(7)-(8):

    B_0(t)/E(t) -> g=gamma/(4q),
    C_0(t)/E(t) -> g,
    C_1(t)/E(t) -> k=Delta/(2q),
    B_1(t)/E(t) ->0, B_2(t)/E(t) ->0.                       (3)

Here g>0 and every displayed ratio has a finite limit. On the diagonal
S(f,k)(t,t)=f(t)k(t). Consequently (2) gives, keeping all terms,

    L:=lim J_2(t,t)/E(t)^2
      =(1/3)[(d_1 m_1+d_2 m_2-d_1 v_1)g^2
                   -2d_1 m_0 gk]
      =(d_1 g^2/3)[2a_0+(Delta/h)a_1-v_1-2Delta/gamma].     (4)

The even-block terms have zero limit because at least one B_1
remains after integration. They were not discarded from (2) or from
the integral. The same reasoning explains the zero limits of all
other terms containing B_1 or B_2. All limits here are of a finite
formula after exact integration; no limit is passed through an
improper integral.

In the second line of (4) use m_0=1/2, d_2/d_1=Delta/(4h),
and k/g=2Delta/gamma. Now use the exact relation
1/gamma=2(c_0+c_1) and v_1=2c_0+2Delta c_1. The bracket in (4)
becomes the bracket in (1). Since q^2=h,
d_1 g^2/3=h gamma^2/(12Delta^2), proving the equality in (1).

It remains to justify its sign with the actual moments. The series
in L966(3) has nonnegative coefficients in x, and h>b>0. For r=0,1
and every w>=0 it therefore gives H_r(h,w)>=H_r(b,w). Both functions
are strictly positive for w>0. Multiplying by A(w)>0 and integrating
the convergent expressions proves

    c_0>=a_0>0, c_1>=a_1>0.                                 (5)

No estimate of their numerical values is used. If B denotes the
bracket in (1), the exact difference identity is

    [-4Delta c_0-Delta(6-1/h)c_1]-B
        =2(c_0-a_0)+(Delta/h)(c_1-a_1)>=0.                   (6)

The right side is nonnegative by (5). The proposed upper bound is
strictly negative, because Delta=20735/4>0,
6-1/h=31103/5184>0, and c_0,c_1>0. Multiplying by the positive
prefactor in (1) proves its full strict inequality.

The finite negative limit supplies a finite T, possibly dependent
on the actual moments, such that J_2(t,t)<0 for every t>T. Choose
t>max(T,0). Continuity gives an open box about (t,t), contained in
the positive quadrant, on which J_2 is negative. On a smaller closed
box A(u)A(v) has a positive lower bound. Thus this negative region
has positive A-product measure. There is no claim about its mass
relative to the complementary region or the sign of the full integral.

### Exact finite check and scope

Run `python3 scripts/li-theta/one-coordinate-marginal-check-180.py`.
The full certificate is
`scripts/li-theta/one-coordinate-marginal-check-180.json`.
The standalone rational calculation enumerates all 24 labeled
placements of the four original tensors, compares their contraction
with (2), computes each tensor's scaled limit and checks the actual
normalization substitution and (6). All eight checks pass; the three
algebraic residuals are zero. The complete contraction table,
per-tensor limits, normalized bracket, domination difference,
residuals and checks were inspected with the scoped JSON inspector.
The analytic slice bounds, moment inequalities and passage from the
limit to a negative region are proved above, not inferred from a
program PASS field or a sample grid.

The supplied EXPLORE assessment
`drafts/literature/2026-11-10-one-coordinate-theta-marginal-review-178.md`
covers this exact attempt and found no inspected theorem determining
the marginal sign. The result adds a local obstruction beyond those
checked sources; it is not a certified originality claim. L969's
three-coordinate negative diagonal alone would not have implied this
marginal obstruction: the surviving positive terms in (4) required
the separate, actual moment comparison (5)-(6). Retire only the
specified one-coordinate pointwise test, with no all-n extension.

### Independent audit, step182

The unchanged SPECIALIZE assessment
`drafts/literature/2026-11-10-one-coordinate-theta-marginal-audit-review-180.md`
covers this audit. It accepts (1)-(6) for exactly the stated actual
moments and fixed parameters. This independently validates an existing
local obstruction; it establishes no new sign for the integrated form.

For completeness the contraction was reconstructed by deleting each
of the three labeled factors in each cubic, rather than importing the
construction's permutation enumeration. For a chosen integrated label,
the other two labels occur in both orders; their contribution to the
normalized average is one third of the integrated moment times S.
Thus the four tensors contribute to 3J_2, respectively,

    d_1[m_1 S(B_0,C_0)+m_0 S(B_1,C_0)+v_0 S(B_1,B_0)],
    d_2[m_2 S(B_0,C_0)+m_0 S(B_2,C_0)+v_0 S(B_2,B_0)],
    -d_2[2m_1 S(B_1,C_0)+v_0 B_1(u)B_1(v)],
    -d_1[2m_0 S(B_0,C_1)+v_1 B_0(u)B_0(v)].

These exhaust all six labeled permutations per tensor, including both
identical-function labels in each subtraction, and sum to (2). Both
the h-origin in v_0 and the complete derivative in v_1 are retained.

The analytic conditions were checked directly from
H_0(x,w)=cosh(sqrt(x)w) and
H_1(x,w)=w sinh(sqrt(x)w)/(2sqrt(x)) at the two positive x values.
L019's decay bounds A times every factor by the integrable function
displayed above. This proves integrability for each fixed u,v, and
products of these bounds prove full absolute integrability. There is
no exceptional slice, assumed probability normalization or unstated
endpoint interchange. The exact definition of gamma gives m_0=1/2.

Direct division of these hyperbolic formulas by E(t) gives (3), with
q=72>1/2. After deletion, and scaling by 3/(d_1 g^2), the four
diagonal contributions to the limit are, in the same order,

    m_1, (d_2/d_1)m_2, 0, -v_1-4Delta m_0/gamma.

In particular averaging permits positive leading terms to survive;
the full-kernel negative limit alone would not prove this result.
Substitution of all five actual moments and 1/gamma=2(c_0+c_1)
gives exactly the bracket in (1), whose coefficients at the stated
parameters are

    2a_0+(20735/20736)a_1-20737c_0-(62205/2)c_1.

Every H_r series used in (5) converges, has nonnegative coefficients
in x, and is evaluated at h>b>0. Termwise comparison and positive
integration therefore give c_r>=a_r>0 for r=0,1. Subtracting the
actual bracket from its proposed upper bound gives exactly
2(c_0-a_0)+(20735/20736)(c_1-a_1). With
Delta=20735/4 and 6-1/h=31103/5184, that upper bound is strictly
negative. This checks the sign with actual moments, regardless of
the possibly small value of gamma. No limit is taken under an
integral. Continuity of (2) then gives a negative interior box;
positivity and continuity of A give it positive product measure.
Neither its relative mass nor the complementary signed mass is bounded.

Run `python3 scripts/li-theta/one-coordinate-marginal-audit-182.py`.
The independent rational certificate is
`scripts/li-theta/one-coordinate-marginal-audit-182.json`.
It imports no construction code or certificate. All nine checks pass:
the complete contraction, normalization and domination residuals are
zero. The twelve labeled deletions (each combining two orderings),
all ten contraction terms, every tensor limit, actual-moment
substitution, complete normalized bracket, upper bound, domination
difference, residuals and check values were inspected in full with
the scoped JSON inspector. The analytic argument above, rather than
the program's pass fields, verifies convergence and the negative region.

The existing direct inputs L019, L966 and L969 suffice; the audited
L967 transfer is inherited through L969. No DAG edge is added. Retain
the scoped pointwise stop and all earlier full-kernel/profile stops.
All-n L966(16), the final integral and RH remain unresolved. The
Fubini imports below support integration only; the sign is the checked
specialization above, not a sign theorem imported from those sources.

## Mathlib

Full matching coverage for this signed marginal and negative-tail
statement has not been checked and is unknown. Supporting Fubini
statements were inspected in the reused source assessment:
[`MeasureTheory.integral_prod`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/Prod.html#MeasureTheory.integral_prod)
and
[`MeasureTheory.integral_integral_swap`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/Prod.html#MeasureTheory.integral_integral_swap).
The required absolute integrability and S-finiteness hold here by
the bounds above and finiteness of A(u)du. Those statements support
integration, not the sign; no full matching Mathlib theorem is imported.
