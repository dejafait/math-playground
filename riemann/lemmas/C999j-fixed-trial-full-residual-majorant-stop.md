# C999j: The fixed-trial full-response coercivity majorant fails

## Hypotheses

Use ell=log(3)/2 and the exact f,g,h of C744z Section8, equations
(19)-(20),(26), with N=512 and denominator 2^40. The free integer
arrays are `scripts/separation-seven/response-prefix-direction-546.json`,
SHA256 `f39d45d9754d0415f5180e2cb5803d8152bfbaba3eb34130b4bf4b91b81da013`.
In particular h is the reflection of f and g has only even modes.
These are fixed data; no optimization or finite inverse is used.

Use C744z's restricted closed form a0 on V0 in H0=ker(C), its
representing operator A0, P0, K=P0 T|H0 and b=Kf+K*h. Retain
the full bounded S and T of C744v, the full separation14 U of
C744z, and c_*=8.9e-18. The c_* source computation remains unreplayed,
as qualified in C744z/L741. The neutral form/core construction has
not been independently audited as a whole. The particular strong-trial
applicability is checked below; no original causal generator domain
membership is asserted for a finite cosine vector.

Import the standard coercive self-adjoint resolvent bound from
Gerald Teschl, *Mathematical Methods in Quantum Mechanics*, author-hosted
GSM99 version, Theorem2.18/proof, printed p77 (317-page PDF), with
the form representation of Theorem2.13, printed pp71-72:
[author PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf).
These inputs were inspected in assessments541/542 and549. They are
not reproved here. Full analytic-response and entry-error contracts
of C744v/w and C744z Section9 are inherited, including directed
Decimal elementary operations and the stated IEEE754 entry contract.
No new source floor or numerical supplement is imported.

## Conclusion

The fixed g belongs to Dom(A0), and the full strong residual
r=b-A0g is well defined. For the exactly neutral vector

    w=e_2-r_2 e_0, r_2=sqrt(2)(1/4)/(1/4+k_2^2), k_2=2pi/ell,

the complete pairings give the strict outward bounds

    -.072313 < <r,w> < -.072157,
    1.00000727428 < ||w||^2 < 1.00000727429,
    ||r||^2 > .00520666,
    ||r||^2/c_* > 5.85018e14 > .094207.                 (1)

Hence the standard sufficient certificate

    ||r||^2/c_* < Q_actual(f,g,h)                       (2)

fails on these fixed data: the audited actual trial energy is in
(.093538,.094207). This rejects only the specified c_* residual
majorant. It neither lower-bounds the actual inverse correction by
5.85018e14 nor signs the exact minimized energy. No negative actual
triple, H2 witness, all-endpoint sign or RH conclusion follows.
This is a local REPRODUCTION of a standard residual method, with an
informative negative feasibility result under inherited contracts;
no novelty beyond the sources checked is claimed. The separate step552
audit below upholds this fixed-data rejection under the stated contracts.

## Proof

### 1. Particular operator-domain applicability

D is the real logarithmically growing diagonal operator in C744v's
orthonormal cosine basis. Finite cosine g lies in Dom(D). Since S
is bounded on L2, Dg+Sg is an L2 vector. For every v in V0 the
closed-form pairing is

    a0(g,v)=<Dg+Sg,v>=<P0(Dg+Sg),v>.

The characterization of the representing operator in Teschl
Theorem2.13 therefore gives g in Dom(A0) and
A0g=P0(Dg+Sg). This does not require V0 to be invariant under D+S,
and does not identify a restricted inverse with a projected inverse.
The bounded T makes b an H0 vector, so r is in H0.

The moment ratios explicitly integrated in C744z(19)-(20) give
both exponential moments of e_2 equal to r_2 times their respective
moments of e_0. Thus w is exactly in H0 and, being a finite cosine
vector, also in V0. It follows, with the first-slot-linear convention,

    <r,w>=<Tf,w>+<Tw,h>-a0(g,w).                       (3)

All vectors here are real. In particular <K*h,w>=<h,Kw>=<Tw,h>;
P0 disappears only against already neutral arguments. The entire
S in a0 and the entire T occur in (3).

### 2. Complete bilinear error ledger

Use the pinned audited archive `scripts/separation-seven/complete-covariance-532.npz`.
Let M be its `m0` matrix and B=`mc`+`mg`. M approximates the
compression of D+S+256C*C. Both g and w are exactly neutral, so
the exact penalty pairing vanishes. Its entry roundoff is still
included in the allowance below. B approximates the full T, with
both its active prime translations and its continuous infinite tail.

