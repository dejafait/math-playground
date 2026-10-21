# L090 — Complete table of the index-sixteen multiplier order

## Hypotheses

Use audited L067's entire degree-48 field K=Q[t]/h for
E: y²+y=x³+x²−2x, primitive H=343h, L077's original nonmonic
b-basis, L078's m-order and L080/L084's n-order. Retain
L085/L086's complete s-order, L087/L088's complete u-order U and
audited L089's identification, for I=√(2U),

\[
V=(I:I)=\sum_{i<44}\mathbf Z u_i+
              \sum_{44\leq i<48}\mathbf Z(u_i/2),\qquad [V:U]=16.
\]

Keep all rational transports and both original point coordinates, the
scale chain 31/62/124/248 and actual identity. Fixed steps
329/331/333/335/337/339/341/343 and complete step-345 evidence are supplied.
The unchanged prior SPECIALIZE assessment is
`drafts/literature/2026-10-19-index-sixteen-multiplier-table.md`.

## Conclusion

Put v_i=u_i for i<44 and v_i=u_i/2 for 44≤i<48. In
`scripts/seven-torsion/index-sixteen-table-347/`, `v-basis.json` and
`v-product-00.json` through `v-product-47.json` give the entire integral
multiplication table

\[
v_iv_j=\sum_{k=0}^{47}e_{ijk}v_k\qquad(0\leq i,j<48).
\]

Independent original-H replay verifies all 2304 ordered products and
110592 integer slots, all six coordinate transports, eight inverse
products, the entire audited lattice and inclusion, and the actual
identity with 96 left/right actions. Scale 496 is checked integral in
every power-coordinate position. Every persisted V division is reread
and checked against its reconstructed actual dividend.

One combined execution passes with conservative inclusive bounds
14 seconds <180 and 84419848 bytes <134217728. This is fixed
known-method reproduction. Its separate critical audit below passes.
No further multiplier, maximality of V, global maximality, complete
units/classes, descent enclosure, rational membership or arbitrary-curve
complex-order/rank comparison follows.

## Proof

