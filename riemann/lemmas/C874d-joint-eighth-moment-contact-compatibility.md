# Corollary C874d: both contacts pass joint ordinary compatibility through S_8

## Hypotheses

Take separately the two full formal logarithmic prefixes of C874b:

1. S_1=16 and S_k=2 for 2<=k<=8;
2. S_1=16, S_2=3 and S_k=2 for 3<=k<=8.

Define

    a_j=[y^j] exp(-sum_(k=1)^8 S_k y^k/k),
    m_j=(-1)^j(2j)! a_j,                         0<=j<=8,
    A_4=(m_(i+j))_(0<=i,j<=4),
    B_3=(m_(i+j+1))_(0<=i,j<=3).

Here y=z^2. The exponential specifies only the finite coefficients
through z^16; its full function is not asserted to be a characteristic
function. No actual-theta realization is assumed.

## Conclusion

For each prefix, A_4 and B_3 are positive definite, and there is a
positive finite atomic probability measure nu on [0,infinity) with
moments m_0,...,m_8. The pushforward by x->sqrt(x) has a normalized
cosine transform h(z) whose logarithm germ at zero satisfies

    log h(z)=-sum_(k=1)^8 S_k z^(2k)/k + O(z^18).

Thus one ordinary probability law for each case simultaneously
realizes the full prescribed prefix, including S_8=2, that defines
C874b's auxiliary H_3>=0, H_2 c=0 and formal flux Phi=16>0. The
ordinary law and the auxiliary logarithmic moment measure are distinct
objects; they are not identified. Adding ordinary probability
compatibility through m_8 to this auxiliary contact premise excludes
neither example at S_1=16.

This is a finite specialization of known moment theory and a negative
test of that exclusion route. It does not construct the theta density,
a common heat trajectory, or an actual contact. No signs for the
actual family, all-order representation, invariant cone or RH result
follow. The independent critical audit below found no error within this
finite scope.

## Proof

### Exact prescribed coefficients and matrices

The formal identity E'(y)=-E(y)sum_(k=1)^8 S_k y^(k-1) gives

    a_0=1,
    n a_n=-sum_(k=1)^n S_k a_(n-k),             1<=n<=8.    (1)

Only S_1,...,S_n enter stage n. The lower coefficients and moments
coincide with C874c's audited data, since adding the term with k=8
cannot change them. The complete moment lists, with both new eighth
entries, are:

| j | first prefix: m_j | second prefix: m_j |
|---|---:|---:|
| 0 | 1 | 1 |
| 1 | 32 | 32 |
| 2 | 3048 | 3036 |
| 3 | 480480 | 474720 |
| 4 | 105369600 | 102814320 |
| 5 | 29540367360 | 28336815360 |
| 6 | 10069614213120 | 9451312960320 |
| 7 | 4037455266324480 | 3689859436623360 |
| 8 | 1859834232358502400 | 1646693332245561600 |

In particular a_8=4000066/45 in the first case and
a_8=453331207/5760 in the second. Multiplication by 16! gives
the displayed m_8 values, with positive sign.

All entries of the two matrices are specified by these lists:

    A_4 = [[m_0,m_1,m_2,m_3,m_4],
           [m_1,m_2,m_3,m_4,m_5],
           [m_2,m_3,m_4,m_5,m_6],
           [m_3,m_4,m_5,m_6,m_7],
           [m_4,m_5,m_6,m_7,m_8]],
    B_3 = [[m_1,m_2,m_3,m_4],
           [m_2,m_3,m_4,m_5],
           [m_3,m_4,m_5,m_6],
           [m_4,m_5,m_6,m_7]].

Their leading principal determinants are exactly:

| prefix/matrix | size 1 | size 2 | size 3 | size 4 | size 5 |
|---|---:|---:|---:|---:|---:|
| first / A_4 | 1 | 2024 | 47818387968 | 32047441048690659164160 | 1113320215666725432364725174570634444800 |
| first / B_3 | 32 | 6085056 | 22170797473628160 | 3171834202320787053983721062400 | — |
| second / A_4 | 1 | 2012 | 45759617664 | 27742027033267458785280 | 792393220741088901384242612269586841600 |
| second / B_3 | 32 | 5973744 | 20391579281571840 | 2526910082682282506355690700800 | — |

Every listed determinant is strictly greater than the required bound
zero. The matrices are real symmetric, so the standard named
Sylvester criterion proves that all four are positive definite.
Nonnegative leading minors alone would not suffice for a PSD decision;
here all minors in the strict criterion are positive.

### Imported even Stieltjes criterion

