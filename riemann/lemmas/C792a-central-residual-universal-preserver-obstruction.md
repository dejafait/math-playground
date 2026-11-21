# Corollary 792a: the central matched residual is not a universal preserver

## Hypotheses

Use L791's fixed central (shift n=0) degree-five model at its exact
positive Banach solution (A,B,C), with its fixed D and S=B R_1>0. Write

F_j=S^j (A)_j(C)_j D^j/[A^j C^j(B)_j(D)_j],
p(y)=sum_(j=0)^5 (-1)^j binom(5,j) F_j/S^j y^j.

Use L791's exact matching F_j=R_j for 0<=j<=4 and L792's conclusions

t_m=-p_5=F_5/S^5>0,
t_a=R_5/S^5>0,
delta=t_m-t_a>0.

These statements concern one exact solution within the complete original
parameter/data enclosures. Their inherited L778 complex analytic error,
quadrature widths, coefficient normalization and trusted software
contracts remain hypotheses. This corollary neither recomputes nor
narrows those enclosures. No actual-root or RH premise is used.

For each integer d>=5, let T_d be any real diagonal linear operator on
R[x] of degree at most d, with

T_d(x^j)=c_j x^j,  c_j=R_j/F_j for 0<=j<=5.

For j>5 the entries are arbitrary real numbers. The first six entries
are fixed independently of the test polynomial and of d. A universal
preserver here means preservation of real-rootedness for every nonzero
real polynomial of degree at most d (allowing a zero image).

## Conclusion

The entries satisfy c_0=...=c_4=1 and 0<c_5<1. The real-rooted polynomial

g(x)=(1+x)^5

is a counterexample to universal preservation for every T_d above. Put
epsilon=1-c_5=delta/t_m and r=epsilon^(1/5), the positive real fifth
root. Then 0<epsilon<1, 0<r<1, and

T_d g(x)=(1+x)^5-epsilon*x^5

has degree five, constant coefficient 1, and exactly one real root and
four nonreal roots. All five roots are simple and nonzero. Explicitly,
with zeta=exp(2*pi*i/5), they are

x_k=1/(r*zeta^k-1),  k=0,1,2,3,4.

This stops the universal-preserver fallback for any larger diagonal
operator retaining this prefix. It does not contradict L792: its
particular model polynomial maps to the actual degree-five Jensen
polynomial, and both are simple-positive-rooted there. Preservation of
that family, degree-dependent changes of prefix, growing-degree signed
bounds, all-degree mixed positivity and RH remain unresolved.

## Proof

