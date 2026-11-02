# Fixed mixed correlation: completed admissibility source comparison

TARGET: Determine whether M(t)=integral_R k(s+t)Q(s-t) ds is absolutely convergent for every real t and defines a tempered regular distribution, for actual theta k and L600's fixed Q.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact-formula, Jacobi mixed-correlation, weighted-convolution and tempered-distribution searches completed; scoped local comparison reused the theta-heat assessment and uncorrected-L2 stop. No inspected theorem settles this exact M; queries and reading limits below. No novelty inference.
SOURCE_EVIDENCE: Read Gröchenig, Weight Functions in Time-Frequency Analysis, Lemma 5.1 and its continuous-space clause, pp. 8-9, plus Definition 1 and Lemma 4.1 proof; Ramond, Distributions and Partial Differential Equations (2015, version 2.06), Definition 5.3.1, Proposition 5.3.2, Exercises 5.3.7/5.3.11 and Proposition 5.6.6; Costin OSU course notes, Theorem 1.256, p. 51. Reuse unchanged DLMF inputs in L600; read L019/L600 fully, relevant real-axis L239 proof and L233.
COMPARISON: Known weighted Young bounds control a weighted norm under explicit weight/membership hypotheses; dominated convergence requires an integrable envelope; tempered convolution assumes a tempered input. None supplies the exact M conclusion without checking those hypotheses and signed translation behavior. L600 is only an ordinary-L2 stop; L233 contains no Q identity.
GAP: For this fixed M, prove or refute full finite-shift absolute convergence, local uniform domination and tempered regular-distribution membership. Required weight bounds, endpoint translation limits and any noncancelling averaged growth remain unproved; pointwise exponential growth alone is insufficient to refute temperedness.
REASON: Coverage now suffices for a bounded specialization of existing endpoint estimates and standard convolution/distribution tests. A citation alone does not verify the logarithmic theta profiles or translated signed mass. No new general theorem, sign mechanism or novelty is claimed.
SCOPE: This exact uncorrected M, real s and t, ordinary Lebesgue integration, and the regular distribution it defines if locally integrable. No endpoint subtraction, symmetrization, weight, regulator, positivity, complete-kernel identity or Xi transfer.

## Exact inputs and prospective test

Let k(u)=K(|u|), with K exactly as defined in L019, equivalently the
even real-axis continuation in L239. Let Q be exactly L600's
uncorrected profile, with its normalization and both endpoint bounds.
No new definition of Q is licensed. L600 and the real-axis portion
of L239 would be essential mathematical inputs to a later attempt;
L019 fixes normalization. L233 explains possible downstream use and
is not a premise establishing any property of M. No cross-notebook
input is proposed. No mathematical assertion about this M has been
derived during the L600 audit.

The literature-only invocation has now completed this comparison and
prepared SPECIALIZE coverage for the unchanged target. The approved
mathematical scope is only the admissibility test below; no result
about M is asserted by approval. The existing DLMF reading need not
be repeated for unchanged identities.

After separate approval, a mathematical attempt would test absolute
convergence for every fixed t, local uniform domination, and the full
translation-endpoint behavior needed for temperedness. A finite shift
preview or Q's failure of L2 is not decisive evidence for this target.
An obstruction would park only this fixed mixed term as an ordinary
Fourier component. Admissibility would establish only that prerequisite;
a complete associated-kernel identity, independent residual control,
the first sign and all higher signs would remain open. Do not infer
Fourier positivity or assume an identity in order to test admissibility.

## Route comparison and stopping conditions

Three possibilities were compared without calculating a new target:

- The unchanged ordinary-L2 square factor is now stopped by audited
  L600; neither more source approval nor another replay is justified.
- A corrected elliptic lift changes the profile but lacks a selected
  correction and a complete identity; an unspecified correction is
  not an independently testable next target.
- This fixed mixed pairing changes both the object and the required
  analytic property. It has an explicit definition and a finite
  convergence/growth discriminator, so it is the selected continuation.

These are local route choices, not a global ban on theta heat methods.
Existing generic/parity/reflected countermodels remain contrasts with
their own hypotheses. Retain the full-factor obstruction in ATTEMPTS.
There is still no specified complete identity with independently
bounded signed residual that warrants a creative sign attempt; that
mechanism gap, together with this target's missing source coverage,
blocks such routing now. This diagnostic is not labeled creative.

Mathlib: matching mixed-correlation/temperedness coverage has not been
checked; availability unknown. The inspected analytic sources suffice
for this test without a Mathlib dependency.

## Inspected primary inputs and limits

