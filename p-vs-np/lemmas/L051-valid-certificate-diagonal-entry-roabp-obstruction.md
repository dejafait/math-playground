# L051 — Valid certificates with hard diagonal entries

## Hypotheses

Work over F₂. Use L048's unconditional formula, ordered-axiom, placeholder and explicit affine-ABP conventions only; neither of its existential size assertions is assumed. The original variables must all occur in the written width-at-most-three CNF. Every clause position, Boolean axiom, pair-once commutator, original name and permitted placeholder is paid for, including unused graph symbols.

For positive D, index matrices by 0,...,D. For each original symbol y, let Z_y,D have independent commuting entries z_y,k in positions (k−1,k), 1≤k≤D, and zero elsewhere. Set X_y=yI+Z_y,D. For every axiom position b let U_b have an independent commuting symbol u_b,r,s at each position r<s and zero elsewhere, and set T_b=t_b I+U_b. All scalar symbols are algebraically independent except for the deliberately repeated diagonal symbol in each matrix. This is the diagonal augmentation of Forbes–Shpilka's positional shifts; it includes the anchor variable below. All matrix entries and scalar dictionaries are explicit.

A receiving roABP computes a formal polynomial over F₂ in these commuting scalar symbols, reading them once in some order, with polynomial univariate edge labels. Its size is an explicit graph size and is at least its maximum layer width. A common-order representation for all entries may choose an order depending on the supplied package. No axiom substitution or quotient of the scalar polynomial ring is imposed when measuring the entries.

## Conclusion

For every integer n≥2 there is an explicit UNSAT formula F_n, a valid supplied affine-ABP certificate C_n, and D_n=binomial(n,2)+2 such that both free-ring identities hold and

    Q_n=2+|F_n|+|C_n|+|A_n|+D_n ≤ K(n+2)³,

for one fixed encoding-dependent K. Every diagonal entry of C_n(X,T) requires roABP width at least 2^floor(n/2) in every order of the complete scalar alphabet. This is superpolynomial in Q_n. Writing all receiving matrices and their complete scalar dictionary costs O((n+2)^6 log₂(n+2)) additional bits, so paying that cost as well does not remove the separation.

Consequently there is no universal polynomial bound in Q on explicit common-order roABP representations of all entries of every supplied valid certificate for this receiver. This is a local specialization of an established polynomial lower bound, classified POTENTIALLY_NEW only for the certificate realization relative to the checked coverage; originality is not certified. The separate informal critical audit at step 153 found no substantive error under these hypotheses. The same F_n has the easy certificate t_1+t_2. Thus this is neither every-certificate hardness nor a refutation of L048's existential premise, and it gives no ER lower bound or unrestricted SAT conclusion.

## Proof

**Scope and imported results.** The pre-invocation SPECIALIZE assessment is `drafts/literature/2026-10-11-diagonal-entry-roabp-obstruction.md`, approved at step 150. The local difference authorized there is exactly realization in a valid supplied certificate, entry extraction and full-size accounting. Attempts 020/021 concern other prescribed representations; Attempt 023 concerns fixed scalar positional substitution. None is a premise of this proof, and their evidence is unchanged.

Forbes–Shpilka–Tzameret–Wigderson, *Proof Complexity Lower Bounds from Algebraic Circuit Complexity*, Theory of Computing 17(10) (2021), [Corollary 6.22, pp.65–66](https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf), gives width at least 2^floor(n/2) in every variable order for every nonzero multiple of ∏_(i<j)(x_i+x_j+α_ij), over any field. Apply this with F=F₂, α_ij=0 and multiplier 1. Each factor is nonzero in the polynomial domain, so the product is nonzero. This is a formal-polynomial statement without a characteristic or field-size restriction; Boolean evaluations are irrelevant. The published lower bound is imported, not reproved. Its statement is on p.65 and proof on p.66; the preceding result is **Proposition** 6.21 despite the proof's “Theorem” cross-reference.

The same paper's [Lemma 3.6, p.19](https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf), supplies the width-preserving univariate matrix-product form for roABPs. The coefficient operation needed below is justified directly in that form. The shifts are [Forbes–Shpilka, arXiv:1209.2408v2, Construction 4.1, printed p.22](https://arxiv.org/pdf/1209.2408v2), with the diagonal augmentation specified in the Hypotheses. No PIT hitting set, field-size assumption from its later corollary, or IPS compatibility theorem is imported. Step-145/149/150 source coverage is reused; the two FSTW statements and Corollary 6.22's proof were checked at their direct source for this application.

