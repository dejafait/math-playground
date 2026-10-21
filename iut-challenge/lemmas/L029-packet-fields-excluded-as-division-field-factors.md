# L029 — Packet fields excluded as division-field factors in the inspected exposition

## Hypotheses

Use L020's ordered packet (K_aux,Q_3), where K_aux=Q_3(pi), pi^27=3. L016 supplies that K_aux is a finite extension of Q_3 with residue field F_3. The second field has the same residue field.

Fix exactly the setup of **Dupuy–Hilado, arXiv:2004.13228v1**, Definitions **3.6.1/3.6.3**, printed pp. 11–13, and **5.3.1/5.5.1**, pp. 26 and 30, with section 5.4, pp. 27–30 ([versioned primary PDF](https://arxiv.org/pdf/2004.13228v1)). Write F_base for the elliptic-curve base field, D=F_base(E[ell]) for the full division field, and D_w for an individual selected completion used as a tensor factor. Here ell is the eligible prime, ell>=5; in particular ell is prime to 3. Definition 5.3.1 also requires sqrt(-1) in F_base. Do not identify these factors with the smaller indexing field or with field components obtained after decomposing a tensor product.

Import **Silverman, The Arithmetic of Elliptic Curves**, second edition, GTM 106 (2009), **Corollary III.8.1.1**, printed p. 96, with **Proposition III.8.1(c,d)**, pp. 94–95: in characteristic zero, rationality of full m-torsion implies mu_m is contained in the field ([primary book PDF](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=114)). Import **Pete L. Clark, Algebraic Number Theory II: Valuations, Local Fields and Adeles**, author-hosted undated 161-page version accessed 2026-10-07, **Proposition 2.30**, p. 76, and **Corollary 2.33(a)**, p. 77: reduction identifies prime-to-p roots of unity in a p-adic field of residue degree f with the residue-field roots of unity, of order p^f-1 ([primary notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf#page=76)). These inputs were inspected in the prior SPECIALIZE assessment `drafts/literature/2026-10-07-packet-initial-data-field-roles.md`; no reproof is needed.

## Conclusion

Neither K_aux nor Q_3 can be an individual selected division-field completion D_w in this setup for any eligible ell. Thus L020's unchanged two-field packet cannot be realized as a packet of those individual factors. Neither field can instead be a completion of the required F_base: its sqrt(-1) prerequisite already fails locally.

This excludes a specific auxiliary realization route. It is not an exclusion of decomposed tensor components, an assertion about the unread native initial-theta-data definition, a theorem about enlarged packets, or an essential IUT flaw. In particular it supplies no failure of the original finite B>=A comparison.

## Proof

Let L be either field. It is a complete discretely valued finite extension of Q_3 and hence is Henselian, with residue field F_3. For K_aux these are the field data established in L016; for Q_3 they are the standard defining local-field data. Clark's cited theorem therefore says that the group of roots of unity in L having order prime to 3 has exactly 3^1-1=2 elements. Consequently L contains no primitive ell-th root of unity for a prime ell>=5, and no primitive fourth root of unity. This argument makes no claim about 3-primary torsion.

By the definition D=F_base(E[ell]), all geometric ell-torsion points of E are D-rational. Silverman's corollary applies with m=ell in characteristic zero, so mu_ell is contained in D. Every completion embedding D into D_w is injective and preserves the multiplicative order of a root of unity. Thus D_w contains a primitive ell-th root. If D_w were isomorphic to L as a Q_3-field, L would contain that root as well, contradicting the preceding local condition. This rules out each individual factor, and therefore the unchanged packet. A single rational cyclic subgroup would not imply this prerequisite; the argument uses the full division field explicitly.

For the separate base-field role, sqrt(-1) in F_base remains a primitive fourth root in every completion of F_base above 3, since the completion embedding is injective and the characteristic is zero. It cannot belong to either L, again by Clark's theorem. Nor can the prerequisite be lost by passing to a division-field completion containing that base completion. This supplementary test distinguishes the roles rather than treating the base completion as the source's tensor factor.

Neither argument concerns arbitrary field components of a tensor algebra or scalar restriction of its associated vector space. The definitions used here are those of the inspected exposition, whose qualifications differ from native initial data. A replacement field containing the necessary roots would change the target; passing a necessary test would still not construct global data, establish actual permitted actions or input membership, transport the pilot, or prove essentiality.

### Critical audit, 2026-10-08

The audit reuses the SPECIALIZE coverage in `drafts/literature/2026-10-07-packet-field-exclusion-critical-audit.md`. It confirms the stated exclusion without enlarging its scope. The following application checks are part of the canonical proof record.

L016's field-data proof applies Eisenstein to X^27-3 over Z_3, so [K_aux:Q_3]=27 and pi has valuation 1/27. In the power-basis expression, distinct fractional valuation parts prohibit cancellation of the least-valuation term. Since coefficient valuations are integral, v(c_r)+r/27>=0 for 0<=r<=26 is equivalent to c_r in Z_3. Thus O=Z_3[pi] and O/(pi)=F_3. This confirms residue degree one, not absolute degree 27. Only this field-data portion of L016 is used; its logarithm table, separator and certificates are unnecessary here. L020 supplies the ordered pair of fields, not an arithmetic realization assumption.

The source role is a completion of D, not merely of the smaller field indexing the places: Definitions 3.6.1/3.6.3 specify the selected factors, Definitions 5.3.1/5.5.1 fix the full division field, and section 5.4 distinguishes the included base completions. Selecting places cannot remove elements already in D. The full E[ell] is rational over D by the defining adjunction of all torsion coordinates, even though the initial base field need not rationalize it. Silverman's corollary applies to E over D. Characteristic zero removes the characteristic restriction; primality together with ell>=5 excludes ell=3. A rational cyclic subgroup has not been substituted for full torsion.

For any nonarchimedean place w, the completion map has zero kernel: a nonzero x in D has nonzero absolute value at w and cannot map to zero. If a primitive root zeta acquired smaller order d in D_w, then zeta^d-1 would lie in this kernel. Its order therefore remains ell. Both candidate fields are finite extensions of Q_3, hence complete and Henselian; Clark's prime-to-3 reduction statement applies to each with f=1. The required order ell cannot divide 2, the order of F_3^times. This contradiction assumes neither a Galois presentation of K_aux nor an identification of a tensor algebra with a single field.

Independently, i^2=-1 in characteristic zero implies order exactly four: i^4=1 but i^2 is not 1. The base-field completion map retains that order. If w restricts to v on F_base, the inclusion into D extends injectively from F_base,v to D_w, so this prerequisite is retained in that role as well. Clark's same prime-to-3 condition excludes order four. This neither replaces the full-torsion argument nor transfers the exposition's base-field prerequisites to the unread native definition.

No mathematical repair or new obstruction resulted. Corrections are the DH page locations, Silverman PDF anchor and Clark corollary page, as already documented in the supplied source assessment. The direct DAG inputs remain L016 and L020. Decomposed tensor components, enlarged fields, native initial data, actual actions and inputs, pilot transport, essentiality and finite B>=A are not settled. The unchanged-factor stop remains valid only as stated.

## Mathlib

Full matching packet-role exclusion: **not checked**. Supporting Weil-pairing, local roots-of-unity reduction, Eisenstein and completion coverage: **not checked**. The precise primary citations above are the imported mathematical inputs; unknown Mathlib coverage is not evidence of absence. This is a necessary-condition specialization of known theorems, with no claim of progress beyond the checked sources.
