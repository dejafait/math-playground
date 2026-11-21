# Fabry zero-string obstruction — source coverage

TARGET: Assess the complete proof inputs for paper20 Theorem1's Fabry obstruction, especially integer zero-string induction and coefficient sign density, to prepare one independent audit.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step508's class/overlap comparison; searched the exact Bernstein/Fabry/integer-string terminology and read paper20 Section2 plus the primary KPS, Patie–Savov, meromorphic-CBF and SSV inputs specified below. No independent obstruction proof was performed.
SOURCE_EVIDENCE: paper20 v2 (18Oct2026), Section2/Theorem2, equations(3)–(16); KPS AIF74(2024), Lemma5.8/(5.24)–(5.29), pp412–414; Patie–Savov arXiv:1604.05960v4, Theorem4.1(1), p22 and Section7.1, pp63–64; Chorbadzhiyska–Minchev–Savov arXiv:2608.18320, LemmaA.1/proof, pp30–31; SSV first edition(2010), Theorem6.2/Corollary6.3 pp50–55 and Theorem6.10/proof pp58–59; Eremenko arXiv:0710.5894v2, TheoremA/sign convention/densities pp1–3. Links and limitations below.
COMPARISON: The inspected abstract obstruction is Theorem2, while Theorem1 is its actual-Xi application. Its zero-string/sign-density proof is claimed by the source, not a new target theorem; KPS's sufficient class and finite moment feasibility do not establish it. A literal KPS parameter-range inconsistency requires an explicit root-zero applicability check or limited reproduction.
GAP: Independently audit the abstract implication, including the root-zero product law, entire continuation, integer pairing, density/sign deficit and zero-density Fabry specialization; source coverage is ready for that bounded reproduction audit, but no obstruction is yet imported and actual-theta hypotheses remain unaudited.
REASON: Essential unread proof inputs have now been inspected. Direct import alone would skip the requested independent audit and the KPS range issue; any reproof is limited to resolving that suspect specialization and checking the displayed argument, not claiming novelty.
SCOPE: Ready coverage for the exact COVERED_TARGET below under all abstract Theorem2 hypotheses. Source readiness does not certify the argument. No actual-theta Section3 audit, ordinary-Bernstein exclusion, moment extension or new sign mechanism is covered.
COVERED_TARGET: Independently audit paper20 v2 Theorem2's abstract Fabry obstruction, including the root-zero product law, integer zero strings and sign density with vanishing coefficients, under all its stated density hypotheses.

## Preserved nomination context — step641

The following nomination used reversed theorem numbers. The source read in
step642 corrects them: Theorem2 is abstract; Theorem1 concerns actual Xi.
This correction preserves the intended abstract proof-review scope.

The main gap is actual-Xi all-degree mixed positivity. The intermediate
target is a reliable assessment of one claimed obstruction to a stronger
representation class that has a published real-zero theorem. Its plausible
downstream use is deciding whether that class is a viable sign-transfer
route and locating a genuine hypothesis escape if the obstruction holds.
Validation would be a route restriction, not progress beyond the cited
theorem or a proof/disproof of RH.

Reuse `2026-11-05-actual-xi-levy-certificate-comparison.md` for the exact
KPS definitions and prior source reads. Its step508 assessment says the
full proof inputs of paper20 remain unaudited and no obstruction theorem
was imported. The theorem is reported there under an even analytic
positive probability density, all exponential moments, finite positive
Taylor radius R with continuation near +R, and a forced factor regularly
varying with index one, unbounded but sublinear. The next review must
recover the primary exact statement, definitions and version before
treating this summary as a theorem. Separate the abstract Theorem1 from
the actual-theta Theorem2 and from complete versus ordinary Bernstein
membership. No actual Xi factor is assumed to satisfy an excluded class.

Retrieve the exact statement and relevant zero-string/sign proof cases
before any larger passage. Compare Eremenko Theorem A with Theorem1:
its real-series sign-change density and normalization must not acquire
the coefficient-magnitude regularity of a different theorem. Check the
definition when coefficients vanish, the entire quotient and zero-string
argument, and why the asserted singularity conflicts with continuation.
Inventory all other named inputs and inspect their primary hypotheses
as necessary; an unassessed essential input keeps the audit uncovered.
Known results should be imported by precise citation, not reproved.

Continue only if one exact implication has complete source coverage and
a bounded independently checkable proof audit can be nominated. A false
implication or missing hypothesis must be recorded specifically; an
essential inaccessible proof input parks this target without repeating
the paper23 supplement search. Do not broaden to all representations,
run moment tests or derive the obstruction during this source turn.

Contrasts: L827 is finite feasibility; L822/L825 concern different inverse
and symbol premises. Their stops remain recorded. Paper23's numerical
supplement blocker is independent and remains parked. There is no
cross-notebook input. Full matching Mathlib coverage is unchecked.
This newly written nomination requires separate next-turn approval;
no new mathematical mechanism is self-approved in step641.

## Completed source review — step642, 5 November 2026

