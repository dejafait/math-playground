# Exceptional Toeplitz minors — prospective Fredholm comparison

TARGET: Review whether a Toeplitz-minor Fredholm identity for phi_(r,R)(z)=z^(-(r-1))G(Rz), r>=2, provides an explicit real trace-class correction and a positive prefactor whose norm bound below one would certify D_(r,r-1)>0 without assuming zero locations or minor signs.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step423 searched exact Toeplitz/Fredholm, nonzero-winding and minor terms; found and inspected Borodin–Okounkov math/9907165v1, Böttcher–Widom math/0604009v1 and Tracy–Widom math/0107118 published author PDF. Reused steps389/407/418 and L775; queries/read limits below. No novelty claim.
SOURCE_EVIDENCE: Böttcher–Widom v1 Section1/Theorems1.1–1.4, Section2/Corollary2.3, Sections3/5/6 and Remarks7.1/7.6; Borodin–Okounkov v1 Section2/Theorem1 and analytic trace-class argument; Tracy–Widom published pp.1194–1195 theorem/hypotheses; Bornemann 0804.2543v2 Section3 (3.1)–(3.5) and (4.1). Exact qualifications below.
COMPARISON: The exact nonzero-index formula retains a finite compressed inverse-Toeplitz boundary determinant, whose sign is not certified by a small Hankel correction. A zero-index formula offers a distinct conditional certificate only on a nonvanishing circle with independently established winding zero, plus real-log/prefactor and norm checks; no arbitrary-radius sign theorem follows.
GAP: No actual operator norm below one, boundary determinant sign, admissible radius for every r, growing-order uniform estimate or exceptional Xi sign has been established. The conditional zero-index specialization is saved separately for approval and later mathematical work.
REASON: Primary exact formulas supply new source-scope evidence against the unqualified shifted-minor norm transfer. Park that transfer; retain only a narrowly specified zero-index theorem application, with zero counts and norms as independent unpaid inputs.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED lacked essential shifted-minor, winding and trace-class hypotheses; this is the first primary comparison for that exact operator mechanism.
SCOPE: Completed literature-only comparison for actual G and arbitrary positive R; exact source formulas are assessed, not yet imported as local lemmas. The zero-winding conditional specialization has a separate assessment requiring approval. No lemma, mathematical script, new sign result or new proof was written.

## Main gap, comparison and selection

The main gap remains actual-Xi all-degree mixed positivity. The
intermediate aim is a concrete sufficient condition for exceptional
coefficient signs, preserving cancellations inside an operator rather
than estimating the full angular complement by its modulus. Even a
usable exceptional-sign test would leave its actual bound, other
indices and the mixed-positivity assembly unresolved.

Three mechanisms were compared in selecting this continuation:

1. The shrinking scalar core with full absolute complement is stopped
   by L775; changing its nearby cutoff exponent is not a new mechanism.
2. A collective signed saddle remains conceivable, but the existing
   step418 comparison supplies neither an explicit contour nor a paid
   phase/remainder budget. It is not selected for another vague attempt.
3. A shifted Toeplitz-minor/Fredholm factorization is selected for source
   review. Its distinct test is whether the exact finite-section or
   boundary correction can be exhibited with an independently checkable
   sufficient operator bound. No such factorization is asserted here.

The original obstruction is preserved in
`ATTEMPTS/2026-11-04-shrinking-angular-box-absolute-complement-stop.md`.
The step407 condensation/multiplier stop also remains relevant: merely
renaming an unpaid determinant or assuming a desired-sign multiplier
would not provide an independent condition. These are route comparisons,
not mathematical premises of a new result.

## Bounded source test and decision rule

Use L018/L021 for G(z)=xi(1/2+sqrt(z)/2)/8=sum a_n z^n and
D_(r,k)=det[a_(k+j-i)]. Katkova's exact identity already covers any
positive radius; this proposal does not assume the scalar saddle radius
is free of contour zeros. The prospective symbol is
phi_(r,R)(z)=z^(-(r-1))G(Rz) on |z|=1. Keep every power of R, finite
minor, normalization and possible sign when comparing conventions.

First retrieve primary statements for the Borodin–Okounkov/Geronimo–Case
Toeplitz determinant formula and a shifted-minor extension, if one exists,
then only the proof cases needed for the present symbol. These names
are search leads, not imported theorems. Check hypotheses on nonvanishing,
winding, logarithm/factorization, regularity and trace class; distinguish
a nonzero-index formula from an unshifted zero-index theorem. Neither
the zeros of G on a chosen circle nor its enclosed zero count is supplied
by L775. Any radius choice must be justified without RH or desired signs.

Continue only if the review identifies an explicit operator/boundary
formula with a genuinely independent, precise sufficient condition for
the sign: the proposed norm threshold is below one, with a positive
prefactor and real structure also justified. Verify that sufficiency
in the primary source or separately assess the elementary determinant
criterion before a future proof attempt. A finite boundary determinant
whose sign remains the original problem is an unpaid condition, not a
solution. An identity alone is not success for this target.

