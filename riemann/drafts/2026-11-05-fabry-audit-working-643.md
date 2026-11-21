# Abstract Fabry audit working record — step643

Approved target: independently audit paper20 v2 Theorem2 under the exact
hypotheses in the pre-existing step642 SPECIALIZE assessment. This is a
reproduction/conceptual audit, not a theta specialization or new mechanism.

Main gap: actual-Xi all-degree mixed positivity. A validated abstract
class obstruction would restrict a possible representation route, without
establishing actual representation or signs. Pass only after checking the
root-zero law, full Mellin domain, entire quotient, integer pairing,
density and Fabry with zero coefficients. Preserve any failed implication.

Initial source read: paper20 v2 Section2, equations(3)–(16), retrieved
5 November 2026. The existing KPS parameter discrepancy remains explicit.
Plan for its bounded check: use the displayed arcsine moments and the
Patie–Savov exponential-functional moments; justify characteristic-series
integration by the nonnegative cosh series. Use analytic continuation to
reach Re(s)>-1/2 before taking the ratio at s and s-1.

Intermediate checks completed: the cosh-series ratio is
t^2/((n+1)phi(n+1)), bounded by t^2/((n+1)phi(1)); this justifies the
root-zero characteristic law. The Mellin identity extends from Re(s)>0
to Re(s)>-1/2 before taking the ratio for real s>1/2. Taylor cancellation
has the normalization in paper20 equation(8), including its factor 4^n.

The multiplicity recurrence gives a finite sum along each unit lattice.
At the first pole an unpaired negative contribution would give negative
zero multiplicity; after cancellation the same argument applies to every
later pair. An interval of integer length contributes exactly its length
in zeros; a terminal partial interval changes the count by at most one.
The sign-deficit sum includes zeros at skipped integer coefficient indices.
For fixed r>0, a global o(x) sign count gives zero limsup increment density;
the subsequent r-down-to-zero limit is therefore zero.

Remaining task: assemble the full canonical proof with every hypothesis,
the imported logarithmic representation, domination for differentiation,
and the zero-radius-normalization endpoint application. The supplied SSV
2010 coverage is reused; this turn's optional mirror retrieval timed out
and supplies no new theorem evidence. No mathematical scripts are planned.
Existing unfinished files are preserved.

Completed: the full canonical argument and source qualifications are in
L828, lemmas/L828-abstract-fabry-complete-bernstein-obstruction.md.
This working record is retained as the interruption checkpoint, not a
second canonical proof. The abstract audit passed; no actual-theta
specialization was attempted.