**1. Complete original package.** Choose originals a,x_1,...,x_n. Their names are a fixed anchor tag and a distinct variable tag followed by the binary index padded to length ceil(log₂(n+1)); thus names have O(log(n+2)) bits and the x_i have numerical lexicographic order. Let the written clause list be

    (a), (¬a), (x_1 ∨ ¬x_1), ..., (x_n ∨ ¬x_n).

It has m=n+2 clauses of width at most two, is UNSAT because of its first two units, and every original actually occurs. Keep every tautological clause and both its literal occurrences, as L048 permits. Their ordered falsity polynomials are

    c_1=1+a,  c_2=a,  c_(i+2)=(1+x_i)x_i.

Write A_n as this clause list followed by all Boolean polynomials y²+y for the n+1 originals, then all y y'+y' y for distinct originals in dictionary pair order. Thus the number of positions is

    M=(n+2)+(n+1)+n(n+1)/2=(n+2)(n+3)/2.

The clause polynomial (1+x_i)x_i equals x_i+x_i², but its position remains distinct from its Boolean-axiom position. Placeholder t_b is the deterministic name of position b, for every 1≤b≤M. The full permitted alphabet of C_n is precisely these originals and all M placeholders, even though the graph will use only t_1,t_2 and the x_i. This specifies every axiom and its position, without silently dropping the anchor's Boolean or commutator axioms.

**2. Graph and both formal identities.** Set k=binomial(n,2), u=t_1+t_2, and let

    P_nc = ∏_(1≤i<j≤n, lexicographic pair order) (x_i+x_j)

be an ordered free-algebra product. Define

    C_n = u + u² P_nc + u P_nc = u+(u²+u)P_nc.       (1)

An explicit graph realizing (1) consists of three directed chains, sharing only their distinct entrance s and exit e. The first has one edge labelled u. The second has first two edges labelled u,u followed by the k edges x_i+x_j in the fixed order. The third has one edge labelled u followed by an independent copy of those k edges. Every internal vertex is private to its chain. There are exactly 2k+4 edges and 2k+3 vertices; no other edges exist. Every label is an allowed affine label with two symbol terms. Paths are exactly the three chains, so their ordered products prove (1), including the four ordered terms in the free expansion of u². The graph is acyclic, explicit, has no empty accepting path, and its maximum path degree is k+2=D_n.

At all placeholders zero, u=0, whence C_n(x,0)=0. Under substitution of the **whole** A_n, u=(1+a)+a=1 as an identity of the free F₂ algebra. Therefore

    C_n(x,A_n(x))=1+(1²+1)P_nc=1.

These substitutions do not commute factors or use any Boolean assignment. Unused placeholders have their specified axiom images but do not enter the graph. Thus both required identities hold formally with exactly the original package. The smaller graph consisting of one u-labelled edge also satisfies both identities for this same F_n; this will matter for the scope of the obstruction.

**3. Complete size accounting.** The written formula, literals and original dictionary cost O((n+2)log₂(n+2)) bits. The complete A_n has O((n+2)²) positions and only a bounded number of words of bounded length per position: clauses expand to at most two words here; Boolean and commutator axioms have two. Original names, placeholder names t_b, position/role fields, references and framing all have O(log(n+2)) bits because b≤M=O((n+2)²). Thus A_n and its full dictionaries cost O((n+2)²log₂(n+2)) bits. This bound retains equal polynomials at separate positions and includes every permitted but graph-unused placeholder.

The graph has O((n+2)²) vertices, edges and label terms. Their endpoints, names and record fields again require O(log(n+2)) bits each. Its complete encoding repeats the full original/placeholder dictionaries and A_n, as required by |C_n|; these cost the same order. Consequently |C_n|=O((n+2)²log₂(n+2)). Charging A_n again in Q_n and adding D_n=O((n+2)²) yields the stated fixed K(n+2)³ bound. All lists are generated by single-index or pair loops of polynomial length; there is no expansion of P_nc into words or enumeration of paths beyond the three written chains.

