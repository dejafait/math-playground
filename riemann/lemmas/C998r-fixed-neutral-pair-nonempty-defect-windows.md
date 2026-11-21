# C998r: One fixed neutral pair gives nonempty defect windows

## Hypotheses

Use C744z's actual complex Hilbert space H0=ker C, closed coercive
form a0 with domain V0, representing operator A0, projection P0,
complete separation7 operator T, E=A0^-1/2, and R=E(P0 T|H0)E.
In particular ||R||<=1, E maps H0 onto V0, and the energy-coordinate
identities of C744z(2)-(3) hold. Retain its whole neutral-core and
unreplayed c_*=8.9e-18 source-computation qualifications.

Use C999l(1)'s EXACT Z:C^510->C^512 at ell=log(3)/2, raw head
indices0,...,511, and the stored dyadic centers Ahat and Bhat of
C999l(3),(6). Its audited Section7 supplies the exact-neutral/domain
and complete-error applicability. Let Bhat_1 be the first510 columns
of Bhat. Retain the inherited analytic response, IEEE754 binary64
and directed Decimal contracts; the old analytic matrices are not
independently replayed here. Both free trial vectors below are real,
separately specified members of the original complex coefficient space.

The general norm and spectral-calculus inputs are imported from
Gerald Teschl, *Mathematical Methods in Quantum Mechanics*, GSM99,
author PDF version12February2009, Lemma1.11(iv), pp47-48,
Theorem3.1, pp90-91, Theorem3.7, p96, and(3.50)-(3.51), p97:
[primary PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf).
The form/inverse-square-root applicability is already supplied by
C744z, using the same source's Theorems2.13/2.18. Assessment705
inspected the needed norm/calculus statements and proof cases. These
general theorems are not reproved or claimed new here.

## Conclusion

For the single frozen pair of free dyadic vectors alpha,beta in
`scripts/separation-seven/defect-window-fixed-pair-707-witness.json`,
define f=Zalpha and g=Zbeta, with all higher raw modes zero. Then,
under the stated inherited contracts,

    .9998 < a0(f,f),a0(g,g) < 1.0002,
    <Tf,g> > .9216,
    |<Tf,g>|^2/[a0(f,f)a0(g,g)] > .8491291032 > 3/4.       (1)

Consequently both spectral projectors

    1_{[0,1/4]}(I-R*R),  1_{[0,1/4]}(I-RR*)              (2)

are nonzero. Separate audit709 in Section4 upholds this qualified local
certificate under precisely the inherited contracts. It does not put
either whole trial vector in a defect window,
bound the signed coupling V14+R^2 on those windows, establish S3
positivity, or resolve RH. Higher/mixed endpoints, C744q/H2,
non-neutral coverage and actual-Xi transfer remain open. This is a
standard-method REPRODUCTION, not progress beyond the general
norm/spectral results checked in the literature.

## Proof

### 1. The one frozen point and exact coordinates

The witness SHA256 is
`99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a`.
It contains all510 free coefficients of each vector as exact rational
dyadics, the full source hashes and the exact analytical completion
rule. It was exclusively created before any certification. An initial
execution stopped at a missing SciPy import, before any pair existed;
the sole proposal used NumPy instead. No failed mathematical pair,
second pair selection, tau change or cutoff change occurred.

For reproducibility only, the proposal takes the first singular pair
of L^-1 Bhat_1 L^-t, with LL^t=(Ahat+Ahat^t)/2, and maps the right
and left vectors back by L^-t. None of the conclusions uses a claimed
SVD, Cholesky or linear-solve accuracy. Once frozen, the dyadics alone
specify the point; rerunning the script reuses it.

In raw coordinates the free coefficients at n=2,...,511 are unchanged.
For p=0,1 the coefficient is minus the same-parity sum r_n alpha_n
(respectively beta_n), with the EXACT r_n of C999l(1), not a rounded
moment nullspace. Thus both moments vanish exactly by C999l's
integration identity, and f,g belong to V0. The penalty256 C*C
vanishes on them. The finite actual energies and pairing are

    a0(f,f)=alpha* A alpha, a0(g,g)=beta* A beta,
    <Tf,g>=beta* B_1 alpha,
    A=Z*(D+S+256C*C)Z, B_1=Z*TZ.                       (3)

All coefficients and kernels here are real, so the displayed pairing
is real. The ambient space and the norm/spectral statements remain
complex. There is no domain equality with compact smooth or causal
generator classes, nor a claim that T preserves H0.

### 2. Complete scalar arithmetic and inherited errors

The full certificate and reproduction script are
`scripts/separation-seven/defect-window-fixed-pair-707.json` and
`scripts/separation-seven/defect-window-fixed-pair-707.py`. Run

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/defect-window-fixed-pair-707.py

