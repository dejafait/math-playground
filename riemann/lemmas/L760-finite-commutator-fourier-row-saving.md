# L760 — finite commutator saving for a boundary-cancelled Fourier row

## Hypotheses

Use the exact real symmetric arithmetic matrix A of audited L759, with
lambda=sqrt(13), L=log(13), N=120, and coefficient indices -120,...,120.
Its least eigenvalue epsilon is simple and even. Set

    T=A-epsilon I,  g=min(spec(T)\{0})>0,
    P=orthogonal projection off ker(T),  R=(T|ker(T)^perp)^(-1) P.

Thus R is zero on ker(T). All norms below are Euclidean operator or
coefficient norms, with complex absolute squares when appropriate.
Let eta=(1,...,1)^T, D=diag(j), and b=eta^T/sqrt(L). Choose a real unit
ground vector u with b(u)>0; put xi=u/b(u) and x=xi/sqrt(L), so
b(xi)=1 and eta^T x=1. Nonzero boundary overlap follows from the source
normalization argument and is independently enclosed below in this cell.

Import the following precise finite-dimensional inputs from
Connes--Consani--Moscovici, *Zeta Spectral Triples*,
[arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1): Lemmas5.1-5.2
(parity and the rank-two commutator), the normalization before Lemma5.4
and Lemma5.4(i), Proposition5.9/(5.25) (the Fourier row), and Theorem5.10's
distinction between xi and x. With the source's real odd beta,

    [D,T]=beta eta^T-eta beta^T,    T D x=-beta.

In particular beta_0=0 and beta_j=j A_(j,0). These follow in the specified
translated orthonormal basis; no change of basis or missing sqrt(L) factor
is permitted. L759 supplies the simple-even hypothesis, not positivity
of the unshifted Weil form in general.

Fix z=i/4 and define, for arbitrary coefficient vectors v,

    ell(v)=2 L^(-1/2) sin(zL/2) sum_j v_j/(z-2pi j/L),
    q=ell-ell(xi)b.

This is a complex linear row, not a Hermitian quadratic form. Transposes
in the algebra below are bilinear transposes; norms retain conjugation.
The finite certificate uses the software/arithmetic trust assumptions
specified in L759 and the scripts described below. Step366 independently
audited the algebra and all finite bounds; section8 records the complete
replay and independent integer-interval calculation. Software arithmetic
semantics remain trust assumptions.

## Conclusion

For this single cell, both parity sectors and all 241 directions,

    3.0555*10^-55 < g < 3.0556*10^-55,
    5.25*10^-30 < rho := g ||q R P|| / ||q|| < 5.26*10^-30.

In particular q is nonzero. There is also an algebraic, quantitatively
controlled partial preimage. Write

    w=zL/(2pi), F=(wI-D)^(-1), k=sqrt(L)sin(zL/2)/pi,
    f=x^T F eta, c=beta^T D x,
    H=-(k f/c)x^T D^2,       r=ell-(k f/c)beta^T D.

Then

    -1447 < c < -1446,
    q=H T+r,  r x=0,  q R P=H P+r R,
    0.02196 < ||r||/||q|| < 0.02197,
    g||H||/||q|| < 7*10^-31,
    rho <= g||H||/||q||+||r||/||q|| < 0.022 < 1/10.

The reduced resolvent remains explicitly on the smaller row r. This is
not an inverse-free exact preimage and not a uniform estimate in N or
lambda. It does improve the estimate that applies 1/g to the entire row,
by a proved factor exceeding 1/0.022. It explains only this modest part
of the much larger certified finite saving in rho.

The more immediate frequency-resolvent ansatz fails this same-cell test.
With a=x^T F beta (nonzero here), H_F=(k/a)x^T F and r_F=q-H_F T,

    1+2.2592*10^-29 < ||r_F||/||q|| < 1+2.2593*10^-29.

Thus the direct ansatz followed by an absolute norm estimate does not
reduce the residual. This failure does not exclude other factorizations.

## Proof

### 1. Imported identities and the two commutator reductions

The cited source results apply because L759 proves a simple even least
eigenvector and T is its nonnegative shift. Source normalization yields
x real and even with eta^T x=1. Consequently eta^T D x=0. Applying
T D=D T-beta eta^T+eta beta^T to D x gives

    T D^2 x=D T D x-beta eta^T D x+eta beta^T D x
           =-D beta+c eta.                                      (1)

