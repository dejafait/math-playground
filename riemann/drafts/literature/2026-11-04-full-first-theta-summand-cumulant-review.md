# Full first theta summand — proposed different base comparison

TARGET: Assess an actual-K cumulant comparison retaining the full n=1 theta summand B, seeking a signed base-Wronskian formula and a relative n>=2 tail bound below 1/2, with r=3,m=5 as the first discriminator.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step393 found the same full-first-summand cumulant comparison in Nuttall wronskRH.pdf and followed basicRH.pdf/RHsplit.pdf; exact-term and stronger-result searches found no inspected certified m=5 relative bound. This is overlap evidence, not novelty evidence.
SOURCE_EVIDENCE: Nuttall wronskRH.pdf (August2012), Sections3.1–4.1 pp.2–5; basicRH.pdf, Theorem3.1/Sections3–4 pp.5–6; RHsplit.pdf (November2012), Sections2–3 pp.2–3; det3CAEXP_2.pdf, Lemma2.1/Theorems2.2/3.5 and Sections3.1–3.3/3.6/3.11/4.2; exact scopes below. Reuse step392's different-kernel proof assessment.
COMPARISON: The full-B comparison and column-split program are already proposed in the sources; unsmoothed polynomial formulas and actual-kernel RR3 do not supply the requested m=5 base-relative inequality. Positive-m evidence inspected is numerical. No theorem is imported.
GAP: A certified signed S_(3,5)(B;u) lower bound and a relative actual tail error below 1/2 for all u>=0 remain unproved here. All-order smoothing, uniform order cost and exceptional coefficient transfer remain separate.
REASON: Essential source comparison is complete for one fixed reproduction attempt; do not call the known mechanism creative or reprove finite-order signs as discoveries. Certifying the stated relative inequality would address a stronger quantitative question than the inspected sign results.
LITERATURE_REASON: Changed base and comparison mechanism; essential polynomial-base determinant and finite-order overlap coverage is missing, so the literature gate remains necessary despite the balance target.
SCOPE: Completed literature only; ready coverage for one bounded fixed r=3,m=5 signed split comparison, not an all-r theorem or an import of numerical claims. A newly written ready continuation requires separate supervisor approval next turn.
COVERED_TARGET: Test S_(3,5)(B;u)>0 and |S_(3,5)(K;u)-S_(3,5)(B;u)|<S_(3,5)(B;u)/2 for u>=0, retaining u=0, using signed cumulant split bounds.

Main gap: actual-Xi all-degree positivity. Plausible use: a signed
base plus relative tail saving could support actual cumulant reverse
regularity, which remains weaker than the missing edge coefficient
sign and the all-degree criterion.

Inputs are L019's exact K and its n=1 summand

    B(u)=(8pi^2 exp(9u/2)-12pi exp(5u/2)) exp(-pi exp(2u)), u>=0,

and L021's moments, with L018's completion convention. For this
proposal use the unambiguous tail convention C_0(F;u)=F(u) and

    C_m(F;u)=1/(m-1)! integral_u^infinity (v-u)^(m-1) F(v) dv, m>=1.

The proposed signed determinant is

    S_(r,m)(F;u)=(-1)^(r(r-1)/2)
                  det[(d/du)^(i+j) C_m(F;u)]_(i,j=0)^(r-1).

No positivity is asserted. The intended comparison would need both
S(B;u)>0 and |S(K;u)-S(B;u)| < S(B;u)/2 on a justified domain. First inspect
r=3,m=5 as a fixed discriminator, with u=0 retained and large-u
estimates stated separately. This choice keeps every displayed
derivative within the tail-integral indices; it is not a claimed
sufficient smoothing threshold. The broader question needs all r
with a justified M(r), not extrapolation from this fixed test.

Continuation test: approve mathematics only with exact source scope
and a concrete signed identity or structured cancellation mechanism.
If a known finite-order result covers the discriminator, import it
with its hypotheses and assess whether it supplies the proposed
all-order mechanism. Reject an estimate that replaces the base by
an absolute norm, assumes its sign, or ignores derivative-order
dependence. A negative discriminator parks that parameter choice;
it is not a global ban on other cumulants.

Reuse the completed step392 review for the direct-transfer stop and
step391 for the k>=r-1+ceil(m/2) coefficient cost. L765/L766 are
contrasts, not inputs proving this comparison. Actual integrated
signs, effective smoothing, exceptional k=r-1 transfer and all-degree
closure remain unresolved. No cross-notebook input is proposed.
Mathlib coverage is not checked. This was the step392 nomination;
the step393 source decision and its limits follow.

## Completed source comparison — step393

### Exact overlap and status

