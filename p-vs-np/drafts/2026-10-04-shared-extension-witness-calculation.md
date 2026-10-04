# Shared ER extension witnesses: calculation checkpoint

The ready SPECIALIZE assessment is `drafts/literature/2026-10-04-shared-noncommutative-er-circuit-ips.md`. Its TARGET matches the saved next action, and its Booleanity/commutation and assembly subtargets are preapproved. This is mathematical work under that existing coverage; no new source review is needed.

The main gap remains an unconditional SAT decision result. The local test asks whether extension-axiom elimination can have one fixed polynomial binary bound in T=2+|F|+|pi|, without materializing L019's occurrence trees. A useful intermediate result would provide original-axiom witnesses for every substituted Boolean, commutator and defining-clause axiom. It would leave certificate propagation/assembly, circuit-to-tree conversion, certificate hardness and the decision transfer separate.

Proposed representation: keep all acyclic extension values P_g as one arithmetic DAG over F₂, with gates 0, 1, original variables, addition and ordered multiplication. A negative literal is 1+P_g. Use only the original Boolean placeholders b_i and pair-once commutator placeholders c_ij.

For each ordered gate pair define K(g,h) recursively by splitting an addition/product gate and using the identities [ab,c]=a[b,c]+[a,c]b and [a,bc]=[a,b]c+b[a,c]. Constant cases are zero; original-variable cases use c_ij (or zero for equal variables). Memoize every gate pair. The proposed number of states is at most S² for S base circuit gates, irrespective of syntactic degree.

Proposed Booleanity recurrences are B(a+b)=B(a)+B(b)+K(a,b) and B(ab)=a K(b,a) b+B(a)b²+a B(b). They must satisfy both B(g)(x,0)=0 and B(g)(x,A(x))=P_g²+P_g as formal noncommutative identities. A commutative calculation or Boolean evaluation alone does not suffice.

For z=ab, the defining-clause falsity products in definition order are ab(1+a), ab(1+b), and (1+ab)ab. Proposed witnesses are B(a)b+a K(b,a), a B(b), and B(z). Literal permutations need explicit adjacent-swap witnesses, and removing repeated factors must use Booleanity; neither normalization may be inferred from semantic equivalence.

Continue if these recurrences are formally valid and all original-axiom outputs can be written with a fixed polynomial total binary cost, even when every rooted circuit is written separately. Stop or repair the mechanism if it needs tree unfolding, retained extension placeholders, bounded degree or uncharged witness copies. The next independent mathematical obligation would be using these witnesses in the screened ER-to-certificate assembly.

Mathlib coverage: **not checked**. Li–Tzameret–Wang v4 Lemmas 3.6–3.7 and the previously read Booleanity/elimination constructions are supporting comparisons, not an imported theorem for this shared noncommutative statement.

Completion, 2026-10-04: [L020](../lemmas/L020-shared-extension-original-axiom-witnesses.md) proves the proposed recurrences and their zero-placeholder identities. The product Booleanity correction is necessary in the free ring. Explicit sorting and duplicate-deletion corrections give the actual encoded extension-clause products. The common network has O(T²) nodes; all rooted outputs written separately, plus the original axiom list, cost O(T⁵) bits, meeting the original-length threshold rather than a degree or unfolding threshold. The new script checks 67 exact small formal-word cases and six structural cases without claiming verification of assembled IPS identities. This is an intermediate local advance by specializing known mechanisms; the preapproved assembly obligation remains for the next step.
