# Lemma 969: the derivative-aware boundary profile has a negative diagonal

## Hypotheses

Use the actual A,K of L019, the H_r,I_r and prescribed Q_eta(n) of
L966, and the complete tensor/face identities of L967. Fix n in {2,3}
and, separately at each order, put

    b=1/4, h=64*9^n, q=sqrt(h)=8*3^n, Delta=h-b,
    c_r=integral_0^infinity A(u)H_r(h,u)du  (r=0,1),
    gamma=1/[2(c_0+c_1)],
    Z(u)=gamma[H_0(h,u)+H_1(h,u)],
    M_n=Q_eta(n) I_0(b)^n I_0(h).                            (1)

The coefficients d_k are exactly L967's positive coefficients:

    n=2: d_1=4h^2/Delta^2, d_2=h/Delta;
    n=3: d_1=h(3Delta+1)^2/Delta^3,
         d_2=h(6Delta+1)/Delta^2, d_3=h/Delta.                (2)

Replace every origin mass 1/2 in L967's full face expansion by
A(u)Z(u)du, including the h-origin and every intersection. This is
the single fixed replacement being tested. No RH, simplicity,
positive Stieltjes representation, or sign of Q_eta is assumed.
The actual-node and multiplicity conventions are inherited unchanged
through L966. No effective or uniform-in-n bound for c_r is assumed.

## Conclusion

The replacement is well defined, with 0<gamma<infinity, and preserves
the entire numerator in an absolutely convergent integral:

    M_n=integral_(0,infinity)^(n+1)
              product_i A(u_i) * Psi_tilde_n(u_1,...,u_(n+1)) du. (3)

The fully symmetrized kernel is specified in (5)-(6) below. It obeys
the strictly negative simultaneous-escape limit

    lim_(t->infinity) Psi_tilde_n(t,...,t)/(t exp(qt))^(n+1)
       =-d_1 Delta/(2q) * [gamma/(4q)]^n < 0, n=2,3.        (4)

Thus the kernel is negative on a nonempty open subset of the positive
orthant, with positive A-product measure, at both orders. This retires
the specified profile as a pointwise nonnegativity certificate. It
does not determine the sign of M_n or Q_eta(n), refute L966(16), or
disprove RH. The all-index inequality remains open. This result was
written in step176 and independently conceptually audited in step178
on 10 November 2026. No statement or formula correction was required.

## Proof

### Exact replacement of all faces

The nonnegative entire series defining H_r in L966 gives H_0(h,u)>0
and H_1(h,u)>0 for u>0. Also

    H_0(h,u)=cosh(qu), H_1(h,u)=u sinh(qu)/(2q).

L019 gives A>0 and the bound C exp(9u/2-pi exp(2u)). Consequently
0<c_0,c_1<infinity: the displayed H factors have at most a linear
polynomial times exp(qu) growth, and their product with this bound
is integrable and bounded near zero. In particular gamma is a fixed
strictly positive finite number for each order, and integral A Z=1/2.
No numerical estimate or approximation to either c_r is required.