If the available theorem excludes the symbol, requires target-equivalent
zero information, or leaves an equivalent unsigned boundary factor,
record that exact obstruction and park this proposed transfer. Do not
try to rescue it by another absolute angular-complement bound. If a
usable test emerges, prepare its exact mathematical target and coverage
for a separate invocation; do not derive and approve it in this review.

No new mathematics was performed for this target in step422. The
coverage remains REVIEW_REQUIRED. Creative work is not yet justified:
the actual correction kernel and independent sign/error budget are
missing. A later creative nomination would require those concrete
objects and a bounded discriminator, not an administrative quota.
Mathlib matching coverage is unchecked; no cross-notebook input is used.


## Completed primary comparison — step423

The nomination above is preserved verbatim below its updated fields; its
statements that the sources are unread describe the starting state only.
The completed comparison here supersedes that pending status. This turn
performs source review, not a new theorem derivation or proof attempt.

### Primary statements and actual read limits

A. Böttcher and H. Widom, *Szegő via Jacobi*,
[arXiv:math/0604009v1](https://arxiv.org/pdf/math/0604009v1),
1 April 2006; published Linear Algebra Appl.419 (2006),656–667,
DOI10.1016/j.laa.2006.06.009. Page numbers below are v1 PDF pages.
Read pp.1–3 for the complete theorem hypotheses, p.4 Corollary2.3 and
its Jacobi proof, p.5 Section3, pp.7–8 Section5's full inverse/projection
argument, pp.9–10 Section6/Remark7.1 and p.13 Remark7.6. Also inspected
Remark7.4's factor normalization; it is not needed if (1) is retained.
The alternative Carey–Pincus comparison and block extension are not
imported; their cited original proofs were not read.

The source uses T_n(f)=(f_(i-j)) and f=z^gamma a with a nonvanishing,
zero-winding C^beta symbol, noninteger beta>1/2. Its (1) fixes

    a_-=exp(sum_(j>=1) ell_(-j) z^(-j)),
    a_+=exp(sum_(j>=0) ell_j z^j),  ell=log a,
    b=a_-/a_+,  c=a_+/a_-,  K=H(b)H(tilde c),
    H(b)_(i,j)=b_(i+j-1),  tilde c(z)=c(1/z),  i,j>=1.

P_m retains coordinates1,...,m and Q_m=I-P_m. The p.2 singular-value
argument shows each Hankel factor is Hilbert–Schmidt and K is trace
class. Theorem1.1 and Theorem1.2's expression for E give

    D_n(a)=g(a)^n E(a) det(I-Q_n K Q_n),
    g(a)=exp(ell_0),
    E(a)=exp(sum_(j>=1) j ell_j ell_(-j)).

Here g(a) is the paper's scalar G(a), renamed to distinguish our entire
G. This identity is exact, unlike the asymptotic statement of Theorem1.2.
No pointwise-positive symbol is required for the identity; a complex
prefactor and a complex determinant are possible under its hypotheses.

For kappa>0, Theorem1.3 additionally requires T_(n+kappa)(a) invertible:

    D_n(z^(-kappa)a)=(-1)^(n*kappa) D_(n+kappa)(a) F_(n,kappa)(a),
    F_(n,kappa)(a)=det_[P_kappa ell2]
       P_kappa (I-H(b)Q_n H(tilde c)Q_kappa)^(-1)
                 T(z^(-n)b)P_kappa.

The determinant is a kappa by kappa compression, not the determinant
of an identity minus the displayed Hankel correction. Corollary2.3
identifies the same boundary factor as the last kappa rows and first
kappa columns of the finite inverse T_(n+kappa)(a)^(-1). Its finite
Jacobi proof is the relevant algebraic case and does not create a
positive boundary factor. Section5 retains this compression throughout.
Remark7.1 uses norm<1 to justify a Neumann inverse; it does not remove
T(z^(-n)b) or give a sign for its compressed determinant. Theorem1.4
retains a boundary Toeplitz determinant even in the asymptotic main
term. Its proof fixes the symbol and kappa: no simultaneous growing-r,
growing-shift, varying-radius estimate is supplied. Remark7.6 handles
positive winding by transposition and still retains a boundary factor.

A. Borodin and A. Okounkov, *A Fredholm determinant formula for Toeplitz
determinants*, [math/9907165v1](https://arxiv.org/pdf/math/9907165v1),
Section2/Theorem1, pp.1–4; published Integral Equations Operator
Theory37 (2000),386–396. Read the analytic statement and trace-class
estimate: the symbol is exp(V), with a Laurent logarithm analytic on
an annulus containing the circle (constant term removed by scaling).
The double-contour kernel has exponentially summable entries. Its
formal-power-series version is a separate setting, not an analytic
license to take log of a nonzero-index symbol. The later Schur-function
proof and examples were not needed or imported; Section3's opening
was inspected only to identify that proof method.

C. A. Tracy and H. Widom, *On the limit of some Toeplitz-like
determinants*, SIAM J.Matrix Anal.Appl.23 (2002),1194–1196,
[author PDF](https://www.math.ucdavis.edu/~tracy/selectedPapers/2000s/CV69.pdf),
DOI10.1137/S0895479801395367. Read pp.1194–1195's exact statement,
uniform finite-section invertibility requirement and Schur-complement
proof opening. This concerns fixed finite row/column perturbations and
an asymptotic finite determinant, not a uniform growing shift. The last
page of its proof was not read; no theorem application is claimed.
Bump–Diaconis was located as a related asymptotic lead but its primary
paper was not read or used.

F. Bornemann, *On the numerical evaluation of Fredholm determinants*,
[0804.2543v2](https://arxiv.org/pdf/0804.2543v2), Section3, pp.9–10,
(3.1)–(3.5), and p.12 (4.1); Math.Comp.79 (2010),871–915.
Read the trace-class product, finite-rank approximation, Plemelj
exponential and invertibility characterization, plus trace-norm
continuity. In particular (3.3) supplies the norm-small trace expansion
needed to assess a future real-operator sign argument. No selfadjoint
positivity assumption may silently replace the real-operator check.
Lemma4.1's stronger positive-selfadjoint setting is not our input.
A proof of the actual-symbol logarithm-symmetry specialization remains future work.

### Comparison with the actual coefficient minor

Reuse step418's checked Fourier normalization: the determinant of
z^(-k)G(Rz) is R^(k*r)D_(r,k), up to transposition of the matrix,
with k=r-1. R>0 makes this radius factor positive. All ordinary
coefficient factorials remain in G, as fixed by L018/L021/L775;
no moment-Gram replacement is made.

The source requires contour nonvanishing before a logarithm or index
can be assigned. The argument principle is the standard interface for
counting enclosed zeros; neither a scalar saddle radius nor G(R)>0
certifies a whole circle. At an arbitrary R the necessary winding
information is not supplied. A nonzero-index reduction cannot be
assumed to have zero shift. Even after a valid reduction, Theorem1.3
retains a sign-bearing boundary determinant and finite-section
invertibility. Calling that determinant a positive prefactor would
assume what must be proved. The proposed unqualified norm transfer is
therefore parked. This is a source-scope negative, not a theorem that
all Fredholm methods fail or a proof that the actual norm is large.

There is a distinct conditional branch worth isolating: circles on
which nonvanishing and exactly r-1 enclosed zeros, counted with
multiplicity, are independently certified. Assessing that branch does
not assert that such a circle exists for every r; tied moduli and
multiplicities can matter. It uses the zero-index theorem for the
whole shifted symbol, rather than declaring the shifted-minor boundary
factor positive. The conjugation-compatible normalized logarithm, positive g^r E, exact
radius normalization and determinant sign criterion must be verified
in a separate mathematical specialization. Even after that verification,
the actual norm<1 and enough admissible radii would remain unpaid.
No actual coefficient sign is obtained in this review.

### Search, overlap, decision and continuation

Queries: `Böttcher Widom Toeplitz determinants nonzero winding number
exact formula minors Borodin Okounkov`; `Toeplitz minors Fredholm
determinant Bump Diaconis Tracy Widom formula`; `Szegö via Jacobi arxiv`;
`A Fredholm determinant formula for Toeplitz determinants Borodin
Okounkov pdf`; and norm/real-Fredholm variants. Retrieved primary
statements before the longer Section5 proof. Search snippets and
secondary accounts were leads only. Geronimo–Case's priority is reported
by Böttcher–Widom; its 1979 paper itself was not read or imported.

Local comparisons: step389 already supplies the signed angular identity;
step418 rules out an automatic varying-symbol Szegő import; step407
retains an unpaid finite determinant in condensation. L765 concerns a
different q-Pascal perturbation norm on k=1024r, and L775 concerns the
shrinking-core/full-complement modulus budget. None establishes the
present Hankel correction norm or bans the conditional zero-index case.
These are contrasts, not mathematical dependencies. No sibling notebook
was read. Mathlib matching coverage is unchecked, not asserted absent.

The threshold remains operator norm strictly below1, with trace class,
real structure and positive prefactor proved first. Continue only with
the separate conditional-certificate specialization in
`2026-11-04-zero-winding-fredholm-certificate-specialization.md`, after
its newly written coverage receives separate approval. Its bounded test
is whether every stated sign/normalization step follows under explicit
zero-count hypotheses without using minor signs or RH. If an additional
unpaid sign appears, abandon that certificate. Actual norm estimation
would be a later, separately assessed target; it is not authorized here.

No justified creative norm attempt is ready yet: the conditional
actual-symbol interface has not been verified and no independent
uniform norm estimate has been identified. That precise blocker takes
precedence over the discovery scheduling preference. All-degree mixed
positivity, other exceptional orders and RH remain open.
