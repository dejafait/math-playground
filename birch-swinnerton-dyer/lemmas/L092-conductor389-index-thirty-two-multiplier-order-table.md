# L092 — Complete table of the index-32 multiplier order

## Hypotheses

Use L067's audited entire degree-48 number field K=Q[t]/h for
E: y²+y=x³+x²−2x, with primitive H=343h. Retain L077's nonmonic
b-basis, L078's m-order, L080/L084's n-order, L085/L086's s-order,
L087/L088's u-order U, L089/L090's v-order V and audited L091's
identification of the entire multiplier of I=√(2V):

\[
W=(I:I)=\sum_{i<43}\mathbf Z v_i+
              \sum_{43\le i<48}\mathbf Z(v_i/2),\qquad [W:V]=32.
\]

Keep both original point-coordinate components, every rational transport,
the actual unit and the scales 31/62/124/248/496. Fixed steps
329/331/333/335/337/339/341/343/345/347 and complete steps 349/351/353
are supplied inputs. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-index-thirty-two-multiplier-table.md`.

## Conclusion

Put w_i=v_i for i<43 and w_i=v_i/2 otherwise. The files
`w-basis.json` and `w-product-00.json` through `w-product-47.json` in
`scripts/seven-torsion/index-thirty-two-table-355/` give the entire table

\[
w_iw_j=\sum_{k=0}^{47}e_{ijk}w_k\qquad(0\le i,j<48),\qquad e_{ijk}\in\mathbf Z.
\]

Complete independent original-H replay passes all 2304 products and
110592 integer slots, all six transports, eight inverse products, the
whole audited lattice and inclusion, and the actual unit's 96 two-sided
actions. The common power-coordinate scale is 992, checked integral in
all 2304 positions. Every new persisted division is reread against its
reconstructed actual dividend.

One combined execution has conservative inclusive bounds
35 seconds <180 and 64359248 new bytes <134217728, including prepared
sources, setup, full input replay, production, independent verification,
preservation and final writing. All 6245 inventoried originals,
272 fixed copies and 12 prepared/generated source artifacts remain
unchanged through execution. Its separate fixed critical audit passes:
six direct full W systems, complete fixed/fresh evidence and preservation
meet inclusive bounds 45 seconds and 69674435 bytes, strictly below
180 and 134217728. This is fixed known-method reproduction. It supplies no new
multiplier, local or global maximality, complete units/classes, descent
enclosure, rational membership or arbitrary-curve rank/order comparison.

## Proof

**Imported order and source applicability.** Import audited L091's
complete multiplier identification, rather than recomputing its radical
or action kernel. Its general input is Peter Stevenhagen,
*The arithmetic of number rings*, in *Algorithmic Number Theory*,
MSRI Publications **44** (2008), pp.209–266,
[Lemma 6.4 p.221 and Section 9 pp.233–235, equation (9-2), both radical
cases, Proposition 9.3 with proof and the following action/kernel/lifting
paragraph](https://library.slmath.org/books/Book44/files/08psh.pdf#page=27).
L067 supplies a number field and L090 a full order V; two is a nonunit
by finite freeness over Z. The ideal I contains 2V and is a nonzero
full finite module. The cited multiplier integrality theorem applies,
without an odd-prime or monogenic restriction. Together with L091's
audited whole-lattice calculation it makes W an integral order. The
named theorem is imported without reproof. It supplies neither the new
table entries nor the resource bound; the explicit specialization and
independent replay below supply them.

**Complete fixed evidence before new products.** The sole invocation is

```bash
python3 -B scripts/seven-torsion/index-thirty-two-table-355/run_once.py
```

It has already run. Exclusive writes and `run-start.json` forbid a second
execution. All evidence below is in that directory. Only `run_once.py`
and `stage.py` were prepared and syntax-checked beforehand, without
mathematical execution; their bytes count. The external watchdog starts
before inventories, copying, source adaptation or arithmetic. Historical
stages, wrappers and producers never execute. `input-replay-body.txt`
retains the adapted complete fixed-input comparison body, and
`replay-definitions.py` the original-H dividend-checking definitions.
No radical, new multiplier, rank-discovery algorithm or other-prime test
is executed.

Fresh byte-identical S/U/V verifiers reconstruct the entire canonical
b/m/n/s/u/v chain, both original point-coordinate maps and the complete
forward/reverse transports. For each table they check all 2304 products,
110592 integer slots, 18432 transport/inclusion entries, eight inverse
products and 96 actual identity actions in original H. They retain its
leading coefficient 343 and every scale. Explicit Fraction reconstruction
includes untouched integer zeros; the checked integer division fast path
retains exact rational fallback.

The complete S/U/V provenance chains and every entry of the
248/447/449/643/643/266-entry copy manifests from steps
343/345/347/349/351/353 are bound to both source and fixed bytes. All
recorded executed source hashes are checked. Large fixed division files
are read in place, not replaced by new calculations. Hashes bind their
provenance; the following full identities establish their arithmetic.

The original step-349 inventory contributes all 27648 division identities:
six step-343 sets (13824), step-347 S/U/V sets (6912) and step-349 fresh
sets (6912). All step-351 S/U/V and V-action divisions contribute 9216,
and all step-353 S/U/V and V-action divisions another 9216. Current fresh
S/U/V replay contributes 6912 further persisted and reread identities.
For every identity, shapes and types of all 95 integer dividend,
47 rational quotient and 95 rational remainder positions are checked.
The dividend is reconstructed from the actual full scaled basis/table;
all remainder positions are zero and the complete equality
dividend=H·quotient+remainder is checked. Action divisions retain the
entire corresponding radical basis J, all coordinates of JA_i=L_iJ,
and the actual polynomial product. Historical U action files remain
under `old-U-` names and use U's radical; actual V actions use V's
radical. These are 46080 fixed and 6912 fresh input identities, not
sampled checks or transfers of an earlier rank.

`solve_replay.py` independently reconstructs the six exact V systems
from the canonical bases without solving with stored inverses. It
persists the complete certificate and checks equality with the complete
certificates from steps 349, 351 and 353. Every row operation, pivot,
upper-triangular zero, determinant, transformed right side and both
original/transformed residual equations in each of those original
certificates is replayed. All six transports, full U/V inclusion and
index sixteen, both actual units and all 11520 scale-chain coefficients
agree. This is a check of fixed solve evidence, not a new multiplier
calculation. `solve-report.json` and `exact-lattice-certificate.json`
retain these results.

**Whole five-column multiplier interface.** Write
a_i=1 for i<43 and a_i=2 otherwise, M=diag(1/a_i), T=diag(a_i),
Q=2M. `successor-interface-body.txt` compares every entry of the original
step-351 and audited step-353 decision and numerator files, and the
independent multiplier certificate. They agree with M, Q, T, index and
determinant 32, kernel dimension five, the actual unit and orientation
[W:V]. Both MT=TM=1 products are checked.

Let G have columns e_43,…,e_47,2e_0,…,2e_47. The original numerator
certificate and step-353 independent preimage each have basis Q and
integer matrices giving both G C=Q and Q D=G, with their full shapes
48-by-53, 53-by-48 and 48-by-53 retained. Every entry, both rational
inverse products for Q and both integral comparisons of displayed and
saved lattices are checked. Thus equality of the entire global
preimages is used, not just their mod-two membership or dimension.
The full independently certified V-radical preimage is also compared
with the saved radical: all 95 generators, both integer generation
directions and both inverse products agree. This binds the basis used
for every V action dividend. Both old and multiplier identity vectors
agree, and M transports the latter to V's actual unit. All of these
checks finish before production, as recorded in
`successor-input-validation.json`.

**Table and coordinate construction.** If c_ijk is V's validated table,
the producer sets

\[
e_{ijk}=c_{ijk}a_k/(a_i a_j).
\]

Indeed w_i=v_i/a_i, so this is the unique expansion of w_iw_j in the
stated basis. Exact integer division is checked at every slot, including
zeros. A forward coordinate matrix A is transported to AM and its
inverse B to TB. This constructs all six maps to/from b, power and L067
coordinates. The actual unit vector is transported by T. The chosen
scale 992 is certified from the actual rational power matrix, not from
a preceding scale label.

`verify_w.py` imports no producer arithmetic and independently checks
every new map entry against the validated old map times M or T. It
checks both inverse products in each of the three coordinate systems,
the two multiplier/inclusion inverse products, all old-order containment
equations and the entire diagonal T. Its determinant is the product of
43 ones and five twos, hence 32 with orientation [W:V]. The actual
transported unit represents the constant polynomial one in the original
field. Both original point components are retained in the full L067 maps.

If P is the new rational power matrix, the verifier reconstructs
W_j=992 P_j in all 2304 positions as exact Fractions, proves every entry
integral, and compares the whole array with both the saved polynomials
and the transported old array. Thus W_j=992w_j and the retained scale
chain is 31/62/124/248/496/992, with original leading coefficient 343.

For every ordered pair (i,j), independently form the entire polynomial

\[
D_{ij}=W_iW_j-992\sum_k e_{ijk}W_k.
\]

Full convolution and division by original H check D_ij≡0 mod H. No
producer reduction or transported product is used as the independent
test. All 2304 identities and 110592 integer slots, including zeros,
pass; all 218880 remainder positions vanish. Every full 95-position
dividend, 47-position rational quotient and 95-position zero remainder
is persisted in `w-division-00.json` through `w-division-47.json`.
The stage rereads every entry, reconstructs D_ij anew from the actual
successor basis/table and verifies D_ij=H·quotient+remainder in every
position. Observed rational-fallback count zero is not a hypothesis.
Finally all 96 left/right actions of the actual identity agree with
the appropriate standard basis vector. `w-verification-report.json`
and `persisted-input-checks.json` have PASS and empty failures.

**Preservation and inclusive bounds.** `canonical-input-hashes.json`
includes the entire 5745-input step-353 inventory and every step-353
artifact, the full retained fixed chain and the prepared attempt note:
6245 originals. The exact two post-353 documentation transitions for
L091 and its audit note are checked against both old inventory hashes
and the current hashes recorded in history 353. All other step-353
inputs agree. The exact step-351 append, both post-349 transitions,
step-347 unique-marker prefix and all earlier exact transitions are
retained and checked against their actual historical inventories.
There is no pathname exemption or blanket documentation bypass.

`preservation-stage.json` records unchanged before/after hashes for
all 6245 originals, 272 fixed copies and 12 source artifacts, including
the prepared and extracted source bodies. All complete tables and
reports, inventories, manifests and preservation records are reread.
The stage, producer, fixed S/U/V verifiers, six-system replay, successor
verifier and watchdog have PASS with no failures. Actual external
execution through final writing is 33.05676433397457 seconds and
64355274 bytes. `final-bound.json` records conservative inclusive bounds
35 seconds and 64359248 bytes, checked after its final write; these are
strictly below 180 and 134217728. There is no retry, correction,
resumption, successor test or new maximality inference. The subsequent
outcome append to the pre-execution note is documented in history 355
as an exact post-execution transition; executed evidence stays fixed.

This supplies the complete table of a known multiplier as a fixed
arithmetic input only. The independent global-arithmetic and BSD gaps
listed in the conclusion remain open.

**Separate fixed critical audit (step 357).** The prior assessment
`drafts/literature/2026-10-20-index-thirty-two-table-critical-audit.md`
approves this distinct replay-only target. The sole completed invocation
is `python3 -B scripts/seven-torsion/W-table-audit-357/run_once.py`.
It must not run again. All evidence in this paragraph is in that fresh
directory. No producer, historical wrapper, radical or new multiplier
test executed. The imported multiplier conclusion and its source
hypotheses above are unchanged.

The watchdog begins before inventories, copying, source adaptation or
arithmetic; the three prepared source files count toward bytes. The
inventory contains all 6245 original step-355 inputs and every step-355
artifact, with the canonical statement, approved assessment, history 355
and prepared audit note: 6801 originals. All 272 step-355 copy-manifest
entries are bound to both their original sources and fixed bytes; all
twelve recorded source hashes agree. The exact history-355 note append
is checked against its old inventory hash, unique append boundary and
current hash. The complete earlier transition chain through step 353 is
retained, with no pathname exemptions.

Byte-identical fixed verifiers reconstruct and replay the entire S/U/V/W
tables in original H. For each table, all 2304 products and 110592 integer
slots, six transports, eight inverse products, actual identity and both
original point components are checked. Complete fixed dividend replay
covers 27648 step-349 identities, 9216 each from steps 351, 353 and 355:
55296 fixed identities. Fresh replay adds 9216 persisted and reread
identities. Each uses all 95 integer dividend entries, 47 exact rational
quotient entries and 95 zero-remainder entries; the dividend is rebuilt
from the actual full basis/table before checking equality with H times
the quotient. U and V action identities use their respective complete
radicals and every entry of JA_i=L_iJ. The original six-system V solve
certificates from steps 349/351/353 and the complete step-355 copy are
matched and replayed, including every operation, pivot, swap sign,
determinant and original/transformed residual. The original/audited W
decisions, both 53-generator numerator preimages and the full 95-generator
radical preimage agree in both integer generation directions, with full
inverse and actual-unit comparisons.

The distinct reconstruction in `W_reconstruct.py` begins with original H,
the canonical nonmonic b formula, L078's two explicit 31-denominator
columns and the successive final-column divisions defining n,s,u,v,w.
All five final W half-columns are retained. General exact unnormalized
forward elimination and back substitution solve six systems: W's power
inverse with the V inclusion and constant-one right sides; V's power
inverse and constant-one right side; the inverse inclusion; W's b
coordinates; their inverse; and W's full L067-coordinate inverse. Stored
W transports/inverses and producer arithmetic do not supply these solve
inputs. L067's audited full original coordinate matrix supplies only the
canonical coordinate conversion.

Writing P_W,P_V for the reconstructed power matrices, the solved
inclusion T and inverse M satisfy P_W T=P_V, P_V M=P_W and TM=MT=1.
The complete T is integral. Direct elimination gives |det T|=32 and
det(P_V)/det(P_W)=det(T), preserving orientation [W:V]. Against the
audited basis P_V M_saved, both comparison matrices are integral and
mutually inverse, with both full basis equations checked. The solved
M, numerator 2M and all six transports agree entrywise with the complete
original/audited data. All eight inclusion/coordinate inverse products
pass. This checks the whole lattice, not merely rank or a selected minor.

The unit is solved from the constant polynomial one, is integral, agrees
with the original and audited interfaces, and passes all 96 left/right
W actions (also all 96 V actions). Exact Fraction arithmetic retains
integer-zero entries throughout. All 13824 scale coefficients in the
31/62/124/248/496/992 chain are independently reconstructed, integral and
equal to the retained basis arrays; scale metadata is checked separately.
`W-exact-lattice-certificate.json` persists every system, reconstructed
matrix, operation, pivot, determinant, solution, inclusion, comparison
and identity. Its complete roundtrip and every original/transformed
residual are reread before acceptance. `W-solve-report.json` and
`persisted-input-checks.json` record the completed checks with no failures.

Final table/report/inventory rereads and complete before/after hashing
preserve all 6801 originals, 322 fresh fixed copies and 14 source files.
`preservation-audit.json`, `audit-report.json`, `watchdog.json` and
`final-bound.json` record success. Actual execution through final writing
is 43.70418291701935 seconds and 69670461 bytes; conservative inclusive
bounds 45 seconds and 69674435 bytes are checked after writing and are
strictly below 180 and 134217728. The subsequent canonical audit addition
and audit-note append are recorded as exact documentation transitions in
history 357; executed evidence remains fixed. This validates the fixed
input without supplying maximality or any further arithmetic conclusion.

## Mathlib

Full matching and supporting Mathlib coverage for this explicit entire
multiplier-order table and its certificates has not been checked.
Unknown availability is not evidence of absence. The cited general
theory, audited input hypotheses and complete exact replay supply the
evidence. The separate fixed critical audit above passes; no additional
Mathlib availability claim is made.