Here is the bilinear specialization of C744w(12)-(15), the same
entry bounds used in C744z(27). Set k_n=n*pi/ell,
nu_0=ell^(-1/2), nu_n=sqrt(2/ell) for n>0, C0=131072.5, and

    rho_n=sqrt(2)/[6(64.25^2+k_n^2/4)],
    t_n=C0^-2+2k_n^2[1/(6C0^3)+C0^-4],
    E_nn=rho_n+2nu_n^2 t_n,
    E_nm=nu_n nu_m(k_n rho_n+k_m rho_m)/|k_n^2-k_m^2|
          for n!=m of the same parity,
    E_nm=0 for opposite parities.

These include the full non-exponential response remainder; the
elementary allowance includes the other response tails, penalty
and diagonal evaluation error. Consequently

    |a0(g,w)-<Mg,w>|
       <=10^-7 ||g||_1 ||w||_1 + sum_nm E_nm |g_m w_n|, (4)
    |<Tx,y>-<Bx,y>|<=2.1e-7 ||x||_1 ||y||_1.           (5)

The 1-norms in (4)-(5) are finite coefficient norms, not spatial
L1 norms. Equation(4) follows directly by multiplying every
entry-error bound by |g_m w_n| and summing; no quadratic error bound
is assumed to extend bilinearly without justification. Equation(5)
is C744z(28), including addition roundoff and the complete continuous
tail. It is used for (x,y)=(f,w) and (w,h). The unretained coefficients
of both operands are exactly zero, so these pairings need no omitted
output-mode estimate. No finite response prefix has replaced S.

All stored binary64 matrix entries are converted exactly to Decimal,
and every scalar product is summed with directed 80-digit intervals.
The exact dyadic free coefficients are enclosed directly, the two
low coefficients by their exact moment-ratio formulas. Machin's
identity with 80 arctangent terms encloses pi; widened correctly
rounded logarithm and square root enclose ell and normalizations.
The source files and archive match their audited pins. The complete
certificate includes every contributing entry allowance and all
coefficient intervals. Coarse strict bounds on its three centers
and errors are

    .9948446641895 < <Mg,w> < .9948446641896,
    error in (4) < .000075781,
    .4613049468456 < <Bf,w>,<Bw,h> < .4613049468457,
    each error in (5) < .000000765.

The full, tighter directed intervals in the certificate give

    -.072312080263 < <r,w> < -.0721574607336,
    |<r,w>|^2/||w||^2 > .0052066612648.

Cauchy--Schwarz in L2 yields ||r||^2>=|<r,w>|^2/||w||^2,
proving (1). The required pairing magnitude for this lower-bound
screen to exceed c_*.094207 is less than 9.156683e-10;
the actual lower bound .0721574607336 is already decisive.

Reproduce with

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/fixed-trial-residual-550.py

The full certificate is `scripts/separation-seven/fixed-trial-residual-550-80.json`;
all checks pass and failures is empty. Its
`residual_norm_squared_lower` and `residual_majorant_lower` contain
enclosures of the calculated lower-bound quantities, not two-sided
enclosures of the full norm. No actual full residual norm is computed.

### 3. Meaning of rejection

Let g_*=A0^-1 b. By C744z(6), subtracting the minimized energy from
the fixed-trial energy gives

    Q_actual(f,g,h)-Q_min(f,h)
        =||A0^(1/2)(g-g_*)||^2=<A0^-1 r,r>.

The imported resolvent bound A0>=c_*I gives
0<=<A0^-1r,r><=||r||^2/c_*. Thus (2) would be sufficient for
Q_min>0. But (1) and Q_actual<.094207 show (2) is false.
The inequality for the inverse correction is an UPPER bound; its
being too large cannot imply Q_min<=0. The full remote U remains
in Q_actual through the audited Section8 enclosure. It is absent
from (3) because U has no middle variable, not because its energy
has been discarded. Stop this fixed-majorant test at the first
screen, with no retuning of g,c_* or a response prefix.

### 4. Independent fixed-data audit — 12 November2026, step552

The prior SPECIALIZE assessment550 authorizes only this audit. Its
conclusion is upheld, retaining every analytic/runtime qualification in
the hypotheses. This is local REPRODUCTION and independent verification
of a recorded obstruction, not a new inequality beyond the checked
sources. No trial, floor or response prefix has been changed.

**Domains and adjoints.** C744v defines D as a real semibounded diagonal
operator and S as a bounded positive operator. A finite cosine vector
belongs to Dom(D), hence its D form pairing with any v in V is the L2
pairing with Dg; adding S preserves this equality. Exact neutrality
from C744z(19)-(20) puts g in V0. Therefore the representation theorem's
criterion applies on H0 with representing vector P0(Dg+Sg), proving the
particular strong-domain assertion. This uses neither invariance of V0
under D+S nor membership in a causal-generator domain. The restricted
closed-form/coercivity construction remains an inherited input; the
whole construction has not been independently audited here.

