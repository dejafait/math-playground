# Corollary C874c: both formal contacts pass ordinary degree-seven positivity

## Hypotheses

Take separately the two logarithmic prefixes of C874b:

1. S_k=2 for 2<=k<=7;
2. S_2=3 and S_k=2 for 3<=k<=7.

In each case S_1 is free. Define finite formal coefficients and moments by

    a_j=[z^(2j)] exp(-sum_(k=1)^7 S_k z^(2k)/k),
    m_j=(-1)^j(2j)! a_j,                     0<=j<=7,
    A_3=(m_(i+j))_(0<=i,j<=3),
    B_3=(m_(i+j+1))_(0<=i,j<=3).

The exponential is used only through degree fourteen. No global
characteristic function or actual-theta realization is assumed.

## Conclusion

For **each** prefix, S_1=16>0 makes both A_3 and B_3 positive definite.
The moments m_0,...,m_7 therefore have a positive finite atomic
probability representation on [0,infinity). Equivalently, there is a
probability law of u>=0 with E[u^(2j)]=m_j for 0<=j<=7, whose normalized
cosine transform has these logarithmic coefficients through S_7.

Thus this degree-seven ordinary probability restriction excludes
neither formal positive-flux contact. This is a specialization of known
truncated-moment theory with explicit finite data, not a new moment
theorem or an actual-theta result. C874b's prescribed auxiliary
extension S_8=2 is **not** established for a representing probability
law here; m_8 and the law's S_8 are unprescribed. No compatibility at
all orders, actual heat trajectory, contact existence or RH conclusion
follows. The independent critical audit below found no error within
this finite scope.

## Proof

### Exact coefficient extraction

Put y=z^2. Differentiating the formal exponential gives

    a_0=1,
    n a_n = -sum_(k=1)^n S_k a_(n-k),          1<=n<=7.       (1)

Only coefficients S_1,...,S_n occur at stage n, so no discarded term
with k>=8 can affect this computation. With S_1=16, (1) and the stated
factorial normalization give the following complete moment lists.

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

For each column the full matrices, with no unspecified entries, are

    A_3 = [[m_0,m_1,m_2,m_3],
           [m_1,m_2,m_3,m_4],
           [m_2,m_3,m_4,m_5],
           [m_3,m_4,m_5,m_6]],
    B_3 = [[m_1,m_2,m_3,m_4],
           [m_2,m_3,m_4,m_5],
           [m_3,m_4,m_5,m_6],
           [m_4,m_5,m_6,m_7]].

Their exact leading principal determinants, in increasing corner size,
are as follows. Each required threshold is **strictly greater than zero**.

| prefix/matrix | size 1 | size 2 | size 3 | size 4 |
|---|---:|---:|---:|---:|
| first / A_3 | 1 | 2024 | 47818387968 | 32047441048690659164160 |
| first / B_3 | 32 | 6085056 | 22170797473628160 | 3171834202320787053983721062400 |
| second / A_3 | 1 | 2012 | 45759617664 | 27742027033267458785280 |
| second / B_3 | 32 | 5973744 | 20391579281571840 | 2526910082682282506355690700800 |

These matrices are real symmetric. The standard named Sylvester
criterion therefore proves positive definiteness of each of the four
matrices from these strictly positive leading minors. No PSD conclusion
is inferred merely from nonnegative leading minors.

The exact arithmetic can be reproduced with

    python3 scripts/heat/contact_ordinary_moment_2132.py

The standard-library Fraction calculation writes complete coefficients,
moments, full matrices, all leading determinants, required thresholds
and failures to `scripts/heat/contact-ordinary-moment-2132.json`.
It checks (1) against the independent truncated product

    product_(k=1)^7 sum_(r=0)^floor(7/k) (-S_k/k)^r y^(kr)/r!
        modulo y^8,

and checks every determinant by both exact elimination and the Leibniz
permutation formula. It also recovers S_1,...,S_7 from m_0,...,m_7
using the triangular inverse of (1). All checks pass with no failures.
Both complete case records, including every coefficient and matrix
entry, and the complete failures array were inspected with
`../scripts/loop/inspect_json.py` at `/cases/0`, `/cases/1` and
`/failures`, using `--full` for these selected values. This is an exact
finite certificate, not a floating eigenvalue or a numerical preview.

### Imported representation theorem and normalization

Use Raul E. Curto and Lawrence A. Fialkow, *Recursiveness, Positivity,
and Truncated Moment Problems*, Houston Journal of Mathematics
**17**(4) (1991), 603-635, **Theorem 5.1, printed p625**, and the
following paragraph's explicit positive-invertible case:
https://www.math.uh.edu/~hjm/v017n4/0603CURTO.pdf.
The invocation-start source assessment is
`drafts/literature/2026-11-21-contact-ordinary-moment-compatibility-2130.md`;
its primary statement and essential proof-case coverage are reused.
No new representation theorem is being proved.

Specialize the theorem's ordinary Stieltjes data to gamma_j=m_j,
k=3, gamma_0=1. Its A(k) and B(k) are exactly A_3 and B_3 above,
with support interval [0,infinity). Both matrices are positive and
invertible. In particular the extra range column
(m_4,m_5,m_6,m_7)^T lies in Ran A_3, which is all of R^4; no singular
range condition is omitted. The theorem supplies a positive finite
atomic representing measure nu on [0,infinity), of total mass m_0=1.
Push nu forward by x -> sqrt(x) to obtain the asserted law of u>=0.

Because this law is finite atomic, its cosine transform

    h(z)=E[cos(zu)]

