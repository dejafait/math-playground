# First-zero preservation: source comparison2257

21 November2026. Literature-only completion of nomination2256. No
new kernel identity, sign, zero enclosure or lemma is proved here.

The main gap is L030-L032/C032a actual-Xi all-degree algebraic mixed
positivity. The intermediate question is a first-real-zero removal
invariant for strict kernel log-concavity. Such an invariant could
supply a shape input for iteration, but would still leave actual-K
hypotheses, later-removal strictness and the all-degree interface open.
A counterexample would reject only the generic invariant, not RH.

## Exact target and comparison

Keep review2256's full hypotheses: K is positive, even and smooth on R;
(log K)''<0 everywhere; for every m>=0 and B>0,
exp(B|u|)|K^(m)(u)| tends to zero at both infinities. The transform is
the half-line cosine transform. The removed x must be its least
positive real zero, multiplicity allowed. The requested output
condition is nonstrict log-concavity. Positivity, the smooth even
origin interface and the exact quotient interpretation must be paid.

Reused the inspected primary statements and proof cases recorded in
[source notes2254](2026-11-21-residual-curvature-source-notes-2254.md):
Csordas1998 Corollary2.11, Csordas2014 Theorems3.5/3.7/4.5, and
Prekopa1973 Theorems6-7. Their conclusions concern the original theta
kernel, weighted product correlations, or nonnegative marginals and
convolutions. None states first-zero sine-resolvent preservation.
The signed sine integrand is outside Prekopa's nonnegative hypotheses;
this excludes that direct application, not every possible representation.
No matching first-zero theorem was found in the sources inspected.

Newly inspected primary ranges:

- E.O. Tuck, *On positivity of Fourier transforms*, Bull. Austral.
  Math. Soc.74(2006),133-138, pp133-135, equations(1)-(4) and the
  complete half-period comparison on p134:
  https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D232B9DEB4819E4D2FF17E8162B8B066/S0004972700047511a.pdf/on_positivity_of_fourier_transforms.pdf .
  Read the smoothness, convergence, boundedness/endpoint conventions
  and positive decreasing-amplitude proof. Its pairing of successive
  sine half-periods supplies a positivity tool, not a curvature
  statement, and does not use a first-cosine-zero condition. Applying
  it to the proposed kernel's translated amplitudes remains a later
  hypothesis check; no generic extension is proved in this review.
- G. Csordas, *Fourier transforms of positive definite kernels and
  the Riemann xi-function*, arXiv:1309.0055v2,21February2014,
  printed p9, Remark3.11 and Example3.12 with its complete displayed
  transform comparisons:
  https://arxiv.org/pdf/1309.0055v2 . The example uses
  exp(-t^2)(15+t^2+t^4), is strictly log-concave for t>0 and has a
  Fourier transform positive on the real axis with nonreal zeros.
  It therefore has no positive real zero to remove. It also fails
  the paper's stronger admissibility condition(v), which requires
  decay exp(-|t|^(2+epsilon)); that condition is stronger than our
  every-exponential requirement. These two decay notions must not
  be conflated. The example is not a counterexample to the present
  first-zero implication. No independent check of its polynomial
  calculations or new consequence is claimed here.
- NIST DLMF1.13(iii), equations1.13.8-1.13.10 and the surrounding
  analytic-forcing hypothesis, https://dlmf.nist.gov/1.13.iii .
  Read the inhomogeneous solution decomposition and variation formula.
  This presentation requires analytic coefficients and forcing on a
  simply connected domain. It is adequate as an ODE reference for the
  fixed analytic nomination below; it is not automatically a theorem
  for every merely smooth K in the generic target.

Reused Tao, *245C, Notes2: The Fourier transform*,6April2009,
Section3 Exercise30 and inversion(11), with inspection already
recorded in notes2225/C919m. Reopened Exercise30's L1 derivative
and fundamental-theorem-of-calculus assumptions:
https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/ .
All needed integrability, endpoint and angular-frequency conversion
checks remain obligations. No general Fourier theorem is reproved.

## Duplicate and failure checks

Read C919m's full tails, origin, positivity and transform proof ranges;
its actual-theta normalization and root bracket are not premises for
an arbitrary K. The proof is a template whose individual hypotheses
must be rechecked. C919p/q's hypotheses and conclusions explicitly do
not establish strict log-concavity. Their all-prefix positive inverses
therefore do not already refute this invariant. No Xi first-zero census
or simplicity follows from these files.

