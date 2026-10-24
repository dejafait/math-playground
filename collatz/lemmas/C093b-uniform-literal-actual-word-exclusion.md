# C093b — Uniform literal full-allocation actual-word exclusion

## Hypotheses

Fix an integer d with 6<=d<=33. Use L055's 25 indexed pairs,
changing only H_0=40-d and H_24=32670621+d. All J_i and all other
H_i are unchanged.
Let b_0,...,b_24 be nonnegative integers with sum_i b_i=B=9250245,
and attach a_i=2+18b_i to outgoing indexed row i.

Use the shortcut map T(n)=n/2 for even positive integers and
T(n)=(3n+1)/2 for odd positive integers. O and E specify actual
input parities. Suppose that, in literal indexed chronological order,

\[
W_0W_1\cdots W_{24},\qquad
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},
\]

is an actual closed concatenation at a positive integer. Require every
junction to be positive, odd and 20 modulo 27, and every final even
tail to be exact. Repeated periods and coincident junctions are allowed.
There is no minimum, seed, least-root, first-return or primitive-period
premise. All logarithms below are natural.

## Conclusion

No such actual closed concatenation exists for any specified d over this
full nonnegative integer tail-allocation simplex in literal order.

This is a local RESEARCH/REPRODUCTION application under the prior
SPECIALIZE assessment
`drafts/literature/2026-10-21-uniform-literal-actual-word-application.md`.
It transfers audited C093a's real-subsystem exclusion to actual words;
it claims no mathematical advance beyond the inspected source machinery.
The separate critical audit below found no defect in this application.
No nonliteral-order exclusion,
universal entry, unrestricted-cycle exclusion, divergence control or
universal eventual descent follows. Attempt 032 and both original d=0
rational witnesses remain valid.

## Proof

Assume the stated concatenation exists. Define chronological times and
the actual junctions by

\[
D_i=4J_i+H_i+a_i,\qquad t_0=0,\quad t_{i+1}=t_i+D_i,
\qquad n_i=T^{t_i}(n_0),\quad s_i=n_i+23/11
\quad(0\le i\le25).
\]

Here n_0 denotes the alleged starting input. All D_i are positive,
so the 25 word intervals are successive time occurrences. Closure
gives n_25=n_0 and s_25=s_0 even if there are repeated junction values
or a repeated shorter period.

Every positive odd residue-20 integer is at least 47. Indeed, writing
it as 20+27q with integer q, positivity implies q>=0, while oddness
implies q is odd, hence q>=1. Therefore, at every junction including
closure,

\[
n_i\ge47>1,\qquad s_i\ge47+23/11=540/11.             \tag{1}
\]

L055's complete table has J_i>=8; its H_i for 1<=i<=23 are at
least 72. The changed entries obey 7<=H_0<=34 and
32670627<=H_24<=32670654 throughout the specified d range.
Thus J_i>=2 and H_i>=3 for all 25 rows. Each a_i is an integer
at least 2 and congruent to 2 modulo 18. With r=25>=3, actuality,
closure, exact tails, (1) and the stipulated residue and oddness
conditions match L041's hypotheses. Use only its passage headed
“Each occurrence's own prefix and the transfer to the next,” whose
necessities hold at every index independently of junction-size ordering.
Its minimum selection, seed, cycle-mass estimates and imported
primitive-cycle bounds are not used.

Fix any 0<=i<25, abbreviate J=J_i,H=H_i,a=a_i, and put
y_i=T^{t_i+4J}(n_0), z_i=T^{t_i+4J+H}(n_0). L041's established
finite actual-word necessities give

\[
y_i+1=(27/16)^J s_i-12/11,\qquad
2^H(2^a n_{i+1}+1)=3^H(y_i+1),
\]
\[
11n_i+23\ge2^{4J+2},\qquad
2^H\le y_i+1<(27/16)^J s_i.                         \tag{2}
\]

Since the actual even tail gives z_i=2^a n_{i+1}, the second identity
in (2) and the first identity yield

