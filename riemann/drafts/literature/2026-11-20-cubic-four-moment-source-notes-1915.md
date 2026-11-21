# Four-moment enclosure coverage — source review1915

20 November 2026. Literature only. No H evaluation, new bound, lemma,
mathematical script, or certificate replay was performed.

The main gap remains actual-Xi all-degree positivity L030-L032/C032a
and C028b's H_d=o(d). The intermediate target is C028s's H>0.
It would pay C028r's strict scalar premise at each fixed degree;
lower residuals, full Schmeisser cost and degree-uniform control remain
independent. Continue only with a rigorous strictly positive lower
endpoint. A zero-containing enclosure decides neither equality nor
the exact sign; a strictly negative upper endpoint would contradict
the nominated strict inequality, not disprove RH.

## Existing coverage changes the proposed construction

Read L019, L021, C028r and C028s including audit1913. Reuse
source-notes1914's finite-hyperbolicity/equality comparison and the
retained source-proof obstruction; no strict source theorem is imported.
The audited coefficient convention in C028s is retained exactly.

Read L970's analytic construction, arithmetic account and audit186;
inspect its interval/exponential primitives for method scope only.
Reuse the ready assessments183/185 in
`2026-11-10-integrated-theta-variance-review-182.md` and
`2026-11-10-l970-independent-audit-coverage-185.md`.
L970 rigorously encloses different cosh/sinh-weighted integrals.
Its numerical boxes cannot be substituted for L021's moments.
Its theta-tail bounds and elementary arithmetic are available method
inputs if a future newly assessed construction becomes necessary.

The narrowly located assessment
`2026-11-09-l917-twelfth-moment-enclosure-audit.md` led to L917.
Read its complete hypotheses, moment statement, tail construction,
finite-panel inclusion argument and audit197. Read L036/L037's full
statements/proofs. L917 already encloses M_k(lambda) for even k through12,
on every closed parameter panel of [0,1/20], using exactly L019's K.
Its definition at lambda=0 is L021's moment definition. This is an
identification of existing definitions, not a newly derived estimate.
Panel0 contains that endpoint. No deformation-zero product is needed.

The canonical L917 proof gives explicit spatial and theta tails,
finite C8 panel remainders, and directed arithmetic hypotheses.
Audit197 accepts inclusion subject to L037's documented Decimal
implementation contracts. Library correctness remains assumed.
This supplies existing enclosure coverage for all four required inputs;
there is no need to derive new polynomial-weight tail constants first.

The retained certificate is
`scripts/heat/low-time-h2-uniform-195.json`.
The JSON inspector located `/panels/0` and displayed the complete
selected `/lambda` and `/moments/0`, `/moments/2`, `/moments/4`,
`/moments/6` values using `--full`. All endpoint digits remain in that
artifact. This confirms the selected records and their scope; it is
not a fresh quadrature audit or an evaluation of H. The prior analytic
acceptance is L917/audit197, not the inspector preview or a PASS label.

L917's zero-containing third H2-minor enclosures and its fixed-budget
stop are preserved. They concern a different expression. No inference
about C028s's H follows from that stop, and no narrowed lambda=0
point value may be substituted for the saved full-panel intervals.

## Primary method statements checked

NIST DLMF, live text retrieved 20 November2026, Section3.5(i),
[equations3.5.1-3](https://dlmf.nist.gov/3.5#i), with its reference to
Davis and Rabinowitz (1984), pp54,137: for real f in C2[a,b], the
one-panel trapezoid error is -h^3 f''(xi)/12, h=b-a, a<xi<b.
The composite form uses error -(b-a)h^2 f''(xi)/12.
This is an importable integration theorem, not a moment value or
an effective derivative bound. It is an alternative to L917's already
accepted C8 scheme; no quadrature reproof is warranted here.
The live release number was not independently verified.

NIST DLMF [8.4.8 and8.4.11](https://dlmf.nist.gov/8.4), read with
the stated nonnegative-integer n convention: Gamma(n+1,z) equals
n! exp(-z) sum_(k=0)^n z^k/k!. For positive real arguments this is
available for polynomial exponential tails. It does not itself
majorize the theta kernel or fix an integration cutoff. No new
substitution or effective constant is derived from it in this review.

[Official Python Decimal documentation](https://docs.python.org/3/library/decimal.html),
displayed as3.15.2, read ROUND_FLOOR/ROUND_CEILING, Context arithmetic,
copy_abs/copy_negate, exp and adjacent-number contracts. Directed
rounding controls basic operations. Decimal.exp instead uses nearest
ROUND_HALF_EVEN; L037 widens it using adjacent representable values.
Exact sign copying and rejection of exceptional arithmetic are retained.
The prior inspected assessments cover the broader construction and
rational-arithmetic contract; no source asserts the implementation
formally verified. Further coefficient propagation may use exact
rational endpoints and does not need new transcendental evaluation.

## Search and comparison limits

Queries included `Riemann xi Taylor coefficients rigorous bounds first
coefficients theta moments cubic Turan interval arithmetic`,
`"Riemann xi" "moments" "rigorous" "quadrature"`,
`"higher order Turan" "first" "coefficients" "numerical"`, and
`site.numberdb.org "Taylor coefficients of the completed" "T"`.
The exact primary enclosure statements used are the DLMF and Python
contracts above, together with the locally accepted L917 proof.
Search snippets did not establish an external four-moment H certificate.

NumberDB's derivative page was a lead; the guessed coefficient-page
URL could not be retrieved. Recent preprint hits concerning logarithmic
inequalities and kernel concavity were not inspected theorem-level
inputs. The moved FLINT acb_calc landing page was only an optional
method lead, not assessed coverage. None is essential once L917's
existing enclosures are reused. No absence or novelty claim is made.

The limited local comparison checked the named cubic assessments,
L917's enclosure assessment, L970's construction/audit assessments and
the selected certificate schema. It located existing moment coverage,
not a previously certified evaluation of this H. Preserve the
width/two-width/tilt and metric-floor stops recorded in1914.

## Decision and bounded continuation

Coverage is SPECIALIZE for applying accepted moment enclosures to
C028s's existing finite expression. No essential source blocker remains.
The next target is to propagate panel0's four full intervals through
the audited coefficient convention and H using exact rational enclosing
arithmetic. This is conventional specialization/reproduction, not a
creative signed-residual mechanism or a novelty claim. One saved-box
test suffices; do not refine the mesh, sweep other parameters or launch
a new quadrature construction within that target.

Accept only a strictly positive H lower endpoint with complete signed
propagation and the inherited arithmetic qualification explicit.
Otherwise retain conditional C028r and record the exact enclosure
failure; do not confuse interval width with an actual counterexample.
Any new construction or different mathematical mechanism needs its own
assessment. A later successful scalar claim requires separate audit.
Full matching Mathlib coverage remains unchecked and unknown.

Outcome EXPLORATION: useful source/duplicate comparison replaced a
proposed new integration construction by an existing audited input.
No mathematical strictness or RH advance was established. No justified
central creative target is specified by this finite scalar repair;
the missing signed full-residual estimate remains the blocker.
