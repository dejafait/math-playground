# L637 conceptual audit checkpoint

Completed: the full audit is canonical in
lemmas/L637-hardy-translate-dual-cost-and-absolute-error-budget.md.
All stated bounds passed under their named imports without correction.
The intermediate reasoning below is preserved as a checkpoint, not a
remaining task or a second canonical proof.

Approved invocation target: critically audit L637's weighted Fourier overlap,
moving-cutoff Hardy correlation and complete TV error comparison, including
the upper-bound-only scope of the obstruction. The supplied EXPLORE assessment
is drafts/literature/2026-11-01-l637-dual-cost-audit-scope.md.

Main gap: actual-Xi pointwise initial signs at unbounded heights and all-degree
mixed positivity. This audit can validate or repair the qualified absolute-budget
stop; it cannot establish either missing positivity statement.

Partial replay: L637 Sections 1--3 pass. The filter has a two-sided Fourier gap;
Plancherel's loss is at most P^2/pi. The q norm tends to ||h||/P<=1 and its
overlap tends to at least 1-1/pi, leaving 3/4-1/pi>0 above tolerance. Both
convergences are independent of X. Safe division uses w>=w0/2. The frozen
Riemann--Siegel cutoff retains the extra one in its floor difference, and
changed coefficients are all O(T^(-1/4)). The Taylor bound need not be small
pointwise because the complete |h| second moment is finite. Both oscillatory
orientations vanish; the cutoff tail and undifferentiated remainder are charged.
Thus the correlation is uniformly O(T^(-1/4)/sqrt(log T)), including crossings.

Moment replay in progress: all six terms in (18) match L622's h=k=1 expression;
L465's phase and gauge bounds follow from the paired gamma logarithms. L622's
Sections 1--4 and separate conceptual-audit passage have been read in full.
Need final explicit check of an open complex neighborhood, Q's normalization,
all coefficient pairs, the fixed translated-weight majorant and the inference
from the upper envelope. Named source coverage is reused, with no retrieval.

Pass test: constants independent of atom count, locations, complex coefficients
and X; any genuine failure must be repaired or the exact claim withdrawn.
No new source theorem, novel result or RH candidate is asserted at this checkpoint.

Completion: verified an open complex domain for all Cauchy contours, the
three-unit Q cost and L^2 conversion, every complex coefficient pair,
the fixed translated-weight majorant at unchanged X, and the full zero-safe
curvature cost. The envelope comparison retains its upper-bound-only scope.
No source retrieval or mathematical script was required. Continuation routing
is recorded only in PROGRESS.md; this audit target is complete.
