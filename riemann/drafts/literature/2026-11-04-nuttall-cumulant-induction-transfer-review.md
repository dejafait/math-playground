# Nuttall cumulant induction — different-kernel source gate

TARGET: Assess Nuttall's Conrey–Ghosh k=1 cumulant induction in cumanal_a.pdf Sections4–5 for a transferable actual-K Wronskian estimate, retaining its smoothing cost and the exceptional k=r-1 coefficient interface.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step392 completed primary Sections3.3–5.5 and exact-title, correction, cumulant/Wronskian/differential-operator searches; narrow local comparisons found only step391's unread lead at this scope. No inspected stronger actual-K transfer theorem was located; this is not a novelty assertion.
SOURCE_EVIDENCE: Nuttall cumanal_a.pdf, 20-page author copy, Sections3.3–5.5, Lemmas4.1–4.3 and5.1–5.5, Theorem5.6/(5.59)–(5.73), printed pp.7–19; source display discrepancies and uniform-error qualifications recorded below. Reuse step391's det3CAEXP_2.pdf Sections4.4–4.6 coefficient-range assessment.
COMPARISON: The induction concerns only a pure exponential base; full Theta1 sign preservation is a fixed-r determinant perturbation with exponential gap Q1/Q=25 and existential M(r). It supplies neither the actual-K base determinant estimate nor usable smoothing order or exceptional k=r-1 transfer.
GAP: Direct transfer is rejected at the assessed scope. Actual-K signed base control, uniform perturbation errors, effective order cost and exceptional-index coefficients remain open; the source theorem itself is not independently audited or imported.
REASON: Inspecting the essential proof changes routing: park direct Conrey–Ghosh transfer. Retaining the full actual n=1 theta summand is a different proposed base comparison needing its own source gate; no new mathematics is approved here.
LITERATURE_REASON: At invocation the changed kernel/technique had essential unread Sections4–5 outside prior coverage; step392 completed those reads. This does not authorize further literature on the unchanged direct-transfer target.
SCOPE: Completed literature-only comparison of this source and its possible actual-K transfer. No new mathematics, lemma, mathematical script, parameter scan or assumed all-degree signs; no research continuation is approved by this assessment.

## Initial nomination — retained; completed decision below