Bounded T and real neutral f,h,w give
<P0Tf,w>=<Tf,w> and <K*h,w>=<h,Kw>=<Tw,h>.
The last equality uses reality; for arbitrary complex data the conjugate
must be retained. Thus (3)'s two distinct orientations are correct. The
two integrated exponential moments in C744z(19)-(20) prove exact
neutrality of w and of the trial, independently of small numerical
moment defects. U has no middle variable and is absent from the residual;
its complete contribution remains in the audited Q_actual enclosure.

**Every entry allowance.** C744w(12) controls D's analytic error by
rho_n; its response diagonal has the independent integral-tail bound
2nu_n^2 t_n. For unequal same-parity entries, multiplying (13) by
2nu_n nu_m gives exactly the E_nm in Section2. At opposite parity the
response and D entries vanish, while the elementary10^-7 still pays
the stored penalty and rounding. Summing these entry errors against
|g_m w_n| proves (4) directly, including each equal-index case. The
finite supports justify terminating this bilinear sum without estimating
unretained output modes. Both separation7 pairings use their full T
entry ledger and the addition allowance, giving (5). The true moment
penalty is zero, but its evaluated entry errors are still paid.

**Independent arithmetic.** Reproduction commands are

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/fixed-trial-residual-550.py 100
    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/fixed-trial-residual-audit-552.py

The first preserves the80-digit certificate and saves the100-digit replay
as `scripts/separation-seven/fixed-trial-residual-550-100.json`. The second
saves the full independent certificate as
`scripts/separation-seven/fixed-trial-residual-audit-552.json`.
It imports no interval arithmetic implementation: integer endpoints at
110 decimal places use exact outward integer/rational operations.
Machin's alternating series encloses pi; independently,
ell=sum_(j>=0)(1/2)^(2j+1)/(2j+1) is enclosed by200 terms with tail
at most (1/2)^401/[401(1-1/4)]. Square roots use integer isqrt with
outward endpoints. These elementary arithmetic identities verify the
constants rather than reprove the imported operator theorems.

The independent enclosures of all2048 coefficients lie inside their
original80-digit intervals. The script verifies exactly the512
contributing entry allowances, including their complete index coverage,
diagonal cases and strict off-diagonal gaps. Their upper endpoints,
and those of all three total bilinear allowances, are dominated by
the original saved upper bounds. Lower endpoints of upper-allowance
calculations are not incorrectly required to nest across precisions.

Each of the three stored-matrix products is accumulated separately as
an exact integer sum over a common dyadic denominator, with independent
coefficient enclosures. If x0,y0 are rational coefficient points with
L1 errors ex,ey and Mmax bounds the absolute contributing entries,
the coefficient uncertainty is bounded by

    Mmax (||x0||_1 ey+||y0||_1 ex+ex ey).

This follows by expanding the two coefficient errors in the bilinear
product and the triangle inequality. All2560 contributing matrix terms
are used; all other terms have an exactly zero operand. Each rational
enclosure lies in the original saved center interval. The binary64
addition error for Mc+Mg is independently below10^-8 on every used
entry. Archive, generator, interval implementation and direction hashes
match the prior pins; all original artifacts remain unchanged.

The independent rational products plus the independent analytic
allowances give, by exact rational comparisons,

    -.072312080263 < <r,w> < -.0721574607336,
    |<r,w>|^2/||w||^2 > .0052066612648,
    ||r||^2/c_* > 5.85018e14 > .094207.

The squared required pairing threshold is checked without a rounded
square root: c_*.094207 times the upper enclosure of ||w||^2 is less
than (9.156683e-10)^2, which is less than the squared pairing lower
bound. All3621 audit checks pass and failures is empty. The complete
coefficient intervals, entry allowances, exact matrix sums, uncertainty
bounds and rational comparison values are in the audit certificate.

Finally, Section3's comparison direction is correct. The coercive
resolvent theorem upper-bounds the inverse correction by ||r||^2/c_*;
the large lower bound on that proposed majorant rejects (2), and says
nothing adverse about the inverse correction or Q_min. The audited
trial enclosure (.093538,.094207), not a value with U removed, is the
threshold. This ends the fixed scalar-majorant test. No sign for the
actual minimized energy, uniform endpoint comparison, H2 witness or
RH follows, and the c_* source computation remains unreplayed.

## Mathlib

Full matching coverage for this restricted residual specialization
and fixed-data certificate has not been checked. Hilbert-space
Cauchy--Schwarz, closed-form representation and spectral bounds are
standard supporting mathematics; no specific Mathlib theorem or
formal verification of the arithmetic runtime is asserted. Unknown
coverage is not evidence of absence.
