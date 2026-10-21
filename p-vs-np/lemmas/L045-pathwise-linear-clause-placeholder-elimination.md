# L045 — Clause-placeholder elimination for a supplied pathwise-linear ABP

## Hypotheses

Work in the free associative algebra over F₂. Let F be an explicitly encoded width-at-most-three CNF, retaining its written clause and literal orders, repetitions and complementary literals. Use L041's translation: c_j is the ordered product of falsity factors v(x_i)=1+x_i and v(¬x_i)=x_i; s_j=1+c_j; f_F=s_1…s_m. Empty products are 1. The original alphabet contains exactly F's original identifiers with their full name dictionary. B_x consists of x_i²+x_i and x_i x_k+x_k x_i for i<k, with independent placeholders σ_i,τ_ik. A consists of the ordered c_j followed by B_x, with a distinct clause placeholder y_j for each written clause, including repetitions.

Supply an explicit finite acyclic affine-F₂ ABP C over x,y,σ,τ with designated source and sink. Its path polynomial satisfies the formal identities C(x,0)=0 and C(x,A(x))=1. Every accepting path has exactly one placeholder-bearing edge. Here a placeholder-bearing edge means that its affine label, after collecting coefficients over F₂, has a nonzero coefficient of at least one y_j,σ_i or τ_ik; its label may also contain constants or original symbols. Parallel edges, dead vertices, unequal lengths, nonextremal designated endpoints and zero labels are allowed. Empty paths contribute 1. No implicit graphs or circuit-valued labels are permitted.

Let Q=2+|F|+|C|+|A| count complete binary graph, label, dictionary, original-name, placeholder, axiom and endpoint framing. Use an ordinary explicit list encoding, as in L035/L036. The supplied identities are hypotheses, not semantic promises to be inferred from ER. In particular no ER-to-C construction is assumed.

## Conclusion

There is a deterministic polynomial-time construction of an explicit acyclic affine-F₂ ABP H over exactly x,σ,τ with the formal identities

    H(x,0)=0,                  H(x,B_x)=f_F.

For one absolute constant K in the fixed encoding, its full bit length is at most K Q^20, including the complete original alphabet, B_x, placeholder dictionary and root framing. Every accepting path of H contains exactly one placeholder edge; this extra property is not needed by L041's witness interface. The construction can produce H without testing the supplied identities.

This is a conditional intermediate representation result, not the general supplied-ER transfer, a universal Boolean-zero witness bound, ER polynomial boundedness, a proof finder for arbitrary UNSAT formulas or a P-versus-NP resolution. A separate critical audit on 2026-10-10 found no substantive error; its all-input checks are recorded below. The construction is classified POTENTIALLY_NEW only within the saved source comparison; the audit is REPRODUCTION and certified originality is not claimed.

## Proof

