# Marked-octic two-adic image — bounded attempt

2026-10-23. Work in progress on the exact unchanged TARGET in
`drafts/literature/2026-10-23-marked-octic-two-adic-point-image.md`;
the assessment existed before this invocation and is SPECIALIZE.
This is a RESEARCH / REPRODUCTION calculation, not a new source review.

The main gap is global supported class/unit arithmetic and rational/integer
point control. The intermediate target is the exact Q2 fake point image
in the entire norm-admissible common scalar quotient. Its plausible use
is filtering later supported representatives. Properness supports that
filter; equality stops it; incomplete models, tables or chart coverage
leave the exact image unresolved.

Use L113's actual G, smooth finite/reciprocal charts, and L114's full
map, norm fiber and both infinity conventions. No L116/L117 input is
assumed. Reuse Bruin–Stoll Section 2 p.3 and Section 4 pp.6–11, with
the dyadic strict bounds and two extra digits in the saved assessment.
ATTEMPTS/050–052, the three-/eleven-adic equality stops and unfinished
L108 remain intact. No backend probes or cross-notebook input.

Plan for this one attempt: first certify coordinate-square disks and
the reciprocal tail; then, as feasible, identify exact full Q2 models,
transport theta and scalars, and compute square/norm/quotient labels.
Do not infer exact fake classes from point existence or finite precision.
Both infinity points must survive separately. Save every finite test
and its actual/required precision on disk. Independent global units,
S-class two-torsion, cover points, degree-nine root recovery, remaining
factors and both L095 systems remain unresolved.

## Completed instance result

The canonical proof is L122,
`lemmas/L122-marked-octic-two-adic-point-image.md`. It constructs exact
quartic models for both entire Q2 factors with theta=(alpha,-alpha),
enumerates the complete square/norm/common-scalar quotient, and exhausts
the two point charts. Its exact point image has five classes versus
the full 64-class norm-admissible ambient set. The representatives are
identity, -theta, 2-theta, 3-theta and 1-2theta. Every class has a
finite realization; both separate infinity points retain identity.

The full certificate is
`scripts/pair-genus-two/marked-octic-two-adic-image-certificate.json`:
99 checks pass, no failures. The code-independent arithmetic replay
`scripts/pair-genus-two/marked-octic-two-adic-image-replay.json` consumes
all unit cosets, norms, norm-fiber pairs and point rows: 291 checks pass,
no failures. Actual/required residue precision is 9/9 and the alpha
error bound is 20>14; all disk inequalities are strict. Complete table
data are retained, with all collisions and one common scalar convention.
No mathematical failure arose in this attempt.

This is local progress by reproduction of assessed source methods,
not a new general theorem or progress beyond their checked theory.
Properness supports a future supported-class membership test, but no
specific global supported class is removed. All independent gaps above
remain. The one continuation is a separate critical audit of L122,
after approval of its new REVIEW_REQUIRED audit assessment. That audit
must check exact transports, complete finite tables, exhaustive charts,
realizations and both infinity rows rather than accept the check flags.

Scoped documentation validation passes with 123 nodes and 318 unique
edges. Its first run reported PROOF.md at 102 lines; joining the two
new overview additions to their related existing paragraphs restored
the 100-line cap without deleting mathematical content. This was a
documentation-length repair, not a mathematical or certificate failure.