The extra receiving dictionary has (n+1)D_n shift symbols and M D_n(D_n+1)/2 upper-triangular placeholder symbols, plus n+1+M diagonal symbols. Its count is O((n+2)^6). Each name uses a fixed namespace tag and indices bounded polynomially in n, so it costs O(log(n+2)) bits. Writing the entire (n+1+M)-tuple of dense (D_n+1)-square matrices also uses O((n+2)^6) entry records; zero entries and repeated diagonals are included. Matrix dimensions and delimiters obey the same bound. Hence the full additional receiver description has O((n+2)^6log₂(n+2)) bits, at most K'(n+2)^7. This is also polynomial in Q_n, since the written formula alone has at least n records. No exponentially long alphabet is hidden in D_n or in the receiver.

**4. Exact diagonal entry.** For upper-triangular matrices B,E over the commuting polynomial ring and any diagonal position r,

    (BE)_(r,r)=∑_s B_(r,s) E_(s,r)=B_(r,r)E_(r,r),

because a nonzero summand requires r≤s≤r. Diagonal extraction also preserves sums and the unit. Induction over a word and then linearity therefore show that evaluating a free polynomial at the stated matrices and taking a diagonal entry equals its commutative scalar image obtained by sending X_y to y and T_b to t_b. This uses no specialization of the strictly upper-triangular symbols and holds at every r=0,...,D_n.

Let P(x)=∏_(i<j)(x_i+x_j) in the commuting polynomial ring and v=t_1+t_2. From (1), every diagonal entry is exactly

    h_n(x,t)=v+(v²+v)P(x).                          (2)

In particular none of a, the other t_b, the shifts or the U entries occurs in h_n. Set every scalar variable except x_1,...,x_n,t_1 to zero (in particular t_2=0), and write t=t_1. The resulting polynomial is

    h'_n(x,t)=t+(t²+t)P(x),    [t²]h'_n=P(x).      (3)

The coefficient equality is in F₂[x][t], not an interpolation claim over the two field elements.

**5. Extraction in every induced order.** Suppose an roABP of width w computes a diagonal entry (2) in any order π of the full scalar dictionary. By the imported matrix-product form it has a representation

    h_n=(M_1(v_1) ... M_s(v_s))_(1,1),

with w-square univariate matrices and (v_1,...,v_s)=π; unused alphabet symbols can be inserted with identity matrices. Evaluate every unwanted symbol at zero in its own matrix. This gives constant matrices at those positions and does not change w. Leave their positions temporarily in the product. The variable t appears in exactly one matrix M_j(t). All other factors are independent of t. Linearity of coefficient extraction therefore gives

    [t²]h'_n=(M_1 ... M_(j−1) ([t²]M_j) M_(j+1) ... M_s)_(1,1),

where all unwanted-variable matrices have already been evaluated. The coefficient is taken entry by entry in M_j, yielding one constant w-square matrix. This argument allows arbitrary univariate degrees and arbitrary location of t; no division or interpolation occurs.

Remove all constant-only positions by multiplying each consecutive constant block into an adjacent surviving x_i matrix. A block before the first surviving matrix is absorbed on its left, a block between matrices on the left of the next, and a final block on the right of the last. Products with constants remain univariate matrices in the same x_i and remain w-square. There are n≥2 surviving variables, so this operation has a surviving matrix available at both boundaries. The relative order of the x_i is precisely π restricted to them. The resulting matrix product, and hence an roABP, computes P by (3) with width at most w in that induced order. This also explicitly justifies constant specialization without increasing width when extra unused scalar variables interleave arbitrarily.

**6. Threshold and consequence.** Corollary 6.22 applied as above to P forces

    w ≥ 2^floor(n/2).

The conclusion holds for every original π, so choosing a common order for all entries cannot evade even one diagonal entry. For any fixed exponent b and constant c, Q_n≤K(n+2)³ implies

    2^floor(n/2)/(c Q_n^b) ≥ 2^floor(n/2)/(c K^b(n+2)^(3b)) → ∞.

Every fixed polynomial bound is eventually bounded by some cQ^b, giving the asserted superpolynomial separation. If the explicit receiver description is also added to the parameter, the same comparison uses the fixed exponent 7 instead of 3. Explicit total graph size dominates width, so the obstruction applies to complete aggregate entry size as well.

