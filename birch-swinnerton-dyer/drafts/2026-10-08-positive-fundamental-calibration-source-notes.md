# Composite fundamental calibration — source review working record

2026-10-08. Literature-only review of the saved calibration-scope target.
No extension is proved and no lemma or mathematical script is changed.

L028 and both 2026-10-06 normalization assessments were read. They cover
prime calibration, full-relative integral generation and exact denominator
bookkeeping; Pal's cited period input already covers square-free positive d.
ATTEMPTS/022--023 remain production stops, not bans on changed scope.

The general primitive-character lead is Brandon Levin, *Modular Symbols
and L-functions*, Stanford Darmon seminar 2011, Section 7, pp. 28--30,
https://virtualmath1.stanford.edu/~conrad/DarmonCM/2011Notes/Modular%20Symbols.pdf .
The proof of Lemma 7.3 leaves the nonunit n case unfinished. Hence these
notes alone do not supply the essential composite-conductor proof case.
Proposition 7.6 attributes the value identity to Bertolini--Darmon,
*Hida families and rational points on elliptic curves*, Proposition 1.3;
that primary source is being retrieved. MTT I.8.3 is another original lead;
the Springer PDF URL redirected to an abstract page and was not read.

Outstanding review obligations: complete primitive-character statement,
nonunit-frequency case or an authoritative cited theorem covering it,
weight-two cusp orientation, primitive full L-function matching at all
finite primes, and total positive-twist period scope. No approved next
mathematical target is inferred from the seminar-note preview.

## Completed primary comparison

The essential statement was recovered in [Bertolini--Darmon, *Hida families
and rational points on elliptic curves*, Invent. Math. 168 (2007),
371--431, Section 1.1, Proposition 1.3, author PDF pp. 6--8](https://www.math.mcgill.ca/darmon/pub/Articles/Research/42.Hida-families/paper.pdf).
Its hypotheses are a normalized cusp form of even weight k>=2, a primitive
quadratic character of conductor m, 1<=j<=k-1, and
chi(-1)=(-1)^(j-1)w_infinity. It defines the symbol on the oriented
path infinity to a/m and gives the character-weighted sum as the
Gauss-sum-normalized critical value. There is no prime-m restriction.
The proof cites MTT (8.6); this is an authoritative theorem import,
not a proposed completion of Levin's unfinished nonunit proof. At
k=2,j=1 the polynomial is constant and the positive character selects
w_infinity=+1. The Shimura period in that proposition is not identified
with the Neron period. The future specialization must remove that
auxiliary normalization before using Pal. No new identity is proved here.

[Wiersema--Wuthrich, *Integrality of Twisted L-Values of Elliptic Curves*,
Documenta Math. 27 (2022), 2041--2066](https://ems.press/content/serial-article-files/29303),
Section 2, equation (6), p. 2048, independently records Birch's formula
with all residues modulo m and the oriented integral lambda(a/m).
Section 1, pp. 2042--2043, uses total real periods and explicitly gives
L(E,chi,s)=L^a(E,bar chi,s) when (m,N)=1. Section 7, pp. 2058--2059,
defines the full motivic Euler product via inertia invariants; Lemma 18
covers additive places remaining nonsemistable, and the following
paragraph identifies the extra factors when they become semistable.
Our coprime case is expressly covered; no integrality theorem or Manin
constant hypothesis is imported. Future applicability bookkeeping must
address good primes outside D, bad primes outside D, and ramified good
primes dividing D, including 2 outside odd D. Their correction-factor
case is excluded by coprimality, not silently suppressed. The quadratic
motivic twist is the Tate-module twist of E; no incomplete Clay L-series
is used for q.

Reusable [Pal v2](https://arxiv.org/pdf/1012.0094v2), Corollary 2.6 and
Theorem 3.2, already inspected in the 2026-10-06 assessment, applies to
positive square-free d, with minimalization factor one for d=1 modulo 4
coprime to Delta. Odd positive fundamental discriminants meet this scope.
The total real period, both components, and minimal differential stay
explicit. No new period proof is required.

[Stein--Wuthrich, Math. Comp. 82 (2013), Section 3.7, p. 1768](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf)
records the quadratic Gauss sum for the character of Q(sqrt(D)) as
sqrt(D) in R>0 for positive D. Its conductor-lowering assumptions are
not used as assumptions on our calibration; only this Gauss-sum convention
is reused. The primitive character is chi_D, not an arbitrary imprimitive
Jacobi symbol. Nonunits have character value zero.

## Decision and remaining mathematical work

SPECIALIZE: known primitive twisting statements and coprime full-L-series
coverage address the changed conductor. The exact relative-functional
calibration and all-generator denominator argument remain unwritten for
composite D. A later research step may import the named results and
specialize conventions; reproof of Gauss-sum theory or twist nonvanishing
is unnecessary. Compare with L028 rather than claiming a new mechanism.
The proof must explicitly handle zero character terms, sign, total period,
all finite factors and coordinate denominators; stop any uncovered part.

This review does not construct q, the full-relative line, a numerical C,
a coefficient, points or a rank comparison. L029's line premise is granted;
L031 is only a fixed benchmark. ATTEMPTS/022--023 are unchanged. Full
Mathlib coverage is not checked. The main gap remains arbitrary-curve
rational rank versus complex order >=2. A broader calibration could use
future fundamental-twist value certificates without a prime restriction;
uniform supply is still parked as SOURCE_BLOCKED.

## Search/access record

Queries: `primitive Dirichlet character modular symbols L(f chi 1) Gauss
sum twist integral theorem`; `site.wstein.org twist primitive character
modular forms Gauss sum`; `Mazur Tate Teitelbaum pdf I.8.3 twist 1986`;
`Hida families and rational points pdf`; `quadratic twist elliptic curve
L series Dirichlet character good reduction additive primes Euler factors`.
Searches located the above inspected primary statements; snippets were
not theorem evidence. No novelty is inferred. MTT Springer redirected to
an abstract; a Michigan candidate URL and GDZ viewer failed. MTT remains
unread, but its access is nonessential because the precise general identity
is available as Proposition 1.3 and equation (6). PDF screenshot calls
returned no usable displayed images; text supplied the cited passages.
No nonunit-frequency derivation was attempted or approved from Levin.

## Separate approval and URL repair (step 097)

The ready assessment lacked direct URLs in its own SOURCE_EVIDENCE field.
Retrieved the Bertolini--Darmon author PDF again: Section 1.1 definitions
and Proposition 1.3 (PDF pp. 6--8) retain primitive quadratic conductor m,
critical-index and parity hypotheses, oriented paths and auxiliary periods.
Retrieved Wiersema--Wuthrich Section 1 (pp. 2042--2043) and equation (6)
(p. 2048): the coprime-conductor full-L-series comparison and all-residue
identity remain available. Their integrality theorems are not imported.
The unchanged Pal and integral-generation coverage is reused. Direct URLs
now occur in the ready assessment itself. No missing mathematical coverage
was discovered, no new result was derived, and no new novelty search is
claimed. This is a process repair, honestly STALLED mathematically.

The saved composite-D target is unchanged. ATTEMPTS/023 concerns repeated
prime-calibration audits without input production; this approved conductor
extension is a distinct applicability test, not input production. Future
work still grants the full relative line, independent nonzero q and complete
integral presentation and must stop if any required hypothesis is uncovered.