**Known full lattice, rather than a new multiplier test.** Import L089's
audited identification of the entire V. Its general input is Peter
Stevenhagen, *The arithmetic of number rings*, in *Algorithmic Number
Theory*, MSRI Publications **44** (2008), pp.209–266,
[Lemma 6.4 p.221 and Section 9 pp.233–235, equation (9-2), Proposition
9.3 and the following action/kernel/lifting paragraph](https://library.slmath.org/books/Book44/files/08psh.pdf#page=27).
Here U is a full order in L067's number field; two is a nonunit and
I contains 2U, so I is a nonzero full finite module. The cited
multiplier integrality theorem applies without odd-prime or monogenic
restrictions. Its audited specialization identifies V as a full integral
order. This theorem is imported without reproof or a new radical/action
kernel computation. It supplies neither these table coefficients nor
the execution bound, which require the finite specialization below.

**Complete inputs before table production.** The fresh `input_verify.py`
and `verify_u.py` are byte-identical copies of the step-343 independent
verifiers, retained also in step 345. They reconstruct the entire
b/m/n/s/u basis chain from H and the explicit L078 columns, both original
coordinate maps and all forward/reverse transports. They check both
inverses for each coordinate pair and the full multiplier/inclusion
inverses, all integer slots and all 2304 original-H products in each of
the S and U tables. Actual identities and their two-sided actions are
checked. Scales 31/62/124/248 and leading coefficient 343 remain explicit;
Fraction reconstruction includes integer zeros.

All 49 S basis/table files agree across steps 329/331/333/335/337/339/341,
and all 49 U files agree across 339/341/343/345. All entries of the
step-343 and step-345 copy manifests are checked against both original
source and fixed-copy hashes. Hash agreement binds provenance; the
polynomial and matrix identities independently validate the arithmetic.

Before V production, `stage.py` rereads all six complete original
step-343 division sets under distinct `original343-` names:
`fixed-S-original-division-`, `fixed-S-fresh-division-`, `division-`,
`fixed-U-division-`, `u-division-` and `action-division-`.
Each contains 2304 full identities, totaling 13824. Each dividend is
reconstructed from the actual scaled basis and complete product table.
For action divisions the right factor is the full radical-basis vector:
the coordinate equation JA_i=L_iJ and its polynomial expansion are
checked in all positions, using the supplied audited J and actions.
This checks existing evidence without recomputing the radical or kernel.
Every 95-position integer dividend, 47-position rational quotient and
95-position rational zero remainder has its shape/type checked and
satisfies the full equality dividend=H·quotient+remainder. The same
checks cover all 4608 fresh S/U divisions. Saved labels and PASS reports
do not replace any of these identities.

**Full audited V interface.** Write a_i=1 for i<44 and a_i=2 otherwise,
M=diag(1/a_i), T=diag(a_i), Q=2M. Every entry of the original and
audited decisions and numerator-lattice certificates agrees. The full
independent multiplier agrees with M, Q, T, determinant 16, index
orientation [V:U] and both actual identities. MT=TM=1 is checked.

For G with columns e_44,…,e_47,2e_0,…,2e_47, both original and
independent numerator certificates have basis Q and give integer
matrices C,D with GC=Q and QD=G. Both rational inverse products for
Q are checked, together with both integral comparison maps between
the saved and displayed bases and both inverse comparison products.
Thus the complete global preimage interfaces agree in both directions;
no mod-two dimension or determinant alone substitutes for this check.
The underlying full multiplier theorem and kernel completeness are
imported from audited L089. No new rank audit is asserted here.
`input-validation.json` is written only after all these input obligations.

**Construction and independent transport replay.** If c_ijk is U's
verified table, the producer sets

\[
e_{ijk}=\frac{c_{ijk}a_k}{a_i a_j},
\]

checking exact integer divisibility in every slot, zeros included.
For each forward U coordinate matrix P and reverse matrix R it saves
PM and TR. It transports the actual identity by T. The independently
adapted `verify_v.py` imports no producer arithmetic and checks every
entry against these formulas, both inverse products, and the full
old-lattice equations (PM)T=P and M(TR)=R. All entries of the inclusion
T, including off-diagonal zeros, are checked. Its determinant is 16,
with the orientation [V:U]. There are 18432 transport/inclusion entries
and eight full inverse products.

The transported identity e_v=T e_u agrees with both audited identities;
the V power matrix sends it to the constant polynomial one. This does
not presume that an order-coordinate e_0 is the unit. Every coefficient
of W_i=496v_i is reconstructed from the actual power matrix as an exact
Fraction and checked integral. All 2304 positions agree with the saved
arrays and with 2(248u_i)/a_i. Original scale 31, all four prior scales,
input scale 248 and enlargement denominator two are checked explicitly.

**Every product and every persisted actual dividend.** For every i,j
the independent verifier forms by full convolution

\[
F_{ij}(t)=W_i(t)W_j(t)-496\sum_k e_{ijk}W_k(t)
\]

and divides by the full primitive H in Q[t]. Division retains all
positions through degree 94. Its integer fast path checks divisibility
by 343 at every step and retains exact rational fallback. All 218880
remainder positions vanish; no rational fallback is needed in this
instance, an observed result rather than a premise. Since H=343h,
division by 496² proves each claimed field product identity. The full
invertible power map identifies the lattice faithfully with K.

For each i the complete 48 divisions are persisted in
`v-division-ii.json`. The encompassing stage rereads every entry,
checks exact shapes/types, reconstructs all 95 actual dividend positions
from the V basis and complete table, and then checks the full equality
to H times the 47-position quotient plus the 95-position zero remainder.
All 2304 checks pass. Both left and right identity actions on every
basis vector agree with that vector. Integrality, full field identities
and the actual identity establish the complete table on precisely V,
without a numerical embedding, selected factor or new maximality claim.

**Single combined bound and preservation.** The sole invocation is

```bash
python3 -B scripts/seven-torsion/index-sixteen-table-347/run_once.py
```

Only `run_once.py` and `stage.py` are prepared before the watchdog,
with syntax checks and no mathematical execution. Their bytes count.
The watchdog starts before inventories, copies, source adaptation and
mathematics. Guarded source adaptations from step 339 create the fresh
producer and V verifier inside it; the two independent input verifiers
are copied there. No historical wrapper or producer executes. Exclusive
writes and the start marker forbid rerunning this execution.

`canonical-input-hashes.json` includes 3330 originals, retaining all
step-345 inventoried inputs and every step-343/345 artifact. Its only
new historical hash transition is the exact documented post-audit L089
addendum, recorded with old/current hashes in `inventory-transition.json`;
all other prior hashes agree. The 449 fixed copies and six source files
are checked unchanged along with all originals at final preservation.
Complete report, table/basis, inventory and manifest rereads, original
and fresh actual-dividend checks, preservation and final writing are
inside the same watchdog. The pre-execution attempt note is subsequently
extended only by a separately recorded documentation transition.

Input, producer, independent V replay, stage, watchdog and final-bound
reports pass with empty failures. Actual execution through final writing
takes 12.411808207863942 seconds and 84415874 bytes. Conservative
inclusive bounds 14 seconds and 84419848 bytes are checked after the
final write, strictly below 180 and 134217728. No retry, correction,
fixture, successor test or other prime executes. Historical failures
and unfinished work remain preserved. The separate critical audit below
validates this fixed input; no general theorem beyond the cited method
or BSD candidate is claimed.

**Separate critical audit, 2026-10-19 (step 349).** The unchanged prior
SPECIALIZE assessment is
`drafts/literature/2026-10-19-index-sixteen-table-critical-audit.md`.
The full L090 construction, audited L089 identification, original basis
definitions, complete verifiers and independent step-341 elimination
mechanism were inspected. Stevenhagen's hypotheses and applicability
above are unchanged; the known multiplier identification is imported
without a new radical or maximality test. The earlier U audit does not
certify the four-column, scale-496 V instance. This audit is fixed
known-method reproduction, not a new general theorem.

The sole execution is

```bash
python3 -B scripts/seven-torsion/index-sixteen-table-audit-349/run_once.py
```

All evidence below is in that directory. `run_once.py`, `stage.py` and
`independent-body.txt` were prepared and syntax-checked without arithmetic.
The external watchdog precedes copies, hashes, source extraction,
arithmetic, rereads, preservation and final writing. Exclusive writes
and the start marker exclude a retry. Only inspected helper definitions
and the full V-lattice comparison block are extracted from step 347;
its stage, preparation function and producer are never executed. The
three replay verifiers are byte-identical copies. The independent
script reuses step 341's forward elimination and canonical b/m/n/s/u
construction, then adds the prescribed V columns and complete solves.

**Original and fresh complete products and divisions.** Fresh replay
reconstructs all three S/U/V bases and checks each table's 2304 ordered
products and 110592 integer entries, including zeros, in original H.
It checks each table's 18432 transport/inclusion entries, eight inverse
products and 96 actual left/right identity actions. Both original point
components, the leading coefficient 343 and every scale remain explicit.
Fraction reconstruction handles zero entries; rational fallback remains
available in division. The observed zero fallback count is not a premise.

Every one of the six step-343 sets retained under `original343-` is
checked again: 13824 full identities. Step 347's persisted S/U divisions
give 4608 additional original identities, and its persisted V divisions
give 2304. These are copied under `original347-` before fresh verifiers
write the separate 6912 fresh S/U/V divisions. For all 27648 identities,
the audit checks the exact shapes and types, reconstructs the actual
95-position integer dividend from the full scaled basis/table, parses
every one of the 47 rational quotient and 95 rational remainder entries,
checks every remainder is zero, and verifies the full H-division identity.
Action dividends retain the full radical basis J and all entries of
JA_i=L_iJ; they are not replaced with ordinary products. No rank or
kernel computation is repeated. The whole original/audited V decisions,
numerator lattices, independent multiplier and both two-sided global
preimage certificates pass the full comparisons described above.
The inherited `all_inputs_before_production` field in
`input-validation.json` is only a historical interface label: no
production occurs in this audit. Likewise the V verifier's stale
`exact_index_eight_orientation` diagnostic is preserved; the actual
checked determinant and index are sixteen.

**Independent complete lattice reconstruction.** Let B,U,V denote the
power-coordinate matrices rebuilt from the canonical b formula and
the explicit successive m/n/s/u/v definitions, without using any saved
inverse in a solve. Let P be the full L067 power-to-two-coordinate map.
The six exact systems, with matrix unknowns, are

\[
 VX=(1_{48}\mid U\mid e_0),\qquad
 UY=(1_{48}\mid e_0),\qquad
 TZ=1_{48},\qquad BC=V,\qquad CW=1_{48},\qquad
 (PV)R=1_{48},
\]

where T is the U-in-V inclusion block of X and e_0 represents the
constant polynomial one. Each solve uses unnormalized forward
elimination and back substitution, with every swap, elimination factor,
pivot, transformed right side, solution entry and determinant persisted
in `exact-lattice-certificate.json`. The certificate is completely reread;
every row operation is replayed, the full upper triangle and nonzero
pivots are checked, and both the original and transformed residual
equations are checked in every position. Thus no solution is certified
by a preview, selected minor or stored PASS label.

The six V transports are V,V^{-1},C,C^{-1},PV,(PV)^{-1}; all 13824
saved entries agree with these independently solved matrices, and both
inverse products are checked for each pair. U and its independently
solved inverse agree in full with the saved U maps. The full L067 map
and H=343h are identified with the original certificate. The complete
inclusion and inverse inclusion agree with the audited V identification,
and their products in both orders are the identity. V is compared
with U times the entire audited multiplier basis in both directions:
the comparison matrices have integral entries, give the full basis
equalities, and are mutual inverses. This establishes equality of the
entire global lattices, not just equality of rational spans or dimensions.
Twice the inverse inclusion agrees with all original and independent
numerator certificates; their full global-preimage equations were checked
separately in the lattice-interface replay.

All pivot and swap-sign data give
\[
 |\det T|=16=[V:U],\qquad \det(U)/\det(V)=\det T.
\]
The unit vectors are solved from e_0, agree with both saved identities
and the audited multiplier identity, and give all 192 left/right actions
on the U and V tables. No basis vector is presumed to be the unit.
All 11520 coefficients of the scale-31/62/124/248/496 m/n/s/u/v
representatives are reconstructed and checked integral. The m arrays
agree with the original b matrix times the saved integral numerator;
the n/s/u/v arrays agree with their complete stored polynomials. All
scale and enlargement metadata agree. Full reconstructed matrices,
systems, operations, scaled arrays, identities, inclusion and integral
comparison matrices are retained and reread under the same watchdog.

**Preservation and bounds.** All 3330 step-347 inventoried inputs,
every step-347 artifact, canonical L090 before this addendum, the
unchanged approved assessment, relevant histories and ATTEMPTS/041/042/044
are inventoried: 4001 original files. All 248/447/449 entries of the
step-343/345/347 copy manifests are bound to both source and fixed bytes;
all six executed step-347 sources retain their recorded hashes.
The complete S and U provenance chains remain unchanged. The only new
historical exception is the exact step-347 attempt-note append with
old hash `d0917f59ac51e1bd824dc732f96b50bbbe4b5e84eb099a28e22b0da1f7e4cd79`
and current hash
`ba7345d0f3cf539defa7231456dbedbcebd5f9d73bbfb1f61159dbf60fb970a5`.
The pre-append bytes are reconstructed by splitting at the unique
completed-execution heading and their hash is checked, so this is
not a pathname exemption. The exact prior L087/L088/L089 documentation
transitions are checked against their original inventories and current
bytes; every other historical input agrees.

At completion all 4001 originals, 643 fixed copies and seven prepared
or executed source artifacts (six Python files and one text body)
are unchanged. All full table/basis files, reports, manifests, inventories
and preservation records are reread. There are no failures in the
audit, S/U/V replays, independent solves or watchdog. Actual execution
through final writing is 18.56054754112847 seconds and 110302065 bytes.
Conservative inclusive bounds, checked after the final write, are
20 seconds <180 and 110306038 bytes <134217728. No correction, retry,
producer, further multiplier or other-prime test runs. The subsequent
lemma and attempt-note outcome additions are documentation transitions
recorded exactly in the step-349 history and continuation assessment;
no executed artifact changes.

This validates the fixed table only. Global maximality, complete
units/classes, full descent enclosure, rational membership and arbitrary
complex-order/rank comparison remain unresolved.

## Mathlib

Full matching and supporting Mathlib coverage for this explicit entire
multiplier-order table and its certificates has not been checked.
Unknown availability is not evidence of absence. The cited general
theory, audited inputs and complete exact replay supply the evidence.
