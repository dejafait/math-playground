# CM ordinary arithmetic source comparison

This is source review only. No new arithmetic specialization, coefficient,
lemma, script or CM extension of L004 is proved here.

## Inspected published statements

Chan-Ho Kim and Masato Kurihara, *On the Refined Conjectures on Fitting
Ideals of Selmer Groups of Elliptic Curves with Supersingular Reduction*,
DOI 10.1093/imrn/rnz129, author-hosted advance-article PDF (2019 heading;
2021 download stamp), [Section 2.1, p.12, Conjecture 2.2 and Theorem
2.3(1)](https://kurihara.math.keio.ac.jp/RefinedConjectures%28KimKuirhara%29.pdf#page=12),
attributes the ordinary CM characteristic-ideal equality to Rubin,
*The “main conjectures” of Iwasawa theory for imaginary quadratic fields*,
Invent. Math. 103 (1991), 25–68, Theorem 12.3,
[DOI 10.1007/BF01239508](https://doi.org/10.1007/BF01239508).
The restatement uses the classical Selmer group over Q_infinity and the
unit-root p-stabilized L-function. The inspection also included p.1's
standing good-reduction/non-anomalous restriction, p.5's irreducibility
simplification, and Section 2.2, pp.13–14: its finite-level argument
introduces non-anomalous/Tamagawa hypotheses. These must not be silently
transferred to, or dropped from, a universal import. No residual
surjectivity premise is stated in the CM branch of Theorem 2.3.

Robert Pollack and Karl Rubin, *The main conjecture for CM elliptic curves
at supersingular primes*, Ann. Math. 159 (2004), 447–464,
[introduction pp.448–449](https://math.arizona.edu/~rpollack/Papers/Main_conjecture_for_CM_elliptic_curves_at_ss_primes.pdf#page=2),
describes the ordinary CM result via elliptic units, character twisting
and restriction to Q_infinity. Its actual signed supersingular theorem
is outside this target. The introduction is not a complete specialization
proof, and was not treated as one.

Balakrishnan–Muller–Stein, *A p-adic analogue of the conjecture of Birch
and Swinnerton-Dyer for modular abelian varieties*, Math. Comp. 85
(2016), 983–1016, DOI 10.1090/mcom/3029,
[Theorem 1.6 and equation (1.3), p.986](https://wstein.org/papers/mcom3029.pdf#page=4),
states Kato divisibility f_A | p^m L_p(A,T) for elliptic A, and explicitly
ord_T L_p >= ord_T f_A. No CM exclusion or residual-surjectivity condition
is imposed there. This is a published theorem translation, not a new
reading of Kato's original proof. Sections 2.1–2.3, pp.987–993, use the
optimal quotient, running c_A=1, total Neron periods, the ordinary unit
root and the untwisted Teichmuller-trivial measure. Equations (2.6)–(2.8)
use T=kappa(gamma)^(s-1)-1; (2.9) retains (1-alpha^(-1))^2. No bad Euler
factors are deleted. The inspected construction and its Proposition 2.9
proof match the already audited L057 input. This supplies a direct
one-sided source for the fixed curve, without needing Rubin equality.
No integral equality, height converse or refined formula is imported.

## Applicability contract, not a new proof

L002 and foundations/03 define the same classical Selmer dual X; fine,
strict, relaxed and signed Selmer groups are excluded. L057's audited
source-applicability passage (lines 74–109 in its file) records the rational
coefficient field, optimal degree-one model, differential scale one,
total minimal real period and good-ordinary seven. Its hypotheses fix
S(r)=F({infinity,r}), unit root of X^2+4X+7, trivial branch and gamma with
kappa(gamma)=8. These are the inputs for the later written import.
L050/L052/L056 and L028 retain the arithmetic, scale, all-relative
symbol and orientation qualifications already inherited by L057.

There is no auxiliary CM character or CM-field cyclotomic descent in
this fixed Kato translation. The primitive p-factor stays present; no
exceptional-zero division is permitted. Period rescaling, inversion of
gamma, extra Euler factors or different local conditions require a
separate justification; they are not performed in this review. The next
import must record precisely the theorem's divisibility ring (or use its
explicit order inequality), retaining any power-of-p qualification.
L058 is a nonzero-coefficient test only; it supplies no lower vanishing
or independent rational directions. L003's non-CM height converse stays
outside the proposed import.

## Source access and boundary of approval

Rubin's author index could not be fetched by the web tool; a shell curl
attempt also failed to produce a file. Springer redirects the PDF URL to
an article page offering paid access; no purchase or authentication was
attempted. EuDML browse retrieval failed. GDZ's volume shell was readable
but no theorem text was obtained from its download/manifest endpoints.
Several guessed author/download endpoints failed; those failures are not
mathematical evidence. Rubin Theorem 12.3, its exact CM-order assumptions,
character normalization, local factors and complete cyclotomic proof
remain unread. The universal Rubin import is therefore parked, not
refuted. No further endpoint guessing is the continuation.

The independent fixed directional import uses the inspected 2016 source
statement instead. The underlying original Kato Theorem 17.4 remains an
indirect citation, as in foundations/05; no fresh proof reading is claimed.
If that published translation is rejected in a later critical audit, the
fixed import must be parked, rather than inventing an Euler-system proof.
Mathlib matching coverage is not checked; no absence claim is made.

## Search and local checks

Queries included CM elliptic curve cyclotomic main conjecture Rubin
ordinary Selmer p-adic L-function; Rubin 1991 Theorem 12.3; the exact
1991 title with pdf/EuDML/GDZ restrictions; and BMS 2016 arithmetic scope.
Search snippets and unrelated recent anticyclotomic leads were discovery
only. Hsieh's long CM-field PDF was located but no load-bearing theorem
from it was read or imported. The 2016 www mirror failed; wstein.org worked.

Local searches were restricted to foundations and drafts/literature;
needed hypotheses were read in L002/L004/L057. No existing CM arithmetic
coverage was found. The prior analytic assessment explicitly left this
scope unread. ATTEMPTS/022 concerns repeated conditional coefficient
reviews without normalized symbols, and does not forbid this source
comparison. L058's completed audit and earlier failed finite schedules
remain closed. No cross-notebook input was read.

## Direct-source recovery check — 2026-10-14

Reopened the [publisher offprint](https://wstein.org/papers/mcom3029.pdf#page=4),
including a visual check of printed p.986. Its good-ordinary standing
scope, classical Selmer dual, Theorem 1.6 and explicit order inequality
are unchanged. Rechecked the running differential hypothesis (p.988),
period choice (p.990), plus-symbol orientation (p.991), trivial-branch
measure and generator coordinate (p.992), and interpolation multiplier
(p.993), against the already audited L057 conventions. No mismatch was
found within the fixed assessed scope. The direct URL is now in the
assessment field itself. No universal Rubin access was retried, and no
new mathematical conclusion is established. Mathlib remains unchecked.