This meets the discriminating test on actual valid certificates, with all declared variables occurring and all input and receiver dictionaries charged. It stops the universal identical-entry common-order roABP bound. It does not address whether selecting a different certificate could make the receiver useful: the u certificate here already has easy entries. No matrix satisfiability equivalence or receiving-axiom substitution theorem is proved or refuted, and no hardness of every certificate follows. Those independent obligations, finite-field proof hardness, arbitrary ER-to-ABP representation and unrestricted SAT transfer remain open. The result is an informally audited local obstruction, not a candidate solution of P versus NP.

**7. Separate critical audit, 2026-10-11 (step 153).** The pre-invocation assessment `drafts/literature/2026-10-11-diagonal-entry-obstruction-critical-audit.md` covers exactly this audit. The published lower bound and matrix-product normal form are reused; no new source theorem, lower-bound proof or existential L048 premise is introduced. The following checks independently verify the local specialization.

The n+1 originals all occur in the clause list, including each x_i through its retained complementary literals. A has (n+2)+(n+1)+binomial(n+1,2)=(n+2)(n+3)/2 distinct positions, even when their polynomials coincide. The three path lengths are 1,k+2,k+1. Their private internal-vertex counts are 0,k+1,k, so there are 2k+4 edges and 2k+3 vertices including the two shared endpoints. Thus no unlisted path or empty path contributes. In particular u² is the ordered free product, not t_1²+t_2² in the free algebra. Substituting u=0 or u=1 directly into (1) proves the two identities without that false commutative simplification. The second substitution uses precisely the first two clause positions; it does not appeal to unsatisfiability to infer a formal identity.

Upper triangularity forces every factor in a diagonal product to stay at the same index. Hence no shift or strictly upper-triangular placeholder entry can enter (2), for any dimension or diagonal index under the stated convention. The repeated diagonals intentionally give the same h_n at every index. After setting t_2 and all unwanted symbols to zero, the only coefficient of t² is P; the lone t term contributes zero. In a width-w product for an arbitrary full order, there is only one t-bearing matrix, so taking its entrywise coefficient extracts the coefficient of the entire product. Every other removed factor is constant. Left absorption of the initial and interior constant blocks and right absorption of the terminal block retain w-square univariate matrices in the induced x order, including when t was first or last. This proves the needed closure directly over F₂, with no interpolation, field extension, commutation of matrix factors or enumeration of graph paths.

For the imported Corollary 6.22, n≥2, the field is F₂, all α_ij are zero and the multiplier is 1. Distinct indeterminates ensure each x_i+x_j is a nonzero polynomial; the polynomial ring is a domain, so P is nonzero. This is precisely the all-field polynomial theorem, not the distinct large-characteristic IPS theorem. The conclusion applies to every induced x order and yields w≥2^floor(n/2).

The input ledger uses O(n²) graph/axiom records with O(log(n+2)) bits per record, with all repeated dictionaries charged. D=k+2 adds only O(n²). The receiver has O(n²) matrices of dimension O(n²), hence O(n⁶) dense entry records, including zeros; its distinct scalar names also number O(n⁶) and have logarithmic payload. Thus Q≤K(n+2)³ and, with the entire receiver charged, R≤K''(n+2)^7 for fixed K''. For any fixed b≥0 and c>0, the logarithm base 2 of the ratio of the width lower bound to cR^b is at least floor(n/2)−7b log₂(n+2)−log₂(c(K'')^b), which tends to infinity. The claimed threshold therefore survives both complete input conventions. Checking only a succinct receiver would not have sufficed.

No load-bearing error, missing mathematical input or bound repair was found. This audit confirms the provisional supplied-output stop and leaves the existing proof unchanged. It is REPRODUCTION of the local argument using the cited theorem, not a new lower bound or certified novelty. The easy one-edge u certificate shows why the conclusion still says nothing about hardness of every certificate. No numerical test or verified proof string is claimed.

## Mathlib

Coverage of this complete certificate/entry specialization and of the imported roABP theorem is **not checked**; absence is not asserted. No Lean proof is claimed. Supporting free-algebra substitution, triangular matrix identities and coefficient extraction would not by themselves supply the imported every-order width lower bound. The cited published theorem supplies that input; the original identities, receiving entry, extraction and complete bounds are proved above.
