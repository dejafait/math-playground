# L025 — Global circuit IPS from supplied reduced local data

## Hypotheses

Let F be an explicitly encoded width-at-most-three CNF and pi a valid ER refutation with L021's fresh acyclic AND definitions, sorted-set clauses, weakening and selected-pivot resolution. Put T=2+|F|+|pi|, in binary bits, including every literal, identifier and inference reference. Use L020's original axiom list A(x): ordered original clause falsity products, original Boolean polynomials and pair-once original commutators. Work over F₂ in the free noncommutative ring on the original x and independent placeholders t for exactly A. Products are ordered and circuits have division-free fan-in-two arithmetic gates and sharing.

Supply a topologically numbered **abstract** value DAG with S nodes, numbered 1 through S. Its base nodes are original variables and constants 0,1. Other nodes are exact signed nodes r_i=1+r_a, a<i, or reduced AND nodes i with designated operands a,b<i. There is a node for every extension and every signed value needed by pi; nonextension variables absent from F map to 0. The operands of an AND definition are the values of its signed literals. For each abstract node supply an x-only representative circuit r_i; original variables retain x_i and constants retain their field values. Internal representative gates are not abstract nodes and need not reproduce the abstract AND operation formally.

For every reduced AND node i supply a circuit H_i(x,t) with formal identities

H_i(x,0)=0,                 H_i(x,A(x))=r_i+r_a r_b.                (1)

Let d,h>=1 bound the formal polynomial degrees, after cancellation, of all representatives and all H_i, respectively. These degrees are measured in independent x,t **before** axiom substitution. No degree bound on internal gates or syntactic degree is assumed. Witnesses may be nonlinear in placeholders. E is the total explicit binary encoding length of all supplied representative and relation circuits, labels and abstract-node/root associations, with axiom framing charged if supplied. All abstract nodes and supplied roots are explicitly encoded. Existence, efficient construction and efficient validation of these degree/identity promises are not assumed.

## Conclusion

One can construct an original-axiom circuit C(x,t) with both formal IPS identities

C(x,0)=0,                         C(x,A(x))=1.                      (2)

Only original x,t are free. Its complete formal degree is at most

D = h+(4S+T²+2T+2)d.                                               (3)

The common construction adds O(S²+T⁴) arithmetic gates beyond the supplied circuits. Its total gate count is O(E+S²+T⁴). With M=E+S²+T⁴+2, a single rooted output plus the full original axiom list has full binary length

O(M(T+log(M+2))+T³).                                               (4)

Even writing every intermediate pair, Boolean, defining-clause and proof-line output as a separate rooted circuit has aggregate length O((S²+T²+1)M(T+log(M+2))+T³). Constants in these bounds are absolute for the fixed encoding convention. The construction uses polynomially many operations in the explicitly supplied data, without testing their promises. With polynomial bounds on S,d,h,E in T, these are polynomial complete size and degree bounds in T.

This is a conditional direct reduced-invariant construction, not an exact correction to L021's unreduced output. It passes the approved global-propagation test. General existence of small supplied data, polynomial trees, checking arbitrary circuit IPS identities, all-certificate lower bounds and transfer to SAT decision complexity remain unresolved. No P-versus-NP candidate or certified originality is claimed.

## Proof

**An acyclic ordered pair table.** Construct K_(i,j) with zero-at-zero identity and substituted value r_i r_j+r_j r_i. Diagonal and constant pairs use zero. Distinct original variables use their original pair placeholder; duplicate input labels, if present, use zero. For other pairs, split the first nonbase node when possible. An exact signed first node inherits K_(a,j), since the commutator of 1 with anything is formally zero. At a reduced AND first node use

K_(i,j)=r_a K_(b,j)+K_(a,j)r_b+H_i r_j+r_j H_i.                    (5)

If the first node is a base input and the second is signed, inherit K_(i,a). If the second is a reduced AND node with operands a,b, use

K_(i,j)=K_(i,a)r_b+r_a K_(i,b)+r_i H_j+H_j r_i.                    (6)

Every recursively referenced pair has strictly smaller sum of indices. Supplied H roots introduce no dependency on constructed table roots. Hence increasing i+j is a valid order, even if the larger-index node is the unsplit second node. The choice of orientation need not split the greatest index.

For (5), the first two terms substitute to r_a r_b r_j+r_j r_a r_b by L020's ordered product-commutator identity. The last two substitute to (r_i+r_a r_b)r_j+r_j(r_i+r_a r_b), cancelling exactly the unwanted product terms. Formula (6) has substituted first part