Reuse L967(8)-(9), including its endpoint and absolute-Fubini proof.
Its calculus input is the ordinary integration-by-parts formula
[NIST DLMF 1.4.16](https://dlmf.nist.gov/1.4.E16), with the improper
integrals in [1.4.22-23](https://dlmf.nist.gov/1.4.v); the version
1.2.8 source comparison is recorded in the prior assessments. No new
integration by parts, boundary condition, or external sign theorem
is asserted here. The changed operation acts after that transfer.

Under the common A(u)du measure the resulting single-coordinate
factors are

    B_0=Z, B_r=2r H_(r-1)(b,.)  (1<=r<=3),
    C_0=Z+2Delta H_0(h,.), C_1=2H_0(h,.)+2Delta H_1(h,.).

A zero-order b factor has only its origin mass, now Z. A positive-
order b factor has only its live part B_r. A zero-order h factor
has its origin mass Z and its live part 2Delta H_0(h). Its first
derivative has no origin mass, and its entire live factor C_1 is
retained. Indeed L967(8) gives, exactly,

    integral A B_r=I_r(b)  (0<=r<=3),
    integral A C_0=1/2+2Delta c_0=I_0(h),
    integral A C_1=2c_0+2Delta c_1=I_1(h).

Products of these identities preserve every tensor monomial. Expanding
each factor into its live and restored-origin terms recovers every
one of the 8 or 16 labeled subsets in L967(9). At an intersection,
each origin coordinate independently contributes Z with integral
1/2, so the original power of 1/2 is preserved. In particular the
h-origin is treated by the same rule. No normal-derivative term is
introduced: this is a replacement of already transferred measures,
not a further differential operation on Z.

For completeness let Sym_m denote the normalized average of the
product over all m! permutations, including repeated factors, as in
L967(2). The complete kernels are

    Psi_tilde_2 = d_1 Sym_3(B_1,B_0,C_0)
                  +d_2 Sym_3(B_2,B_0,C_0)
                  -d_2 Sym_3(B_1,B_1,C_0)
                  -d_1 Sym_3(B_0,B_0,C_1),                 (5)

    Psi_tilde_3 = d_1 Sym_4(B_1,B_0,B_0,C_0)
                  +d_2 Sym_4(B_2,B_0,B_0,C_0)
                  -d_2 Sym_4(B_1,B_1,B_0,C_0)
                  +(d_3/2) Sym_4(B_3,B_0,B_0,C_0)
                  -(3d_3/2) Sym_4(B_2,B_1,B_0,C_0)
                  +d_3 Sym_4(B_1,B_1,B_1,C_0)
                  -d_1 Sym_4(B_0,B_0,B_0,C_1).             (6)

These are exactly L967(5)-(6) with the displayed factor replacement;
in particular the even-block and distant subtractions remain present.
Every factor is bounded in absolute value by C_n(1+u^2)exp(qu).
Multiplication by A gives an integrable function, since exp(2u)
eventually dominates every linear or logarithmic term in u. Each
product term therefore has a finite absolute integral by product
integration. There are finitely many terms and permutations, so
absolute Fubini proves (3) from the moment identities. The same
bounds justify the integrations of restored intersections. Constants
may depend on n,h,gamma; no n-limit or uniform onset is used.

### Simultaneous escape and full symmetrization

Set E(t)=t exp(qt) for t>0. Directly from the hyperbolic formulas,

    B_0(t)/E(t) -> gamma/(4q),
    C_0(t)/E(t) -> gamma/(4q),
    C_1(t)/E(t) -> Delta/(2q).                              (7)

For example cosh(qt)/E(t)=(1+exp(-2qt))/(2t) tends to zero,
whereas H_1(h,t)/E(t)=(1-exp(-2qt))/(4q). The extra term
2Delta H_0(h) in C_0 consequently vanishes under this normalization;
it has not been discarded from the kernel or integral.

At b=1/4 the remaining factors are exactly

    B_1(t)=2cosh(t/2),
    B_2(t)=4t sinh(t/2),
    B_3(t)=6t^2 cosh(t/2)-12t sinh(t/2).                    (8)

They follow by differentiating cosh(sqrt(b)t) once and twice in b,
as already displayed in L967(18). Since q>1/2, (8) implies
B_r(t)/E(t)->0 for r=1,2,3: a fixed polynomial times
exp(-(q-1/2)t) tends to zero. All ratios in (7)-(8) are bounded
for sufficiently large t.

On the diagonal every permutation of any given product has the
same value. Its normalized symmetrization is therefore exactly the
product, with no remaining factor 1/(n+1). Each term in (5)-(6)
containing C_0 also contains at least one of B_1,B_2,B_3. Divide
that product by E(t)^(n+1); it tends to zero by (7)-(8). This
includes the negative even-block terms as well as all positive terms.
The only remaining term is

    -d_1 C_1(t) B_0(t)^n / E(t)^(n+1),

whose limit is precisely (4). Every factor in its unsigned limit
is strictly positive. The actual, possibly very small value of gamma
cannot change that sign; the eventual threshold may depend on gamma.

Equivalently, the C_0 part has exponential rate at most nq+1/2,
whereas the retained C_1 term has rate (n+1)q and a nonzero leading
coefficient of t^(n+1). The rates are respectively 289/2 versus
216 for n=2 and 1297/2 versus 864 for n=3. These strict gaps arise
because every C_0 product contains a b derivative while the negative
term contains only the faster h-profile factors.

The strictly negative limit yields a finite T_n such that the diagonal
value is negative for every t>T_n. Choose any such positive t. All
coordinates are then inside the positive orthant. Continuity of the
finite kernel gives a small open box around that point on which it
remains negative. A is continuous and strictly positive on the closure
of a sufficiently small box, so its product assigns the box positive
measure. No lower bound for its relative mass, or comparison with
the complementary region, is asserted.

### Exact check and scope of the stop

Run `python3 scripts/li-theta/h-derivative-profile-check-176.py`.
Its full certificate is
`scripts/li-theta/h-derivative-profile-check-176.json`. It reuses
L967's exact finite polynomial utilities and tensor coefficients,
expands every complete diagonal term with the new factors, and checks
the dominant rate, degree and coefficient. The coefficients in (4),
after removing gamma^n, are exactly

    n=2: -36/20735;
    n=3: -313457776129/207992562237775872.                    (9)

Both leading residuals are zero, the complete C_0 parts meet the
strictly lower rate bounds above, and no faster term occurs. The
complete diagonal polynomials and check fields are recorded for
inspection. This finite algebra supports the explicit analytic proof;
it does not numerically certify c_r, test the integral's sign, or
constitute an independent audit. The proof needs no numerical c_r.

This differs from L967's old one-coordinate obstruction. The new
profile includes the distant derivative, and that profile now appears
in every zero-order b slot. Simultaneous escape makes the distant
negative product dominate all compensation terms. Only this fixed
rule has been tested. No family of profiles, integrated comparison,
or all-n extension is ruled out. L968 explains why an eventual proof
of all-n L966(16) would suffice for RH; that is downstream motivation,
not an input to (3)-(4). No claim of originality beyond the bounded
source comparison is made.

### Independent conceptual audit, step178

The audit accepts (1)-(9) for precisely n=2,3 and the fixed actual
normalization in (1). It reuses the prior SPECIALIZE assessment and
L967's audited transfer, not the construction script's conclusions.
The inputs remain L019, L966 and L967. Inherited actual paired nodes,
algebraic squares and multiplicities have not been changed. L968 is
only downstream motivation. There is no new external sign input.

For a separate reconstruction of the tensors, introduce a formal z
and expand through degree n:

    Y(z)=sum_(r=1)^n I_r(b) z^r/[r! I_0(b)],
    log(1+Y)=sum_(ell=1)^n (-1)^(ell-1)Y^ell/ell + O(z^(n+1)).

For each k, multiply its degree-k coefficient by k*d_k and then by
I_0(b)^n I_0(h). Finally include -d_1 I_0(b)^n I_1(h).
This recovers exactly the four tensors of (5) and seven of (6);
in particular the third-order coefficients are d_3/2,-3d_3/2,d_3.
L966(2) independently yields (2), with D=(1,4) or (1,6,9).
No even partition or distant derivative is omitted in either expansion.

Here is an explicit check that the replacement preserves each face,
not just the sum. For any assigned tensor factor H_r(x,u), write its
transferred measure as its live A D_u H_r density plus its origin
mass delta_(r,0)/2. At b the zero-order live density is zero; at h
it is 2Delta A H_0(h). Positive b orders have no atom and live
density 2r A H_(r-1)(b); the h derivative has no atom and live
density A[2H_0(h)+2Delta H_1(h)]. These are all the possibilities.
For a fixed labeled live set S, replace each of its m-|S| origin
coordinates by A Z. Its integrated term is multiplied by

    [2 integral A Z]^(m-|S|)
      =[2 gamma(c_0+c_1)]^(m-|S|)=1,  m=n+1.              (10)

Zero face terms stay zero. This holds for every tensor placement,
including h-origin placements, before summing or symmetrizing. It
therefore checks all 8 or 16 labeled subsets and every intersection.
The argument never differentiates the replacement density.

Independently, enumerate the m! placements of the reconstructed
tensors, keeping repeated factors, and use the live moments just
listed and origin moment 1/2. Each labeled face of size j gives
exactly L967's T_(n,j)/binom(m,j), with its complete tables (11)-(12).
This checks the coefficients as well as the general mass argument
(10). It also checks the all-origin zero and the opposite signs of
the full interiors; neither interior sign is used to sign M_n.

The analytic conditions in (10) are actual conditions, not numerical
assumptions. The positive theta series gives A(u)>0. L019's bound
shows that A times each factor used here is bounded by

    C(1+u^2) exp((q+9/2)u-pi exp(2u)),                    (11)

for finite C depending on the fixed parameters. This is bounded near
zero and integrable at infinity. Hence c_0,c_1 are strictly positive
and finite, gamma is fixed before any t limit, and integral A Z=1/2
holds exactly. Products of (11) justify absolute Fubini for all
restored faces and the full signed kernel. The prior finite-box
transfer applies with its vanishing infinity endpoints; no new
improper interchange, n limit or uniform-in-gamma bound is needed.

For an independent asymptotic check, differentiate H_0(x,t)=cosh(sqrt(x)t)
at b once and twice, obtaining (8). The leading data of B_1,B_2,B_3
are respectively e^(t/2), 2t e^(t/2), 3t^2 e^(t/2). The exact
H_0,H_1 formulas at h give (7), including both parts of C_0 and C_1.
On the diagonal each term of the normalized m! average is the same
product, even when factors repeat. Thus its multiplicity is one.
Every C_0 tensor has rate at most nq+1/2, strictly below (n+1)q;
all its polynomial factors are dominated by that strict exponential
gap. For example the B_3 term has degree 5 at n=3, still negligible
relative to t^4 exp(864t). The only term at rate (n+1)q is
-d_1 B_0^n C_1, of degree n+1 and coefficient (4).

Removing gamma^n, this coefficient simplifies independently to

    n=2: -q/(8Delta)=-36/20735,
    n=3: -(3Delta+1)^2/(128h Delta^2)
                       =-313457776129/207992562237775872. (12)

Both are strictly negative for the actual gamma>0. Continuity gives
a negative box strictly inside the orthant, and strict positivity of
A gives it positive product measure. This last conclusion requires
neither an effective onset nor a lower bound for the box's mass. It
does not compare its negative integral with the complement.

Run `python3 scripts/li-theta/h-derivative-profile-audit-178.py` for
the independent exact finite check. It imports no notebook code and
reads no old certificate. It reconstructs the tensors from the formal
logarithm, enumerates all 24 labeled faces and all placements, and
checks the complete list of diagonal leading rates and coefficients.
The full certificate is `scripts/li-theta/h-derivative-profile-audit-178.json`.
All 44 exact checks pass with zero face residuals; the actual rate
bounds are 289/2<216 and 1297/2<864, and (12) is strictly below the
required nonnegative threshold. The complete check records and every
term's leading data were inspected. Analytic normalization, convergence,
the hyperbolic leading data and sign interpretation are supplied by
the proof above, not certified by a PASS field or floating point data.

This is independent local validation of the existing fixed-profile
obstruction, not a new theorem or integrated sign result. Retire only
the specified full-kernel pointwise rule. The all-index L966(16)
comparison and actual-Xi mixed positivity remain open. The construction
proof, script and certificate are preserved without alteration.

## Mathlib

Full matching coverage for this replacement and diagonal obstruction
has not been checked and is unknown. No Mathlib theorem is imported.
Supporting product-integration and elementary exponential-limit facts
would not supply the signed comparison. Reference portal:
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
