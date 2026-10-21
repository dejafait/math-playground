# Conductor-36 central-value diagnostic — source comparison

TARGET: Assess direct central-value recovery from L056's oriented {0,infinity} path for y^2=x^3+1, including the sign and the hypotheses of the analytic-rank-zero theorem.
CHECKED: 2026-10-14
DECISION: IMPORT
SEARCH_EVIDENCE: Checked L028, L050, L052, L056 and L057's normalization passages, foundations/02, the fixed CM assessments and ATTEMPTS/022 and ATTEMPTS/029; searched for Kolyvagin finiteness from L(E,1) nonzero including CM, then inspected Wiles's official theorem and BMS's actual definitions. No existing fixed central-value extraction was located in this scoped comparison; no novelty claim.
SOURCE_EVIDENCE: BMS, Math. Comp. 85 (2016), 983–1016, DOI 10.1090/mcom/3029, Sections 2.1–2.2 pp.988–991, equation (2.4) and the identity following the plus-symbol definition; Wiles, Clay official description, unnumbered analytic-zero/one theorem p.4 and CM discussion p.3; Stein–Wuthrich, Math. Comp. 82 (2013), Section 3 pp.1761–1762, for convention comparison only.
COMPARISON: Known central-value and analytic-rank-zero results cover the proposed diagnostic; the complete existing path record identifies generator 1 as {infinity,0}. Import the identities and theorem, retaining reversal of {0,infinity}, total minimal period and L052's degree-one differential qualifications; no new lemma or reproof is needed for the source review.
GAP: The fixed central value has not been extracted or a rank theorem applied in this turn; arbitrary analytic-order-at-least-two rank equality remains unresolved.
REASON: Essential source coverage is now supplied for the independent fixed diagnostic; repeating quadratic precision or parked universal CM retrieval would not test lower vanishing.
SCOPE: Exact conductor-36 minimal model, associated normalized rational-coefficient newform, total real minimal period, L056's audited full-relative functional and the existing oriented path record; only the complex central value and conditional rank-zero implication are covered.
COVERED_TARGET: Extract L(E,1)/Omega(E) from L056 at generator 1={infinity,0}, verify the reversed {0,infinity} sign, and apply the analytic-rank-zero theorem only if the exact value is nonzero.

## Inspected primary statements and applicability

Balakrishnan–Muller–Stein, *A p-adic analogue of the conjecture of Birch
and Swinnerton-Dyer for modular abelian varieties*, published version,
[Sections 2.1–2.2, pp.988–991](https://wstein.org/papers/mcom3029.pdf#page=6),
defines the real period by integration over all real points, imposes
c_A=1, permits compatible Shimura periods in (2.4), and states
[0]^+_f=L(f,1)/Omega^+_f. The plus numerator has the minus sign before
pi*i times the two integrals from r and -r to infinity. Its scope is
weight-two newforms on Gamma_0(N), with totally real coefficient field;
CM of the elliptic curve is not excluded. Here that field is Q.
L052's degree-one identification and differential-scale justification,
already audited in L057, meet the period and optimal-quotient conditions.
No ordinary-prime premise is needed for this complex identity.

[Stein–Wuthrich, Section 3, pp.1761–1762](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=5)
uses the same total-period and plus-symbol convention, but explicitly
assumes non-CM for the remainder of its article. It is a convention
comparison, not authority for extending its arithmetic results to E.
BMS supplies the CM-inclusive identity. L028's existing orientation
identity identifies the plus symbol with F({infinity,r}); the proposed
{0,infinity} path must therefore be reversed before using [0]^+.
No factor of two or unsigned period substitution is authorized.

[Wiles, *The Birch and Swinnerton-Dyer Conjecture*, official Clay description,
unnumbered theorem p.4](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf#page=4)
states rank equality for elliptic curves over Q of analytic order zero
or one, using modularity. Its preceding p.3 CM discussion separately
records Coates–Wiles's nonvanishing implication. The universal stated
zero/one theorem already suffices here: L050 supplies E/Q and its
associated modular newform; nonzero L(E,1), if later certified, supplies
analytic order zero. No non-CM, residual-surjectivity or ordinary-prime
condition occurs in this rank assertion. Do not infer a refined formula
or full Sha statement from the quoted theorem. The original
Coates–Wiles proof and auxiliary-twist proofs were not inspected and
are unnecessary to this use of the official named theorem.

## Complete path identification, duplicates and failure comparison

Read `scripts/conductor36-table/presentation.json` at `/endpoints/1`
and `/basepaths/1` using the inspector with `--full` for each selected
value. The endpoint is exactly [[1,0],[0,1]], meaning infinity to zero.
The complete basepath record has the same start/end, empty start chain,
one end-chain segment with h=[0,1,-1,0], coset 1, unit 35 and
Gamma_0(36) witness [-1,0,0,-1]. Its raw vector is the second standard
basis vector of length 72; its quotient coordinate vector is the first
standard basis vector of length 13. This is extraction of existing
path evidence, not a new path algorithm or a replay of L056's table.
A metadata scan found no literal zero-to-infinity original endpoint;
reversal of this specified generator is the covered means of evaluating
that orientation. No table integer or normalized value was extracted.

L056 already contains the full functional; the next step must use it,
not recompute Fourier sums or infer a value from narrow width. L057
already records the central interpolation normalization, but supplies
no extracted complex central value. ATTEMPTS/022's missing-symbol stop
has been addressed by L056; ATTEMPTS/029's universal-source blocker and
repetition stop remain intact. This independent test does not reopen
those routes. No cross-notebook input was used.

## Threshold, limitations and Mathlib

Continue with the covered finite extraction only while L050/L052's
model/newform/period qualifications and L056's audited table remain the
inputs. Verify generator 1 and reversal explicitly, then compare the
exact rational value to zero. A nonzero value ends higher-order use of
this fixed model and permits the known rank-zero theorem; zero alone
would not establish analytic order two. Failed orientation or scale
identification parks the dependent application. No rational directions,
arbitrary-curve complex-order comparison, augmentation defect or Sha
gap is closed by this review. Full matching Mathlib coverage was not
checked. This is local source approval, not mathematical progress beyond
the inspected literature; no lemma or mathematical script was written.
