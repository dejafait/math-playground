# Sector-sextic attempt1470 — working record

The unchanged EXPLORE assessment1468, completed in review1469, authorizes
only the fixed sextic (2,4) witness/impossibility test. Main gap:
actual-Xi all-degree positivity and the unpaid exceptional-root deficit.
A witness stops this finite shortcut; impossibility retains a finite
prerequisite. Neither outcome supplies actual-factor applicability.

C020n and its audit1468 were read, with C020m/audit1464 and the reused
Walsh interface as comparison. No exact sextic result was found in the
targeted existing records. No new source search is needed.

Initial reduction to test: an allowed nonreal quadratic factor has
form 1+a z+b z^2, a>0, t=b/a^2 in (1/4,5/18]. Its image of x^6 is
x^4(x^2+6a x+30b), with quadratic discriminant a^2(36-120t),
which is at least (8/3)a^2>0. Walsh therefore certifies preservation
of sextics for each such factor, including repeated roots. A product
of these factors is still a preserver on the same space. Real linear
factors have the usual Rolle count contraction. These observations
do not yet prove a partial-count law for a quadratic factor.

Planned bounded test: attempt either an exact input with four real and
two nonreal roots whose output has two real and four nonreal roots, or
a proof excluding this throughout the permitted quadratic range and
its products. Coefficient nonnegativity of an individual input may be
arranged by a sufficiently large rational translation if a rational
input is found, since translation commutes with q(D). This remains a
construction plan, not a certified witness. Root samples cannot prove
impossibility. Retain multiplicities and all exceptional cases.

The quartic positivity proof handles a root-free output; it alone says
nothing about a sextic output retaining two real roots. Any extension
of that reasoning requires a separate argument within this target.

Interim evidence: search1470 tested 40,000 inputs for the endpoint
q=1+z+(5/18)z^2 (20,000 fourfold-root inputs, 20,000 other samples).
No floating candidate occurred; this is not a proof. The initial JSON
serialization failed on a NumPy integer key; it was corrected and the
same seeded run completed. Full output is in the search1470 JSON.

For p=x^4(x^2+3x+c), exact multiplication at this endpoint gives
q(D)p=x^2(x^2+4x+10/3)(x^2+5x+c). Thus a boundary cancellation
retains two real roots in the nonzero quartic factor. This covers only
that subfamily. A separate inverse-moment check found determinant
-1238/19683 for the 4-by-4 matrix at t=5/18, whereas C020n's
3-by-3 determinant is positive. The quartic inverse-positivity mechanism
therefore cannot simply be extended; its significance to the exact
(2,4) test remains unresolved. These interim computations are not an
impossibility claim, and do not change the approved target.

## Completion

The exact inverse-method obstruction and its full proof are now
canonical in C020o. Certificate1470 verifies the positive input,
negative inverse value, sector boundary and degree-six Walsh
normalization. It does not certify a (2,4) witness. All relevant exact
coefficient/matrix/check fields were inspected, without algebra failures.
Independent critical audit remains pending.

The refined floating search used 80,000 inputs (20,000 fourfold-root,
40,000 two-double-root, 20,000 other real-root samples) and found no
candidate. The first 20,000 overlap the initial run; these are not
120,000 independent inputs. Approximate output-real-count tallies were
39,289 with four and 40,711 with six. Neither run proves impossibility.
NumPy is available; SymPy and SciPy imports failed, and no packages
were installed. Exact certification uses only standard-library rationals.

The saved target remains unresolved. A concrete continuation is to
parameterize a putative double output root by Tp(x)=0 and (Tp)'(x)=0,
with four real input roots and one conjugate pair, and check the local
root-count change exactly. This addresses partial counts directly.
The unchanged assessment covers the same finite target; it does not
permit inferring the full class from a single factor or omitting
multiplicities. C020o is method-stop motivation, not an assumed partial-
count theorem. No central actual-Xi creative mechanism is supplied.
