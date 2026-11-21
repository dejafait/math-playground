# All-order full-base localization — completed source comparison

TARGET: Assess an effective all-order extension of L769/L770: for each integer r>=2, seek M(r)>=2r-1 giving a positive signed full-B cumulant determinant and relative complete-theta error below 1/2 for all integers m>=M(r) and u>=0.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step402 searched effective/all-order/first-term/iterated-integral sign-regularity terminology and inspected the primary arbitrary-order beta formula and low-height discussion; reused step391–393/398 overlap and failure assessments. No inspected matching effective full-B theorem was located; this is not a novelty claim.
SOURCE_EVIDENCE: Nuttall basicRH.pdf (October2012), Sections1.1–1.3 and3–5, Theorem3.1/(3.1)–(3.12), pp.1–2,5–6; wronskRH.pdf (August2012), Sections3.2–4.1, pp.3–5; cumanal_a.pdf Theorem5.6/(5.61)–(5.73), pp.17–19, with essential Sections4–5 proof cases reused from step392; Progrepa.pdf Sections2–3 reused from step398.
COMPARISON: The arbitrary-order beta formula is unsmoothed and single-variable; full-base cumulants/ratios remain conjectural or numerical. The Theta1 theorem is different-kernel and existential. L769/L770 supply audited r=4 quantitative control only; neither a citation nor extrapolation supplies the requested M(r).
GAP: An all-order signed full-B integral lower bound including low-coordinate configurations, paid confluent cancellation and derivative costs, and an explicit all-height/all-m threshold are unpaid. Exceptional coefficient transfer remains independent.
REASON: Essential exact-scope source comparison is complete for one bounded development attempt using the signed-integral/reciprocal/conditional method; this turn derives no all-order identity, estimate or theorem.
LITERATURE_REASON: Changed integer order r>=2 and explicit r-dependent onset exceed step398's fixed-r coverage; the arbitrary-order polynomial and low-height cases required this separate review.
SCOPE: Fixed but arbitrary integer r>=2, original C_m factorials and full B, all integers m>=M(r)>=2r-1 and real u>=0; constants may depend on r, but the onset must be explicit. No uniform-in-r asymptotic or exceptional-index assertion is assumed.
COVERED_TARGET: Develop the all-order extension of L769/L770 by seeking an explicit M(r)>=2r-1 with S_(r,m)(B;u)>0 and |S_(r,m)(K;u)-S_(r,m)(B;u)|<S_(r,m)(B;u)/2 for every integer r>=2, integer m>=M(r) and real u>=0, paying signed low-height contributions and coalescing-node cancellation.

The following paragraphs preserve the step401 nomination. The completed
step402 comparison and bounded continuation follow them.

The main gap remains actual-Xi all-degree positivity. This target could
supply effective eventual smoothing signs at arbitrary finite order;
the exceptional coefficient interface and RH would remain unresolved.
Use L019's exact K and full first summand B, and the original factorial
convention for C_m. The proposed signed determinant is
S_(r,m)(F;u)=(-1)^(r(r-1)/2) det[partial_u^(i+j) C_m(F;u)]
for i,j=0,...,r-1. This defines the question, not a derived result.

First inspect the primary arbitrary-order polynomial formula and the
essential full-B versus Theta1 proof cases. Reuse read source ranges
when adequate; newly needed cases must actually be read. Check stronger
effective results, smoothing conventions and all-height quantifiers.
Import a matching theorem with its precise hypotheses and citation;
otherwise identify the uncovered signed estimate before approving a
bounded development attempt. Do not extrapolate the 19/72 factor or
the four-coordinate constants to arbitrary r.

The discriminator is whether order-dependent determinant cancellation
and any low-height signed full-B contribution can both be controlled
with an explicit M(r). Positive scalar tails, entrywise error bounds,
fixed-u asymptotics and finitely many successful orders are insufficient.
A viable target must cover coalescing nodes and all height regimes and
have a quantitative threshold capable of forcing relative error<1/2.
Retain an unpaid signed regime explicitly if one appears; failure of a
coarse bound at one onset does not refute eventual smoothing. Persistent
source blockers require independent work, not an unchanged search.