\[
n_{i+1}=2^{-a}\bigl((27/16)^J(3/2)^H s_i
                         -(12/11)(3/2)^H-1\bigr).
\]

Consequently, with precisely C093a's definitions
kappa=23/11, G_i=(27/16)^{J_i}(3/2)^{H_i} and
Q_i=(12/11)(3/2)^{H_i}+1, we obtain

\[
s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+\kappa.                \tag{3}
\]

Both subtracted terms remain inside the tail factor; kappa is added
after division. The positive lower domain permits logarithms.
Using 11n_i+23=11s_i, the first inequality in (2) gives

\[
4J_i\log2\le\log s_i+\log(11/4).                    \tag{4}
\]

The last two inequalities in (2) give, at the same input,

\[
H_i\log2\le\log(y_i+1)
 <\log s_i+J_i\log(27/16).                          \tag{5}
\]

Thus the required H guard is strict, even if its lower power bound
is an equality. These are necessities for actual words; no parity
or integer-realization converse is asserted.

The arbitrary choice of i includes i=24. Its actual tail ends at
n_25=n_0, so (3) at i=24 is the closing endpoint, while (4) and
(5) remain guards at its own input s_24 with its own outgoing pair.
The imported necessity requires only a>=2 and an odd endpoint and
therefore includes a_24=2, as well as tail 2 at every other row.

Now (1), (3), (4) and (5), together with the unchanged literal indexed
order, integer allocation, budget and closure, are exactly every
hypothesis of audited C093a. Its exclusion contradicts this real tuple.
This proves the claim. There is no rotation or new cut in the argument;
no outgoing row, tail or guard is detached from its chronological input.
All 25 occurrences are retained, without any distinctness assumption.

### Sources, overlap and qualifications

C093a supplies the exclusion, L041 supplies the finite occurrencewise
necessities, and L055 supplies only the explicit indexed table. L055's
original rational witness and its d=0 guards are not transferred to this
different table. C088b's audited d=5 transfer is a precedent, not
a premise for this changed range. The ready assessment found no identical completed
d=6,...,33 actual-word application; this is not a novelty claim.

The upstream finite-word affine source is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The prior assessment reuses its inspected hypotheses and essential
printed proof cases. The words here are finite and nonempty. Any
fixed-point denominator qualification used upstream is already handled
in C093a's audited inputs; this application takes no new fixed point.
L041 already proves the arbitrary-tail actual-word necessities, so no
reproof of affine or parity-coding machinery, fresh source retrieval
or numerical certificate calculation is needed.

Attempt 032 stops the full C077a sufficient-test conjunction at d>=5;
this proof instead invokes independently established C093a and does
not infer those failed tests from actuality. No minimum/seed, survivor
feasibility, integer test on shifted coordinates, primitive-count
threshold or realization converse enters. Both d=0 witnesses and
the recorded failures retain their scopes. Cyclic-order reduction
and all universal gaps remain independent.

### Independent critical audit — 2026-10-22, step 402

