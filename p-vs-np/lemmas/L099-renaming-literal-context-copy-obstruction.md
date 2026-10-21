# L099 — Exponential active copies in literal renaming extraction

## Hypotheses

Use L097's assumption-free three-scheme Frege presentation with MP and
ground axioms true and ¬false, its ordered F₂ translation tr, and its
corrected affine-ABP axiom seeds. Add an inference Aρ from an earlier A,
where ρ is an explicitly written simultaneous variable-to-variable map,
fixing unlisted variables. Charge formulas, maps, names and references.
There are no nonlogical assumptions or extension definitions.

Fix the following **literal context-copy implementation**. Starting with
the final proof line under the identity map, request earlier witnesses
backwards. An MP with antecedent j and implication h requests both parents,
using K_i=K_j tr(ℓ_i)+K_h. A renaming line requests the parent under the
composed map. Axiom seeds and local MP multiplier graphs are the fixed
blocks from L097; a seed is copied as a whole block. Cache requests by
source line/block and action on the labels actually occurring in that
block or witness. Merge two copies only when these actions agree after
affine-label collection over F₂. Unused dictionary names are ignored.
Retain separate summands and parallel paths, as in L097.

Permit deleting zero-labelled edges and graph pieces with no accepting
path. Do not replace a proof by another proof of the same conclusion,
recompute a different seed for an equal conclusion, identify unequal
block polynomials, or synthesize a factored graph for an entire collection
of relabeled blocks. Such changes are other implementations. The bound
below counts whole seed copies under this explicitly fixed convention,
not the minimum possible graph size after arbitrary restructuring.

For a width-at-most-three source CNF F and its supplied proof π ending
exactly ¬F, include L087's complete occurrence pair, provenance and B
dictionary in the input and put Q=2+M+|F|+|π| before extraction.

## Conclusion

Variable renaming, including noninjective renaming, has a valid affine
Boolean/commutator placeholder reception preserving both extraction
identities. Nevertheless there is an explicit family (F_n,π_n), n≥1,
with Q_n≤C(n+2)³, for which the literal implementation requests at least
2^n pairwise nonmergeable, final-output-reachable copies of its initial
axiom seed. Each copy has a nonzero individual contribution after axiom
substitution. Thus its explicit copied output and writing time have no
fixed polynomial bound in original Q.

The family uses only bijective swaps, all source variables occur in F_n,
and every stage belongs to the final inference ancestry. Its distinguishing
variables occur on used seed paths, not just in maps or dictionaries.
The conclusion also survives injectively replacing source variables by
their chosen occurrence representatives and complementing them.

The separate step-388 critical audit below finds no substantive defect
in this informal implementation obstruction and clarifies reception of
freshly generated complemented seeds. No executable translator or verified
proof strings are claimed.
It does not lower-bound alternative ABP witnesses, ordinary Frege proofs,
SF proofs, or SAT decision time. The formulas have easy alternative proofs.
General source-to-occurrence normalization for renaming/SF, polynomial
short-proof availability and the exact fg transfer remain independent.
The result has no certified originality.

## Proof