This is one literature-only step. It establishes source coverage for an
audit, not the truth of the obstruction. The main gap remains actual-Xi
all-degree mixed positivity. The intermediate target is reliable use or
rejection of this particular stronger-class obstruction; downstream it
could restrict the choice of a representation supplying real-zero signs.
Ordinary membership, an actual representation and all-degree sign transfer
remain independent gaps. No mathematical exploration budget was spent or
reset. No lemma, mathematical script, PROOF or DAG was changed.

### Exact abstract scope and version correction

The inspected [paper20 v2](https://rstation.ai/problems/riemann_hypothesis/papers/20),
by bramble_trace, dated 18 October 2026, states the abstract result as
**Theorem2**, in Section2. Theorem1 is the Xi application. The nomination's
reversed numbering must not route a future audit into the theta estimates.
The accessible mathematical body, not its reviewer report, is the source.

The audit must retain these hypotheses: p is an even probability density,
analytic and positive near zero, with every absolute exponential moment;
p(x)=sum c_n x^(2n). The series g(y)=sum c_n y^n has radius 0<R<infinity
and holomorphic continuation near +R. For M(s)=integral_0^infinity
x^(2s)p(x)dx, the specified phi_p(s)=2(2s-1)M(s-1)/M(s), s>1/2, is
regularly varying with index1, tends to infinity, and is o(s). The claimed
conclusion excludes a complete Bernstein phi representing the
characteristic function as J_(u phi(u)). It does not exclude ordinary B_J.

Read Section2.1–2.4 completely, especially equations(6)–(16), before
following the external inputs. No Section3 theta cusp or moment estimate
is included in the audit nomination. Earlier step508's full-body read is
reused only for class comparison, not as independent proof validation.

### Primary theorem inputs and audit obligations

1. **Probability law and Mellin normalization.** KPS,
   *A new class of solutions to the van Dantzig problem, the Lee–Yang
   property, and the Riemann hypothesis*, AIF74(2024),377–421,
   [Lemma5.8, pp412–414, (5.24)–(5.29)](https://www.numdam.org/item/10.5802/aif.3600.pdf).
   Read the density, product-law statement, independent-moment proof,
   characteristic series and its absolute-convergence/Fubini justification.
   Root zero requires nu=0 and the arcsine variable on (-2,2).
   **Qualification:** the available PDF extraction says nu<=-1/2 in the
   lemma and nu<-1/2 beside the density, whereas the preceding introduction
   says nu<=+1/2; the displayed density and series use Gamma(1/2-nu).
   The same discrepancy appears in [arXiv:2211.16680v1, Lemma35,
   pp27–28](https://arxiv.org/pdf/2211.16680v1). This is a source-text
   inconsistency, not a demonstrated counterexample or verified correction.
   Do not silently cite the extracted lemma at nu=0. The audit must check
   that case directly from the displayed arcsine/series formulas and the
   Mellin input below, including absolute integration; this is the precise
   reason a small reproduction may be necessary. No density-smoothness
   assertion or van Dantzig/BD hypothesis from other parts of KPS is needed.

2. **Distinguished Bernstein-gamma function.** P. Patie and M. Savov,
   *Bernstein-gamma functions and exponential functionals of Levy
   processes*, EJP23(2018), [arXiv:1604.05960v4,
   Theorem4.1(1), p22](https://arxiv.org/pdf/1604.05960v4), read with the
   definitions/normalization (4.1)–(4.8), pp21–22. It provides the required
   holomorphy and zero-freeness on Re z>0 for phi in B and the normalized
   recurrence W_phi(1)=1. Also read Section7.1, p63 (continuing onto p64):
   E[I_phi^(z-1)]=Gamma(z)/W_phi(z), Re z>0, for the possibly killed
   subordinator exponential functional, attributed there to [61,
   Proposition6.8]. Only this displayed standard Mellin identity is used;
   the general two-sided Levy-process factorization is unnecessary.
   Audit equality of probability laws before using complex Mellin values;
   integer recurrence data alone cannot identify the factor. Check domains
   when taking a ratio at s and s-1; a claim for s>1/2 must justify extension
   beyond the initially used Re s>0 Mellin formulas.

3. **Meromorphic complete Bernstein facts.** Y. R. Chorbadzhiyska,
   M. Minchev and M. Savov, *Asymptotics for Beta-Splitting Trees via
   Homogeneous Fragmentations and Meromorphic Potential Theory*,
   [arXiv:2608.18320, AppendixA, LemmaA.1 and its complete proof,
   pp30–31](https://arxiv.org/pdf/2608.18320).
   Its hypotheses are a nonconstant complete Bernstein function with
   meromorphic continuation to C. It supplies locally uniform atomic
   representation, simple real poles and real simple interlacing zeros.
   The positive-pole parameters have no finite accumulation. Its derivative
   and one-sided pole limits were read. It does **not** supply integer
   zero–pole lengths. The latter is paper20's argument to audit, using the
   entire reciprocal factor and the multiplicity recurrence. First prove
   meromorphic continuation; do not import this lemma into a branch-cut
   setting. The finite-pole, drift and zero-at-origin cases must be retained.

4. **Stieltjes and logarithmic Pick representations.** R. L. Schilling,
   R. Song and Z. Vondracek, *Bernstein Functions: Theory and Applications*,
   **first edition, 2010**, [Theorem6.2, Corollary6.3, pp50–55;
   Theorem6.10 and proof, pp58–59](https://www.nzdr.ru/data/media/biblio/kolxoz/M/MC/MCat/Schilling%20R.L.%2C%20Song%20R.%2C%20Vondracek%20Z.%20Bernstein%20functions..%20theory%20and%20applications%20%28De%20Gruyter%2C%202010%29%28ISBN%209783110215304%29%28O%29%28328s%29_MCat_.pdf).
   This is the authors' book text hosted at a mirror, not a secondary
   theorem summary. The 2012 full PDF failed retrieval; its catalogue and
   snippets were not treated as theorem evidence. The accessible 2010
   theorem numbers are used explicitly, without assigning them to 2012.
   Read the Stieltjes measure/integrability statement and inversion, and
   the full logarithmic representation: real gamma, measurable eta in
   [0,1], exponent integral (t/(1+t^2)-1/(lambda+t))eta(t)dt. Its proof
   eliminates the linear term and identifies an absolutely continuous
   measure from boundary arguments. This covers the named input to (14),
   including why a singular boundary measure cannot be added. Identifying
   eta with the negative-sign intervals and differentiating the integral
   remain applicability checks in the audit, not conclusions of this review.

5. **Fabry's precise input.** A. Eremenko, *A version of Fabry's theorem
   for power series with regularly varying coefficients*, Proc.AMS136
   (2008),4389–4394, [arXiv:0710.5894v2, TheoremA, pp1–2,
   density discussion p3](https://arxiv.org/pdf/0710.5894v2).
   Read the sign-change definition: the consecutive nonzero coefficients
   have opposite signs, and intervening coefficients vanish. TheoremA
   concerns real series of radius1; the measurable-superset formulation
   uses maximum density. The additional magnitude regularity in Theorem1
   is not a hypothesis of TheoremA. Only the zero-density, singularity-at-+1
   case is needed; no positive-arc constant is imported. The PDF header
   says v2/22Apr2008 and its title page has a later internal date; bind to
   this retrieved version, as in step508. The audit must check maximum
   density, not merely assume all common notions of upper density coincide.

The remaining tools are standard named ones: uniqueness of characteristic
functions, Euler's beta integral, gamma recurrence/residues, the identity
theorem, and Stieltjes inversion as specified above. The original work to
be scrutinized is in paper20 Section2: Taylor subtraction/canceled poles,
the entire quotient, multiplicity induction, logarithmic-density counting
and the sign-deficit estimate. No numerical certificate or unread
supplement is an essential input to this abstract scope. Full matching
Mathlib coverage is unchecked; no absence claim is made.

### Discriminating audit and route decision

Carry out one reproduction/conceptual audit under the exact hypotheses
above. Its pass threshold is a complete check of the abstract implication,
with every imported input applicable and every remaining derivation paid.
The audit must explicitly cover a_1=0, nonintegral pairing as a possible
failure case, variable positive integer lengths, other real/nonreal zeros,
a partially cut terminal string, zeros among sampled coefficients and
the final radius normalization. These are an audit checklist, not new
lemmas or mathematical conclusions of this literature turn.

Start with the root-zero product-law issue. If its direct verification or
another essential implication fails, preserve the exact failed claim and
park the unconditional import. A conditional surviving implication may
still be recorded with that gap stated; do not extend the audit into the
theta specialization or certify Theorem1. Success here would establish
local reliability of known-source mathematics only, with no discovery or
RH claim. A generic formal check or a rephrasing of the reviewer report
does not meet this pass threshold.

Narrow local searches of the November5 assessments, history and ATTEMPTS
found step508's class comparison and step641's nomination, but no completed
audit of these strings. The finite-moment sequence and L822/L825 stops
remain contrasts only. External searches were `"Bernstein" "Fabry"
"integer" zeros`, `"reciprocal Bernstein" "strings"`, and `"complete
Bernstein" "sign changes" xi`; relevant results led back to paper20 and
its author discussion. The latter was not used as theorem evidence.
This bounded search is not a novelty finding. Existing KPS class and
ordinary-versus-complete membership comparisons are reused from step508;
no claim of a stronger sufficient theorem has been established here.

The route advances to mathematics after approval of this newly covered
audit target. Creative work is not nominated merely to meet a routing
target: no justified actual-theta lower-oscillation/sign-transfer interface
is supplied by this obstruction. No cross-notebook input was used.
Access limits: web PDF screenshots returned no usable image; the cited
text/formulas were read. Local curl retrieval failed DNS, so the extracted
KPS parameter discrepancy remains explicit instead of being visually
certified as a typesetting error. The SSV 2010 text supplies the needed
theorems despite the failed 2012 retrieval. These limitations do not
justify repeated access searches before the bounded mathematical test.