**Known method and reason for the specialization.** T. Forgacs,
J. Tipton and B. Wright, *Multiplier Sequences for Simple Sets of
Polynomials*, [arXiv:1108.5627v1](https://arxiv.org/pdf/1108.5627v1),
29 August 2011, printed p.8, Proposition 2 and Remark 3, give the
geometric-prefix rigidity of classical multiplier sequences using
reciprocal polynomials and translated binomials. Their infinite result
is not applied by assuming an extension of a finite sequence.

O. Katkova, B. Shapiro and A. Vishnyakova, *Multiplier sequences and
logarithmic mesh*, [arXiv:1010.6052v1](https://arxiv.org/pdf/1010.6052v1),
28 October 2010, printed p.2, Theorem 4 and the preceding definitions,
give the finite criterion: an invertible diagonal operator on degree
at most k preserves hyperbolicity if and only if its binomial symbol
sum_(j=0)^k binom(k,j)c_j x^j has real roots of one sign.
The degree-five restriction below is invertible. Its binomial symbol
itself supplies the explicit failure, so no sufficient direction or
general theorem is reproved. The specialization is necessary to check
the actual residual orientation and to avoid a finite-to-infinite leap.
Both primary cases were inspected in the reused step484 assessment.

**Normalize before applying the test.** All F_j for j<=5 are positive:
the rising-factorial factors and S are positive. L791 gives c_j=1
through j=4. The last binomial factor is binom(5,5)=1 and its sign is
(-1)^5=-1, so p_5=-F_5/S^5. Consequently

c_5=R_5/F_5=(R_5/S^5)/(F_5/S^5)=t_a/t_m,
epsilon=1-c_5=(t_m-t_a)/t_m=delta/t_m.

Since delta>0 and t_a>0, one has 0<delta<t_m. Thus 0<c_5<1 and
0<epsilon<1, strictly, at the exact solution. In particular there is
no zero multiplier, vanishing leading coefficient, approximate equality
or altered parameter choice. The strict signs hold with the full input
widths by L792; no center value is substituted.

**Witness and complete root calculation.** The input g has its only
root -1 with multiplicity five. Linearity and the fixed multipliers give

H(x)=T_d g(x)=sum_(j=0)^4 binom(5,j)x^j+c_5 x^5
                  =(1+x)^5-epsilon*x^5.

Its leading coefficient is c_5>0 and H(0)=1. Form the reciprocal
polynomial, as a polynomial identity including z=0:

K(z)=z^5 H(1/z)=(z+1)^5-epsilon.

Its five roots are z_k=-1+r*zeta^k. They are distinct because r>0
and the fifth roots of unity are distinct. Since r<1, no z_k is zero.
For k=1,2,3,4, the number zeta^k is nonreal: a real fifth root of unity
can only be 1. Thus these four z_k are nonreal and z_0=r-1 is real
and negative. Inversion preserves nonreality for a nonzero complex
number (Im(1/z)=-Im(z)/|z|^2). It is also injective. The five x_k=1/z_k
are therefore distinct roots of H, exactly one real and four nonreal.
They exhaust its degree five. This proves simplicity and nonvanishing,
with the only real root x_0=1/(r-1)<-1. No numerical root solver or
root plot is used. In particular H violates even mere real-rootedness,
so the finite binomial criterion's same-sign refinement is unnecessary.

**Every larger space.** The subspace of polynomials of degree at most
five is invariant under every diagonal T_d. Its restriction has exactly
the six entries just tested. Since g belongs to this subspace, T_d g=H
for every d>=5, regardless of any later entries or their vanishing.
Universal preservation on the larger space would include g and hence
contradict the exhibited nonreal roots. No infinite extension and no
invertibility of the larger operator is needed.

For clarity on the excluded inference, the model polynomial is
p(y)=sum (-1)^j binom(5,j)F_j/S^j y^j, rather than g. Multiplying its
coefficients by c_j gives sum (-1)^j binom(5,j)R_j/S^j y^j, the actual
normalized Jensen polynomial. L792 establishes real-rootedness for this
particular image. The failed universal test supplies no obstruction
to that narrower conclusion and no new result beyond specialization
of the checked multiplier method.

### Separate algebraic audit, 5 November 2026 — step487

The preexisting SPECIALIZE assessment
`drafts/literature/2026-11-05-central-preserver-obstruction-audit.md`
approved exactly this normalization, complete root calculation and
restriction audit. The review found no mathematical defect. L791/L792's
audited conclusions, full original parameter/data widths and inherited
L778 analytic/evaluator/software contracts remain premises; their
certificates were not replayed or independently revalidated here.

**Residual orientation.** Substitution of L791's F_j into its displayed
p gives p_j=(-1)^j binom(5,j)F_j/S^j. Thus the fifth coefficient is
exactly -F_5/S^5, with neither a factorial nor an extra binomial factor.
The same normalization gives actual coefficient -R_5/S^5. L792's
delta=(-t_a)-p_5 is therefore t_m-t_a, not its negative. Positivity of
S,t_m,t_a and delta gives c_5=t_a/t_m in (0,1). Exact matching through4
gives the other five entries equal to1. These statements concern the
same exact Banach solution, rather than different points of its box.

**All roots and their multiplicities.** The reciprocal identity holds
coefficient by coefficient: K(z)=(z+1)^5-epsilon. Its leading coefficient
is1 and K(0)=1-epsilon=c_5>0; H has degree5 and H(0)=1. Consequently
reciprocity loses no root at zero or at infinity. For each k=0,...,4,
z_k=-1+r*zeta^k satisfies K(z_k)=0 and

K'(z_k)=5*r^4*zeta^(4k) != 0.

The five values are distinct, and |r*zeta^k|=r<1 excludes z_k=0.
This verifies all five denominators in the stated x_k. At x_k=1/z_k,
differentiating H(x)=x^5 K(1/x) also gives

H'(x_k)=-x_k^3 K'(z_k) != 0.

Thus simplicity is checked directly as well as by the exhaustive degree
count. The only real fifth root of unity is1: the other possible real
unit, -1, has fifth power -1. Hence exactly z_0 is real, and inversion
gives precisely one real and four nonreal roots of H. The real root is
less than -1 because -1<r-1<0. No limiting multiple-root argument or
numerical approximation to r is used.

**Quantifiers and restriction.** The witness g is fixed and belongs to
every degree-at-most-d space for d>=5. Diagonality makes its image depend
only on the first six entries; arbitrary later entries, including zeros,
cannot alter H. Only the degree-five restriction is invertible, and the
proof needs no invertibility of the larger operator and no infinite
extension. The witness is not the model p. On p the entries instead
produce precisely the actual scaled Jensen coefficients, whose root
conclusion remains L792's separate input. No claim of failure for every
simple positive-rooted input or for changing prefixes is licensed.

This completes the finite audit using the cited known method, with no
new general preservation theorem or progress beyond its source scope.
The direct mathematical inputs remain L791 and L792; no DAG edge or
main assembly argument changes. A repeat audit needs a concrete new
defect or changed premise. Actual-family signed control remains open.

## Mathlib

Full coverage for this residual-preserver specialization and the finite
multiplier criterion is unchecked. Supporting ingredients are elementary
polynomial identities, complex fifth roots of unity and reciprocal
roots. No absence of Mathlib coverage or formal verification is claimed.