Essential possible inputs: L019 kernel/decay and audited L769/L770 at
r=4 only. L767/L768 are precedent. Preserve the different-kernel transfer
stop and step391's coefficient range k>=r-1+ceil(m/2); exceptional-index
signs are neither assumptions nor consequences of this nomination.
No cross-notebook input is proposed. Mathlib coverage is unchecked.

This extends an established cumulant method. The fixed-order audit
supplied no independently justified exceptional-index mechanism, so
increasing determinant order alone does not justify creative routing.
This source review should determine whether there is useful quantified
development to do. No theorem or ready assessment is created here.

## Completed comparison — step402

### Primary arbitrary-order formula and its limits

John Nuttall, [*Basic Wronskians in the Riemann Hypothesis*](https://publish.uwo.ca/~jnuttall/basicRH.pdf),
seven-page author report, explicitly dates itself October2012 on p.1.
Sections1.1–1.3 and3, pp.1–2,5–6, concern g(t)=exp(-y)(2y-3),
y=exp(t), after a tilt removal. Theorem3.1/(3.1)–(3.3) states

    W_r(y)=sum_(j=0)^r (-1)^(r-j) h(r,j)y^j,
    h(r,j)=2^(2j-r-1) f1(r) eta(r-j)/j!,
    f1(k)=prod_(a=0)^k a!, eta(k)=(2k+2)!/((k+1)!k!).

Equation(3.12) places this polynomial in the unsmoothed two-way
Wronskian with factors exp(-r y), (-1)^(r(r-1)/2) and
y^(r(r-1)/2). Read the induction (3.4)–(3.11), using the adjacent
Wronskian identity (1.10)/(2.4); no independent proof audit or import
is claimed. Section4.2's beta-zero discussion is numerical; Section5
proposes extending the method to cumulants. It provides neither a
positive-level integral nor an effective smoothing threshold.

This is precise precedent, not the needed multivariable signed
factor in a cumulant determinant integral. In particular, removing
an exponential tilt in an unsmoothed Wronskian does not justify
removing it inside C_m. Use L019/L769's actual B throughout any
development. No specialization of this source theorem is performed
or assumed in this literature-only turn; a future formula use must
justify every scale/tilt/factorial conversion separately.

### Full-base low-height and different-kernel cases

Nuttall, [*Wronskians and the Riemann Hypothesis*](https://publish.uwo.ca/~jnuttall/wronskRH.pdf),
August2012, Sections3.2–4.1, pp.3–5: the reported numerical beta root
at r=7 is about3.3078878, beyond pi. This flags a low-height signed
regime for inspection, without proving its sign or refuting eventual
smoothing. Section3.3/Conjecture1 and Table1 concern full-first-term
cumulants; Section4.1's ratios are numerical trends, not uniform
error bounds. Reuse step393's display/sign qualifications. No claimed
zero pattern, table, sample onset or ratio is imported as a theorem.

Nuttall, [*Cumulants, the Riemann Hypothesis, and Similar Problems*](https://publish.uwo.ca/~jnuttall/cumanal_a.pdf),
20-page author copy, internal date unestablished: reuse step392's
essential induction, determinant-integral and saddle proof cases in
Sections4–5. Rechecked Theorem5.6 and (5.61)–(5.73), pp.17–19.
For each fixed r>1 it claims a sufficiently large M making all signed
Wronskians of orders p<=r positive on u>=0, for Theta1 only. Its pure
base, exponential gap25 and unquantified final large-/small-mu
comparison give no effective full-B threshold. The estimate must
also pay growing determinant cancellation; entrywise asymptotics
are insufficient. Source convention/error qualifications remain
those of step392. No source-proof acceptance or new defect is claimed.

Nuttall, [*Progress Report on the RH and the Eight CG Functions*](https://publish.uwo.ca/~jnuttall/Progrepa.pdf),
March2013, Sections2.1–3.2, pp.2–4, was opened and its core
statements checked; reuse step398's complete comparison. The full
RH cumulant assertion is a conjecture/program with numerical support,
and lower-index gaps remain. It contains no matching quantitative
full-B theorem. Its use here is scope evidence only.

### Known-results comparison and bounded development gate

The existing r=3 and r=4 local results do not cover arbitrary order.
The exact all-order beta formula above removes any justification for
reinventing an unsmoothed formula as a discovery. The missing result
is an effective integrated sign and relative comparison with the full
theta sum on the stated joint domain. Reuse step398's Wang–Yang
Theorems1.1–1.3 comparison: discrete coefficient Laguerre bounds do
not give height-dependent tail-cumulant bounds. No new reading or
import of that source is needed. No inspected stronger matching
theorem was found; absence from this bounded search certifies no
originality.

DECISION EXPLORE authorizes the single COVERED_TARGET, after the
separate next-turn approval required for newly ready coverage. It is
development of a known comparison program. A useful first outcome
may be only a general signed-integral representation or an effective
base lower bound; the independent complete-K error and coefficient
transfer may remain open. This is not permission to assume them.

Use the audited L769/L770 strategy as a proposed method, not a proved
generalization: retain the polynomial factor; seek an order-dependent
signed lower bound relative to a positive leading-term reference;
control low-coordinate contributions and complete-theta errors; pay
the divided-difference derivative costs before dividing determinants.
The 19/72 lower factor and all four-coordinate constants are r=4
only. Low-height signs must be proved or their negative contributions
bounded; they cannot be dropped from the integration region.

The bounded discriminator is an explicit, computable choice of
order-dependent cutoffs and constants yielding a strictly positive
base lower bound and relative error<1/2 for all m above a stated
M(r), including x0=pi exp(2u) near pi, transition heights and x0
arbitrarily large. Coalescing nodes and mixed low/high configurations
must be included. A valid signed representation with a paid lower
bound is partial progress even before the full comparison succeeds.
If a quantitative regime remains unpaid, preserve it and stop the
attempt there; repetition requires a refined estimate or new input.
A failed coarse onset rejects that onset, not every eventual M(r).
Finite orders/grids or fixed-u limits are inconclusive.

Inputs: L019 exact K/B and decay, audited L769/L770 at r=4 only,
with L767/L768 as normalization precedent. Reuse step391's
k>=r-1+ceil(m/2) interface and step392's different-kernel transfer
stop. No hypothetical all-order sign, beta-zero pattern or favorable
remainder cancellation is an input. Even a successful M(r) leaves
exceptional coefficients and actual-Xi all-degree positivity open.

### Search record, access and routing

Queries included `"Riemann" "cumulants" "effective" sign regularity`,
`"Nuttall" "cumulants" arbitrary order first term Wronskians`,
`"Basic Wronskians" Riemann general order polynomial`,
`"Riemann" "cumulants" "sign-regularity" theorem`,
`"Nuttall" "Wronskians" "polynomial" zeros beta`,
`"cumulants" "Riemann" "uniform" "order"`,
`"first term" "Wronskians" "Riemann" cumulants proof`,
`"cumulant" "sign-regular" "Riemann"`,
`"Wronskians" "cumulants" "bound" Nuttall`,
`"iterated integrals" "eventual" "sign regularity"`, and
`"Nuttall" "cumulants" "2024" OR "2025" OR "2026"`.
Statistical cumulants were irrelevant hits. A recent Willow/Blind
Zone search hit concerns another determinant/shift question; its
theorem is unread and is not used for coverage or as a new target.
No search snippet is theorem evidence.

Accessed2026-11-04. Browser PDF text supplied the essential statements
and proof cases. Screenshot requests for basicRH pp.5–6 yielded no
inspectable images; no visual typography verification is claimed.
Precise source citations above support scope comparison; future use
of a load-bearing formula must check its convention and proof rather
than silently correct a display. No essential source-access blocker
remains for the direct local signed-integral development.

Local duplicate/failure checks were confined to step391–393/398
assessments, the two matching ATTEMPTS, selected histories and the
relevant L019/L769/L770 definitions/proof ranges. Existing changes
were preserved. No sibling notebook or cross-notebook result was read.
No new mathematics, lemma, mathematical script, DAG edge or PROOF
change was made. Mathlib coverage of the full source theorem and
all-order uniform comparison remains unchecked, not known absent.

Outcome EXPLORATION: exact-scope source coverage is now ready, with
no mathematical advance or newly established obstruction. Next route
is proof_attempt/development. No justified creative mechanism was
found: arbitrary-order smoothing is already the primary proposal,
and no independently supported exceptional-index mechanism emerged.
This mathematical blocker, rather than the turn-balance target,
explains retaining established-route development. Do not spend another
unchanged literature turn once this coverage has been approved.