**Source scope.** The ready assessment `drafts/literature/2026-10-10-er-to-clause-product-boolean-witness.md` authorizes this bounded supplied-C test. Hrubeš, *Proof complexity and arithmetic circuits*, WACT 2016 slides, [Proposition 3 and proof, PDF pp.32–39](https://www.cs.tau.ac.il/~shpilka/wact2016/program/slides/Pavel_ProofComplexity.pdf), gives a commutative EF/Boolean-ideal circuit comparison, not this graph theorem. Li–Tzameret–Wang, [arXiv:1412.8746v4](https://arxiv.org/pdf/1412.8746v4), Lemmas 3.5–3.7, printed pp.16–18, retains formula/tree input and clause axioms. Neither theorem is imported as the conclusion. Use the audited local L035/L036 constructions for x-only affine graphs: W(u,v)(0)=0, W(u,v)(B_x)=uv+vu, and B(u)(0)=0, B(u)(B_x)=u²+u. They supply polynomial full encoding and exactly one placeholder edge per accepting path. Their hypotheses allow all the designated-endpoint cases used below. Disjoint serial/parallel composition is the standard graph construction of Raz–Shpilka, [*Deterministic Polynomial Identity Testing in Non Commutative Models*](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf), Lemma 2 Step 1, printed p.5; the endpoint qualification is checked below. No reproof of these source theorems is needed. The additional argument is the ordered clause correction and its marked-edge assembly.

**Marked-edge decomposition.** Prune C to vertices and edges on source-to-sink paths, preserving its polynomial. Split each normalized affine label into parallel constant-1 and single-symbol edges; a zero label contributes no edges. Call the resulting graph C'. Each C' accepting path projects to an accepting path of C. Hence it uses at most one placeholder-symbol edge. Mixed labels can create paths with no placeholders, so it would be incorrect to assert that normalization preserves the exactly-one property.

Delete all placeholder-symbol edges from C', leaving an x-only graph C_0 with the same designated roots. Its polynomial is C(x,0), thus zero by hypothesis. For every placeholder-symbol edge e:u→v with symbol t_e, let P_e be the x-only C_0 subpath polynomial from the source to u, and S_e the x-only C_0 subpath polynomial from v to the sink. Represent these by copies of C_0 with those designated roots, not by expanding paths. Partitioning the accepting paths into those with zero or one placeholder gives the formal identity

    C = C_0 + sum_e P_e t_e S_e = sum_e P_e t_e S_e.       (1)

For a fixed edge, every such prefix/suffix pair concatenates into a path: an overlap producing a repeated vertex would give a directed cycle. Conversely every accepting path with one placeholder has a unique marked edge and these x-only subpaths. These are finite sums; their regrouping uses distributivity, not commutativity. Placeholder-free paths may cancel; the equality C_0=0 uses the formal identity, not pathwise vanishing.

**Boolean and commutator branches.** If t_e is σ_i or τ_ik, use the branch

    H_e = f_F P_e t_e S_e.                                (2)

All surrounding factors have explicit x-only affine graphs. This branch vanishes at zero placeholders and substitutes to f_F P_e A_e S_e, where A_e is its indicated B_x axiom.

**Clause branches and factor order.** If t_e=y_j, put L_j=s_1…s_(j−1), R_j=s_(j+1)…s_m and D_e=R_j P_e, all x-only. Define

    H_e = L_j s_j W(D_e,c_j) S_e
                    + L_j B(c_j) D_e S_e.                (3)

Every graph factor in this expression is copied independently. L035/L036 take only the x-only graphs D_e,c_j. No witness graph or placeholder-containing operand is passed to either construction. At zero placeholders both summands vanish. At B_x their sum is

    L_j [(1+c_j)(D_e c_j+c_j D_e)
                         +(c_j²+c_j)D_e] S_e
      = L_j (1+c_j)D_e c_j S_e
      = f_F P_e c_j S_e.                                 (4)

Indeed (1+c_j)c_j D_e=(c_j+c_j²)D_e, which cancels the second correction in characteristic two. No factor is moved without its commutator correction. The factor s_j in the first summand is essential. All equations are free-algebra identities, including repeated-variable and complementary-literal clauses.

**Assembly.** Let H be the parallel sum of all H_e with fresh common endpoints. By (2)–(4), distributivity and (1),

    H(x,B_x)=sum_e f_F P_e A_e S_e
            =f_F C(x,A(x))=f_F.

Every branch vanishes at zero placeholders, so H(x,0)=0. Every accepting branch path contains exactly one placeholder: the central edge in (2), or the one supplied by W/B in (3), with x-only surroundings. A sum with no branches is the disconnected zero graph.

For every ordered product or sum, take disjoint copies and forward constant-1 connectors. This produces an acyclic affine graph. A designated exit may have outgoing internal edges, but following them cannot later return to that exit to take its connector in a DAG. Thus such edges produce no extra accepted routes; coincident entrance/exit contributes precisely the empty internal path. Disconnected operands give zero. The construction does not unfold formulas, enumerate paths or introduce new free symbols.

**Complete bit bound.** Every input record count, affine-entry count and original-name payload is O(Q); coefficient collection and splitting leave O(Q) vertices/edges/entries (up to encoding constants). There are O(Q) marked placeholder edges. The x-only C_0 copies have O(Q) records and at most O(Q) raw label payload before renumbering. Each c_j has at most eight words of length at most three; each s_j has at most nine. Build disjoint bounded word-path gadgets as in L041, retaining duplicate paths and all original names. Every L_j,R_j,f_F graph has O(Q) records and O(Q²) raw name payload even when names are copied at every occurrence; all empty products have constant-size graphs. Concatenating R_j and P_e uses O(Q) records. With endpoint renumbering and complete original/B_x framing, every operand input to L035 or L036 therefore has full length at most K_0 Q³. The B_x list and its dictionary are already a sublist of the charged A; retaining them costs O(Q), and no implicit additional variable range is introduced.

Use L035's conservative O(E⁴) and L036's O(E⁶) full bounds. Each W or B block has at most K_1 Q^18 bits; all other factors in each branch have at most K_2 Q³ bits. There are at most twice O(Q) clause summands plus O(Q) nonclause summands. Their complete separately encoded blocks, connectors and enclosing roots cost O(Q^19) before final dense renumbering. Final endpoint/symbol references and record framing can increase that bound by at most O(log(Q+2)): the total number of records is polynomial in Q, and original-name payloads are retained within those bounds. Thus K Q^20 bounds all output bits, including a single complete x/B_x dictionary and axiom list. Even retaining separate block framing would satisfy this bound. Constants are independent of F,C, degree and path count.

All operations are finite polynomially bounded loops on explicit labels, edges, clause gadgets and block copies, together with L035/L036's polynomial-time constructors. Topological pruning, dictionary mapping and ordinary string writing are polynomial in Q. The bound concerns full binary encoding rather than only arithmetic nodes. Degree is at most the number of output edges; no semantic degree assumption or circuit-to-ABP conversion occurs.

**Boundary and route checks.** An empty clause has c_j=1, s_j=0 and f_F=0; (3)–(4) still hold (B(1) substitutes to 0), and the disconnected zero witness could be used directly. If m=0, f_F=1 and F is satisfiable; no supplied C can satisfy both identities, since scalar evaluation makes every B_x axiom zero. More generally the supplied identities imply F is UNSAT by scalar Boolean evaluation; the construction does not need a decision algorithm. With n=0, all corrections and dictionaries can be empty and the same formal algebra applies. If C's designated endpoints coincide, acyclicity makes its polynomial 1 from the sole empty path, violating C(x,0)=0; the hypotheses are consequently inconsistent in that case, rather than requiring a missing gadget. Subpath endpoints may coincide and are covered above. Clause repetitions retain distinct y_j and their actual positions. No faithful values, W/V/U bound, arbitrary linearization or general ER-to-C premise is used. Attempts 020/021 concern prescribed output conversions; this construction is free to choose a different H and does not invalidate those obstructions. L021 supplies a shared circuit, and L037 permits nonlinear placeholder paths, so neither supplies the present input promise automatically.

**Independent critical audit, 2026-10-10.** This audit reuses the approved scope in `drafts/literature/2026-10-10-pathwise-clause-elimination-critical-audit.md` and the already audited L035/L036 interfaces. It checks the existing construction; it adds no representation theorem or stronger bound.

For normalization, regard an edge of C' as the choice of one nonzero summand in a particular original edge label. Parallel original edges remain distinct choices. Every accepting C' path therefore projects to an original accepting path, and its number of placeholder-symbol edges is at most the number of placeholder-bearing original edges on that path, namely one. A path with no placeholder belongs to C_0 even if it chose an x or constant summand from an originally mixed label. Substitution of zero for the placeholders in the entire finite path sum is exactly the polynomial of C_0. Thus the formal hypothesis, rather than a support-path argument, proves C_0=0. Pruning removes only edges on no designated accepting path; it does not remove paths merely because their contributions cancel or have zero labels.

Fix a surviving placeholder-symbol edge e:u→v. Any C_0 path from the source to u and any C_0 path from v to the sink concatenate with e: a repeated vertex would give a directed cycle in C'. Every resulting path has exactly that marked edge, and cutting at it recovers the pair uniquely. Conversely every accepting path with one placeholder gives such a pair. This proves the coefficient factorization P_e t_e S_e and (1), including zero subpath polynomials and cancellations among parallel paths. No grouping identifies distinct clause placeholders, even for repeated clauses. For a concrete mixed-label check take the opposing unit CNF (x)∧(¬x), with c_1=1+x, c_2=x. A two-vertex C with parallel labels y_1+x and y_2+x satisfies the path promise, C(x,0)=x+x=0 and C(x,A)=1. Its normalization has two placeholder-free paths; deleting them is justified only after their polynomial is summed. Formula (1) retains y_1+y_2 and the construction substitutes to f_F(c_1+c_2)=f_F, with f_F=x+x². This checks a cancellation case without replacing the general argument by an example.

For a clause branch abbreviate c=c_j and D=R_j P_e. The three displayed ordered terms in (4) expand to

    (1+c)D c + (1+c)c D + (c²+c)D
      = D c+c D c+c D+c²D+c²D+c D
      = D c+c D c.

The repeated words cancel in F₂ without any interchange of c and D. Reattaching L_j,S_e gives L_j(1+c_j)R_j P_e c_j S_e, with precisely the order in f_F P_e c_j S_e. In particular, the s_j factor is present in the actual W summand. D and c are x-only copies built before either witness call. L035 uses the complete commutator dictionary restricted from B_x; its output embeds into the common x,σ,τ alphabet with unused σ symbols permitted. L036 uses that same complete B_x. A copied placeholder always refers to the same original axiom, not to a fresh independent symbol for each copy. Nonclause branches use their indicated original σ or τ directly. Each branch is zero at zero placeholders. Summation and the supplied second identity therefore prove both claimed output identities, without a Boolean evaluation substituted for a free-ring equality.

An accepting path in a serial product has one internal path in each disjoint factor, in the specified order. The only transition to the next factor leaves the designated exit; taking an internal outgoing edge at that exit cannot yield a later exit without a cycle. Internal incoming edges at an entrance give no alternative outside entry. Coincident internal entrance/exit contributes its unique empty path; a factor with no such internal path gives no accepting branch path. Every new connector runs forward between copies. Fresh outer endpoints for the parallel sum force selection of exactly one branch. It follows that each accepted path contains exactly the single placeholder edge in its central L035/L036 block or nonclause atom, including paths whose polynomial contributions cancel. Zero labels, dead vertices and no-branch outputs do not add paths. The empty-clause, m=0, n=0 and coincident-C-root cases have the outcomes stated above; in particular m=0 or coincident C roots cannot be valid supplied IPS inputs. No exception requires an uncharged gadget or additional variable.

For a separate full-bit ledger, fix the ordinary explicit encoding once and absorb its record constants into absolute constants a_i. Let r be the number of marked edges after splitting. Explicit input records and affine entries give r≤a_1 Q and O(Q) vertices/edges in C_0. Every clause gadget has bounded records, every complete product L_j,R_j,f_F has O(Q) records, and every referenced original name has length at most Q. Thus each x-only operand graph, including duplicated raw names, has O(Q²) payload; binary vertex references, list framing and roots still fit a_2 Q³. The complete B_x and its placeholder/name dictionary are retained from A and cost O(Q); restricting to commutators for L035 costs no more. Consequently every actual L035/L036 input has E≤a_3 Q³, including all its required framing. No supplied graph with placeholders is hidden in this input budget.

The audited bounds give |W|≤a_4 E⁴≤a_5 Q¹² and |B|≤a_6 E⁶≤a_7 Q¹⁸, so each can be bounded by a_8 Q¹⁸. Each clause edge contributes two disjoint summands, each with at most one such block and a fixed number of surrounding O(Q³)-bit graph factors; each other edge contributes one summand with its atom. There are at most 2r summands. Thus the sum D of their separately framed bit lengths, plus connectors and new roots, satisfies D≤a_9 Q¹⁹. This charges graph copies, isolated vertices, label entries, internal W/B framing and every occurrence of an original name before any global renumbering.

To write one output graph, retain the original-name and axiom payload and map local symbol references to the common x,σ,τ dictionary. Every record or reference field present in the separate encodings consumes at least one bit, so there are O(D) such fields. There are at most O(D) output vertices/edges and O(Q) explicitly framed allowed symbols. Dense endpoint/symbol identifiers and self-delimiting counts therefore take O(log(D+Q+2))=O(log(Q+2)) bits per field. A fixed encoding constant bounds total output length by a_10(D+Q)log(Q+2). Since Q≥2, this is at most K Q²⁰ for one fixed K. This argument charges all renamed endpoints, new connectors, global roots, list framing, the complete B_x, unused permitted symbols and the original names. Long names are retained as payload, not treated as unit-cost identifiers. Parsing, coefficient collection, finite graph copying, dictionary mapping and the imported local constructors have polynomial bit time; no loop enumerates full paths. This verifies the claimed exponent rather than inferring it from graph counts alone.

Both identities, the path property and the KQ²⁰ bound survive the audit. No mathematical error was repaired, no numerical certificate or implementation was used, and no stronger claim follows. L035/L036 and L041 remain the direct inputs recorded in the unchanged DAG. General ER-to-C data and a replacement for arbitrary nonlinear supplied C remain independent unresolved obligations; the fixed-output stops in Attempts 020/021 are preserved. Full matching Mathlib coverage remains not checked.

## Mathlib

Full matching coverage is not checked. The cited noncommutative witness/ABP results and complete encoding theorem are used as informal mathematical inputs; no Mathlib theorem or formal Lean verification is asserted. Supporting free-algebra distributivity alone would not constitute full coverage.