Read the exact nearby stops for finite-divisor signed composition667
and finite-block extension1117; they concern signed minors and changing
finite information, respectively, not this continuous shape invariant.
Read the strict-log-concavity and superexponential-mixture stops and
their canonical L049/L050 proofs. They refute generic real-zero
sufficiency, not preservation at a specified first real zero. The
mixtures introduce nonreal factors; neither proof identifies the
required quotient's logarithmic curvature. Their negative evidence
remains intact. No cross-notebook premise was used.

## Bounded searches and read limits

Actual query strings included:

- `Fourier transform division first zero log concave kernel preservation Polya`;
  `"logarithmic concavity" "zeros" "division" Fourier`;
  `"admissible kernel" "first" "zero" concavity`.
- `"Fourier" "first zero" "log-concave"`;
  `"Fourier" "division" "Wintner"`;
  `"kernel" "real zeros" "logarithmically concave" removal`.
- `"log-concavity" "division" "Fourier transform" kernel`;
  `"first zero" "kernel" "logarithmic" Fourier removal`;
  `"log concavity" "Hermite" "Gaussian" polynomial Fourier zeros`.
- `"exp(-t^4-t^2)" Fourier zeros log concavity`;
  `"e^{-t^4" "log-concavity" Fourier division`;
  `"first zero" "factor" "log-concavity" kernel`.
- `Dimitrov Rusev Zeros entire Fourier transforms exp polynomial quartic pdf`;
  `"Fourier" "t^4" "t^2" "Polya" zeros`.

No matching preservation theorem or matching fixed-member curvature
counterexample was identified. Search misses are not novelty evidence.
The last search located Dimitrov--Rusev's2011 survey, pp1-108, author
PDF at https://www.dcce.ibilce.unesp.br/~dimitrov/ProfRusev/EJA_Paper_24_02_11/Dim_Rus_main.pdf .
Only search metadata was seen; no theorem from it is imported. Quartic
Gaussian transform papers and recent xi preprints were also leads only.
No assertion about all zeros of a quartic transform is used. Wintner/
Spira originals and optional Koumandos remain unread and nonessential
to the fixed finite test. No persistent essential access blocker arose.

## One fixed nomination, not a mathematical result

Prepare only K_*(u)=exp(-u^4-u^2), with no parameter search. The
discriminating test is at the single fixed spatial point u=1:

    Delta_*(x)=G_x(1)G_x''(1)-G_x'(1)^2.

Before interpreting this value, the later attempt must establish all
input hypotheses for K_*, existence of a least positive real Fourier
zero, and certify that zero in (0,8). The interval is a proposed
finite search cap, not an asserted zero enclosure. It must exclude
every smaller positive zero, rather than pick a sign change. Do not
assume simplicity; any uniqueness or derivative assertion used to
certify the bracket must itself be established. If this cap cannot be
certified, stop this fixed attempt without enlarging it automatically.

The later attempt must separately verify the complete tails for every
derivative, strict curvature including the origin, shifted-amplitude
positivity, the even-origin matching, and the quotient identity. No
one of those checks has been executed here. C919m is a comparison
template, not an imported generic lemma. The fixed analytic model
avoids the DLMF smooth-versus-analytic scope mismatch, but its actual
hypotheses still need verification.

Finite integration and differentiation tools are already covered by
notes2249/2254 (Conrad Theorem12.3, dominated convergence, DLMF3.5.6-8,
real Taylor remainder). Model-specific derivative and tail estimates,
zero exclusion, quadrature and arithmetic errors remain to be supplied.
If scripts are used later, save full certificates and explicitly state
any numerical backend contracts. No mathematical script was written
or run in this turn. No quadrature setup or numerical prediction is
being represented as tested.

A strict rigorous lower bound Delta_*(x)>0 at the certified first zero
would refute the generic invariant. A nonpositive upper bound tests
only this member and this point; it would not prove preservation.
An enclosure containing zero is inconclusive. Failed admissibility
or root certification is a failed test setup, not a counterexample.
Do not retune the kernel or spatial point after seeing the answer.

EXPLORE coverage authorizes only this one bounded future test after
separate approval of the updated assessment. It does not approve a
generic preservation proof, other members or actual-Xi specialization.
This is an ordinary source-supported calculation nomination, not a
protected creative mechanism. The blocker to the latter is a concrete
comparison principle linking the first-zero restriction to curvature;
no such principle was located or proposed rigorously. Full matching
Mathlib coverage is unchecked, not asserted absent.

Outcome EXPLORATION: completed a new source comparison and prepared a
test; no preservation theorem, counterexample or RH progress beyond
the checked sources is established. No lemma, mathematical script,
DAG, PROOF or supervisor state changed. Newly prepared ready coverage
requires separate approval next turn.
