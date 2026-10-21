# C088b — d=5 literal full-allocation actual-word exclusion

## Hypotheses

Use L055's 25 indexed pairs, replacing only H_0=40 by 35 and
H_24=32670621 by 32670626. All J_i and all other H_i are unchanged.
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

No such actual closed concatenation exists over this full nonnegative
integer tail-allocation simplex in literal order.

This is a local RESEARCH/REPRODUCTION application under the prior
SPECIALIZE assessment
`drafts/literature/2026-10-20-d5-literal-actual-word-application.md`.
It transfers audited C088a's real-subsystem exclusion to actual words;
it claims no mathematical advance beyond the inspected source machinery.
The separate critical audit below found no defect. No nonliteral-order exclusion,
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
least 72. The two changed entries are H_0=35 and H_24=32670626.
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

Consequently, with precisely C088a's definitions
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
hypothesis of audited C088a. Its exclusion contradicts this real tuple.
This proves the claim. There is no rotation or new cut in the argument;
no outgoing row, tail or guard is detached from its chronological input.
All 25 occurrences are retained, without any distinctness assumption.

### Sources, overlap and qualifications

C088a supplies the exclusion, L041 supplies the finite occurrencewise
necessities, and L055 supplies only the explicit indexed table. L055's
original rational witness and its d=0 guards are not transferred to this
different table. C084a's audited d=2,3,4 transfer is a precedent, not
a premise or a d=5 result. The ready assessment found no identical
completed d=5 actual-word application; this is not a novelty claim.

The upstream finite-word affine source is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The prior assessment reuses its inspected hypotheses and essential
printed proof cases. The words here are finite and nonempty. Any
fixed-point denominator qualification used upstream is already handled
in C088a's audited inputs; this application takes no new fixed point.
L041 already proves the arbitrary-tail actual-word necessities, so no
reproof of affine or parity-coding machinery, fresh source retrieval
or numerical certificate calculation is needed.

Attempt 032 stops the full C077a sufficient-test conjunction at d>=5;
this proof instead invokes independently established C088a and does
not infer those failed tests from actuality. No minimum/seed, survivor
feasibility, integer test on shifted coordinates, primitive-count
threshold or realization converse enters. Both d=0 witnesses and
the recorded failures retain their scopes. Cyclic-order reduction
and all universal gaps remain independent.

### Independent critical audit — 2026-10-20, step 365