Primary source: John Nuttall,
[*Cumulants, the Riemann Hypothesis, and Similar Problems*](https://publish.uwo.ca/~jnuttall/cumanal_a.pdf),
20-page author-hosted manuscript. Its claims remain unverified here.
Distinguish the actual-theta framework from this separate analogous-
kernel manuscript and its proof status.

Essential local inputs for any later actual-K target are L019's exact
theta kernel and decay, L021's moments and L018's completion convention.
L766 is an unaudited contrast only; L765 remains a norm stop. Use
the existing K(u)=4Phi(u/2) normalization assessment with all factorials.
No cross-notebook input is proposed. Mathlib coverage is unchecked.

Main gap: actual-Xi all-degree signs. Plausible downstream use: an
actual-theta cumulant estimate could supply structured sign information
unavailable to product-K pointwise signing. Effective order cost,
coefficient transfer and exceptional-index coverage remain separate.
The direct source formula only reaches k>=r-1+ceil(m/2); smoothing
does not by itself remove that cost.

Continuation test: nominate at most one precise actual-K inequality
only if its induction has independent source support, usable order
cost and a bounded sign/threshold discriminator. Reject transfer if
the proof relies on a kernel-specific identity with no justified
analogue, assumes the desired Wronskian signs, or gives no usable
order cost. Record any narrower useful input with its independent
gaps. This nomination approves no mathematics; it requires a separate
literature decision next turn.

## Completed primary comparison — step392

**Exact scope.** Nuttall, *Cumulants, the Riemann Hypothesis, and
Similar Problems*, author copy linked above, accessed 2026-11-04,
20 pages; no internal version date established. Theorem5.6, printed
p.17, asserts: for each fixed integer r>1 there exists M such that

    (-1)^(p(p-1)/2) W(p,M;u)>0, u>=0, 1<=p<=r,

where W is the derivative determinant of an iterated-tail cumulant
of Theta1. Section3.3/(3.27) works with m>2r. No effective M(r)
is stated. This is a claimed Theta1 result, not a theorem for L019's
K. No theorem is imported into the local DAG; no reproof or
independent correctness claim is made.

**Induction versus perturbation.** Section4.1/Lemma4.1, pp.8–9,
uses the adjacent-Wronskian identity (4.8), attributed to Karlin,
*Total Positivity* (1968), p.60/(4.2). Its input is
exp(-beta exp(u)), after removal of an exponential tilt. This is
the induction; it does not supply signs for arbitrary perturbations.
The original Karlin statement was not newly read.

Sections4.2–4.3, pp.9–12, give a cumulant determinant integral
with a Vandermonde and a derivative determinant. For the pure base,
the latter becomes a Vandermonde in y_i=Q(u)exp(v_i).
Lemma5.4, pp.14–16, uses their signed product to obtain a squared-
Vandermonde lower bound. An independently signed base is essential.
Lemma5.1, p.12, bounds the remainder by
1.01 a1(u) exp(-2pi exp(u)), with
a1(u)=exp(u/4-pi exp(u)/12). Lemmas5.2–5.3 use Q(u)=pi exp(u)/12
and Q1(u)=25Q(u). Section5.5, pp.17–19, expands the determinant
into 2^r column choices and compares remainder-containing terms
with the base lower bound. This uses exponential separation,
not merely positive factors or rapid decay.

**Proof cases and qualifications.** Lemma5.2 uses the moving saddle
nu exp(nu)=m/Q(u), with Gaussian scale m(1+nu). Lemma5.5 treats
large mu=m/Q(u); Section5.5.3 also discusses small mu. The final
all-u comparison (5.71)–(5.73) supplies no explicit uniform remainder
constants or effective M(r). Those errors, the base normalization,
and simultaneous strictness for all p<=r are not independently
audited. No effective actual-K conclusion is licensed.

Before formula use, resolve display inconsistencies: (3.24) makes
Psi1 a single tail integral, but (4.14) labels the v^m/Gamma(m+1)
integral Psi_m. Equations(5.10)/(5.23) use m(1+nu), while (5.26)
prints m+nu1. These are disagreements between displayed conventions,
not a disproof or silently corrected theorem. PDF text was read;
screenshot calls supplied no inspectable images, so visual checking
is not claimed.

## Actual-K comparison and decision

L019's full n=1 summand is

    B(u)=(8pi^2 exp(9u/2)-12pi exp(5u/2)) exp(-pi exp(2u)).

It contains a nonconstant polynomial factor in exp(2u). Positivity
of B and L019's positive summand expansion do not identify its
derivative determinants with the source's pure-base Vandermonde.
The missing signed lower bound cannot be replaced by an absolute
norm. No actual-K estimate with usable order cost follows by citation.

Reuse step391's K(u)=4Phi(u/2) normalization and coefficient-range
assessment: even eventual cumulant reverse regularity leaves
k>=r-1+ceil(m/2) in that direct formula and exceptional cases.
No k=r-1 sign is decided here. L765's norm stop and unaudited L766
are preserved as contrasts. No RH candidate or beyond-source
mathematical advance is claimed.

Park direct Conrey–Ghosh transfer. The different proposed test retains
all of B as the base, rather than treating its polynomial factor as
an exponentially separated error. A signed base representation and
relative n>=2 tail control are only proposed targets, not established
facts. The separate next assessment is REVIEW_REQUIRED. An effective
smoothing theorem would still leave the exceptional coefficient
interface and other independent all-degree gaps unresolved.

## Searches, read limits and Mathlib

Queries: `Nuttall "Cumulants" "Conrey" Ghosh induction reverse rule`,
`"cumanal_a" Nuttall`, `"Nuttall" "cumulants" "Theta" sign regularity correction`,
`"Riemann" "cumulants" "Wronskians" differential operator`, and the
exact manuscript title with `theorem`. Read Sections3.3–5.5 in full,
including all Lemmas4.1–4.3 and5.1–5.5 and Theorem5.6's proof.
Author-homepage and bibliographic hits provided no independently
inspected correction or stronger actual-K theorem. Search snippets
were not used as theorem evidence. No novelty inference follows.

Local searches used exact Nuttall/cumulant/source filenames in
literature, ATTEMPTS and foundations, then the relevant step391
review/history and first-summand/Christoffel terms in selected
actual-theta/Jensen assessments. The prescribed Jensen primitive
stop concerns another mechanism; it gives no base-Wronskian identity.
Read L019/L021/L766 for the local interface, preserving L766's
unaudited status; L018's completion convention was reused there.
The older actual-theta paper was opened to identify the source,
not newly audited. No sibling notebook was read.

Mathlib coverage of the full cumulant theorem, its uniform estimates
and the proposed B comparison is not checked. Unknown coverage is
not absence. No new lemma, mathematical script or computation was
produced in this source-only step.