The script checks all recorded561 input hashes and all original/audit
success fields. In particular the complete raw archive has SHA256
`33dbfa73fec9980e5d51d5142d2c167421bbbcebb6ed2a2b4edd3a864bfda402`,
matching534, and the saved Ahat/Bhat archive has SHA256
`f9e5288f6bc3465f690fca70d1a71537c4df5b405029e9785cd9706a9c0dcf6a`.
Its entire arrays, not sampled entries, are used. No new finite center
is assembled, so C999l(6)'s allowances apply to precisely their saved
centers. Those allowances include complete response/shift tails,
head errors, matrix-product rounding and exact-Z conversion. The
10^-7 elementary entry allowance alone would be insufficient.

Let z=1.008 and s=1.414213562373096, with s^2>2 checked rationally.
Use the following rational bounds, also compared against the complete
saved error upper endpoints:

    eta_A=.00024 z^2+10^-7,
    eta_B=s z^2*512*(2.1*10^-7)+10^-7.                  (4)

The first bounds ||A-Ahat||. The second bounds the error of the
whole two-orientation Bhat, hence also ||B_1-Bhat_1|| by restriction
to its first510 columns. No omitted-endpoint norm or infinite inverse
action is needed to evaluate finite actual pairings in(3).

Every dyadic center entry is converted by its exact integer ratio.
Using a common power-of-two denominator in each matrix and vector,
the script contracts all510^2 terms by arbitrary-precision integer
multiplication and summation. Thus the centers

    c_f=alpha* Ahat alpha, c_g=beta* Ahat beta,
    c_T=beta* Bhat_1 alpha, n_f=||alpha||^2,n_g=||beta||^2

are exact rationals, with zero new scalar rounding allowance needed.
For q=n_f n_g, the rational number

    h=(floor(sqrt(floor(q*10^160)))+1)/10^80

has h^2>=q, checked exactly. The actual scalar intervals are therefore

    a0(f,f) in [c_f-eta_A n_f,c_f+eta_A n_f],
    a0(g,g) in [c_g-eta_A n_g,c_g+eta_A n_g],
    <Tf,g> in [c_T-eta_B h,c_T+eta_B h].                (5)

The full rational endpoints, individual error charges, squared-modulus
lower bound and strict comparison are saved in the certificate.
All28 checks pass. The interval values displayed for orientation are
energies approximately[.999813570243,1.000186429757] and pairing
approximately[.921653806295,.921890094036]; these rounded displays
are not the certificate. Exact rational outward comparisons give
the simpler bounds in(1). In particular

    (.9216)^2=.84934656
        > .75030003=(3/4)(1.0002)^2.                  (6)

The complete certificate improves the squared-ratio lower bound to
>.8491291032; its exact squared-pairing lower bound exceeds the
three-quarters energy-product upper bound by >.0991660679.
The rational outward comparisons are saved separately in
`scripts/separation-seven/defect-window-text-bounds-707.json`.

### 3. Actual energy coordinates and both spectral windows

Set x=A0^1/2 f and y=A0^1/2 g. C744z's form representation gives
||x||^2=a0(f,f)>0 and ||y||^2=a0(g,g)>0. Since Ex=f,Ey=g and
g belongs to H0, bounded self-adjointness of E gives

    <Rx,y>=<E P0 Tf,y>=<Tf,g>.                         (7)

The norm duality of the cited Teschl Lemma1.11(iv), or its
Cauchy--Schwarz bound applied to these two vectors, now gives

    ||R||^2 >= |<Rx,y>|^2/(||x||^2||y||^2)>3/4.        (8)

By C744z, R is a contraction. Thus D_-=I-R*R and D_+=I-RR*
are bounded self-adjoint operators with spectra in[0,1]. If the
first projector in(2) were zero, the spectral integral of D_- would
give D_->=(1/4)I, since all of its spectral mass would be above1/4.
It would follow that R*R<=(3/4)I and ||R||^2<=3/4, contradicting(8).
The same argument for D_+ uses ||R*||=||R||, also in the cited
Lemma1.11(iv), and proves that the second projector is nonzero.
The cited bounded spectral calculus applies without compactness,
an eigenbasis, a spectral gap or an endpoint non-atomicity assumption.

This specialization proves only nonvacuity of the two fixed windows.
No positivity assumption on the full S3 block or its off-diagonal
coupling was used. A future signed-coupling estimate remains an
independent essential gap; neither(1) nor(2) supplies it.

### 4. Separate fixed-point audit — 13 November2026, step709

The invocation-start SPECIALIZE assessment707, separately approved708,
covers this audit. Assertions(1)-(2) survive without changing any
coordinate, cutoff, tau, center or allowance. This is independent local
verification of the existing REPRODUCTION, not a new general theorem
or progress beyond the norm/spectral methods cited above.