is entire, has h(0)=1, and has coefficients (-1)^j m_j/(2j)!=a_j
through z^14. It thus agrees with the defining formal exponential
modulo z^16. The germ log h with value zero at zero has the same
coefficients through z^14 as that exponential's logarithm. This proves
the claimed finite prefix and does not assert any higher coefficient.
L058/L874's actual-theta normalization explains why these are the
ordinary u^2 moments relevant to the original restriction; a measure
nu or its square-root pushforward need not equal that theta law.

### Scope of the negative result

The unchanged C874b contact data have formal flux 16>0. This calculation
shows that adding only the existence of an ordinary probability law
with the specified moments through m_7 cannot exclude either prefix.
It does not supply one law simultaneously realizing the prescribed
S_8=2 auxiliary extension: that condition would involve m_8, outside
the tested matrices. Neither auxiliary atoms representing logarithmic
moments nor ordinary atoms representing m_j are identified with the
actual theta density. Parameter compatibility, actual contact and
flux signs, initialization, equality, and global/all-degree closure
remain unresolved. The main gap L030-L032/C032a is unchanged.

### Independent critical audit — 21 November 2026, step2134

The two witnesses and the finite representation conclusion pass the
approved independent audit. This is verification of the local
specialization and exclusion stop, not a new moment theorem or an
advance beyond the checked sources. No hypotheses or mathematical
conclusions above have changed.

`python3 scripts/heat/contact_ordinary_moment_audit_2134.py` imports no
code from the original program. For each n=0,...,7 it independently
enumerates all nonnegative multiplicities r_1,...,r_7 with
sum k r_k=n and sums

    product_(k=1)^7 (-S_k/k)^(r_k)/(r_k!).

The finite multinomial expansion proves that these are exactly the
exponential coefficients a_n. Every coefficient and factorial-normalized
moment agrees with the original complete certificate and both printed
moment columns. Independently evaluating the finite series

    log(1+v)=sum_(r=1)^7 (-1)^(r+1) v^r/r modulo y^8,
    v=sum_(j=1)^7 a_j y^j,

recovers (16,2,2,2,2,2,2) and (16,3,2,2,2,2,2). Terms r>=8 have
order at least eight and cannot affect any tested coefficient. Thus
the inverse test does not reuse the original triangular recurrence.
All matrix entries and real symmetries were checked. Fraction-free
integer Bareiss elimination, with exact division checked at every
stage, reproduces all sixteen leading determinants in the table;
each is strictly greater than the required threshold zero. The
original code's elimination and permutation determinant formulas
were also inspected. Its replay produces byte-identical original
certificate contents.

The complete independent coefficients, logarithm coefficients,
moments, matrices, leading minors and comparison flags are saved in
`scripts/heat/contact-ordinary-moment-audit-2134.json`. Both full
case records and the complete empty failures array were inspected
with `../scripts/loop/inspect_json.py --full` at `/cases/0`, `/cases/1`
and `/failures`; replay identity, exit code and stderr were also
inspected in full. All sixteen strict sign checks pass, with no
arithmetic, table, normalization or replay discrepancy.

For source applicability the primary Theorem 5.1 statement,
equations (5.1)-(5.2), and its explicit positive-invertible paragraph
were reopened at printed p625. The relevant finite-atomic support
argument in Theorem 4.1's proof, pp622-623, was also reopened,
reusing the prior assessment's essential proof-case coverage rather
than reproving the imported theorem. Screenshot calls returned no
inspectable page images; no fresh visual glyph verification is claimed.
The nonsingular paragraph is legible and sufficient for this audit,
independently of ambiguous OCR signs in the general criterion.
Here gamma_0=1>0, k=3, A(k)=A_3 and B(k)=B_3 are both strictly
PD and hence invertible; the column (m_4,m_5,m_6,m_7)^T is in
Ran A_3=R^4. The supplied measure has nonnegative support and
mass one. No theorem about merely nonnegative leading minors,
singular inverse, or prescribed eighth moment is being invoked.

Under x->sqrt(x), its jth ordinary moment becomes E[u^(2j)]=m_j.
Finite atomicity makes h(z)=E[cos(zu)] entire and h(0)=1. If E(z)
denotes the defining exponential, coefficient agreement gives
h(z)-E(z)=O(z^16) near zero. Both functions are nonzero on a
sufficiently small disk, and h/E=1+O(z^16). The logarithm germ
at one therefore gives log h-log E=O(z^16), with both logarithms
zero at zero. This checks precisely the asserted degree-fourteen
logarithmic prefix. No global nonvanishing or interchange of
infinite integrals is needed. L058/L874's normalized positive theta
law has the same cosine factorial convention; it need not be this
finite atomic law. In particular the index m_j here means the
u^(2j) moment, not L874's subscripted raw u moment.

The auxiliary C874b atoms encode S_2,...,S_8, whereas this ordinary
law is certified only through m_7. Its actual next logarithmic
coefficient depends on m_8, which is not prescribed by this audit.
Consequently the phrase positive-flux contact refers to a formal
prefix whose flux is determined through S_7; it does not establish
that the same ordinary law also satisfies the prescribed H_3
extension with S_8=2. The finite restriction is parked, while that
simultaneous compatibility question, actual theta, parameter tilts,
actual contact/flux signs, initialization, equality and global closure
remain open. The audit introduces no additional mathematical input
and requires no DAG or argument-overview change.

## Mathlib

Full matching coverage is not checked, including Curto-Fialkow's
truncated Stieltjes theorem and these prescribed-prefix witnesses.
Supporting coverage of Sylvester's criterion, formal power-series
operations and finite atomic integration is also unchecked; no absence
is claimed. Reference: https://leanprover-community.github.io/mathlib4_docs/.