Also c=-(D x)^T T D x<=0. Strict negativity and the displayed quantitative
bound are certified below, so dividing by c is legitimate in this cell.
The case D x=0 in other matrices is not silently excluded: then c=0
and this construction is unavailable.

The Fourier formula from Proposition5.9 gives ell=k eta^T F and
ell(xi)=sqrt(L) k f. Hence q=k(eta^T F-f eta^T). Transposing (1) yields

    H T=-k f eta^T+(k f/c)beta^T D,

which proves q=H T+r exactly. Since T x=0 and q x=0, r x=0. Using
T R=P and r P=r gives q R P=H P+r R. P is a contraction and the finite
spectral theorem gives ||R||=1/g. Therefore

    g||q R P||/||q|| <= g||H||/||q||+||r||/||q||.                 (2)

This argument openly retains the inverse on r; it neither declares R
small nor treats the source's nonzero overlap as a quantitative bound.
All constants and denominators in (2) are enclosed for the actual matrix.
The use of the source commutator is a necessary specialization for the
new row bound, not a reproof of the imported source theorem.

For the direct ansatz, the elementary finite inverse identity gives

    [F,T]=F[D,T]F,
    x^T F T=a eta^T F-f beta^T F.

It follows that

    r_F=(k f/a)(beta^T F-a eta^T).                              (3)

Equation (3), with both parities retained, is the failed residual tested
below. Simply adding r_F R to H_F P reinstates the uncontrolled full
norm cost; its residual norm is slightly larger than ||q||.

### 2. Exact data, arithmetic, and finite candidates

The entry intervals are the complete audited L759 artifact
`scripts/spectral-triples/finite-parity-359.json`. They enclose the exact
arithmetic matrix, including every signed prime and archimedean term.
No new matrix-entry approximation, asymptotic, or numerical stability
assumption is introduced. L759's independent audit justifies reuse of
these inputs and of their even/odd basis conversions.

Reproduce the point diagnostic and then the certificate from this notebook:

    python3 scripts/spectral-triples/commutator-screen-364.py
    python3 scripts/spectral-triples/commutator-certificate-364.py

The first program uses 160-digit point Decimal LDL solves and inverse
iteration. Its output, `scripts/spectral-triples/commutator-screen-364.json`,
is explicitly NONRIGOROUS and supplies only candidate vectors. In the
certificate every saved candidate coordinate and candidate eigenvalue
is treated as an exact decimal rational, and its mathematical error is
bounded afresh. Neither convergence of inverse iteration nor accuracy
of the point solves is a premise.

The complete certificate is
`scripts/spectral-triples/commutator-certificate-364.json`. It records
input and script hashes; normalized candidate intervals; all residual
coordinates; every new parity LDL pivot; the full Fourier, boundary and
dual rows; candidate preimages and their error bound; both commutator
residuals; all norm intervals; arithmetic flags; checks; and failures.

