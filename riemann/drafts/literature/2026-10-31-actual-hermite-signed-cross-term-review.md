# Actual Hermite cross-term margin: source comparison

TARGET: Compare Christoffel–Darboux and Turan formulas for Romik's actual Hermite partial sums with the signed margin needed to transfer L564's derivative error to Xi'^2-Xi Xi'' on [T,2T], T>=1, N=ceil(16(T+1)^2), retaining every cross term.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Inspected the primary statements listed below after exact Hermite/CD/Turan mixed-sum searches; checked the named local Hermite assessments and parity/Pollaczek failures. No inspected theorem supplies the requested actual-truncation margin. One explicit kernel-cone coefficient diagnostic is nominated separately; no novelty or impossibility claim follows from the search.
SOURCE_EVIDENCE: NIST DLMF 18.2.12–13, Table 18.3.1, 18.9.25, 18.14.13, 18.18.23; Arzhang (2015), Theorem 3.1, proof (6)–(12), Corollary 3.2; Romik arXiv:1902.06330v3 (2.1)–(2.3), Theorem 2.7/(2.23), Appendix A.2, Chapter 7(1); O'Sullivan arXiv:2007.13582v2 (1.2)/(1.4), Theorems 1.2–1.3/1.6/8.1, Corollaries 3.7–3.8, and the application proof (8.2)–(8.5). Exact scopes and unread originals are distinguished below.
COMPARISON: CD positivity concerns its prescribed diagonal kernel; Hermite Turan concerns adjacent basis indices. Arzhang gives divided-difference identities without a signed weighted-discriminant bound. O'Sullivan's hyperbolicity families use different coefficients, while the general sufficient theorems retain unproved coefficient/root hypotheses. None automatically controls the complete D(P_N) or L564 perturbation margin.
GAP: No independent all-height signed condition is proved. A nonnegative diagonal-CD-cone representation of the complete actual-coefficient D(P_N) is a testable proposal, not an established representation with nonnegative weights; its highest coefficients and eventual signs remain uncomputed.
REASON: The source comparison clears the prior discovery gap and identifies one bounded coefficient test using accessible standard identities and ready actual-coefficient asymptotics. It parks automatic theorem transfer while leaving actual signed grouping open.
SCOPE: Completed source comparison only; no new identity, inequality, lemma or mathematical script. The separately nominated large-N kernel-cone diagnostic requires the supervisor's separate continuation approval.
LITERATURE_REASON: The prior ready assessment excludes signed margins; this turn supplies the missing primary comparison for the changed mixed-sum target, including the stronger O'Sullivan lead located during discovery.

Essential inputs: L018–L020, L564 and Romik's cited actual b_(2n)
and P_N. L233/C233a motivate the first-sign gap only. No
cross-notebook result is proposed. The normalization is Xi itself,
and N is the even-index cutoff, so P_N has degree 2N.

## Primary statements and applicability

Write D(f)=f'^2-f f''. The source comparison keeps the actual P_N
defined in L564; no Gaussian multiplication or change of height is
made. The required conclusion is a signed margin on the entire real
interval, strong enough for the full derivative perturbation.