John Nuttall, [*Wronskians and the Riemann Hypothesis*](https://publish.uwo.ca/~jnuttall/wronskRH.pdf),
August 2012, seven-page author report, Sections3.1–3.3 and4.1,
printed pp.2–5, is a direct precedent for this mechanism. It retains
the complete first summand, defines its iterated tails in
(3.14)–(3.19), states eventual all-order base regularity as
Conjecture1, and reports numerical full/base Wronskian ratios in
Section4.1. It supplies no certified uniform relative bound below
1/2. The polynomial zero observations and Tables1–2 are numerical;
they are not proof of the all-order assertions. Its removal of an
exponential tilt concerns the unsmoothed Wronskian, not replacement
of the full base inside its cumulants. Equations(3.3)/(3.18) and
Conjecture1 have apparent display/sign inconsistencies in extracted
text; no formula is imported through them. Screenshot requests
returned no inspectable images, so visual resolution is not claimed.

The earlier assessment's K(u)=4Phi(u/2) convention applies to the
Phi in det3CAEXP_2.pdf and RHsplit.pdf. This identifies the source's
full first summand with B after the same scaling. A future proof must
carry the integration/derivative scale factors explicitly. It must
not identify either paper's tilt-removed auxiliary function with B.

### Polynomial base and finite-order scope

Nuttall, [*Basic Wronskians in the Riemann Hypothesis*](https://publish.uwo.ca/~jnuttall/basicRH.pdf),
seven-page author report, Sections1.1–1.3 and3–4, printed pp.1–2,5–6,
Theorem3.1/(3.2)–(3.12), gives a coefficient formula for the
unsmoothed beta case with polynomial 2y-3. Its proof uses adjacent
Wronskians, coefficient identities and induction; Section4.2 still
describes the beta zero pattern numerically. The theorem is not a
formula for positive-level cumulants. It therefore does not settle
S_(3,5)(B;u), even though it removes the need to invent an
unsmoothed polynomial-base formula. No independent audit or import
of this theorem is claimed.

Nuttall, [*Wronskians, Cumulants, and the Riemann Hypothesis*](https://publish.uwo.ca/~jnuttall/det3CAEXP_2.pdf),
16-page author copy (journal: Constr. Approx.38 (2013),193–212,
DOI10.1007/s00365-013-9200-8), Theorems2.2/3.5, printed pp.4,12,
asserts RR3 and a strict negative third derivative determinant for
Phi at t>=0. Section3 uses the full n=1 polynomial, explicit n=2
mixed columns and n>=3 derivative-tail bounds; Section3.11 combines
nine terms. Inspected cases include the base F0, the first mixed
term and the derivative remainder Lemma3.2. These are m=0 estimates;
neither their one-sided sign bounds nor the cumulant definition
(4.3) is the required absolute relative comparison at m=5. The
complete finite-order proof and its external inputs are not audited
here. No assertion that the fixed sign is new, or that its known
proof certifies this relative error, is licensed.

### Positive-level splits and missing certificate

Nuttall, [*Structure of Wronskians Related to the Riemann Hypothesis*](https://publish.uwo.ca/~jnuttall/RHsplit.pdf),
November 2012, three-page author report, Sections2–3, printed pp.2–3,
(2.1)–(2.7)/(3.1), defines full-summand tail cumulants and expands
determinants by column choices grouped by summand indices. It
explicitly distinguishes the polynomial m=0 case from m>0. Its
numerical range includes m=0,...,5, n=1,2,3 and a finite t-grid
through 0.25; it omits splits judged insignificant. No error
certificate for omitted splits, n>=4 or the unbounded t-domain is
supplied. This is especially close overlap with the proposed
discriminator, but does not certify its sign or relative bound.
The algorithm is a reproducible lead, not a theorem to import.

### Bounded continuation and stopping test

One fixed-order reproduction attempt is justified by this completed
comparison. Use the COVERED_TARGET literally, with the original C_m
factorials and B. Seek a signed representation/lower bound and
certified mixed-split remainder, treating u=0, a compact interval and
the unbounded tail explicitly. This is a proposed task, not a result
derived this turn. Source conjectures, numerical tables and assumed
signs may not be used as inputs. The source's ordinary determinant
multilinearity is a method to develop, not permission for an
uncontrolled infinite-column expansion.

Continue beyond the fixed test only if a signed lower bound and a
relative bound strictly below 1/2 are certified on the claimed full
domain. A rigorous negative value, failure of the 1/2 inequality,
or an inability to control cancellation should stop this parameter
choice, with the precise scope retained. A sampled positive result
is inconclusive. Even a successful comparison is a fixed-order
quantitative reproduction and leaves effective M(r), larger orders,
the k=r-1 interface and RH open. Another identical attempt needs
new input or a refined estimate; the source overlap itself is not
a global ban.

No genuinely new central mechanism was justified in this review:
the mechanism nominated as different in step392 has a direct
literature precedent. The next purpose is difficult development of
that established route, not creative discovery. No reproof of an
available matching theorem is requested; the missing quantitative
certificate is the reason for the attempt.

### Search record and read limits

Queries included `John Nuttall Riemann cumulants theta function
determinant first term det3CAEXP_2`, `"Wronskians, Cumulants"
polynomial first term Nuttall`, `"Nuttall" "cumulants" "m=5"`,
`"theta" "sign regular" "polynomial" Nuttall`, `"Nuttall"
"cumulants" "first term" bound`, `"wronskRH" correction cumulants`,
`"Riemann" "cumulants" "relative" Wronskian`, and `"Nuttall"
"basic Wronskians" cumulants proof`. Followed the author's links
to basicRH.pdf and RHsplit.pdf after reading the directly matching
report. Accessed all on 2026-11-04; web crawl dates are not manuscript
dates. The new author-report versions have the page counts above;
no date was established for basicRH.pdf. Karlin and the original
Csordas–Varga proof remain external citations, not newly inspected
proofs; they are not assumed for the proposed direct comparison.

Local duplicate/failure checks used exact cumulant/Nuttall/first-
summand terms in the relevant literature assessments and November4
theta/cumulant ATTEMPTS. Reused step391's normalization and smoothing
cost, and step392's separate-kernel stop; L019/L021 were read for
the exact local inputs. There was no all-notebook or sibling-proof
scan. No mathematical calculation, script, lemma, source theorem
import or independent source-proof verification occurred. Mathlib
coverage of the proposed comparison and source formulas is unchecked.