**Coverage and imports.** This is the bounded test approved in the
pre-invocation EXPLORE assessment
`drafts/literature/2026-10-20-substitution-frege-occurrence-transfer.md`.
It already inspected Samuel Buss, *Some Remarks on Lengths of Propositional
Proofs*, manuscript dated July 3, 2002,
[§8 Theorem 15, Corollary 16 and Lemma 17, pp.22–24](https://mathweb.ucsd.edu/~sbuss/ResearchWeb/proplengths/paper.pdf).
That simulation permits noninjective renaming in assumption-free proofs.
It motivates testing this rule; no simulation theorem is used to infer a
graph bound. Likewise Krajíček–Pudlák,
[*Propositional proof systems, the consistency of first order theories
and the complexity of computations*, JSL 54 (1989), §6 pp.1076–1077](https://msekce.karlin.mff.cuni.cz/~krajicek/scan10.pdf),
does not supply an affine-ABP transfer.

Use the qualified extraction recurrence of Li–Tzameret–Wang,
*Characterizing Propositional Proofs as Non-Commutative Formulas*, SIAM
J. Comput. 47(4) (2018), 1424–1462,
[40-page author revision, Theorem 3.1/Lemma 3.3 pp.13–14](https://www.doc.ic.ac.uk/~itzamere/Ideal_non-commutative.pdf),
with corrected seeds and graph reception from L097 §4. The revision date
is unestablished; the assessment inspected it on 2026-10-20. In particular
tr(true)=0 and tr(A→B)=(1+tr(A))tr(B). L097's ground-constant repair
is retained. Its fixed-tautology-template argument supplies the finite
ordinary proof used below. None of these source statements contains the
renaming-copy lower bound; that narrower implementation claim is proved
here. No new search or novelty inference is made.

**1. Receive arbitrary variable maps correctly.** On a finite original
alphabet V write B_x=x²+x and B_{x,t}=xt+tx for distinct unordered pairs,
with free placeholders σ_x and τ_{x,t}. For a map ρ:V→W extend it to the
free algebra with placeholders by

    x       ↦ ρ(x),
    σ_x     ↦ σ_{ρ(x)},
    τ_{x,t} ↦ τ_{ρ(x),ρ(t)}  if ρ(x)≠ρ(t),
    τ_{x,t} ↦ 0             if ρ(x)=ρ(t).

Pairs on the right are put in the receiving dictionary's canonical order.
Denote this homomorphism by ρ̂. Constants are fixed. Applying the receiving
B substitution to ρ̂ agrees with applying ρ after the source B substitution:
the Boolean case is ρ(x)²+ρ(x), and the collapsed commutator is
ρ(x)ρ(x)+ρ(x)ρ(x)=0. Sending all placeholders to zero also commutes
with this operation. Hence

    K(x,0)=0 and K(x,B_V)=P(x)
    imply
    ρ̂K(w,0)=0 and ρ̂K(w,B_W)=ρP(w).

This applies to nonlinear placeholder words as well: equality on every
free generator proves equality of homomorphisms on every polynomial.
An affine edge remains affine after collecting repeated coefficients.
The graph remains acyclic; a collapsed zero edge may be removed.
One explicit relabeling has polynomial bit cost in its written input
and complete receiving dictionary. For composable maps,
η̂ρ̂=(ηρ)̂: if a pair first collapses it stays collapsed; if it collapses
only at the second map, both sides send it to zero. Thus backward context
composition is sound. This local fact supplies no bound on the number
of contexts requested by an entire proof.

**2. Explicit source formulas and proofs.** Use distinct variables
z,x_1,x'_1,…,x_n,x'_n. Let X_n be a fixed left-associated disjunction
x_1∨…∨x_n (X_1=x_1), and let

    T = X_n → (true → X_n),        a=x_1…x_n,
    p = tr(T) = (1+a)a = a+a².

T is the first axiom scheme, A→(B→A), with A=X_n and B=true.
Its initial axiom seed K_0 therefore satisfies K_0(0)=0 and K_0(B)=p
by L097. There is no need to derive true as a premise of this axiom.

Let ρ_i exchange x_i and x'_i and fix all other variables. These are
commuting involutions. Starting with the proved occurrence T_0=T,
append these four lines for each i=1,…,n:

    R_i = ρ_i T                  by renaming from T_{i-1};
    U_i = T → (R_i → T)          an instance of A→(B→A);
    D_i = R_i → T                MP from T_{i-1}, U_i;
    T_i = T                     MP from R_i, D_i.

T_i denotes a new line, even though its formula is T. Both earlier
copies are genuinely referenced: there is an MP path through D_i
from T_{i-1} to T_i and one through R_i. The map changes the written
formula R_i, since x_i occurs in X_n.

Let R be a fixed conjunction of the following 2n clauses in the displayed
order for i=1,…,n:

    (x_i∨¬x_i), (x'_i∨¬x'_i).

Take the explicitly bracketed CNF

    F_n=(z∧¬z)∧R,                A_n=¬F_n.

The two units have width one and the other clauses width two. The fixed
tautological template ¬((z∧¬z)∧r), with r replaced by R, has an
ordinary proof of A_n of O(|R|+1) symbols, using L097's fixed-template
reception. A fixed proof can be chosen with only its schematic variables:
any other variable in a fixed proof may be uniformly replaced by z
before instantiation. Constants have their specified axioms.

After the diamond prefix, append that proof of A_n, then the axiom
A_n→(T→A_n), then T→A_n by MP with A_n, and finally A_n by MP
with T_n. This is an assumption-free renaming-Frege proof π_n of exactly
¬F_n. Every diamond and T_0 belongs to the final inference ancestry.
An independent earlier proof of A_n is intentionally available; replacing
the final supplied derivation by it is outside literal context copying.

**3. The backward requests double on actual used labels.** Let Z_i be
the seed for U_i. Two applications of the unchanged MP recurrence give

    K_i = ρ̂_i(K_{i-1}) p + K_{i-1}(1+ρ_i p)p + Z_i.       (1)

Under a later context σ, the two requests for K_{i-1} have contexts
σρ_i and σ. Starting from K_n under identity, reverse induction yields
every subset of the remaining swaps. At the initial axiom this produces
all 2^n contexts ρ_S=∏_{i∈S}ρ_i.

These requests cannot merge under the stated cache test. After B
substitution their copied seed outputs are

    ρ̂_S(K_0)(B)=a_S+a_S²,
    a_S=t_1…t_n,  t_i=x'_i if i∈S and t_i=x_i otherwise.  (2)

For n≥1 the two words in each polynomial have different lengths n and
2n. The length-n words a_S distinguish all subsets S, so all outputs
in (2) are distinct nonzero polynomials. If two actions agreed on every
actual affine seed label, their copied graphs would be identical and
their B-substituted outputs would coincide, contradicting (2).

This distinction persists after discarding seed pieces without accepting
paths. Such pruning preserves (2). Moreover each selected name t_i
occurs in (2). A polynomial from a graph whose used labels contain neither
t_i nor a placeholder involving t_i cannot acquire t_i upon B
substitution. Thus the distinguishing information occurs in used labels;
it is not a difference solely on dictionary entries or absent names.
At least one accepting path exists in each copy since (2) is nonzero.

**4. Final reachability and nonzero individual contributions.** For a
fixed order on a finite alphabet, the degree-lexicographic leading word
of a product of nonzero free polynomials is the concatenation of their
leading words, with nonzero coefficient. To see uniqueness, maximal
degree forces maximal degree in each factor; the split at the first
factor's degree is fixed, and lexicographic maximality then forces each
leading word. This proves directly the no-zero-divisors fact used here.

p has positive degree, as does every ρ_S p. Therefore p and
(1+ρ_i p)p in (1), and their images under later swaps, are nonzero.
Every particular route from a copied K_0 through (1) to K_n has an
ordered product of these nonzero right multipliers. Its individual
B-substituted contribution is nonzero by (2) and the preceding product
fact. In particular its multiplier graphs have accepting paths after
zero-edge removal, so this copy survives source-to-output reachability.

At the final MP from T_n to A_n the right multiplier is b=tr(A_n).
From the written clause and conjunction trees it is precisely

    b=(1+z)z ∏_{i=1}^n
          (1+x_i+x_i²)(1+x'_i+(x'_i)²).                  (3)

The product order is the clause order above. Each factor is nonzero,
so b is nonzero. The final extraction contains the summand K_n b.
Thus each of the 2^n seed copies still has a nonzero individual
contribution and an accepting path to the actual final output.

Different summands can cancel after addition and B substitution;
indeed extraction must return the final translated conclusion.
No inference here treats the number of uncancelled monomials as the
copy count. The implementation retains separate blocks and paths and
cannot delete these copies by graph reachability or zero-edge removal.
Cancelling or refactoring the entire witness is an untested different
mechanism. Under the specified whole-seed-copy convention, each of the
2^n nonmergeable requests entails a separately written nonempty block
and hence at least one bit and one write operation.

**5. Original input length and occurrence reception.** Each diamond
has four O(n)-symbol formulas and a two-entry swap map. Variable and
line indices have O(log(n+2)) bits. The template proof and final MPs
have O(n log(n+2)) bits; therefore

    |π_n|=O(n² log(n+2)),       |F_n|=O(n log(n+2)).

F_n has 2+4n literal occurrences; L087's gadget adds four, so its pair
has q=4n+6 variables. Each tester has at most three states at every
nonterminal level. Explicit diagrams, both orders and provenance have
O((n+2) log(n+2)) bits. The complete Boolean/commutator dictionary has
O((n+2)²) bounded-length words with O(log(n+2))-bit names and indices,
hence M=O((n+2)² log(n+2)). Including all input framing yields
Q_n≤C(n+2)³ with an absolute encoding constant C.

For every fixed K,d, the ratio 2^n/[K C^d(n+2)^(3d)] tends to infinity
(take logarithms and use log(n+2)/n→0). Consequently no bound KQ_n^d
can pay these mandatory copies for all n. This proves the failure of
the original-Q polynomial ledger, not merely a large cost at small n.

All source variables occur in F_n. Choosing their first occurrence names
as in L098 is therefore injective on this whole source proof; there are
no foreign source variables to collapse. Transport each ρ_i to the swap
of the corresponding two occurrence representatives and fix the other
occurrence names. This gives exactly θ(ρ_iP)=ρ'_i(θP) on every formula,
so the same proof prefix and its final ¬θF_n remain valid with renaming
inferences over occurrence variables.

Uniform propositional complementation commutes with these swaps. On
translation it induces the algebra automorphism κ:y↦1+y, whose square
is identity. The proof follows at variable, constant and connective
nodes since tr respects the written substitutions. Thus the copied seed
endpoints become κθ(a_S+a_S²); they remain nonzero and distinct, and
all used right multipliers remain nonzero. The same lower bound applies
if the literal extractor starts on this normalized source proof. This
rules out a collapse of the evidence under representative selection or
the complement convention. It does not claim a general occurrence
normalization theorem or analyze every possible later guarded assembly.

**Scope of the stop.** Abandon this literal implementation's universal
polynomial ledger. L097/L098 for ordinary proofs are unaffected because
they use a single fixed whole-proof substitution, not the repeated
inference (1). F_n has an immediate contradictory-unit proof, so neither
optimal-proof nor optimal-witness hardness follows. Buss's renaming/SF
simulation is not a promise of short proofs in F alone, and its strength
does not make this copying failure a lower bound on SF or EF. A different
reuse invariant or output certificate remains possible. Attempts
018/030/031 concern separate failures and are not premises here.

**Independent critical audit — 2026-10-20, step 388.** The prior EXPLORE
assessment `drafts/literature/2026-10-20-renaming-context-copy-critical-audit.md`
authorizes this audit. Reuse its inspected Buss/LTW coverage with the
qualifications above; L099 is the object checked, not an assumed input.
The following checks use L097's corrected fixed-seed and MP interfaces
and L087's explicit pair construction. They establish the qualified
implementation stop for local use, without a stronger representation
theorem or certified originality.

1. **Receiving homomorphisms.** Check the two substitutions on each
   original, Boolean placeholder and unordered commutator placeholder.
   Reversing the canonical pair order changes nothing in characteristic
   two. Identifying its endpoints sends the commutator to zero, not to
   a Boolean placeholder. A once-collapsed pair cannot separate under a
   later map. These facts verify both commuting squares and composition,
   including nonlinear placeholder products and affine-label collisions.
   The receiving dictionary must contain every image name and distinct
   image pair; this is part of the complete-dictionary hypothesis.
   No injectivity is used in this interface.

2. **Actual proof and ordered recurrence.** The first scheme translates
   to (1+a)(1+b)a. Substituting b=tr(true)=0 and
   a=tr(X_n)=x_1…x_n gives p=a+a², also when n=1.
   Each R_i renames the immediately preceding line whose formula is T;
   D_i and T_i are precisely the two stated MPs. With r=ρ_i p,
   the translations of D_i and U_i are (1+r)p and
   (1+p)(1+r)p. Hence the two incoming witness contributions to T_i
   are exactly (1), and after B substitution their sum is

       r p + p(1+r)p + (1+p)(1+r)p
       = r p + (1+r)p = p.

   This verifies the multiplication order and the extraction invariant;
   it also illustrates why counting noncancelling total monomials would
   be invalid. L097 §3 supplies a fixed proof of the final contradiction
   template in this precise presentation. Instantiating it preserves
   ground axioms and MP. Its auxiliary proof letters can first be
   identified with z without changing its conclusion. The final two
   MPs use both the independent A_n proof and T_n, so their final
   ancestry includes every diamond and the initial seed.

3. **Contexts, pruning and cache rule.** At level i a later context is
   a product of swaps with indices greater than i. The two parents
   append ρ_i or the identity. Induction down to level zero gives
   exactly one branch choice for each subset of {1,…,n}. Distinct
   length-n words in (2) cannot cancel against length-2n words, including
   n=1. Agreement on all actual affine labels would imply agreement
   of path polynomials and their B images, which contradicts (2).
   This argument remains valid after zero-edge and reachability pruning,
   since that pruning preserves the polynomial. Distinct outputs alone
   would not exclude partial subgraph sharing; the whole-seed restriction,
   explicitly selected in step 385 before constructing the family, is
   essential to the number-of-copies conclusion.

4. **Final activity, not just ancestry.** For each branch, the seed's
   B image and every right multiplier are nonzero. In the leading-word
   argument in §4, maximal degrees fix the factor split, so no other
   pair can cancel its leading concatenation. It applies over F₂ and
   after every swap. Directly translating the actual source CNF gives
   (3): the unit prefix contributes (1+z)z, and a tautological clause
   contributes 1+x+x². All are nonzero free polynomials, although their
   scalar Boolean values need not be nonzero. Thus every individual
   route remains nonzero even after the final multiplier b.
   If that route's pre-B graph had no accepting path it would have zero
   polynomial and hence zero B image, a contradiction. Global
   cancellation between separate routes remains allowed. No rank or
   minimum-ABP-size conclusion is inferred from this reachability check.

5. **Original input bound.** There are 4n diamond lines of O(n) symbols
   each and n explicitly written two-entry swaps. A fixed template proof
   instantiated with R has a constant number of O(n)-symbol lines;
   final axiom/MP formulas have that size as well. Dense names, references
   and map entries have O(log(n+2)) bits. The original CNF contributes
   two unit occurrences and 4n tautological-clause occurrences, and
   L087 adds exactly four gadget occurrences. Thus q=4n+6.
   Each diagram has at most 3q+2 vertices and 6q transitions. The
   provenance, two permutations and name tables have O(q log(n+2))
   bits for this family. There are exactly q+q(q−1)/2 B entries with
   boundedly many symbols per entry; names and placeholder indices
   cost O(log(n+2)) bits. Complete framing therefore fits
   O((n+2)² log(n+2)), without extraction outputs or witness degrees
   in Q. This verifies the sharper family-specific Q≤C(n+2)³,
   independently of L087's looser general input bound. Exponential
   copy count exceeds every fixed polynomial in that original Q.

6. **Occurrence and complement reception.** All 2n+1 source variables,
   including z and every x'_i, occur in F_n. First-occurrence selection
   is injective on every variable in the supplied proof. Transported
   swaps act only on the selected representatives; they need not
   preserve the unused occurrences' provenance groups, since they are
   legal renaming rules on assumption-free tautologies. Their commuting
   relation with θ verifies every renamed line and preserves the exact
   conclusion ¬θF_n. Uniform complementation commutes with these swaps,
   preserves axiom instances and MP, and induces κ on translations.

   In particular, the complemented extractor may generate a **new**
   initial seed J rather than literally complementing the old seed
   graph. No equivariance of the seed-generating algorithm is assumed.
   L097 guarantees J(0)=0 and J(B)=κθ(p). Under the transported subset
   swaps its B images are κθ(ρ_S p), by the verified renaming interface.
   Injectivity of θ and invertibility of κ make them distinct and
   nonzero. The translated multipliers and final endpoint are likewise
   their κθ images. Repeating checks 3–4 therefore proves the same
   lower bound for freshly generated normalized seeds. Their formulas
   and names still have the stated polynomial input length. This
   clarifies §5 without changing the theorem or requiring a general
   guarded occurrence-transfer construction.

The audit retains the stop in precisely the stated model. It supplies
neither compression hardness for the sum of contexts nor a lower bound
on alternative witnesses, proofs or decision algorithms. There is no
change to the two direct mathematical inputs recorded in the DAG.
The existing independent proof of A_n remains an explicit easy alternative.
No executable or formal verification was performed.

## Mathlib

Full matching coverage for this literal-copy obstruction, the renaming
placeholder map, and the explicit proof-family ledger is **not checked**.
No absence or formal-verification claim is made. The precise primary
inputs reused above cover the proof-system convention and ordinary
extraction; the family, active-context count and original-Q comparison
are the local mathematical attempt, not an imported full-statement match.