(r_i r_a+r_a r_i)r_b+r_a(r_i r_b+r_b r_i)
 =r_i r_a r_b+r_a r_b r_i.

Adding r_i(r_j+r_a r_b)+(r_j+r_a r_b)r_i leaves r_i r_j+r_j r_i. This checks the second orientation separately without reversing a coefficient. Every summand contains a zero-at-zero witness, so all table roots vanish at t=0.

Induction on i+j proves

deg K_(i,j)<=h+(i+j)d<=h+2Sd.                                     (7)

Base placeholders have degree one<=h. In (5) or (6), each earlier pair is multiplied by one degree-at-most-d value, and its index sum is at most i+j-1. Relation terms have degree at most h+d. Signed inheritance decreases the index sum without increasing degree. Each pair needs a constant number of gates, so the table adds O(S²) gates. Semantic degree bounds suffice: multiplying root polynomials adds their degrees even if internal syntactic degrees are larger.

**Boolean and defining-clause witnesses.** Base Boolean roots are zero for constants and original Boolean placeholders for x. Signed nodes inherit B_a because (1+r_a)²+(1+r_a)=r_a²+r_a formally over F₂. At reduced AND node i set p=r_a r_b and use L024's complete update

M_i=r_a K_(b,a)r_b+B_a r_b²+r_a B_b,
B_i=M_i+H_i r_i+p H_i+H_i.                                       (8)

L024 proves B_i(A)=r_i²+r_i and B_i(x,0)=0, retaining the product commutator correction. The already completed table supplies K_(b,a); only Boolean roots of earlier nodes occur in (8). Thus no circular dependence is introduced. From (7), induction in i gives

deg B_i<=h+(2S+2i)d<=h+4Sd.                                      (9)

Indeed, the commutator term is bounded by h+(2S+2)d, the earlier B_a term by h+(2S+2(i-1)+2)d, the B_b term by h+(2S+2(i-1)+1)d, and the new H terms by h+2d. For i>=1 these are all within the claimed bound. Bases and signed inheritance also satisfy it.

For the three definition-order clause polynomials use L024's

D_1=B_a r_b+r_a K_(b,a)+H_i(1+r_a),
D_2=r_a B_b+H_i(1+r_b),
D_3=M_i+H_i p.                                                    (10)

They vanish at zero placeholders and substitute, respectively, to r_i(1+r_a), r_i(1+r_b), and (1+r_i)r_a r_b. Their degrees are at most h+(4S+2)d. Complements in the definition are exact signed values. All Boolean and definition outputs add O(S+T) gates beyond the pair table and supplied roots.

**Direct reduced clause invariant.** Define rho by sending each proof variable to its supplied reduced value, original variables to themselves, and other nonextension variables to 0. This is a formal substitution from the free ring on proof variables; it is not asserted to carry a definition z+ab to zero. The witnesses (10) supply rho of those defining clauses instead. For every proof line D construct Q_D with

Q_D(x,0)=0,                   Q_D(x,A)=rho(f(D)).                   (11)

Here f(D) is the ordered falsity product. Original initial clauses use original placeholders; (10) supplies extension initial clauses. Normalize initial lists as necessary. For an adjacent swap in LuvR, add L K_(u,v)R. For duplicate deletion LqqR -> LqR, add L B_q R. Their formal substituted values are exactly the differences. Prefixes/suffixes are x-only products of reduced factors, and complementary literals are retained. Thus these operations do not require rho to respect the abstract AND relation exactly.

Weakening multiplies the earlier root on the right by the product of newly added factors, then normalizes. For resolution move the selected positive and negative pivot factors to the fronts using the same corrections. Let p be its reduced positive value and let U,V be the remaining products. The corrected parent roots R,Q satisfy R(A)=(1+p)U and Q(A)=pV. Build J for pU+Up along U's factor list by L021's recurrence

U_0=1, J_0=0,
U_k=U_(k-1)q_k,
J_k=J_(k-1)q_k+U_(k-1)K_(p,q_k).                                  (12)

Then R V+U Q+J V substitutes formally to

(1+p)UV+UpV+(pU+Up)V=UV.

All three summands vanish at t=0. Normalizing the concatenated residual lists gives the actual encoded resolvent, including duplicates and retained opposite literals. This is L021's ordered assembly applied only to the now established witness identities, with no exact-value or placeholder-linearity assumption inherited. The final empty clause proves (2). No step multiplies two constructed placeholder-dependent roots; nonlinear supplied H sectors are nevertheless retained. We do not claim that C is placeholder-linear without that additional premise on H.