The new program extracts only the audited class I and its 170-digit
floor/ceiling contexts from the original generator's syntax tree, without
executing that generator or overwriting its artifacts. Ordinary +,-,*,/
and monotone sqrt/exp operations therefore have L759's outward-rounding
guarantees. Interval squares use zero as the lower endpoint when an
interval crosses zero. Exact source symmetry allows symmetric LDL
elimination using the enclosing lower-triangular entries. Only Rounded
and Inexact flags occur; exponent-range and invalid-operation flags are
explicitly rejected. The software contract is the standard
[Python Decimal reference](https://docs.python.org/3/library/decimal.html),
as already assessed in L759; this is not formal interpreter verification.

### 3. Ground eigenvalue, vector, and both actual-gap bounds

Normalize the saved real even rational candidate v exactly as
w_0=v/||v||. Interval normalization encloses every coordinate of w_0.
Let theta be the fixed rational candidate eigenvalue and e an upper
bound for ||(A_even-theta I)w_0||. The finite-dimensional spectral theorem
places an eigenvalue within e of theta. The certificate verifies
theta+e<5*10^-56; L759 puts every other even eigenvalue above 10^-55.
Thus the nearby eigenvalue is precisely epsilon, and

    epsilon in [theta-e,theta+e].

Let u have unit norm and choose its sign so <u,w_0>>=0. Expanding in an
orthonormal eigenbasis and using the same separation gives

    ||P w_0|| <= e/(10^-55-theta)=delta,
    ||u-w_0||^2=2(1-<u,w_0>) <= 2 delta^2.

The program uses the looser E=2delta and checks E<1. The full interval
calculation gives E<1.22*10^-104. This argument does not use an
unproved finite-error consequence of first-order perturbation theory.

At the exact shift tau=3.0559*10^-55, new interval LDL elimination has
one negative pivot in the 121-dimensional even block and zero in the
120-dimensional odd block; no pivot contains zero. The same Schur
complement induction and Sylvester law of inertia used in L759 apply
to these new shifts. Hence every eigenvalue other than epsilon is
strictly above tau, so g>tau-epsilon.

For the other side, normalize a saved rational odd vector y exactly.
The least odd eigenvalue is at most its Rayleigh quotient y^T A_odd y.
It is an eigenvalue outside the ground line. Therefore

    g <= y^T A_odd y-epsilon.

Combining the interval Rayleigh quotient with the epsilon enclosure
proves 3.0555*10^-55<g<3.0556*10^-55. This is a two-sided enclosure of
the actual gap, not a substitution of L759's coarse 5*10^-56 lower bound.

### 4. Boundary and Fourier row enclosures, including the odd part

At z=i t, t=1/4, put p=2 sinh(tL/2)/sqrt(L) and nu_j=2pi j/L. In the
orthonormal parity bases, ell has real even entries and imaginary odd
entries respectively

    ell_even,0=p/t,
    ell_even,j=sqrt(2) p t/(nu_j^2+t^2),         1<=j<=120,
    Im ell_odd,j=-sqrt(2) p nu_j/(nu_j^2+t^2),  1<=j<=120.

The boundary row is (1,sqrt(2),...,sqrt(2))/sqrt(L) in the even block
and zero in the odd block. These follow by pairing the source's j and
-j terms; the odd entries at the nonreal z have not been omitted.

From ||u-w_0||<=E, the certified intervals

    b(u) in b(w_0)+[-||b||E,||b||E],
    ell(u) in ell_even(w_0)+[-||ell_even||E,||ell_even||E]

enclose the exact quantities. The first interval is strictly positive
(approximately 3.72706*10^-29), fixing the chosen sign and allowing
division. Enclose ell(xi)=ell(u)/b(u), then every coordinate of
q_even=ell_even-ell(xi)b and q_odd=ell_odd. Summing interval absolute
squares gives the nonzero full ||q|| enclosure. The small boundary
overlap is explicitly propagated through this division, not hidden in
a constant or assumed bounded below for a family.

### 5. Certified norm of the exact reduced-resolvent row

Let K be the fixed complex rational row supplied by the point solve:
real in the even block and imaginary in the odd block. This row is a
candidate only. Compute interval enclosures for every coordinate of
s=K T-q using the exact entry and epsilon enclosures. Put h=q R P.
Because q annihilates u, so does s, and

    (K P-h)T=s,     ||K P-h||<=||s||/g.

Since u is real even,

    |K u| <= |K_even w_0|+||K_even|| E.

Consequently

    ||K-h|| <= ||s||/g+|K_even w_0|+||K_even|| E.                (4)

The certificate uses the rigorous lower endpoint of g in (4). Its
resulting error is less than 2.33*10^9; the candidate norm is about
3.87048*10^54. Thus ||K|| plus/minus the explicitly certified error
encloses ||h||. Combining this with the nonzero ||q|| enclosure and
both gap endpoints proves the displayed 5.25*10^-30<rho<5.26*10^-30.
No point eigensolver value or partial certificate preview proves this
claim; the interval residuals and full parity inertia are essential.

### 6. Independent algebraic estimate within the same certificate

Enclose u coordinatewise using w_0 plus/minus E, then enclose
x=u/(sqrt(L)b(u)). Extract beta_j=j A_(j,0) from the exact full matrix
intervals. Parity reduces

    c=beta^T D x=sum_(j=1)^120 sqrt(2) j beta_j x_even,j.

Although this sum has severe cancellation, its complete interval
enclosure lies in (-1447,-1446). No positivity or favorable sign of
individual summands is presumed. Evaluate H and r from their exact
formulas, keeping all the odd Fourier coordinates of r. The saved
norm intervals give

    0.02196<||r||/||q||<0.02197,
    g||H||/||q||<7*10^-31,
    g||H||/||q||+||r||/||q||<0.022.

Together with (2) this is a commutator-based explanation for a finite
saving exceeding the required factor ten. It does not depend on the
candidate K or its direct inverse computation. It does depend on the
certified ground-vector enclosure, c, boundary evaluation, and actual
gap for this cell. The still-large remainder r R is bounded openly.

For (3), write w=i y, k=i k_0, f=-i S, with y,k_0,S real. Parity makes
a real. The certificate checks a is nonzero and evaluates every real
even and imaginary odd component of r_F. Its full norm ratio minus one
lies between 2.2592*10^-29 and 2.2593*10^-29. This proves the stated
failure of the direct ansatz, without rounding that excess to zero.

### 7. Scope, validation status, and retained work

The completed certificate reports CERTIFIED_FINITE_RATIO_AND_ANSATZ_TEST
with no failures. Every load-bearing scalar bound above, all 241 parity
pivots at tau, and the full residual vectors are retained on disk.
The first point screen remains explicitly diagnostic. The direct failed
ansatz is retained alongside the second commutator estimate; no failed
norm estimate is omitted or promoted to a sign argument.

This is local progress beyond the specific bounds in the inspected
source passages, not a certified originality claim. The source identities
and standard linear algebra are known inputs; the direct norm computation
is not itself a new mechanism. The additional result of the original
attempt is the bounded commutator remainder in this finite cell. Its
independent critical review is completed in section8; this verification
is not a further discovery beyond the inspected sources. The original
source overlap assessment is
`drafts/literature/2026-11-04-commutator-dual-factorization-test.md`.

An inverse-free exact preimage, quantitative family control of c and
boundary overlap, uniform simple-even hypotheses, actual trial residuals,
both limiting processes, and nonzero locally uniform Xi transfer remain
unproved. Neither the very small rho nor the weaker algebraic estimate
proves a Laguerre sign, mixed positivity, or any part of RH by itself.
There is no RH candidate here.

### 8. Independent conceptual and computational audit (step366)

The prior SPECIALIZE assessment is
`drafts/literature/2026-11-04-l760-commutator-bound-audit.md`.
This audit is REPRODUCTION: it verifies the previously unaudited partial
result with unchanged cell, hypotheses and conclusions. Source identities
are imported at the precise locations above. Audited L759 remains the
only local mathematical input. No entry generator or family theorem is
reproved here; Mathlib coverage remains unchecked.

**Algebra and normalization.** The boundary row eta^T/sqrt(L) forces
xi=sqrt(L)x. Using xi instead of x in T D x=-beta would lose that factor.
The parity identities beta^T x=eta^T D x=0 give exactly (1), and
c=-(D x)^T T D x has the stated sign. The strict interval for c supplies
the extra fact needed for division. The inverse commutator identity has
the plus sign [F,T]=F[D,T]F; multiplication by x^T yields (3) with its
stated sign. Thus q=HT+r and qRP=HP+rR hold with the inverse retained.

At imaginary z, pairing j and -j gives exactly the real even and
imaginary odd Fourier rows in section4. The boundary row is purely
even, so none of the odd Fourier row is removed from q or r. Bilinear
transposes establish the algebra, whereas the Hermitian Euclidean norm
is the norm of the concatenated real even coordinates and imaginary
coefficients of the odd coordinates. The code's matrix-vector products
are transposed row products because both blocks are real symmetric.
This accounts for all 241 directions, without a parity restriction on
the argument of q.

**Spectral and residual errors.** L759 separates every nonground even
eigenvalue from the exact rational center theta by 10^-55-theta. Expansion
of the exact unit candidate w_0 in an orthonormal eigenbasis gives
||P w_0||<=delta. Choosing the sign of u so its inner product with w_0
is nonnegative gives <u,w_0>=sqrt(1-||P w_0||^2). Since
1-sqrt(1-delta^2)<=delta^2 for 0<=delta<=1, E=2delta safely bounds
||u-w_0||. The verified positive boundary interval fixes the same sign
as b(u)>0. Every division by that small interval is propagated explicitly.

Inertia at tau separates epsilon from every other eigenvalue in BOTH
blocks. The odd Rayleigh quotient bounds the least nonground eigenvalue
from above even if that eigenvalue were even. These are opposite bounds
on the same actual g. For the exact rational candidate K, s=KT-q
annihilates u because Tu=0 and qu=0. Multiplying by R gives KP-qR=sR;
the orthogonal kernel term has norm |Ku|, bounded by the even candidate
and E. This proves (4), with the LOWER gap endpoint in its denominator.
The UPPER gap endpoint is separately needed to bound rho and g||H||/||q||.
No point solve or first-order perturbation statement substitutes for
these finite-error arguments.

**Complete replay and independent arithmetic.** Run from this notebook:

    python3 scripts/spectral-triples/commutator-audit-366.py

The script copies the original program and inputs to a temporary
directory and preserves all original artifacts. Its full output
`scripts/spectral-triples/commutator-replay-366.json` matches every
original field except elapsed time, including all coordinates, residuals,
pivots, bounds, checks and arithmetic flags. Only Rounded and Inexact
flags occur. Candidates remain exact rational data, not accuracy premises.

The independent calculation uses integer endpoints on the grid 10^-440.
Fraction parsing encloses the saved input intervals. Addition/subtraction
are exact on that grid; integer floor/ceiling of all endpoint products
and quotients gives outward bounds. Divisors meeting zero are rejected;
interval squares crossing zero have lower endpoint zero. For [l/S,u/S],
S=10^440, integer square roots of lS and uS, raising the upper root when
necessary, give enclosing grid endpoints. This calculation uses no
Decimal arithmetic.

The Fourier prefactor is recomputed without the original exponential
implementation: for a=L/8 in (0,1), sum the positive sinh series through
degree199. The next term is a^201/201!; all later term ratios are <1/2,
so twice the next term bounds the positive omitted tail. Both interval
endpoints are retained. Also f=-iS is independently computed from
x^T F eta instead of inferred from ell(xi)/(k sqrt(L)). This checks the
normalization factor by a second path.

The independent inertia computation uses the fixed input B and the
unit-lower-triangular dot-product recurrence

    d_j=B_jj-sum_(r<j) H_jr^2 d_r,
    H_ij=(B_ij-sum_(r<j) H_ir H_jr d_r)/d_j.

Induction encloses the exact LDL factors. Every pivot avoids zero;
Sylvester's law gives one negative pivot among all 121 even pivots and
zero among all 120 odd pivots at tau. This differs from the original
evolving Schur-complement algorithm. All factors, pivots, normalized
vectors, residuals and rows are saved in
`scripts/spectral-triples/commutator-audit-366.json`. Every coordinate
in 32 corresponding original scalar/vector groups is also checked for
nonempty intersection with its independent enclosure. Agreement of
success flags or selected previews is not used in place of computation.

Every stated bound survives: E<1.22e-104, error (4)<2.33e9, both strict
gap/rho brackets, -1447<c<-1446, 0.02196<||r||/||q||<0.02197,
g||H||/||q||<7e-31, and direct-ansatz excess in
(2.2592e-29,2.2593e-29). The certificate reports AUDIT_PASSED with no
failures. The commutator estimate rho<0.022 remains weaker than the
certified inverse-row ratio and still retains rR. Neither estimate
supplies actual trial residuals, uniform parameters or either limit.

The first independent checker used a 10^-240 absolute grid. Squaring
the approximately 6.06e-160 ground residual on that grid lost the
precision needed for E<1.22e-104. Its stopped source and report are
preserved as `scripts/spectral-triples/commutator-audit-366-first-pass.py`
and `.json`. Increasing the independent grid precision fixes this checker
limitation without altering any original certificate or mathematical
claim. It is not evidence of a failed L760 bound. The original pending
audit status is retained in the step364 history.

## Mathlib

Full matching and supporting Mathlib coverage was not checked. Unknown
coverage is not absence. The named finite-dimensional spectral theorem
and Sylvester law of inertia are standard inputs, not claims of a Lean
formalization of this arithmetic matrix or its interval certificates.
