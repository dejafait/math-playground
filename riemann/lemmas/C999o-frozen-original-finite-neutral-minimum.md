# C999o: Positive original finite-middle minimum for the frozen endpoints

## Hypotheses

Use ell=log(3)/2 and the complete cosine operators D,S,T,T*,U of
C744v/w/z, with exactly offsets0,7ell,14ell. Put M=D+S. The neutral
form domain V0 and its smooth core are those of C744z. Retain the
analytic-response and IEEE754/Decimal contracts of C744v/w, the
whole-neutral-core qualification of C744z, and its unreplayed
c_*=8.9e-18 source computation. No RH, H2, global sign, reference
inverse, quarter allocation or infinite-complement positivity is assumed.

The endpoint free integers are exactly C999n Section1's
`free_numerators` in `scripts/separation-seven/endpoint-complement-locator-581.npz`,
divided by2^40, first512 for f and last512 for h. They occupy free
modes512:1023; all free modes2:511 vanish. Complete both endpoints
using C999m(1), with exact moment ratios, not rounded physical lows.
The archived hashes are checked against the original manifest. Endpoints
are independent, have zero imaginary free coefficients, and are unchanged.

The middle space W consists of ALL exactly neutral complex vectors
with raw support0:1023. It is the sum of C999l's exact Z_H space and
C999m's exact Z_T space restricted to free modes512:1023. There is no
parity or reflection relation between endpoints or in W.