**Complete degree accounting.** Each proof clause has at most T factors, every transient normalization list has at most 2T, and there are at most T source records; these are deliberately conservative consequences of the fully charged binary length. Each reduced factor has degree <=d, including complements. A swap/deletion correction has one K or B multiplied by prefixes and suffixes with at most 2T factors, so its degree is bounded by h+(4S+2T)d. Adding it to a current certificate does not multiply that certificate. Initial witnesses, including normalized width-three definitions, therefore have degree at most

R_0=h+(4S+2T+2)d.

For (12) with r factors, induction gives deg J_r<=h+2Sd+(r-1)d for r>=1; J_0 is zero. After multiplication by V this is at most h+(2S+2T)d<=R_0. Moving pivots and final normalization have the same R_0 allowance. In resolution each corrected parent is multiplied by at most T reduced factors; weakening has the same allowance. Thus for record number k, including all earlier parents,

deg Q_k<=R_0+kTd.

The induction uses only references to earlier records; reusing a parent does not increase the longest path beyond T. With k<=T this is (3). The intermediate J roots, all correction sectors and all table/definition/Boolean outputs also lie within this bound. It is a pre-substitution degree estimate in the full free x,t ring, not a Boolean quotient degree or a bound on only one sector.

**Sharing and full binary cost.** Representatives and H circuits have at most O(E) explicitly encoded gates. Retain them once in the common DAG, adding O(S²) pair gates and O(S+T) Boolean/definition gates. L021's unchanged list implementation uses O(T²) normalization operations per source line, each with O(T) new prefix/suffix gates, hence O(T⁴) total additional gates. The U,J,V operations and weakening fit this allowance. Earlier witness and proof roots are referenced, never recursively copied. Arbitrarily many later uses are charged as explicit bounded-fan-in edges.

Densely renumbering the common circuit may enlarge supplied references, so the claimed cost is polynomial in E, rather than E plus an unqualified small additive bit cost. Each of its O(M) nodes needs O(log(M+2)) reference/framing bits. Original input identifiers are charged at most T bits each, and field coefficients have constant size. This yields O(M(T+log(M+2))) bits. The original axiom list has O(T²) constant-width entries, with identifier/framing cost O(T) each, giving O(T³) bits. Output/root framing is included. These prove (4).

There are O(S²+T²+1) table, Boolean, definition and proof-line roots even with the augmented pair-axiom outputs. Writing each separately uses at most the entire common DAG per output, proving the aggregate bound stated above. This conservative allowance does not assume sharing across separately written files. No identity test, enumeration of words, unfolding of representative circuits or efficient verification of semantic degree is part of the general construction.

**Scope and diagnostic.** This result differs from L020/L021 by permitting r_i != r_a r_b formally and by controlling the whole certificate degree. It differs from the stopped exact-lift route by never constructing a witness from an unreduced exponentially high-degree value to r_i. It supplies only the approved conditional propagation input, not existence of its hypotheses. L024 is used for its proved local identities, not as an assumption that recursively generated B,K have degree h.

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-reduction/check_reduced_global.py`. Independent word substitution checks both pair orientations, 121 ranked pairs, 11 Boolean roots and nine defining-clause roots on an eleven-node abstract DAG. Its supplied relation includes a genuine nonlinear-placeholder kernel term; the full corrections are retained. A nine-line valid ER refutation uses reduced extension defining clauses and checks every reduced clause invariant and both final IPS identities. A corrupted second-orientation coefficient order is detected. Full finite polynomials, pair ranks, source records, parameter bounds and failures are saved in `scripts/coefficient-reduction/reduced-global-results.json`. The all-S,T proof and asymptotic cost are the preceding inductions, not the finite preview or numerical checks.

## Mathlib

Coverage: **not checked** for the full conditional propagation theorem, semantic-degree bound or binary accounting. L020, L021 and L024 supply the local mathematical inputs; their applications and the global difference are justified above. Li–Tzameret–Wang, [*Characterizing Propositional Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4, 11 September 2015, Lemmas 3.6–3.7, printed pp. 17–18](https://arxiv.org/pdf/1412.8746v4), provides supporting ordered formula-commutator corrections, not this reduced shared-DAG degree bound. Forbes–Shpilka–Tzameret–Wigderson, [*Proof Complexity Lower Bounds from Algebraic Circuit Complexity*, Theory of Computing 17(10), 2021, §4.2, Propositions 4.4–4.6, Lemma 4.9 and Corollaries 4.10–4.11](https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf), provides restricted commutative multilinearization mechanisms, not a checked full match here. The prior EXPLORE comparison authorizes the unimported conditional recurrence; no source theorem is reproved to inflate progress, and no originality or Mathlib-absence claim follows.
