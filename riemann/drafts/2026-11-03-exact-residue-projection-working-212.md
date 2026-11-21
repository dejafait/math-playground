# Actual negative-angular projection attempt — step 212

Invocation-start scope: the supplied EXPLORE assessment
`drafts/literature/2026-11-03-exact-pole-residue-angular-gram.md`, its
covered target, and the supervisor's explicit research approval. One
mathematical attempt only; no source refresh is needed.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
for the unchanged fixed L703/L708 family, prove
`||P_-c_0||_2^2/D >= c^2*n^2*exp(-n/16)` on an unbounded subsequence,
with fixed positive c and original L666 D. Contractive projection would
then feed L666's conditional H bridge. Global charge, support,
realization and signs would remain independent gaps.

Continue only with the displayed estimate or a quantitative intermediate
estimate that identifies its remaining exponential loss. Stop this
attempt if it yields only unevaluated coordinates, ambient norm costs
or uncontrolled sums. A failed sufficient projection test is not a
refutation of the full E_0/D target or RH.

Inputs read: L666 Sections 1--4; L703 hypotheses/conclusion and
Sections 4--5; L708 hypotheses/conclusion; L725 hypotheses/conclusion
(accepted interior limsup only, not an angular coercivity input).
C645p Section 1 is a comparison: the scalar projection interface is
to be justified directly. L700 and L701's recorded common-sign and
bulk-pairing failures, and the low-moment origin stop, are preserved.
No cross-notebook input, profile approximation or changed masses.

Pending calculation: set p_j=-80*j/(121*n), take the actual residues
rho_j of the complete scalar c_0, and use the cited finite
Takenaka--Malmquist basis. Retain the signed sum before taking each
coordinate square; compare the joint norm to original D. All source
theorems are imported as assessed, not claimed as new discoveries.

Status at this checkpoint: unfinished; no quantitative bound or new lemma.

## Completed bounded attempt

These are intermediate working calculations, not a new canonical lemma
or an accepted quantitative input. The completed part specializes the
already assessed finite basis and Fourier identities. No actual residue
vector is replaced by an arbitrary one.

Set J=n-1, beta=d/U=80/121, p_j=-beta*j/n and

    r_(j,a)=Res_(u=p_j) W_a(u),
    rho_j=R^(-1)*sum_(a in Z_n) r_(j,a),
    f_-(u)=sum_(j=1)^J rho_j/(u-p_j).

The exact L666 product has no interior poles except these distinct
simple p_j, all with |p_j|<beta<1. Its other possible poles a/t_j
have modulus at least d>1; zero is regular. Cancelled poles have zero
residue, and W_x=1 has none. Thus c_0-f_- is holomorphic on a
neighborhood of the closed unit disk. For each fixed n,

    1/(u-p_j)=sum_(ell>=0) p_j^ell*u^(-ell-1), |u|=1,

converges absolutely and uniformly. The holomorphic remainder has only
nonnegative modes, so P_-c_0=f_- exactly. The constant mode is in the
remainder. This directly justifies the scalar interface without
assuming C645p audited or interchanging a limit in n.

Import scalar Fourier orthogonality/Parseval from A. Levitt, *Analyse
de Fourier et applications*, Theorem 1.3/Exercise 1.2 and Theorem
1.11/Corollary 1.12, printed pp.6,8, in the version already inspected
on 2 November 2026 ([author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf));
and the residue/simple-pole rules from R. W. Howell--J. H. Mathews,
*Complex Analysis*, [Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html).
All circle measures here are normalized by 2*pi. These are standard
inputs, not newly proved theorems.