This RESEARCH/REPRODUCTION proof audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-22-uniform-literal-actual-word-critical-audit.md`.
It found no defect in the stated application. The result validates an
existing restricted exclusion; it supplies neither a further exclusion
nor progress beyond the inspected source machinery. C093a's completed
step-398 audit and its numerical inputs are imported, not reconstructed.

**Parameters and all chronological occurrences.** Reading L055's full
pair table against both C093a and C093b confirms identical indexed
pairs after the two specified replacements. Every J_i>=8, the unchanged
H_i for 1<=i<=23 are at least 72, H_0 lies in [7,34], and H_24 lies
in [32670627,32670654]. Thus L041's integer J>=2,H>=3 hypotheses
hold throughout the closed d interval. The same integer b_i and budget
B=9250245 give the same a_i=2+18b_i>=2 at each outgoing row, with
a_i congruent to 2 modulo 18. L055 supplies its pair table only;
its original allocation, witness, seed and minimum are not premises.

Each D_i=4J_i+H_i+a_i counts exactly the shortcut letters of W_i
and is positive. Therefore t_i locates the input of indexed row i,
and the two intermediate times in the proof are T^(4J_i)(n_i) and
T^(4J_i+H_i)(n_i). Closure is exactly n_25=n_0. Repetition of a
shorter period and coincident values do not identify distinct time
occurrences or delete any of the 25 outgoing words.

For every such input, n_i=20+27q_i with integer q_i. Positivity
excludes q_i<0, since that would give n_i<=-7; oddness requires
q_i odd. Hence q_i>=1, n_i>=47 and s_i>=540/11 at all 25
inputs and at i=25 by closure. In particular n_0 is odd and greater
than 1. Together with actual closure and exact tails, these facts
match every L041 hypothesis with r=25.

**Necessity at the same outgoing input.** L041's occurrencewise
passage and its completed 2026-10-08 audit explicitly establish the
identities and inequalities in (2) independently of junction-size
ordering. L031 (4) and its arbitrary-tail boundary-valuation passage
confirm the scope: the odd factor 2^a n_(i+1)+1 gives v_2(y_i+1)=H_i,
and H_i>=3 gives v_2(11y_i+23)=2, hence the stated own-input
bound on 11n_i+23. No two-word closure converse or E^2-only
transport result is used. L041's earlier minimum selection and its
cycle estimates add no premise to these finite-word necessities.

Fix an arbitrary i in {0,...,24}. Substitution of the first identity
in (2) into the second gives
2^a n_(i+1)=(3/2)^H[(27/16)^J s_i-12/11]-1.
Dividing by 2^a and adding kappa gives precisely C093a (1): both
negative terms lie inside 2^(-a), and the shift 23/11 is outside.
There is no replacement of an exact endpoint by an upper estimate.

All logarithm arguments are positive. Since 11n_i+23=11s_i,
the logarithm of its lower power bound gives
4J_i log2<=log s_i+log11-2log2=log s_i+log(11/4).
This is exactly the non-strict J guard. The other lower power bound
and the strictly negative prefix offset give
H_i log2<=log(y_i+1)<log s_i+J_i log(27/16).
Thus the required H guard is strict even if the first inequality
is an equality. Both guards belong to s_i and its outgoing pair;
neither is a guard at s_(i+1).

**Closing edge and contradiction.** The arbitrary index includes
i=24, whose endpoint is n_25=n_0 and whose guards remain at s_24.
If b_24=0 then a_24=2: the exact tail identity and the oddness of
2^a n_25+1 used above still hold. The same argument covers tail 2
at any other row. No endpoint is lost at the original cut, and no
rotation or normalization is performed.

The identical d, table, integer allocation, literal order, all lower
domains, all 25 exact endpoints, closure and both guard signs now
supply every C093a hypothesis on this very tuple. Its audited real
exclusion contradicts existence. Integrality of shifted coordinates,
survivor feasibility and an actual-word realization converse are
unnecessary. No seed, minimum, primitive-count estimate, nonliteral
order reduction or failed full C077a conjunction has been imported.

The direct inputs remain exactly L041,L055,C093a, as recorded in
the DAG. L031 was inspected to verify L041's cited scope; it is not
a new direct input. C088b's step-365 audit is a d=5 comparison only,
not coverage of this changed range. The scoped construction and
source-review records contained no completed identical C093b audit.
The precise primary citation and Mathlib qualifications above/below
remain unchanged; no new source theorem or numerical check is claimed.
Attempt 032 and both d=0 witnesses remain valid. Nonliteral orders,
other tables, unrestricted cycles, entry, divergence and universal
eventual descent remain unresolved.

The argument and dependencies are unchanged, so PROOF.md and DAG.md
are not edited for audit status alone. This canonical audit supersedes
their pending-audit wording for C093b.

## Mathlib

Full matching Mathlib coverage for this changed-range actual-word exclusion
has not been checked. Supporting affine and logarithm facts are not a
matching theorem. Unknown coverage is not absence, and no Lean verification
is claimed.