Use Raul E. Curto and Lawrence A. Fialkow, *Recursiveness, Positivity,
and Truncated Moment Problems*, Houston Journal of Mathematics
**17**(4) (1991), 603-635, **Theorem 5.3, printed pp626-627**:
https://www.math.uh.edu/~hjm/v017n4/0603CURTO.pdf.
Its statement and complete essential proof were inspected in the
invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-21-contact-joint-eighth-moment-review-2134.md`.
This theorem is imported, not reproved.

For real gamma_0,...,gamma_(2k), gamma_0>0, the theorem supplies a
positive representing measure on [0,infinity) precisely when

    A(k)=(gamma_(i+j))_(i,j=0)^k >=0,
    B(k-1)=(gamma_(i+j+1))_(i,j=0)^(k-1) >=0,
    (gamma_(k+1),...,gamma_(2k))^T in Ran B(k-1).

Finite atomic representation is included. Singular matrices are
allowed by the theorem; its range qualification must be retained.
Specialize gamma_j=m_j and k=4. The initial mass gamma_0=m_0=1
is strictly positive; A(k)=A_4 and B(k-1)=B_3 are both positive
definite. Hence Ran B_3=R^4 and the column

    v=(m_5,m_6,m_7,m_8)^T

belongs to that range. For additional exact verification, the program
records the following solutions to B_3 q=v, with the common denominator
in each row applying to all four numerators:

    first q = (-4515752751821095680,
                192518530198606080,
                -1857734766859104,
                5721433136496) / 5164225291;

    second q = (-10943217259009823932489936080,
                 475499290956877065938028480,
                 -4697270560306343513497752,
                 14878444773974024956464) / 13878122568316374391.

Both products B_3 q-v are the zero vector exactly. Thus the full even
criterion is satisfied, and nu exists with total mass m_0=1. No
singular inverse, unspecified extension moment or untested range
condition is used. This result does not require the separate matrix
Schur-complement criterion.

### Cosine normalization and simultaneous finite interpretation

Push nu forward under x->sqrt(x) to obtain a finite atomic probability
law rho on [0,infinity). It satisfies E_rho[u^(2j)]=m_j, 0<=j<=8.
Its cosine transform h(z)=E_rho[cos(zu)] is a finite sum of entire
functions with h(0)=1. Its coefficients through z^16 are
(-1)^j m_j/(2j)!=a_j, exactly as in L058/L874's normalized convention.

Let E(z)=exp(-sum_(k=1)^8 S_k z^(2k)/k). The even entire functions
h and E therefore satisfy h-E=O(z^18). On a sufficiently small disk
both are nonzero and h/E=1+O(z^18). Taking the logarithm germs with
value zero at zero gives log h-log E=O(z^18). This proves all eight
prescribed logarithmic coefficients for the same ordinary law. It
does not infer a global logarithm or equality with E outside that
finite coefficient range, nor vanishing higher logarithmic coefficients.

C874b gives the auxiliary measures 2 delta_1 and delta_0+2 delta_1,
respectively, which encode these S_2,...,S_8 and make H_3>=0.
Its null vectors (-1,1,0) and (0,-1,1) satisfy H_2 c=0, and its
finite heat recurrence gives Phi=16 in both cases, independent of
S_1. Fixing S_1=16 retains that calculation. Since the ordinary law
just obtained has the very same finite S prefix, it satisfies these
auxiliary algebraic contact restrictions as well. Auxiliary masses
are not ordinary probabilities or u atoms. No equality of these
measures is needed or asserted.

The formal value Phi=16 exceeds the desired upper bound zero. It is
only the value prescribed by that finite recurrence, which L874
identifies with an actual flux under its additional actual-family
hypotheses. Those hypotheses have not been realized by rho. Thus the
calculation stops the exclusion based on these joint finite premises;
it neither refutes an actual-theta sign theorem using more structure
nor proves or disproves RH. The main gap L030-L032/C032a persists.

### Exact verification and limits

Reproduction command:

    python3 scripts/heat/contact_joint_eighth_2136.py

The standard-library Fraction program writes the full certificate to
`scripts/heat/contact-joint-eighth-2136.json`. It checks (1) against
the independent finite product

    product_(k=1)^8 sum_(r=0)^floor(8/k) (-S_k/k)^r y^(kr)/r!
        modulo y^9,

and independently computes log(1+v) by its eight finite powers,
v=sum_(j=1)^8 a_j y^j. Terms of power >=9 cannot alter the tested
coefficients. Recovering -k[y^k]log(1+v) gives exactly the two specified
prefixes through S_8. All lower moments agree with both the original
C874c certificate and its independent step2134 audit.

Every leading determinant is checked by exact elimination and a
separate Leibniz permutation sum. The full B_3 q-v residuals vanish.
All eighteen required strict minors pass; there are no failures.
Complete case records, including all coefficients, logarithms,
moments, matrix entries, determinants, range columns, solutions and
residuals, were inspected using `../scripts/loop/inspect_json.py` with
`--full` at `/cases/0` and `/cases/1`, together with `/failures`.
This supplies exact finite arithmetic, not floating eigenvalue evidence
or an independent critical audit of the new mathematical write-up.

Actual-theta identification, compatibility as continuous parameter
tilts of that specific density, actual contact existence and signed
flux, initialization, equality handling and global/all-degree closure
remain unresolved. No degree sweep or parameter sweep was performed.

### Independent critical audit — 21 November 2026, step2138

The two complete prescribed prefixes pass the approved independent
audit. This accepts the joint finite exclusion stop; it is verification
of a local specialization of known moment theory, not a new moment
theorem or an actual-theta signed result. The mathematical argument,
hypotheses and conclusions above are unchanged.

Run `python3 scripts/heat/contact_joint_eighth_audit_2138.py`.
This program imports no code from the original calculation. To compute
a_n it enumerates all nonnegative integer multiplicities r_1,...,r_8
with sum k r_k=n and sums

    product_(k=1)^8 (-S_k/k)^(r_k)/(r_k!).

The finite multinomial expansion of the exponential proves this formula;
terms of weighted degree greater than eight cannot enter any tested
coefficient. It reproduces all nine coefficients and every
factorial-normalized moment in each complete table column, including
the printed a_8 values and m_8. It independently checks the logarithm
by the multiplicity formula

    [y^n]log(1+sum_(j=1)^8 a_j y^j)
      = sum_(sum j r_j=n, r=sum r_j>0)
          (-1)^(r+1)(r-1)! product_j a_j^(r_j)/(r_j!).

This is the multinomial expansion of log(1+v); for n<=8, powers
v^r with r>=9 cannot contribute. It recovers the full prescribed
(16,2,2,2,2,2,2,2) and (16,3,2,2,2,2,2,2), without using the
original coefficient recurrence or its repeated-polynomial-power code.

Integer Bareiss elimination, with every division checked to be exact,
independently reproduces all eighteen leading minors. They agree with
both the complete certificate and the printed table, and each exceeds
the required bound zero. Every matrix entry and real symmetry was
checked. Thus Sylvester's strict criterion applies to A_4 and B_3
in both cases; no inference from nonnegative leading minors is made.
Cramer's rule, using separately evaluated integer determinants with
each B_3 column replaced by v, reproduces both full range solutions.
After rational reduction, their common numerators and denominators
agree with those printed above. All eight entries of the two complete
B_3 q-v residuals are exactly zero. No discrepancy was found.

The complete independent coefficients, logarithm coefficients, moments,
matrices, minors, Cramer determinants, solutions and residuals are in
`scripts/heat/contact-joint-eighth-audit-2138.json`. Both complete case
records and the empty failures array were inspected with
`../scripts/loop/inspect_json.py --full` at `/cases/0`, `/cases/1`
and `/failures`. The original generator and both original complete
case records were also inspected. No replay of the original generator
or new primary-source extraction is claimed for this audit.

For theorem applicability, reuse the inspected Theorem 5.3 statement,
complete proof and support/singular-case coverage in the ready
step2137 assessment
`drafts/literature/2026-11-21-contact-joint-eighth-audit-review-2136.md`
and its step2135 source assessment. The exact citation is Curto and
Fialkow (1991), Theorem 5.3, pp626-627, as given above. Its real data
are gamma_j=m_j, gamma_0=1>0, k=4, A(k)=A_4, B(k-1)=B_3,
and its required column is exactly (m_5,m_6,m_7,m_8)^T. The now
independently certified strict PD implies both nonnegative matrix
conditions and Ran B_3=R^4; the explicit residual checks agree.
The imported theorem includes finite atomic nonnegative support, so
the mass-one probability conclusion follows without a singular inverse,
an unprescribed moment, or a reproof of representation theory.

The normalization was checked directly against L058 and L874:
under x->sqrt(x), E[u^(2j)]=m_j, and the cosine coefficient is
(-1)^j m_j/(2j)!. Finite atomicity supplies entire h and h(0)=1.
The coefficient agreement and evenness therefore give h-E=O(z^18),
not merely O(z^16). Continuity supplies a disk where both functions
are nonzero; the logarithm germs vanishing at zero have difference
O(z^18). This proves all eight coefficients for one law in each case;
the two cases need not share a law. Neither global logarithmic
equality nor vanishing higher coefficients is inferred.

C874b's auxiliary measures represent S_(j+2), whereas the ordinary
measure represents m_j. Their distinct roles and the unchanged formal
flux 16>0 are retained. The finite logarithm match does not identify
either law with the theta density or identify a formal contact flux
with an actual-family flux: that transfer requires L874's additional
actual-family hypotheses. Actual theta, parameter compatibility,
contacts/signs, initialization, equality and global/all-order closure
remain unresolved. The fixed joint finite exclusion is parked; no
degree or parameter sweep was performed. Mathlib coverage remains
unchecked as qualified below.

## Mathlib

Full matching coverage is not checked for Theorem5.3 or these finite
prefixes. Supporting coverage for Sylvester's criterion, finite
power-series algebra, matrix range solutions and finite atomic
integration is also unchecked. No absence is asserted. Reference:
https://leanprover-community.github.io/mathlib4_docs/.
