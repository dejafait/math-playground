# L088 — Complete table of the index-eight multiplier order

## Hypotheses

Use audited L067's entire degree-48 field K=Q[t]/h for
E: y²+y=x³+x²−2x, primitive H=343h, L077's original nonmonic
b-basis, L078's order R with basis m, L080's multiplier R⁺ and
L084's full table in basis n. Retain audited L085/L086's entire
order S, with basis s, and audited L087's identification

\[
I=\sqrt{2S},\qquad U=(I:I)
=\sum_{i=0}^{44}\mathbf Zs_i+
\sum_{i=45}^{47}\mathbf Z(s_i/2),\qquad [U:S]=8.
\]

All coordinate maps retain the whole field and both original coordinates.
The fixed S basis/product files in steps 329/331/333/335/337 and full
step-335/337 lattice evidence are inputs. No producer PASS label is an
arithmetic premise. Prior SPECIALIZE coverage is
`drafts/literature/2026-10-19-index-eight-multiplier-table.md`.

## Conclusion

Put u_i=s_i for i<45 and u_i=s_i/2 for i=45,46,47.
The files `u-basis.json` and `u-product-00.json` through
`u-product-47.json` in `scripts/seven-torsion/index-eight-table-339/`
give the full integral multiplication table

\[
u_i u_j=\sum_{k=0}^{47}d_{ijk}u_k\quad(0\leq i,j<48)
\]

of the entire audited U. Independent original-H replay checks all 2304
ordered products and 110592 integer slots, zeros included, all six rational
transports, both inverses for each pair, the full multiplier/inclusion
pair, actual identity and its 96 left/right actions. All 2304 persisted
U division certificates are checked against reconstructed actual dividends.
The full integral inclusion has index eight in the orientation [U:S].

One combined execution passes with inclusive conservative bounds
7 seconds <180 and 31591485 bytes <134217728. This is fixed known-method
reproduction, not a new general theorem. Its separate critical audit below
passes. No maximality test of U, global maximality, field discriminant,
complete units/classes, descent enclosure, rational membership or
arbitrary complex-order/rank comparison is supplied.

## Proof