**Independent complete arithmetic.** Run

    python3 scripts/separation-seven/defect-window-fixed-pair-audit-709.py

The full evidence is `scripts/separation-seven/defect-window-fixed-pair-audit-709.json`.
The checker does not import or execute the proposal/certifier707. It
converts each individual matrix entry and each of the1020 frozen free
coordinates into a Fraction, then contracts each row separately. This
differs from707's whole-matrix common-denominator integer contraction.
All780300 matrix terms in the three scalar contractions are included.
Both norms, all three center contractions, every interval endpoint,
each error charge and all five strict-ledger rational values agree
exactly with707. All43 audit checks pass, with no failures.

The witness, original selection/certification script, complete saved
center archive, raw archive and every input hash in the707/witness/561
ledgers agree. All559 original input hashes also agree. The upstream
success records were checked for consistency, not used as substitutes
for the new scalar arithmetic; the upstream response matrices and
c_* certificate were not independently regenerated here. The exact
strict squared-pairing lower bound is approximately.849445738657346;
the required three-quarters energy-product upper bound is approximately
.750279670702551. Their exact difference exceeds.0991660679, and the
exact ratio lower bound exceeds.8491291032. These decimal displays
are explanatory; the full rational values and comparisons are saved.
All five simplified outward comparisons in the text certificate also
survive independent computation.

**Neutrality, domains and saved-center errors.** For c=+/-1/2,
direct integration of the normalized cosine mode gives

    integral_0^ell exp(cx)e_n(x)dx
      =nu_n c[(-1)^n exp(c ell)-1]/(1/4+k_n^2).

Within either parity its ratio to the p=0 or p=1 mode is exactly
C999l(1)'s r_n, simultaneously for both signs of c. Hence the exact
completion cancels both moments for each frozen free vector. Finite
support implies membership in the logarithmic form domain V; the
moment cancellation gives V0. No rounded completion or numerical
moment residual is used. C744z Section1's closed coercive restriction
therefore supplies the actual A0 and the bijection E:H0->V0. The
positive energy intervals make x=A0^1/2 f and y=A0^1/2 g nonzero.
No equality with a compact smooth generator domain is required.

The559 script assembles its saved a as Zhat^t Mhat Zhat and its
saved b as Zhat^t[That Zhat,That^t Zhat]. These are exactly C999l(6)'s
specified centers, without replacing a by its symmetrization. C744w's
response/head errors, C744z(28)'s complete T error, the exact-Z
conversion and matrix-product rounding are already included in those
audited allowances. The checker verifies that(4)'s rational bounds
dominate the full saved upper endpoints, not just elementary entry
errors. For the first-column-block injection i:C^510->C^1020,
||i||=1 and B_1-Bhat_1=(B-Bhat)i, so the full B allowance bounds
this restriction in the needed orientation. Exact row contraction
introduces no further rounding. The checked h>0 with h^2>n_f n_g
justifies the pairing radius; the two energy radii follow from the
operator-norm bound. Thus(5) applies to the actual vectors and forms.

**Both spectral conclusions.** Since Ey=g in H0, the orthogonal P0
and self-adjoint E give <Rx,y>=<E P0 Tf,y>=<Tf,g>. This uses bounded
T and E on their stated spaces, not invariance of H0 under T or an
unrestricted inverse. Cauchy--Schwarz and the positive actual energies
give(8). C744z's inherited contraction implies that both defects are
bounded self-adjoint operators with spectrum in[0,1]. If the spectral
projector for either defect on[0,1/4] were zero, its quadratic spectral
integral would be at least(1/4)||v||^2 for every v. For I-R*R this
implies ||R||^2<=3/4; for I-RR* it implies ||R*||^2<=3/4. Adjoint
norm equality contradicts(8) in both cases. This includes the endpoint
without assuming an atom, eigenvector, compactness or a spectral gap.
The cited Teschl results supply the general norm and spectral facts;
this paragraph checks only their specialization to the actual objects.

No defect-window membership of a whole trial vector, dimension estimate
beyond nonzero, signed localized coupling, full S3, H2, endpoint
complement or actual-Xi statement is inferred. All original analytic
response, neutral-core, IEEE754/Decimal and unreplayed c_* qualifications
remain. No cross-notebook result or additional mathematical input was
introduced; the DAG row is unchanged. The scalar extraction705 stop
and the different617/603/635/640/652 stops are not reopened.

## Mathlib

Full matching Mathlib coverage for this frozen numerical certificate
and its restricted logarithmic-form realization has not been checked.
The imported norm/adjoint and spectral-calculus results are the precise
primary references above. No absence claim or matching Mathlib
declaration is asserted.