**Standard kernels and products.** [NIST DLMF 18.2.12–13](https://dlmf.nist.gov/18.2#v)
(Szegő, *Orthogonal Polynomials*, 4th ed., Theorem 3.2.2 and
(3.2.4)) assumes an orthogonal family p_j, positive squared norms
h_j and leading coefficients k_j. It states

    K_m(x,y)=sum_(j=0)^m p_j(x)p_j(y)/h_j
      =k_m/(h_m k_(m+1))
        [p_(m+1)(x)p_m(y)-p_m(x)p_(m+1)(y)]/(x-y), x!=y,
    K_m(x,x)=sum_(j=0)^m p_j(x)^2/h_j
      =k_m/(h_m k_(m+1))
        [p_(m+1)'(x)p_m(x)-p_m'(x)p_(m+1)(x)].

The diagonal case was read explicitly. [Table 18.3.1](https://dlmf.nist.gov/18.3#T1)
fixes Hermite weight exp(-x^2), h_j=sqrt(pi)2^j j!, k_j=2^j.
These match Romik. The diagonal formula has prescribed weights,
not arbitrary pairs of truncation coefficients.

[DLMF 18.14.13](https://dlmf.nist.gov/18.14.E13), citing Skovgaard
(1954), states H_j(x)^2>=H_(j-1)(x)H_(j+1)(x) for real x and
j>=1. It is an index inequality, not D(P_N)>=0.
[18.9.25](https://dlmf.nist.gov/18.9.E25) gives H_j'=2j H_(j-1)
for j>=1; H_0'=0. [18.18.23](https://dlmf.nist.gov/18.18.E23) gives

    H_m(x)H_n(x)=sum_(r=0)^min(m,n)
        binom(m,r)binom(n,r)2^r r! H_(m+n-2r)(x).

These are standard cited algebraic tools, not a weighted sign theorem.
In particular positive linearization constants leave the alternating
coefficients and the subtraction in D unresolved.

**A derivative-CD search hit.** Asghar Arzhang, *A survey on
Christoffel–Darboux type identities of Legendre, Laguerre and Hermite
polynomials*, Mathematical Sciences 9 (2015), 193–197,
[doi:10.1007/s40096-015-0167-4](https://doi.org/10.1007/s40096-015-0167-4),
Theorem 3.1/(5), expands (H_n(y)-H_n(x))/(y-x) in products
H_i(x)H_j(y). Corollary 3.2/(13)–(14) does so for the s-th
derivative, 0<=s<=n. The proof (6)–(12) splits even/odd m+n,
uses a principal-value Hilbert-transform integral, then product
linearization. These passages were inspected. They assert identities,
not coefficient positivity or a discriminant margin. No principal-value
identity or printed coefficient formula is imported for the diagnostic.

**Actual coefficients and stronger hyperbolicity results.**
Romik [v3](https://arxiv.org/html/1902.06330v3#S2) supplies the
actual coefficients/convergence. Reuse the full proof-case assessment
in `2026-10-31-hermite-moving-degree-first-sign-review.md` for
Theorem 2.7/(2.23). Its relative error is O(log log n/log n),
with unspecified onset. Appendix A.2/(A.9)–(A.13) fixes the same
Hermite normalization. Chapter 7(1) discusses sufficient conditions,
including real-rooted monomial input, without proving that input
for the actual truncations. No coefficient-ratio conclusion is
derived here, and no differentiation of a big-O error is authorized.

Cormac O'Sullivan, *Zeros of Jensen polynomials and asymptotics for
the Riemann xi function*, [arXiv:2007.13582v2](https://arxiv.org/html/2007.13582v2),
9 December 2020, Theorems 1.2–1.3, uses

    gamma(m)=m! xi^(2m)(1/2)/(2m)!,
    P^(d,n)(X)=sum_(j=0)^d binom(d,j)gamma(n+j)H_(d-j)(X).

This differs from Romik's alternating b_(2j) truncation. Corollary
3.7 assumes real-rooted monomial input. Theorem 8.1 restates Turan's
1959 Theorem III: for real c_j, G=sum_(j=0)^d c_j H_j has simple
real zeros if sum_(j=0)^(d-2)2^j j!c_j^2<2^d(d-1)!c_d^2.
Theorem 1.3 applies this using gamma-ratio bounds, not the b sequence;
its application proof (8.2)–(8.5), including the finite-sum majorant,
was read. No such norm inequality for P_N is assumed or tested here.
Theorem 1.6 gives a stronger b_(2n) asymptotic with relative error
O(log^(3K)(n)/n^K) at fixed K and unspecified constants. Its statement
and coefficient identification in §6 were read; its full proof is
not assessed for use. Romik's ready weaker asymptotic suffices for
the nominated leading-coefficient diagnostic.

## Discovery record and access limits

Queries included `Romik 1902.06330 Hermite expansion Riemann xi
partial sums real roots Turan`, `Hermite polynomial linear combinations
Turan inequality Christoffel Darboux weighted sums`, `Hermite Laguerre
inequality linear combinations`, `Hermite Christoffel-Darboux
nonnegative linear combination`, and the exact O'Sullivan title.
Followed primary statements above. Searches returning Jensen/Taylor
coefficient signs were compared by their coefficient definitions.
No search result or third-party research portfolio is theorem evidence.

Turan's original 1959 PDF at math.bas.bg/izvestia_im/1959/1959-123-137.pdf
returned no readable text. Screenshot calls exposed only placeholders,
not inspectable page images; shell retrieval failed DNS. Search-index
text suggesting its Theorem IV is an unread lead, not an approved
theorem input. Chatterjea (1960), BUMI 15(1), 25–27, was also an
unread lead after timeout/502 responses. Neither is essential to the
selected diagnostic, which uses the accessible standard formulas.
Do not continue this route by repeating these access attempts.

Local overlap checks covered the named prior Hermite assessments,
Hermite working notes and L564 approval-loop stop. L530's two-atom
Pollaczek obstruction and L356's complete parity failure retain their
own scopes. L562's generic PF obstruction is reused from startup and
the prior comparison, without rereading its proof or importing it.
No prior diagonal-CD-cone diagnostic was found in the checked paths;
this is not a novelty claim.

## Decision and one bounded diagnostic

Park automatic CD/Turan sign transfer. Retain one independent proposal:
test whether the complete D(P_N) has a nonnegative expansion in

    K_j^H(t,t)=sum_(ell=0)^j H_ell(t)^2/(2^ell ell!),
    0<=j<=2N-1.

The normalization is sqrt(pi) times the cited standard kernel.
The proposed coefficient signs are finite algebraic conditions on the
actual b sequence, not a premise that P_N is real-rooted or signed.
No expansion coefficients or signs are calculated in this turn.
The highest two coefficients provide a bounded first test, nominated
in `2026-10-31-hermite-cd-cone-leading-coefficient-test.md`.
An eventual negative coefficient would reject this cone certificate
at arbitrarily large cutoffs, not D(P_N)>=0 or RH. If both leading
signs pass, all remaining coefficients and a quantitative margin must
still be controlled before any L564 transfer. This is conventional
algebra/asymptotic specialization; a creative sign mechanism remains
unjustified at present. All higher signs remain independent.

Mathlib coverage of the full interface was not checked. None of the
sources or this review is an independent manuscript audit. No lemma,
DAG or argument-overview change is made by this source-only step.
