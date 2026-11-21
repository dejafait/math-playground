# C998x: Fixed-Gram signed Schur threshold and direct-density cost stop

## Hypotheses

Keep C998r's frozen real f=Zalpha,g=Zbeta, C999l's exact completion
as used there, C998s's h=P0Uf, and C744z's complete operators T,U
and neutral form a0 on V0. Here ell=log(3)/2. All512 raw modes,
334 separation14 shifts, identity2187, full K14 and both exact P0
moments remain. The witness is
`scripts/separation-seven/defect-window-fixed-pair-707-witness.json`,
SHA256 `99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a`.
Independent triple scalars are arbitrary complex numbers.

Retain the analytic-response, neutral-core, IEEE754/Decimal and
unreplayed c_* source qualifications. C998r/audit709's already
certified actual scalar intervals are inputs; their old numerical
matrices and error estimates are not regenerated here. C998u(5)-(9)
and audit726 supply the COMPLETE derivative measure and nonnegative
exponential energies, including every density, atom and self term.

Invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-13-prefix-gram-preflight-review-744.md`
covers this standard-method preflight. Import Jean Gallier,
*The Schur Complement and Symmetric Positive Semidefinite (and
Definite) Matrices*,24August2019, Proposition2.2 p4 and the
congruence factorization pp2-4,
[primary PDF](https://www.cis.upenn.edu/~jean/schur-comp.pdf).
The complex bounded-block setting is Dritschel--Rovnyak,
*The Operator Fejer-Riesz Theorem*, arXiv:0903.3639v1,
AppendixA LemmaA.1/full proof pp28-29,
[primary PDF](https://arxiv.org/pdf/0903.3639v1).
Assessment744 inspected these statements and proof directions.
Only their application below is derived; they are not reproved.

For the attempted evaluation, reuse719's inspected Trefethen,
*Is Gauss Quadrature Better than Clenshaw-Curtis?*, SIAM Review50
(2008),67-87, Theorem4.5/(4.14) p77, Gaussian proof pp79-80,
[primary PDF](https://people.maths.ox.ac.uk/~trefethen/CC.pdf),
and723's Beylkin--Monzon, ACHA19(2005),17-48,
Section5.3/(39)-(42), pp34-35,
[primary PDF](https://www.colorado.edu/amath/sites/default/files/attached-files/bey-mon-2005.pdf).
The former requires analytic integrands on the entire enclosing
ellipse; the latter starts with a discretized source. Neither is
assumed to supply a quadrature error, finite work bound or precision.

## Conclusion

Put F=a0(f,f), G=a0(g,g), p=<Tf,g>, q=C(0)=||h||_2^2,
t=<Tg,h>, E=a0(h,h). All six quantities are real. The actual
Hermitian Gram for (af,bg,ch) is

    M=[[F,-p,-q],[-p,G,-t],[-q,-t,E]].                 (1)

Its leading block B2 satisfies, under the retained contracts,

    lambda_min(B2)>389/5000=.0778,
    det B2>3737901/25000000=.14951604.                 (2)

For a_j=2j+1/2 and mu=Dh, define the EXACT finite expression

    L256=d0 q+sum_(j=0)^255 Q_(a_j)/a_j^2,
    Q_a=integral integral exp(-a|x-y|)dmu(x)dmu(y).

Then E>=L256. A sufficient condition for M to be positive definite
on the coefficient space C^3 is

    L256 > (G q^2+2p q t+F t^2)/(FG-p^2).             (3)

The signed 2pqt term is retained. No value of either side or its
margin is established. This fixed-span criterion does not prove
C744z(4)'s all-vector S3 positivity.

ONE proposed aggregate prescription uses32 Gauss density nodes per
open breakpoint panel and direct, shift-by-shift raw-mode evaluation
of the complete density, then256 ordered exponential sweeps. Its
mandatory mode multiplications alone are

    32*510*55725=909432000>100000000.                  (4)

Thus it fails the total-work cap before quadrature, precision,
storage, signed entries or any scalar batch are paid. The favorable
product count alone would permit at most3 nodes per panel with this
direct evaluation organization; no assertion about their accuracy
follows. This is a failed specified prescription, not a complexity
lower bound for coefficient aggregation, different quadrature or
variational certificates. No actual Gram sign or RH claim results.

## Proof

### 1. The signed matrix and the leading-block hypothesis

C744z(5) gives the three-cell form on independent scalar multiples
of the prescribed profiles. Its three cross terms are

    -2Re[p a conj(b)+t b conj(c)+<Uf,h> a conj(c)].

The form is linear in its first argument. All kernels, profiles and
projection moments are real, so p,t are real. C998s(2) gives
<Uf,h>=||h||_2^2=q: it is NOT zero merely because h is neutral.
This proves (1), with the opposite entries conjugate as required
for arbitrary complex a,b,c. No middle minimization occurs here.

The complete exact rational intervals used by C998r/audit709 imply
F,G>.9998 and 0<p<.922. The new small script checks the upper
pairing bound against the FULL saved interval endpoint, rather than
against its displayed decimal preview. For all a,b in C,

    F|a|^2+G|b|^2-2p Re(a conj(b))
       >=(min(F,G)-p)(|a|^2+|b|^2)
       >(.9998-.922)(|a|^2+|b|^2).

Also FG-p^2>(.9998)^2-(.922)^2. These two rational comparisons
give (2). In particular B2 is positive definite, not merely
invertible or nonnegative. The old leading-entry intervals have
errors larger than1e-6; they suffice for (2), but are not advertised
as meeting the proposed all-entry numerical error contract.

### 2. Exact Schur specialization and outward error direction

The off-diagonal column below B2 in (1) is v=(-q,-t)^t.
Its inverse is

    B2^-1=(FG-p^2)^-1 [[G,p],[p,F]].

The imported Schur criterion applies by (2), and gives
M>0 exactly when E>v*B2^-1v. This debt is the right side of (3).
For clarity, Gallier's real symmetric conclusion also holds on complex
coefficients: for z=x+iy, z*Mz=x^tMx+y^tMy. Thus no real-scalar
restriction is introduced in applying that theorem to this real matrix.
Both signed cross entries involving h remain; taking only q or
only t would change the test. In particular t has not been replaced
by |t|, and the possibly cancelling product pqt has its actual sign.

C998u(8) and its audited monotone limit give E>=L256 without a
two-sided approximation of the omitted j>=256 energies. The local
d0 q remains exact, without discarding it or assigning a favorable
sign. Replacing ONLY E by L256 decreases M by the nonnegative
matrix diag(0,0,E-L256). Thus (3) is sufficient.

For a future numerical use, a valid lower enclosure L_- and an
upper enclosure D_+ of the COMPLETE signed rational debt, over
joint enclosures for F,G,p,q,t with positive determinant, would
give the strict sufficient test L_- - D_+>0. Signed interval
arithmetic must enclose 2pqt, not discard it. Errors in q enter
both d0 q and the cross entry; the outward directions must cover
both uses. Independent overenclosures may lose sharpness but are
safe. No such enclosures,1e-6 entry ledger or Schur margin have
been computed. A nonpositive lower margin could only reject this
sufficient comparison, not prove an actual negative triple.

### 3. Freeze one aggregate evaluation organization

Use C998u(5)-(6)'s exact entrance and exit breakpoints and outer
endpoints. On each resulting open piece, select32-point Gauss
quadrature of the entire smooth density b. At each proposed node,
evaluate f'(x+d_n) by its raw-mode sum for EVERY active shift;
evaluate the full K14 derivative contribution and BOTH projection
corrections as well. No shift-pair correlation array is assembled.
Every atomic contribution, both outer traces, coincident-location
merging and the central self-interactions would be retained in the
subsequent aggregate measure and256 strict-left/right sweeps.
All entries, C(0), constants and moment enclosures would also need
certification. These are obligations, not supplied evaluation services.

The order32 is a single frozen ordinary high-order panel proposal,
not a minimum order proved sufficient. It is not selected from
computed errors or a parameter sweep. Its ERROR sufficiency is
irrelevant to the mandatory cost obstruction below. No nodes or
weights were constructed. In particular smooth b alone does not
make exp(-a|x-y|) analytic across x=y inside a self-panel; the
analytic Gauss theorem cannot silently pay that interaction.

### 4. Exact breakpoint inventory and mandatory work

An interior entrance for n>2187 is log(n)-14ell; an interior exit
for n<2187 is log(n)-13ell. C998u gives distinctness, including
entrance/exit comparisons, and identity2187 has no interior event.
There are333 events and334 open panels. For z=log(n)-a ell,

    exp(2z)=n^2/3^a.

Thus every event-order comparison is an exact integer comparison:
z1<z2 iff n1^2*3^a2<n2^2*3^a1. The script enumerates prime
powers by primality and exact powers and the strict squared bounds
3^13<n^2<3^15. It checks all334 integers, identity2187, all333
interior locations, and every adjacent strict ordering; no rounded
logarithms are used. Initially exactly n<=2187 are active. At each
entrance add n, and at each exit remove n. Summing the334 exact
active counts gives55725 shift/panel incidences. A separate count
sums, for each shift, its number of active panels from its event
rank and agrees. The full event list, active sets and counts are
saved in the certificate.

C998s Section1 verifies that all510 free coefficients at indices
2,...,511 are nonzero. Exact Z changes only indices0 and1. Their
derivative coefficients are also nonzero because these indices
are positive. Even granting precomputed derivative coefficients,
nodes, weights, shifts and sine values at ZERO cost, the frozen
direct density evaluation multiplies each of these510 coefficients
by its sine value at each of32 nodes on each active shift/panel.
This gives (4). The omitted index1, every addition, all full-K14
and projection work, atoms, sorting, sweeps, local energy, signed
cross entries, rounding, output and replay can only increase work.
The count is for this direct organization; algebraic coefficient
updates or reused sum identities are different algorithms.

The per-common-order product count is510*55725=28419750;
floor(100000000/28419750)=3. This arithmetic consequence is not
a test or approval of a lower-order prescription. No retuning
was performed. With32 nodes the excess is809432000. Failure of
this necessary work condition parks the prescription before any
claim of complete error, precision or byte bounds. In particular
no memory or bit-complexity conclusion is inferred.

### 5. Evidence, preserved failures and scope

Run `python3 scripts/separation-seven/prefix-gram-preflight-745.py`.
It writes `scripts/separation-seven/prefix-gram-preflight-745.json`:
346/346 checks pass, no failures. The script verifies only the
integer inventory/counts, retained witness hash and selected exact
old interval comparisons; it does not revalidate the old analytic
matrices, responses or c_* computation. No energy, density node,
Gram or large numerical batch was run.

This changes the decision for the new direct-density aggregate
prescription independently of stops720/722's piece-pair products,
724's two-sided tail demand, and743's uniform-kernel production
bundle. Those failures remain. The one-sided prefix avoids their
particular tail-approximation requirement, but does not pay density
preparation. Existing stops705 and C744z(26)/(30) are neither
discarded nor treated as global prohibitions.

The result is REPRODUCTION: local specialization and an informative
implementation-specific negative, not mathematics beyond the checked
block and numerical-analysis sources. Full S3, uniform control of
V14+R^2 against both defects, defect-window localization, other
entries/endpoints, C744q/H2 and actual-Xi/global assembly remain open.

## Mathlib

Full matching coverage for this prescribed fixed-profile Gram,
prefix application and finite cost certificate is not checked.
No supporting Mathlib theorem was used or independently inspected
in this step. Unknown availability is not evidence of absence.