**Known order and full multiplier.** Import L087's audited full lattice
identification. The general result is Peter Stevenhagen, *The arithmetic
of number rings*, in *Algorithmic Number Theory*, MSRI Publications
**44** (2008), pp.209–266,
[Lemma 6.4 p.221 and Section 9 pp.233–235, equation (9-2),
Proposition 9.3 and its following action/kernel/lifting paragraph](https://library.slmath.org/books/Book44/files/08psh.pdf#page=27).
Here S is an order in L067's number field, two is a nonunit, and I
contains 2S, so I is a nonzero full finite module. The cited multiplier
integrality result and L087 identify the entire integral overorder U;
there is no odd-prime or monogenic restriction. That known result is
imported, without reproof, new radical calculation or stopping-criterion
application. It supplies neither the instance coefficients below nor
their resource bound. This is the reason for a finite specialization.

**Complete S input before production.** The fresh `input_verify.py` is
a byte-identical copy of step 335's repaired independent input verifier.
It reconstructs H=343h, content one and degree 48, the explicit original
b-basis, its two power-coordinate inverses, and L067's full coordinate
transports and inverse products. L078's two exceptional columns are
reconstructed from the explicit even/odd arrays divided by 31. The
scale-31/62/124 chain, L080/L084's entire R⁺ and L085/L086's entire S,
all six S transport matrices and eight inverse products, full inclusion
of index four and actual identity are checked, including all zeros.

The 49 S basis/product copies agree with steps 329/331/333/335/337.
All 2304 S products and 110592 integer slots pass direct original-H
replay before U production. For V_i=124s_i, this verifies every coefficient
of V_iV_j−124Σ_k c_ijk V_k modulo H. Every division retains 95 dividend,
47 quotient and 95 zero-remainder positions. `stage.py` independently
reconstructs actual dividends from V and the full table, checks every
position and verifies H times the saved quotient plus remainder. It does
this for all 2304 original step-335 certificates (also matched against
step 337's fixed evidence) and all 2304 fresh input-replay certificates.
Thus neither saved dividend labels nor fresh PASS labels replace
complete input arithmetic. `input-validation.json` records completion
of these obligations before production.

The two full fixed decisions from 335 and 337 agree as data. Let

\[
a_i=\begin{cases}1&i<45,\\2&i\geq45,\end{cases}\quad
M=\operatorname{diag}(1/a_i),\quad T=\operatorname{diag}(a_i),
\quad Q=2M.
\]

Every entry of the saved multiplier M, numerator Q and inverse T,
index/determinant eight and kernel dimension three agrees. The entire
saved numerator-lattice basis is Q. Step 337's separately audited
`independent-multiplier.json` agrees on the full basis, numerator,
inclusion, determinant and both identities. This imports its verified
full-preimage result; it does not infer multiplier equality from an index
or from closure of a smaller enlargement.

**Producer and full rational transports.** Matrices act on columns.
If B_s, P_s, C_s transport S coordinates to the original b, power and
L067 coordinate systems, respectively, the producer writes

\[
B_u=B_sM,\quad P_u=P_sM,\quad C_u=C_sM,
\qquad
B_u^{-1}=TB_s^{-1},\quad P_u^{-1}=TP_s^{-1},\quad
C_u^{-1}=TC_s^{-1}.
\]

Its table construction uses d_ijk=c_ijk a_k/(a_i a_j), checking every
division integral before saving the integer. This is an efficient
construction, not its independent product verification.

`verify_u.py` imports no producer arithmetic. Starting from the entire
independently verified S transports, it separately constructs all entries
of M and T, checks both MT=TM=1 and all six U transports against the
displayed formulas, and checks both inverse products for every pair.
It additionally checks the full old-lattice inclusions P_u T=P_s,
B_u T=B_s, C_u T=C_s, with the corresponding inverse equations.
There are 18432 transport/inclusion entries and eight inverse products.
Every entry of T is checked, including off-diagonal zeros; its diagonal
is 45 ones followed by three twos. Hence S is included in the actual U
with [U:S]=|det T|=8 in the correct orientation. All saved U lattice
entries agree with the audited L087 multiplier.

If e_s is S's actual identity, e_u=T e_s is checked integral and equals
both fixed L087 identities. P_u e_u is the constant polynomial one.
No order-coordinate e₀ is presumed to be the unit. Every representative
W_i=248u_i is reconstructed from 248P_u using explicit Fraction
arithmetic, including untouched integer zeros, and checked integral
before conversion. All 2304 polynomial coefficients agree with the
saved arrays and with 2V_i/a_i. The metadata separately checks original
scale 31, prior scales 31/62/124, current scale 248, input scale 124
and enlargement denominator two. No old scale is silently discarded.

**Every U product directly in original H.** The independent verifier
reads all 48 integers of every table entry, including zeros, forms by
its own full polynomial convolution

\[
F_{ij}(t)=W_i(t)W_j(t)-248\sum_{k=0}^{47}d_{ijk}W_k(t),
\]

and divides it by H in Q[t], retaining every position through degree 94.
For an integer leading value x, `divmod(x,343)` takes an integer fast
path only if the remainder is zero. Otherwise it constructs Fraction(x,343);
rational leading values also use exact fractions. No float is admitted
in a transport, table slot or division. All 218880 remainder positions
vanish. No rational fallback was needed in this instance, but its
absence is checked, not assumed. Since H=343h, dividing this congruence
by 248² proves each product identity in K. Rational invertibility of
P_u identifies the whole lattice faithfully with the full field.

For each i, `u-division-ii.json` persists all 48 complete divisions:
95 integer dividend positions, 47 exact rational quotient strings and
95 exact rational zero-remainder strings per product. Within the same
watchdog, `stage.py` rereads every table row, every basis representative
and every persisted division, independently reconstructs F_ij from the
actual W and table, and checks full equality to the saved dividend.
It then multiplies the entire saved quotient by H, adds the remainder,
and compares all 95 positions to that reconstructed dividend. All 2304
checks pass; saved labels or hashes alone cannot supply this equality.
Finally both left and right table actions of e_u on every basis vector
equal that vector. The full table is integral and closed with actual
identity, on exactly L087's already identified U. No new associativity
axiom or selected field embedding is substituted for these field identities.

**Single combined bound and preservation.** The sole invocation is

```bash
python3 -B scripts/seven-torsion/index-eight-table-339/run_once.py
```

Four sources (`run_once.py`, `stage.py`, `produce.py`, `verify_u.py`)
were prepared before the watchdog; preparation compiled source only and
executed no mathematical checks. Their bytes count in the recursive total.
The external watchdog starts before inventories, hashes, copies and
mathematics. A start marker and exclusive writes forbid another run.
The 102 fixed copies include the 49 S basis/products, 48 original product
divisions, the input verifier, both decisions, independent multiplier
certificate and numerator lattice. The input verifier is the fifth
source, copied only inside the watchdog.

`canonical-input-hashes.json` records 1582 originals, retaining the whole
step-335/337 evidence and earlier canonical provenance. The only allowed
change from step 337's historical inventory is L087's documented audit
addendum, appended after that execution's preservation. Its old/current
hashes and reason are explicit in `inventory-transition.json`; all other
prior inventory hashes match. A fresh current hash of L087 is included
in the new preservation check. No historical evidence is overwritten.

`copy-manifest.json`, `code-hashes.json` and `preservation-stage.json`
retain full before/after inventories. Every one of the 1582 originals,
102 copies and five sources agrees at final preservation. All complete
fresh reports are reread in the stage. The producer, input, independent
U verifier, stage and watchdog report PASS with empty failure lists.
No retry, fixture, correction, successor test or other prime executes.
ATTEMPTS/041/042/044 and all unfinished work remain preserved.

The encompassing stage takes at most 5.325493 seconds; the external
watchdog through final writing takes at most 5.430380 seconds and
31587510 bytes. `final-bound.json` conservatively bounds inclusive final
writing by 7 seconds and 31591485 bytes, and these bounds are checked
after its write. All setup, full input validation, production, independent
replay, persisted-evidence rereads, preservation, logs and final reports
are included, strictly below 180 seconds and 134217728 bytes.
The result advances a local arithmetic input by a known construction;
it does not close the independent global or BSD gaps. The separate
critical audit of this production instance is recorded below.

**Separate critical audit, 2026-10-19 (step 341).** The prior SPECIALIZE
assessment is `drafts/literature/2026-10-19-index-eight-table-critical-audit.md`.
The full proof, complete original verifier/stage/watchdog sources, L087's
separate audit, canonical original b/m basis statements and the earlier
independent elimination implementation were inspected. Stevenhagen's precise
multiplier result above is imported under the unchanged full-field/order
hypotheses. Its audited L087 specialization identifies the entire U. No
multiplier recomputation, new maximality criterion or reproof of the cited
theorem is needed for this fixed table audit.

All fresh evidence is in `scripts/seven-torsion/index-eight-table-audit-341/`.
The single execution was

```bash
python3 -B scripts/seven-torsion/index-eight-table-audit-341/run_once.py
```

Three sources (`run_once.py`, `stage.py`, `independent.py`) were prepared
before the watchdog, using source-text preparation and syntax checks only.
Their bytes count in the final recursive total. The external watchdog starts
before copying, inventories or mathematics. Exclusive writes and the start
marker prohibit rerunning this execution. Historical wrappers and producers
never execute. The fresh `input_verify.py` and `verify_u.py` are byte-identical
copies of the step-339 sources, retaining their original relative path depth.

The inventory includes every step-339 original and inventoried input, this
lemma before this addendum, the unchanged assessment, the reused independent
source, and ATTEMPTS/041/042/044: 1855 original files. Every prior step-339
canonical hash agrees. The old step-337 inventory transition remains explicit:
only L087's documented post-audit addendum explains its historical old/current
hash difference; no additional mathematical input change is allowed. Current
L087 is preserved in the new inventory. The 254 fixed copies include all 49 S
basis/product files, all 49 U basis/product files, the three complete sets of
original divisions, full multiplier inputs, the two verifiers and six reference
reports. Reference PASS labels supply no arithmetic check. Every S basis/table
copy agrees with steps 329/331/333/335/337/339; the original fixed S divisions
also agree with steps 335/337.

**Complete fresh replay and original persisted evidence.** Fresh S replay
checks all 2304 ordered products and 110592 integer slots, including zeros,
in original H. It reconstructs the full b/m/n/s chain, six transports and
eight inverse products, actual identity and both actions on all 48 basis
vectors, retaining scale 31/62/124. Fresh U replay similarly checks all 2304
ordered products and 110592 slots, all six transports, eight inverse products,
full old inclusion, actual identity and 96 actions, with scale 248. Each
verifier checks H's leading coefficient 343 and the full degree-48 field
transports. Exact Fraction reconstruction includes integer zeros. The division
fast path checks divisibility at each step and retains rational fallback;
zero fallback counts are observed, never assumed.

`stage.py` separately reconstructs actual product dividends from the full
basis representatives and tables. For each certificate it checks the exact
integer row/column indices, all 95 integer dividend positions, all 47 rational
quotient strings and all 95 rational zero-remainder strings. It independently
expands H times the entire quotient plus remainder and compares all positions
to the actual dividend. This checks three fixed sets of 2304 divisions:
step 339's original fixed S divisions, its fresh S divisions, and its U
divisions. Those 6912 originals have distinct fixed names and are never
replaced by generated evidence. The same full check applies to the two new
replay sets, another 4608 divisions. All 11520 checks pass within the same cap.

**Independent full lattice solves.** `independent.py` imports no producer or
verifier helper, and no saved inverse supplies a solve input. It constructs
b from every coefficient of original H using L077's formula, m using both
complete explicit L078 arrays divided by 31, and n/s/u using the stated final
one/two/three-column changes of L080/L085/L087. Thus its power-coordinate
matrices are independently reconstructed throughout the full basis.

Write these reconstructed power matrices as B, S, U, and let P be audited
L067's full power-to-original-coordinate matrix. Unnormalized rational forward
elimination and back substitution solve these six complete systems:

\[
 UX=[1_{48}\mid S\mid e_0],\qquad
 SY=[1_{48}\mid e_0],\qquad
 TZ=1_{48},\qquad BW=U,\qquad WV=1_{48},\qquad
 (PU)Q=1_{48},
\]

where T is the S-in-U inclusion block obtained from X, and e_0 is the
constant-one polynomial in power coordinates, not an assumed unit vector in
order coordinates. The solve results agree with every entry of all six saved
U transports (13824 entries), the full old S power inverse, both actual
identities, and both directions of the full multiplier inclusion (4608
entries). Both inverse products for each transport and both inclusion products
are checked. The inclusion and inverse inclusion agree with both fixed
decisions, the full audited multiplier and full numerator lattice; no selected
columns or saved index label replaces these comparisons.

All entries of T are integral. Its independently computed determinant has
absolute value eight, with orientation [U:S]. The separately computed ratio
of the old and new power-basis determinants equals det(T), including signs.
The identity solutions are integral, represent constant one, agree with both
saved identities and independently act on both sides of every basis vector
in the two full tables (192 actions). All 9216 scaled coefficients for
m/n/s/u are integral, with scales 31/62/124/248; every applicable saved array
and scale/enlargement metadata agrees. P retains both original coordinate
components, rather than a selected embedding.

`exact-lattice-certificate.json` persists the complete reconstructed matrices,
six systems, right-hand sides, row operations, nonzero pivots, swap signs,
triangular forms, transformed right-hand sides, solutions, determinants,
scaled arrays, identities and inclusions. The full file is reread. Every row
operation is replayed, every triangular zero and pivot/sign is checked, and
both original and transformed full residual equations are recomputed. Every
applicable reverse inverse is also checked; the augmented systems have their
reverse inverse checks explicitly before persistence. Complete serialized
round-trip equality binds the reread systems to those original checks.
No minor-only certificate or numerical solve is used.

**Inclusive bounds and preservation.** All full report/basis/table rereads,
complete persisted division checks, independent certificate rereads, final
hashing and evidence writing occur inside the single external watchdog.
`audit-preservation.json`, `copy-manifest.json`, `canonical-input-hashes.json`
and `code-hashes.json` are also fully reread. All 1855 originals, 254 fixed
copies and five prepared/copied sources remain unchanged. Preservation of
this lemma precedes this documentation addendum. Earlier failures and
unfinished work are preserved; no retry, correction, malformed fixture,
successor, other prime or new maximality test runs.

`audit-report.json`, both replay reports, `independent-report.json`,
`watchdog.json` and `final-bound.json` pass with no failures. The external
execution, including final writing, took 9.817413 seconds and 49805004 bytes.
The persisted conservative inclusive bounds are 11 seconds <180 and
49808978 bytes <134217728, checked after the final write. This validates a
fixed known-method arithmetic input, without a new general mathematical
result. Global maximality, complete units/classes, full descent enclosure,
rational membership and arbitrary-curve analytic-order/rank equality remain
unresolved.

## Mathlib

Full matching and supporting Mathlib coverage for this explicit complete
multiplier-order table and its certificates has not been checked.
Unknown availability is not evidence of absence. The cited multiplier
theory, audited inputs and full exact finite replay supply the evidence.
