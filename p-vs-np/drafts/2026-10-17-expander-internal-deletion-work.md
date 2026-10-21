# Step 284 — structural threshold work

Approved target: determine whether L031's used expander family meets L073's
logarithmic positive-internal deletion promise. Reuse the unchanged
SPECIALIZE assessment `drafts/literature/2026-10-17-expander-internal-deletion-threshold.md`.

The exact p_i gates and shared original x_v vertices contain the once-subdivided
graph J=I(G), independently of sigma. No sign vertex or original may be deleted.
For D consisting of positive internal vertices, J-D=J-(D intersect {p_i}).
The inspected subdivision/subgraph/deletion theorems therefore reduce the
test to a lower bound on tw(G). Marx's half-balanced separator, followed by
a union of components of size between n/4 and n/2, gives
tw(G)+1 >= epsilon*n/4; thus tw(H-D)<=2 forces
|D intersect {p_i}| >= epsilon*n/4-3. This counting specialization and its
full hypotheses are to be written canonically, with the source citations.

Length comparison under check: B=11*Delta+5 gives
T <= 128*B*n*log_2(2*B*n). Using log_2(n)<=n-1 for integer n>=2 yields
T+2 <= C_Delta*n^2, C_Delta=128*B*log_2(2*B)+1.
Hence epsilon*n/4-3 > log_2(C_Delta)+2*log_2(n) is a sufficient finite-size
failure test. The linear-versus-logarithmic comparison stops this family
application only, not alternative data/certificates or other proofs.

Completed: the full proof, citations and threshold tests are canonical in
`lemmas/L074-expander-internal-deletion-threshold.md`; Attempt 028 records
the stopped family application. This scratch note is not a second proof.
No script or external search was needed. Arbitrary ER, formula-only bounds,
W/V/U and SAT transfer remain unresolved. All existing unfinished work is preserved.
