# Scaled ordinary Jensen root-tail source review1516

Literature-only review of assessment1515's saved target. The main gap is
L030--L032/C032a actual-Xi all-degree positivity. A degree-uniform vanishing
reciprocal-height tail could isolate escaping roots in C028b. Compact
nonreal-root mass and its RH-equivalent upper payment remain unresolved.
No mathematical estimate is established in this review.

## Inputs and duplicate comparison

Read C028a's definitions and coefficient-budget stop, C028b's normalization,
inversion, multiplicity argument and fixed-zero persistence, and C028e's
hypotheses, conclusion and coefficient identification. Reused source-notes1500
(actual Theta and Jensen conventions),1507 (Poisson--Jensen) and1510
(real-line exterior tail). Targeted searches of November18 Jensen/reciprocal
assessments and Jensen attempts found no matching uniform root-plane tail
assessment. C028e's centered real variable Q_d is a different object from
U_d=J_d(u/d)/gamma_0. The Schmeisser/Hermite coefficient-budget stop and
inverse-degree stop1515 do not test the present counting mechanism.

## Primary statements and essential proof cases inspected

**Sheng-Chi Liu, lectures**, *Lecture Notes in Analytic Number Theory*,
Lecture23 dated18 March2019, printed pp.57--58, Theorems23.1.2 and23.2.1:
https://bpb-us-w2.wpmucdn.com/faculty.umaine.edu/dist/1/19/files/2022/08/analyticnumbertheory.pdf .
Inspected the complete counting proof on p.58. Part(i) bounds the number
of zeros in the closed radius-R disk, with multiplicities, by
O_(f,epsilon)(R^(alpha+epsilon)) for nonzero entire f of order<=alpha
and f(0)!=0. Its proof retains the Jensen boundary mean before inserting
the order bound. Contour zeros are handled by slightly larger zero-free
radii; origin zeros by division by their multiplicity factor.
The constant depends on f: applying part(i) separately to each polynomial
would not give uniformity in d. Part(ii)'s displayed integration by parts
has apparent sign/factor transcription issues and is not imported; only
part(i) and its Jensen counting method are needed. A screenshot of p.58
timed out; the complete relevant text and counting formulas were readable.

**Min Ru**, *Nevanlinna Theory*, undated author-hosted notes, printed
pp.1--2, TheoremA1.1.1 and CorollaryA1.1.3:
https://www.math.uh.edu/~minru/log.pdf .
Inspected the theorem, complete zero/pole-removal proof, boundary-radius
reduction and Jensen corollary. Nonzero functions meromorphic on the
closed disk have logarithmic zero/pole accounting with multiplicity;
the corollary removes the origin order before evaluating at zero.
For the proposed entire polynomials there are no poles and the existing
normalization is1 at zero. Use only zero-free outer radii, or justify the
boundary limit; repeated roots require no simplicity hypothesis.
Import the named formula, without reproof. It supplies no uniform family
growth bound by itself.

**Cormac O'Sullivan**, *Zeros of Jensen polynomials and asymptotics for
the Riemann xi function*, arXiv:2007.13582v2,9 December2020:
https://arxiv.org/html/2007.13582v2 .
Rechecked Introduction(1.2), Section3.1 definitions, Theorem3.1 proof sketch
and Corollary3.2. Theta(u)=xi(1/2+sqrt(u)) is entire of order1/2;
gamma_j=j!xi^(2j)(1/2)/(2j)!, and the ordinary Jensen polynomial uses
binom(d,j)gamma_j. The proof sketch states compact convergence after
scaling by1/d. C028b already verifies Theta=gamma_0 F. These are
unconditional input conventions, not an assertion of actual hyperbolicity.
Order1/2 does not assert finite type at exactly that order. The requested
tail exponent leaves room for an order exponent strictly between1/2 and1.

## Comparison and approved difference

These sources cover the general growth/counting method, but none inspected
states the exact degree-uniform reciprocal-height tail. The only proposed
new local work is to check uniform growth from the positive coefficients
and scaled binomial multipliers, retain the resulting common constant
through Jensen counting, and perform the finite-root tail summation.
This is a routine specialization of classical tools, not a creative central
sign mechanism. Qualitative compact convergence alone is inadequate.
The proof must cover every d>=3, R>=R_0, all multiplicities, closed counting
disks and the strict tail cutoff. Constants may depend on F only. The
order-zero status of each individual polynomial cannot replace common
growth control. No bound is derived or approved as true in this turn.

Continue if that finite-family uniformity check and the tail estimate
meet R^(-1/4) without root reality, RH or a compact-zero-mass assumption;
otherwise preserve the failed hypothesis and park this target. Do not
infer H_d=o(d) from a tail estimate: a fixed compact nonreal zero still
forces C028b's positive lower bound. Full matching Mathlib coverage was
not checked; unknown coverage is not absence.

## Search evidence and limits

Queries: `Jensen formula zero counting n(r) log M(2r) entire order reciprocal
zeros tail`; `"Jensen polynomials" "zeros" "uniform" "order"`;
`"Jensen polynomials" "reciprocal" "tail"`; `"Jensen polynomials"
"zero counting"`; `"Jensen polynomials" "reciprocal" "uniform"`;
`"scaled Jensen polynomials" "growth" zeros`.
No exact-match theorem was established by this bounded search, and no
novelty is inferred. A search lead titled *An asymptotic Jensen-Polya
criterion for GRH*, https://borowiecki.dev/pdf/2610.38870 , remains unread
and unverified; no statement, validity or applicability is imported from
its snippet. It is not essential to applying the classical counting tools.
Source access succeeded for the essential statements. No lemma, mathematical
script, certificate, PROOF or DAG edit was made. Initial notebook-local git
status was excessively large; no sibling notebook was inspected and all
pre-existing changes were preserved. This is new source coverage and an
actionable test, not a mathematical advance or a reset of exploration usage.