The invocation-start EXPLORE assessment584, separately approved585,
licenses this fixed calculation as REPRODUCTION. General form/domain
coverage is imported from Teschl, *Mathematical Methods in Quantum
Mechanics*, GSM99 author version, 12February2009, Theorems2.13/2.18,
printed pp71-72/77,
[author PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf).
Arithmetic/enclosure coverage reuses Rump, *Verification of Positive
Definiteness*, BIT46(2006),433-452, Theorem2.3, Corollary2.4, (2.12),
Lemma2.6 and Corollary2.7, author PDF pp4-6,
[author PDF](https://www.tuhh.de/ti3/paper/rump/Ru06c.pdf).
As assessment539/completion540 expressly permits, the implementation uses
the full-factor-reconstruction alternative, with its own operation-error
bounds. It does not assert that a Cholesky success flag implements
Corollary2.7. No reproof of the imported general theorems is needed;
the finite residual identity below specifies their elementary application.

## Conclusion

**Step588 conceptual audit:** Section6 upholds the step586 calculation
under the unchanged stated contracts. The original finite neutral-middle
minimum satisfies

    .42327662 < min_(g in W) Q_actual(f,g,h) < .42418215.       (1)

This distinguishes the positive original finite sign from C999n's
negative sufficient reference-minus-quarter comparison. It supplies
neither a lower bound for the unrestricted middle minimum nor a
uniform endpoint-complement sign. The infinite middle correction,
other endpoint directions, C744q margin, H2 slack/existence,
non-neutral coverage and actual-Xi global assembly remain open.
There is no negative smooth triple, off-line zero or RH candidate.

## Proof

### 1. Exact coordinates, domains and the direction of comparison

Write k_n=n*pi/ell, nu_0=ell^(-1/2), nu_n=sqrt(2/ell) for n>0.
For n=2,...,1023, p=n mod2, set

    r_n=(nu_n/nu_p)(1/4+k_p^2)/(1/4+k_n^2),
    (Zv)_n=v_n (n>=2),
    (Zv)_p=-sum_(n>=2,n mod2=p)r_n v_n.                     (2)

C999l(1)'s exact moment calculation applies separately in each parity
and kills both exponential moments. The two low moment columns are
independent, so this Z parametrizes precisely W, including complex
vectors. It concatenates the specified Z_H and finite Z_T coordinates.
Every vector is finite cosine support, belongs to V0 and Dom(D), and
has well-defined original form energy. The moment penalty is zero
algebraically and is never inserted in a rounded physical quadratic form.

Use C744z(5) to define, for the fixed endpoints,

    E=<Mf,f>+<Mh,h>-2 Re<Uf,h>,
    rho=Tf+T*h,
    A=Z* M Z, b=Z* rho,
    Q_actual(f,Zv,h)=E+v*Av-2 Re(v*b).                       (3)

Here matrix products use the usual conjugate transpose and represent
the same real energy as the inherited first-slot-linear notation.
Thus both T orientations and the signed remote U are retained. In
particular U is not replaced by a norm or omitted. A is real symmetric
and Hermitian on complex coordinates. Once A>=alpha I>0 is certified,
the finite minimum exists uniquely and equals E-b*A^-1b.

For any specified exact free vector v, let c=Av-b. Square completion
in these SAME finite coordinates gives

    Q_actual(f,Zv,h)-||c||^2/alpha
       <= min_(g in W) Q_actual(f,g,h)
       <= Q_actual(f,Zv,h).                                (4)

Indeed the exact reduction is c*A^-1c, between0 and||c||^2/alpha.
This covers all complex minimizers even though the chosen trial and
forcing are real. W is contained in V0, so the unrestricted minimum
is <= this finite minimum, not >= it. Positive (1) cannot settle it.

### 2. Complete entries and exact neutral coefficients

The script below replays C999n's generator only before its selection,
eigenvector, solve and write sections. It expands its physical columns
from {0,1} union512:1023 to ALL0:1023. It builds full1024-by1024 M,T,T*,U.
Every entry in each old rectangle agrees bit-for-bit with its saved
counterpart. This agreement checks preservation, not analytic accuracy.
The complete T/T* arrays are transposes, and all16 separation7 powers,
all334 separation14 powers and the exact zero-delay2187 identity remain.
The continuous terms include j=1:7 with the inherited full operator
tail, and the local response includes the64-term exact recurrence,
the65536-term equal-index sum with correction, and its full remainders.

C999n Section4's changed-range proof applies to every n,m<=1023,
not only its old column subset. Its upper cancellation ratio<1024,
minimum nonzero frequency gap>5.71920, maximum recurrence remainder
<.000057097552, equal-index bound<5.125617e-9 before normalization,
and normalized off-diagonal bound<.000039933931 are independent of
that subset. The local diagonal D, combined elementary allowance and
response bounds give uniform local entry error<.000097173. Thus use

    |M_exact-Mhat|_max <= epsilon_M=.0001,
    |T_exact-That|_max, |T*_exact-Tshat|_max,
    |U_exact-Uhat|_max <= epsilon_C=.000001.                 (5)

This is a looser specialization of that audited range ledger. The local
bound includes the constant and equal-index cases and symmetrization;
the cross bound includes all signed shifts, continuous remainders,
zero shift, arithmetic and orientations. No old512-column accumulated
operator norm is transferred. All center entries are checked finite
with magnitude<400. Bounds (5) represent the original full operators,
not truncated or periodic replacements.

Directed60-digit intervals and the80-term Machin enclosure reconstruct
every exact ratio in(2), both fixed endpoints and the middle trial.
The ratio centers form Zhat. The full ratio-error Frobenius norm delta
and a valid operator bound z satisfy

    delta=||Z-Zhat||_F <1.269e-18,
    ||Z|| <= z=sqrt(1+sum_(n=2)^1023 r_n^2)<1.007416847.

For each free vector the low coefficients are recomputed as interval
sums, not assumed to be saved neutral centers. Their total L1 errors
against the stored raw centers obey

    delta_f<2.883e-23, delta_h<1.428e-23, delta_g<1.560e-22;
    l_f<1.441497349, l_h<1.441499682, l_g<.511202650.          (6)

Here each l is an upper bound for the exact physical coefficient L1
norm. Every free endpoint integer is checked to convert to its exact
dyadic value. The proposed middle free binary64 entries are themselves
exact dyadics; no solve accuracy is presumed. Full interval coefficients
and all centers, including all1022 free middle coordinates, are saved.

### 3. Finite coercivity with all matrix and factor errors

Let Ahat=sym(fl(Zhat^t Mhat Zhat)). The library Cholesky merely proposes
F for Ahat-.5 I. With u=2^-53 and gamma_j=ju/(1-ju), reconstruct the
ENTIRE matrix difference. The norm of that reconstruction is inflated
for its own multiplication/subtraction error by

    gamma_2048 ||F||_F^2
       +gamma_8(||Ahat||_F+.5 sqrt(1022)+||F||_F^2+1).

Together with the reconstruction center norm this is <1.249e-9.
Thus Ahat>=(.5-1.249e-9)I, because FF* is nonnegative; neither a
factor inverse nor a Cholesky-library accuracy assumption is used.
Its squared factor Frobenius norm is <5467.338. All norm upper bounds
inflate the sum-of-squares/sqrt evaluation by factor1.00000001 plus
1e-30; the largest array has1024^2 entries, so its standard gamma
bound is smaller than this allowance under the inherited contract.

The full arithmetic error of the two matrix products and symmetrization
is bounded by

    e_assembly=gamma_4096||Zhat||_F^2||Mhat||_F+1e-7
               <1.881e-7.

The analytic and exact-coordinate matrix errors are at most

    e_entries=z^2*1024*epsilon_M<.103924604,
    e_coordinates=delta(2z+delta)||Mhat||_F<4.845e-16.

The first uses the full1024-square entry bound in(5); the second uses
||Zhat||<=z+delta. Their total, subtracted from the verified center
floor, yields a certified alpha with

    A>=alpha I, alpha>.3960752074>.39.                      (7)

This finite floor does not strengthen any infinite-domain scalar floor.

### 4. Original trial energy and complete solve error

For every computed scalar x*Mhat*y, the two dot products have error
at most1e-8||x||_1||y||_1: dimensions are<=1024, max entry<400, and
400(2gamma_1024+gamma_1024^2)<1e-8. The scalar center energy is the
complete signed expression(3), using the raw center trial ghat=Zhat v.
Analytic entry uncertainty contributes at most

    epsilon_M(l_f^2+l_h^2+l_g^2)
       +2epsilon_C(l_f l_h+l_g l_f+l_g l_h)<.000448819837.

For any local term, raw-coordinate perturbations cost at most
401 delta_x(2l_x+delta_x); for a cross term they cost at most
401(delta_x l_y+delta_y l_x+delta_x delta_y), multiplied by its
coefficient2. Sum these for all three local and all three cross terms.
Their complete total is <5.419e-19. With the scalar dot allowances
this gives the ORIGINAL exact neutral trial enclosure

    .4232842736504860 < Q_actual(f,Zv,h)
                                    < .4241821437347197.    (8)

To bound the gradient in(4), form center vectors

    w_c=fl(Mhat ghat-That fhat-Tshat hhat),
    c_c=fl(Zhat^t w_c).

The physical entry error is
32[epsilon_M l_g+epsilon_C(l_f+l_h)]<.001728104383.
Physical coordinate error is bounded by
||Mhat||_F delta_g+32*400(delta_f+delta_h). A valid arithmetic
allowance for w_c is

    e_w=gamma_4096(||Mhat||_F||ghat||_2
             +||That||_F||fhat||_2+||Tshat||_F||hhat||_2+1)
        <3.022e-11.

For the outer product use e_c=gamma_2048||Zhat||_F||w_c||_2.
Consequently the exact c in(4) satisfies

    ||c|| <= ||c_c|| +(z+delta)(e_physical_entries
                     +e_physical_coordinates+e_w)
                     +delta||w_c||_2+e_c
           <.001740921499.

The complete center residual norm is <1.871e-15, but the bound above
pays the MUCH larger entry uncertainty; it does not equate a floating
solve residual with an exact one. Equation(7) gives

    ||c||^2/alpha < .000007652102.                          (9)

Combining the actual directed endpoints of(8)-(9) in(4) yields

    .423276621549049831354866407322692148945417094753073201572447
      <= min_(g in W) Q_actual(f,g,h)
      <= .424182143734719607800773351890720653244522290765186247076765.

The shorter outward-rounded interval(1) follows. These are bounds for
the exact finite minimum under the entry contracts, not just for the
saved dyadic center or a proposed eigenvalue.

### 5. Reproduction, preservation and limitations

Run from this notebook:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/original-galerkin-586.py

The full certificate is `scripts/separation-seven/original-galerkin-586.json`;
full matrices, neutral coordinates, factor, frozen numerators and trial
are in `scripts/separation-seven/original-galerkin-586.npz`. All24 checks
pass, with no failures. The record includes complete ratio/profile
intervals, operation/error bounds, source/input/archive hashes and
preservation checks. The initial implementation failure, an unsupported
interval exponent operation before bounds were produced, is preserved in
`scripts/separation-seven/original-galerkin-first-pass-586.json`. Its
correction did not change any mathematical parameter or frozen endpoint.

Entry generation reuses the audited elementary implementation; agreement
with saved arrays is not independent transcendental verification. The
analytic ledger(5) supplies that link. At step586 a separate conceptual
audit of the range specialization, exact neutrality, all arithmetic debts
and complex finite variational direction remained required; Section6
now supplies that audit under the unchanged contracts. Existing
symbol/quarter stops remain intact. Nothing estimates the infinite
middle Schur correction, closes all endpoint directions, verifies H2,
or resolves the actual-Xi positivity gap.

### 6. Separate conceptual audit — step588, 12 November2026

The invocation-start SPECIALIZE assessment586, separately approved587,
covers precisely this audit. No endpoint, middle dimension, separation,
operator, sign or moment convention is changed. This is REPRODUCTION:
independent checking of the existing finite claim, not a new general
theorem or progress beyond the checked sources on RH. The original
certificate and first-pass exception remain unchanged.

**Exact neutral space and complex variational direction.** For each
parity, direct integration in C999l(1) gives the same ratio r_n for
both exponential moments. The ratios of the positive-exponent to
negative-exponent moment in the two low columns are respectively
exp(ell/2) and -exp(ell/2); the columns are therefore independent.
Thus (2) parametrizes every complex neutral raw0:1023 vector, without
an extra parity or endpoint restriction. Finite cosine sums lie in
Dom(D), so (3) is the original form on these vectors. In the inherited
first-slot-linear notation, Re<Tg,h>=Re<g,T*h>; in conjugate-transpose
coordinates this is Re(g*T*h). Hence b contains T f+T* h, and E
contains -2 Re(h*U f). All signs in (3) are correct.

The finite A is Hermitian and strictly coercive by the check below.
For arbitrary complex v, completing the square gives exactly
Q(v)-min Q=(Av-b)*A^-1(Av-b). The operator inequality A^-1<=I/alpha
proves (4). In particular the Euclidean coordinate residual is the
correct residual for this coordinate coercivity bound; no physical
orthonormality of Z is assumed. Real coefficients in the chosen trial
do not restrict the complex infimum. The inclusion W subset V0 gives
inf_V0 Q<=min_W Q. Neither this identity nor any imported form theorem
gives a lower bound on inf_V0 Q from (1).

**Full entry extension.** The independent audit runs the old generator
only through entry assembly, with every raw column0:1023, stopping
before selection, solving or writes. All four1024-square saved matrices
agree entry-for-entry, including the complete adjoints T*=T^t and
U*=U^t and the full zero-delay identity. Independent integer enumeration
recovers all334 remote prime powers and the unique zero delay2187.
Every remote weight, signed delay and strict overlap is enclosed anew;
all16 nearest translations and both seven-term continuous orientations
are retained. Array agreement establishes preservation, not analytic
accuracy: C744w's formulas and C999n Section4's case analysis supply
the analytic link.

That analysis applies to the enlarged square because it used only
n,m<=1023 and the maximal cancellation ratio at(1023,1022), which is
<1024, not the old column subset. The off-diagonal response estimate
uses |k_n-k_m|>=pi/ell>5.71920 and normalization2nu_n nu_m<8.
The equal-index sum, its integral remainder, constant mode and exact
zero shift use their separate formulas. Re-enclosing the ledger gives
local cap<.000097172487<.0001, response suffix<2.117e-34 and the
separation7 continuous suffix<1.465e-25; separation14 is smaller.
The334-shift arithmetic, including its unequal/equal/constant cases,
retains C999n Section4's <1e-7 allowance inside epsilon_C=1e-6.
The symmetrized local center retains its uniform bound. Thus no old
512-column operator error is transferred to the new1024-square matrix.

**Coordinates, norms and finite floor.** At80 directed Decimal digits,
Machin's enclosure and exact logarithm/square-root enclosures reproduce
all1022 ratios and all3072 physical profile coefficients. Every new
interval is inside its original interval. Every free dyadic and the
full Zhat sparsity/identity pattern are checked. In particular the
two low coefficients are recomputed; saved low centers are never
declared exactly neutral. Their L1 discrepancies satisfy (6).

Every Frobenius norm used in the factor/assembly/residual checks is
also evaluated from the exact integer sum of squares of ALL its saved
dyadic entries. Each exact norm is below the original1.00000001-inflated
norm. The largest sum has1024^2 terms and gamma_(1024^2)<1e-8;
the stored nonzero values checked in these norm computations exceed
1e-130 in magnitude, so their squares are normal. The inherited
absolute underflow charges are additionally dominated by1e-290 in
the independent certificate. No hardware/libm contract is promoted
from these checks to an unconditional real-arithmetic theorem.

The complete saved F is used to reconstruct Ahat-.5I-FF*. Matrix
product/subtraction rounding is charged as in Section3; an arbitrary
proposed F suffices because FF* is nonnegative. For the two products
Zhat^t Mhat Zhat, entrywise dot-product error followed by
|| |B| ||_2<=||B||_F bounds the accumulated Frobenius error by the
stated gamma_4096 expression, including symmetrization. The separate
analytic debt is z^2*1024*epsilon_M and the exact-coordinate debt is
delta(2z+delta)||Mhat||_F. Subtracting every debt gives

    alpha > .39607520749859 > .3960752074.

No eigenvalue, inverse-factor or Cholesky accuracy claim enters this
floor. These estimates hold for all complex coordinate vectors.

**Exact signed scalars and residual.** The audit evaluates all six
scalar products f*Mhat f, h*Mhat h, ghat*Mhat ghat, h*Uhat f,
ghat*That f and ghat*Tshat h by integer sums of exact dyadics. Each
lies in its original floating-dot enclosure. With the original full
entry and coordinate debts retained, but these dot roundoff debts
unneeded, the exact neutral trial energy satisfies

    .4232843888564016 < Q_actual(f,Zv,h) < .4241820285288059.

Independently compute EVERY coordinate of

    w_0=Mhat ghat-That fhat-Tshat hhat,
    c_0=Zhat^t w_0

as an exact rational. Put w_c=fl(Mhat ghat-That fhat-Tshat hhat)
and c_c=fl(Zhat^t w_c). Complete rational comparisons give
||w_0-w_c||<5.972e-16 versus the paid3.022e-11, and
||Zhat^t w_c-c_c||<1.299e-23 versus the paid4.290e-16. The latter
is only the outer product's roundoff; it is not ||c_0-c_c||.
The exact dyadic ||c_0||<1.324e-15 is only the center, not the true gradient.
Let e_p be Section4's full physical entry plus coordinate error.
The exact gradient obeys

    ||Av-b|| <= ||c_0||+z e_p+delta||w_0||
                < .001740921468124,
    ||Av-b||^2/alpha < .000007652101169.

The first inequality follows by inserting Z_exact^t w_0 between
Z_exact^t w_exact and Zhat^t w_0; its entry error uses the exact
physical L1 norms and all1024 physical rows. It neither discards
the analytic entry error nor substitutes a floating solve residual.
All coordinate and scalar uncertainty is therefore paid. Equation(4)
now gives the independent outward-rounded enclosure

    .4232767367552330 < min_(g in W) Q_actual(f,g,h)
                                             < .4241820285288059.

The full80-digit enclosure lies inside the original full enclosure
in Section4, and hence upholds (1). Its small tightening comes from
exact evaluation of saved center products, not a changed mathematical
parameter or an improved analytic estimate.

Reproduce without overwriting any prior artifact:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/original-minimum-audit-588.py

The full certificate is `scripts/separation-seven/original-minimum-audit-588.json`.
All1455 checks pass, with no failures. It records all exact ratios,
profile intervals, rational scalar products, both complete rational
residual vectors, norm evidence, bounds, source/archive hashes and
preservation checks. No original solve or selection is rerun. Analytic
and IEEE754/Decimal contracts, whole-core and unreplayed c_* qualifications
remain. The full neutral-middle inverse, other endpoint directions,
C744q margin, H2, non-neutral coverage and actual-Xi assembly are still
unpaid. Only this frozen finite test is closed.

## Mathlib

Full matching coverage for this frozen finite neutral minimum is not
checked. No theorem is claimed absent. The general form and arithmetic
sources above support the method; neither supplies the numerical sign
without this specialization and certificate. This is local progress by
standard-method reproduction, not progress beyond the checked sources
on RH or a claim of originality.
The step588 audit leaves full matching Mathlib coverage unchecked.