This RESEARCH/REPRODUCTION proof audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-20-d5-literal-actual-word-critical-audit.md`.
It found no defect in the stated actual-word application. The audit
checks the transfer to C088a, taking that lemma's separately audited
real exclusion as an input; it does not independently recertify the
upstream numerical bounds or establish a larger exclusion family.

**Table, allocation and chronology.** Comparing the complete L055
table with both statements gives identical pairs at all 25 indices:
the only replacements are H_0=35 and H_24=32670626. The unchanged
entries at indices 1 through 23 all have H_i>=72, and every J_i>=8.
Thus every row satisfies L041's J_i>=2,H_i>=3 requirements. Both
C088a and this application use exactly B=9250245 and the same
nonnegative integer b_i, with a_i=2+18b_i attached to outgoing row i.
No assertion about L055's original tails, minimum, seed or witness
guards is imported with its table.

The finite positive lengths D_i count the actual shortcut letters:
each OOEO has four steps, followed by H_i odd steps and a_i even
steps. Consequently the defined t_i are precisely the consecutive
word boundaries, and n_i is the input of indexed row i for every
0<=i<25. The prefix states used in (2) equal T^(4J_i)(n_i) and
T^(4J_i+H_i)(n_i). No time cut is changed. A shorter repeated
period or equality of two junction values does not merge their
indexed occurrences.

**All lower domains and the scope of L041.** For each of the 25
positive odd residue-20 inputs, n_i=20+27q_i with integer q_i.
If q_i<0 then n_i<=-7, contradicting positivity. Parity gives q_i
odd, hence q_i>=1 and n_i>=47. Thus s_i=n_i+23/11>=540/11 at
every outgoing input, and closure gives the same at i=25. In
particular the starting value is odd and greater than 1. The actual
closed word, r=25, exact tails and a_i>=2 congruent to 2 modulo 18
therefore satisfy all of L041's stated hypotheses.

Only L041's passage “Each occurrence's own prefix and the transfer
to the next” is used. Its identities and valuations are proved at
an arbitrary occurrence; the 2026-10-08 audit explicitly records
their independence of junction-size ordering. Its earlier choice
of a smallest designated junction therefore adds no hypothesis here.
L031 (4) and its “Exact boundary valuations, without assuming E^2
transport” passage confirm the arbitrary-tail scope of this input.
Neither the two-word closure converse nor L041's cycle-mass, seed
or imported primitive-period estimates enters the transfer.

**Endpoint and guard matching at an arbitrary index.** Fix any
i in {0,...,24}. In L041's identities put s=s_i, J=J_i,
H=H_i, a=a_i and m=n_(i+1). Solving its already established
identity 2^H(2^a m+1)=3^H(y+1), using
y+1=(27/16)^J s-12/11, gives precisely (3). In particular both
(12/11)(3/2)^H and 1 are subtracted before division by 2^a;
23/11 is added afterwards. This is C088a (1) with exactly its
G_i,Q_i and kappa, not a bound on or a different shift of that
endpoint.

For the first guard, L041 gives 11n_i+23>=2^(4J_i+2).
Since 11n_i+23=11s_i>0, monotonicity of the natural logarithm
gives (4), with log11-2log2=log(11/4). No strict J inequality
is asserted or needed. The valuation passage furnishing this bound
uses H_i>=3 and the actual even tail; its hypotheses hold separately
for this outgoing row and not merely for a selected small input.

For the second guard, L041 gives 2^H<=y+1, while its exact prefix
identity gives y+1=(27/16)^J s-12/11<(27/16)^J s. All quantities
inside logarithms are positive. Hence
H log2<=log(y+1)<log s+J log(27/16), exactly the strict H half
of C088a (2). Possible equality in the lower power bound does not
remove the strict upper inequality. In particular no guard for
row i is being applied to s_(i+1).

**Closing edge and the final invocation.** The preceding argument
quantifies over all 25 indices, including i=24. There m=n_25=n_0
by actual closure, so its endpoint is s_25=s_0; its two guards
remain at s_24. At a_24=2, the factor 2^a m+1 in L041's
valuation argument is still odd, the tail identity still holds,
and no inequality used here changes sign. The same observation
covers tail 2 at any other row. No endpoint is omitted at the cut.

The identical table and integer allocation, all lower domains,
all 25 exact endpoints including closure, and both own-input
guards now give every C088a premise on this one literal tuple.
C088a's audited real exclusion is therefore applicable and
contradicts the assumed actual words. Neither integrality of the
shifted coordinates nor any realization converse is needed.

The primary finite-word citation and qualifications above are
unchanged; the audit does not reprove that machinery. The scoped
construction/audit records contained no completed identical C088b
audit before this step. C084a's other-table transfer is only a
precedent, not a mathematical input. Attempt 032's failed full
sufficient-test conjunction is not invoked or repaired, and both
d=0 rational witnesses retain their different tables and scopes.
Nonliteral cyclic orders, other tables, unrestricted cycles,
divergence and universal eventual descent remain unresolved.

The argument and its direct mathematical inputs are unchanged.
PROOF.md and DAG.md are therefore not edited for audit status alone;
this canonical audit supersedes their pending-audit wording for C088b.

## Mathlib

Full matching Mathlib coverage for this table-specific actual-word
exclusion has not been checked. Supporting affine and logarithm facts
are not a matching theorem. Unknown coverage is not absence, and no
Lean verification is claimed.