1. Karlheinz Gröchenig, *Weight Functions in Time-Frequency Analysis*,
   Fields Institute Communications **52** (2007), 343-366;
   [arXiv:math/0611174v1](https://arxiv.org/abs/math/0611174v1),
   submitted 7 November 2006. Read the
   [24-page Fields PDF](https://www.fields.utoronto.ca/programs/scientific/06-07/ISAAC/grochenig.pdf),
   Definition 1, pp. 2-3; Lemma 4.1 and its proof, pp. 4-5;
   and Section 5 through Lemma 5.1, pp. 8-9. Weights are continuous
   nonnegative functions; v is submultiplicative and m is v-moderate
   when m(x+y)<=C v(x)m(y). With norm ||f||_(L^p_m)=||fm||_p,
   the continuous-space clause gives L^1_v * L^p_m subset L^p_m.
   The p=infinity weighted-envelope case is relevant. The printed proof
   of Lemma 4.1 uses absolute convolution and the weight inequality;
   Lemma 5.1 refers to that argument and Feichtinger [11] for detail.
   Feichtinger, *Gewichtsfunktionen auf lokalkompakten Gruppen* (1979),
   451-471, was identified in the bibliography but not inspected.
   No assertion from that unread paper is needed. A weighted essential
   norm conclusion alone does not verify every finite shift or temperedness.

2. Thierry Ramond, *Distributions and Partial Differential Equations*,
   title date 19 January 2015, footer autumn 2014, version 2.06,
   [author's PDF](https://www.math.u-psud.fr/~ramond/docs/cours/distributionsedp.pdf).
   Read the Schwartz norms on p. 91; Definition 5.3.1 and the complete
   extension proof of Proposition 5.3.2, pp. 99-100; Exercises 5.3.7
   and 5.3.11, pp. 100-101; and Proposition 5.6.6 with its proof,
   p. 115. Temperedness is the bound |<T,phi>|<=C N_p(phi) on
   compactly supported smooth tests, with
   N_p(phi)=sum_(|alpha|,|beta|<=p) sup |x^alpha partial^beta phi|.
   Exercise 5.3.11 states N_p(tau_a phi)<=C_(p,phi)(1+|a|)^p
   and asks to exclude exp(x). This is an exercise, not a proved
   endpoint theorem for M. Exercise 5.3.7 supplies the warning that
   exp(x)exp(i exp(x)) can be tempered despite its growth.
   Proposition 5.6.6 assumes T in S' and phi in S, then places their
   convolution in S'; its proof uses the assumed T seminorm bound.
   It cannot be invoked before its input hypothesis is verified.

3. Ovidiu Costin, OSU 805-12 *Course notes*, Chapter 1, Section 1.8a,
   [course-hosted PDF](https://math.osu.edu/~costin/805-12/c1.pdf),
   Theorem 1.256 and following parameter paragraph, printed p. 51
   (PDF page 56). Read the complete statement: measurable functions
   converging almost everywhere and dominated in absolute value by
   one L1 function have convergent integrals; the text explicitly
   includes metric-space parameters and complex functions.
   This is the named Lebesgue dominated convergence theorem, imported
   without reproof. The PDF has no inspected revision date; this is
   the 65-page version served on 2026-10-31.

The sources above were read through primary PDF text, including the
complete load-bearing statements and the indicated proof cases.
Optional screenshots of Ramond/Costin timed out and a temporary local
PDF download failed DNS resolution; neither is essential missing
coverage because the primary theorem text was retrieved completely.
The MIT OCW lecture-14 landing page was opened but its PDF theorem
content was not read and is not an input.

## Searches, strongest comparison and duplication

Searches on 2026-10-31 used:

- `"Riemann" "theta" "mixed correlation" heat kernel`;
- `theta Jacobi derivative convolution exponentially growing tempered distribution`;
- `"theta" "k(s+t)" "Q(s-t)"` and `"k(s+t)Q(s-t)"`;
- `"Jacobi" "mixed correlation" kernel` and
  `"theta" "correlation" "elliptic derivative" Riemann`;
- `tempered distributions positive function exponential growth translated test function lecture notes`;
- `weighted convolution submultiplicative exponential weight L1 theorem lecture notes`;
- `"weighted convolution" "exponential" "Young" theorem`;
- `weighted Young inequality moderate weight convolution lecture notes Gröchenig`;
- `site.maths.ed.ac.uk dominated convergence theorem measure notes`.

No returned inspected theorem states admissibility of this exact M.
The strongest relevant inspected general inputs are the weighted module
bound and the distribution seminorm criterion, with the qualifications
above. Search snippets, unrelated theta-distribution probability papers,
and other returned leads supply no mathematical premise. This bounded
search does not certify novelty.

Scoped local reads/checks concerned L019/L239/L233/L600, the existing
Jacobi profile assessment, the theta-heat/autocorrelation assessment,
and `ATTEMPTS/2026-10-31-uncorrected-jacobi-heat-l2-factor-stop.md`.
The parent's recorded parity/reflected/generic countermodels retain
their original scope; their assessment is reused rather than replayed.
The stop expressly excludes any conclusion about mixed terms. No local
completed proof of this fixed M was located in those records. No sibling
notebook input was read and no cross-notebook theorem is being imported.

## Exact specialization permitted after the source gate

Use L019 to fix k and its strict positivity, the real-axis portion
of L239 for its even extension and complete endpoint bounds, and
L600 for the unchanged Q and its full-series endpoint estimates.
L233 is possible downstream context only. No Fourier identity with Q
is an input.

A mathematical attempt may choose weights and verify their hypotheses,
write explicit integrable envelopes for the entire fixed-shift product
and for t in each compact interval, then apply dominated convergence
with every hypothesis checked. It must retain the change-of-variable
scaling and both translation directions when testing temperedness.
A negative conclusion needs signed averaged mass violating the
Schwartz seminorm bound, or another complete distributional obstruction;
large pointwise values alone are insufficient. A positive conclusion
needs an actual tempered-distribution bound, not only convergence or
an exponential upper bound. No endpoint limit, sign, weight membership,
or conclusion of either kind has been calculated in this review.

**Continuation/abandonment test.** Finish the all-finite-shift and local
integrability tests and compare full translated signed mass with the
polynomial seminorm threshold. Nonadmissibility parks only this fixed
uncorrected mixed term as an ordinary tempered Fourier component.
Admissibility licenses examination of a later specified identity; it
proves no first sign or higher sign. A complete identity and independent
residual estimate are still absent, which blocks a justified creative
central-sign attempt at present. This routine specialization is not
being relabeled creative to satisfy scheduling preferences.