Import the finite orthonormal system from P. S. C. Heuberger, T. J.
de Hoog, P. M. J. Van den Hof and B. Wahlberg, *Orthonormal basis
functions in time and frequency domain: Hambo transform theory*, SIAM
J. Control Optim. 42 (2003), 1347--1373, Proposition 2.1 and
(2.1)--(2.2), p.1350 ([author PDF](https://publications.pvandenhof.nl/Paperfiles/SIAM2003.pdf),
[DOI](https://doi.org/10.1137/S0363012902405340)):

    Phi_k(u)=sqrt(1-p_k^2)/(u-p_k)
                    *product_(l<k)(1-p_l*u)/(u-p_l), 1<=k<=J.

The real distinct poles meet the source's strictly interior condition.
Its exterior-analytic, vanishing-at-infinity convention is the negative
mode convention here. Phi_k lies in the span of (u-p_j)^(-1), j<=k,
and its p_k pole is not cancelled. Triangularity gives the whole finite
J-dimensional span. No infinite completeness or separation assumption
is used.

Use the inner product linear in the first argument and set
b_k=mean_u f_-(u)*conjugate(Phi_k(u)). On the circle,

    conjugate(Phi_k(u))=sqrt(1-p_k^2)*u/(1-p_k*u)
                          *product_(l<k)(u-p_l)/(1-p_l*u).

The finite residue rule with du/(2*pi*i*u) now gives

    b_k=sqrt(1-p_k^2)*sum_(j=k)^J
        rho_j/(1-p_k*p_j)*product_(l<k)(p_j-p_l)/(1-p_l*p_j), (A)
    ||P_-c_0||_2^2=sum_(k=1)^J |b_k|^2.                    (B)

For j<k the corresponding numerator zero removes the term. All displayed
denominators are nonzero; a cancelled rho_j contributes zero. Thus each
full signed sum is retained before its square. No polewise absolute or
least-eigenvalue replacement is made.

To test whether the actual algebra pays the norm, keep the exact spatial
sum and put

    C_n(u)=product_(j=1)^J(u-p_j),
    Q_n(u)=C_n(u)*c_0(u)
      =R^(-1)*sum_(a in Z_n) (x/a)
        *product_(l=1)^J [(x-t_l*u)/(a-t_l*u)]
        *product_(l=1)^J (u-t_l*a/U).

Q_n is rational and holomorphic on |u|<d, not generally a polynomial.
The anchor term is exactly C_n/R. At each p_j,
rho_j=Q_n(p_j)/C_n'(p_j). Substitution in (A) cancels just the l<k
factors and leaves the complete expression

    b_k=sqrt(1-p_k^2)*sum_(j=k)^J
        Q_n(p_j)/[product_(k<=l<=J,l!=j)(p_j-p_l)
                         *product_(l=1)^k(1-p_l*p_j)].      (C)

This is a divided difference of order J-k of the actual function
Q_n(u)/product_(l=1)^k(1-p_l*u). Here that terminology denotes exactly
the finite sum (C), not an imported estimate. The proposed use of the
triangular system was to bound the whole sum (B). Distinct nodes and
positive spatial masses do not supply that bound: the difference
denominators alternate in sign, and the actual Q_n values still contain
complex signed spatial sums. The anchor vanishes at every p_j. No
lower magnitude or favorable sign has been obtained for the complete
coordinates. Even an independently justified reflection symmetry would
only give reality, not positivity. L700/L701 are scoped contrasts, not
premises of a claim that (B) is small.

The original-D comparison cannot be replaced by a negative-mode
diagonal. For each a let f_a=P_-W_a, F_a=W_a-f_a and let b_(k,a)
be the analogous coordinates before the R^(-1) spatial sum. Orthogonal
decomposition gives

    b_k=R^(-1)*sum_a b_(k,a),
    D=sum_a [sum_k |b_(k,a)|^2+||F_a||_2^2]/(U-|a|^2).     (D)

Every denominator is positive. The anchor has f_x=0 and F_x=1,
contributing 1/(U-d^2) to D. Dropping the ||F_a|| terms would make
the proposed lower ratio easier and would not prove the original target.

For an explicit remaining rate, L661's recorded audited diagonal
envelope, quoted also in L666 Section 6, states

    D<=n*exp(2*kappa*n+6)/(3*sigma^2),
    kappa=91/5000, sigma^2=137/5000,
    1/16-2*kappa=261/10000.

A sufficient outcome would therefore be, for a fixed C_*>0 on an
unbounded subsequence,

    sum_k |b_k|^2 >= C_* n^3 exp(-261*n/10000).             (E)

Division by the recorded D bound would give the required ratio with
c^2=3*sigma^2*exp(-6)*C_*. The corresponding norm scale is
sqrt(C_*) n^(3/2) exp(-261*n/20000). These are sufficient thresholds,
not necessary conditions or achieved estimates. No lower bound at
this scale, or paid intermediate lower rate for the complete sum, was
obtained. The only immediate lower bound supplied by this calculation
is zero; this does not imply the actual projection is zero or too small.

## Decision and limits

Outcome EXPLORATION; classification REPRODUCTION. The basis
specialization is known mathematics. The quantitative actual-vector
estimate is unresolved, with no new informative negative, admissible
countersequence, uniform coercivity input, novelty claim or RH candidate.
Stop this coordinate closure as prescribed by the gate: the signed
sums remain uncontrolled. Reopening needs a materially new estimate
relative to original D, not another basis, absolute residue sum,
ambient least eigenvalue or continued origin value.

No mathematical script or numerical screen was needed. No lemma,
PROOF or DAG changed. Full matching Mathlib coverage for this
specialization and quantitative target was not checked; general
Hilbert-space support would not prove (E).

One independent nomination is the original constant angular coefficient
mu_n=mean_u c_0(u), where the anchor survives, with proposed subsequence
threshold |mu_n|>=exp(-n/100). This is not the rational continued
value c_0(0). The low-moment origin stop distinguishes those quantities;
C645o/C645p have relevant but unaudited identities. The narrowly checked
working records do not establish the mean bound for the fixed L703
profile. This nomination is REVIEW_REQUIRED. No asymptotic estimate or
noncancellation of mu_n is derived or approved here.
